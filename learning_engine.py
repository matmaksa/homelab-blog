#!/usr/bin/env python3
"""
Learning Engine v2 – Closed Learning Loop mit Confidence-System, Aging,
und Performance-Analyse.

Workflow:
  reviews/*.json  →  Mustererkennung  →  quality_learnings.md + performance_learnings.md

Confidence System:
  1 Vorkommen → observation (keine harte Regel)
  3+ Vorkommen → pattern (Empfehlung)
  5+ Vorkommen → rule (aktive Qualitätsregel)

Aging:
  90 Tage nicht gesehen → Archivierung
"""
import json, os, re, sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

BLOG_DIR = "/root/homelab-blog"
REVIEWS_DIR = os.path.join(BLOG_DIR, "reviews")
AI_CONTEXT = "/root/.hermes/skills/monetization/blog-core/references/ai_context"
LEARNINGS_PATH = os.path.join(AI_CONTEXT, "quality_learnings.md")
PERF_PATH = os.path.join(AI_CONTEXT, "performance_learnings.md")
LOG_FILE = os.path.join(BLOG_DIR, "logs", "pipeline.log")
AGING_DAYS = 90
MIN_REVIEWS_FOR_FULL = 5

def log(level: str, message: str):
    try:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{ts}]\n{level}\n{message}\n\n")
    except Exception:
        pass

# ─── Datenstruktur für Learnings ──────────────────────────────────

class Learning:
    """Ein einzelnes Learning mit Confidence-System."""
    def __init__(self, rule: str, category: str = "general"):
        self.rule = rule
        self.category = category
        self.occurrences = 1
        self.first_seen = datetime.now().isoformat()
        self.last_seen = datetime.now().isoformat()

    @property
    def confidence(self) -> str:
        if self.occurrences >= 5:
            return "high"  # rule
        if self.occurrences >= 3:
            return "medium"  # pattern
        return "low"  # observation

    @property
    def status(self) -> str:
        if self.occurrences >= 5:
            return "rule"
        if self.occurrences >= 3:
            return "pattern"
        return "observation"

    def record_occurrence(self):
        self.occurrences += 1
        self.last_seen = datetime.now().isoformat()

    def is_stale(self) -> bool:
        try:
            last = datetime.fromisoformat(self.last_seen)
            return (datetime.now() - last).days > AGING_DAYS
        except (ValueError, TypeError):
            return False

    def to_dict(self) -> dict:
        return {
            "rule": self.rule,
            "category": self.category,
            "occurrences": self.occurrences,
            "confidence": self.confidence,
            "status": self.status,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
        }

# ─── Review-Loader ────────────────────────────────────────────────

def load_reviews() -> list[dict]:
    reviews = []
    if not os.path.isdir(REVIEWS_DIR):
        log("WARNING", "Learning Engine: reviews/ directory not found")
        return reviews
    for fname in sorted(os.listdir(REVIEWS_DIR)):
        if fname.endswith(".json"):
            path = os.path.join(REVIEWS_DIR, fname)
            try:
                with open(path) as f:
                    data = json.load(f)
                    review = data.get("review", {})
                    review["_slug"] = data.get("slug", fname)
                    review["_timestamp"] = data.get("timestamp", "")
                    reviews.append(review)
            except (json.JSONDecodeError, OSError):
                continue
    return reviews

# ─── Mustererkennung ─────────────────────────────────────────────

def extract_learnings(reviews: list[dict]) -> dict[str, Learning]:
    """Extrahiere gewichtete Learnings aus Reviews."""
    learning_map = {}  # rule text → Learning

    def add(rule: str, category: str = "general"):
        key = rule.strip().lower()
        if key in learning_map:
            learning_map[key].record_occurrence()
        else:
            learning_map[key] = Learning(rule.strip(), category)

    for r in reviews:
        slug = r.get("_slug", "?")
        changes = r.get("required_changes", [])
        errors = r.get("spec_errors", [])
        ready = r.get("publish_ready", True)
        quality = r.get("overall_quality_score", 0) or 0
        reader = r.get("reader_score", 0) or 0
        purchase = r.get("purchase_clarity_score", 0) or 0

        # Negative Muster: required_changes
        for c in changes:
            cat = "kaufargument" if any(k in c.lower() for k in ["kauf", "empfehl", "geeignet", "alternativ"]) else "schreibregel"
            add(c, cat)

        # Negative Muster: spec_errors
        for e in errors:
            if isinstance(e, dict):
                field = e.get("field", "?")
                claim = e.get("article_claim", "")
                source = e.get("source_value", "")
                add(f"Spec-Fehler: {field} – '{claim}' statt '{source}'", "faktenfehler")
            elif isinstance(e, str):
                add(f"Spec-Fehler: {e}", "faktenfehler")

        # Positive Muster: hohe Scores
        if quality >= 8 and reader >= 8 and purchase >= 8:
            add(f"Hohe Qualität: {slug} (Q={quality}, L={reader}, K={purchase})", "erfolgsmuster")

        # Negative Muster: publish block
        if not ready:
            add(f"publish_ready=false: {slug}", "publish_blocker")

    return learning_map

def extract_performance(reviews: list[dict]) -> dict[str, Learning]:
    """Extrahiere positive Muster (was hat funktioniert?)."""
    pmap = {}

    def add(rule: str, category: str = "general"):
        key = rule.strip().lower()
        if key in pmap:
            pmap[key].record_occurrence()
        else:
            pmap[key] = Learning(rule.strip(), category)

    for r in reviews:
        slug = r.get("_slug", "?")
        quality = r.get("overall_quality_score", 0) or 0
        reader = r.get("reader_score", 0) or 0
        purchase = r.get("purchase_clarity_score", 0) or 0
        changes = r.get("required_changes", [])
        ready = r.get("publish_ready", True)

        # Hohe Scores = erfolgreiches Muster
        if quality >= 8:
            add(f"Artikel mit Qualität {quality}/10: {slug}", "erfolgreiche_artikel")
        if reader >= 8:
            add(f"Hoher Leserwert {reader}/10: {slug}", "erfolgreiche_leserfrage")
        if purchase >= 8:
            add(f"Klare Kaufentscheidung {purchase}/10: {slug}", "erfolgreiche_kaufargumente")

        # Wenig required_changes + publish_ready = gute Vorlage
        if ready and len(changes) <= 1:
            add(f"Sauberer Artikel mit {len(changes)} Änderungen: {slug}", "erfolgreiche_struktur")

        # Hohe Scores in allen Metriken
        if quality >= 7 and reader >= 7 and purchase >= 7:
            add(f"Rundum guter Artikel: {slug} (Q={quality}, L={reader}, K={purchase})", "erfolgsmuster")

    return pmap

# ─── Confidence-basierte Formatierung ─────────────────────────────

def format_learnings_by_status(learning_map: dict[str, Learning]) -> tuple[list, list, list, list]:
    """Sortiere Learnings nach Status in Active Rules / Emerging / Observations / Archived."""
    active = []   # confidence == "high" (5+)
    emerging = []  # confidence == "medium" (3-4)
    observations = []  # confidence == "low" (1-2)
    archived = []  # stale (>90 days)

    now = datetime.now()
    for l in sorted(learning_map.values(), key=lambda x: x.occurrences, reverse=True):
        if l.is_stale():
            archived.append(l)
        elif l.confidence == "high":
            active.append(l)
        elif l.confidence == "medium":
            emerging.append(l)
        else:
            observations.append(l)

    return active, emerging, observations, archived

def render_quality_learnings(learning_map: dict[str, Learning], total_reviews: int, avg_scores: dict) -> str:
    """Generiere quality_learnings.md mit Confidence-System."""
    active, emerging, observations, archived = format_learnings_by_status(learning_map)

    lines = []
    lines.append("# Quality Learnings (Confidence-basiert)")
    lines.append(f"\n*Generiert am: {datetime.now().strftime('%d.%m.%Y %H:%M')}*")
    lines.append(f"*Basis: {total_reviews} Review(s)*\n")
    lines.append("---\n")

    # Statistik
    lines.append("## 📊 Statistik")
    lines.append(f"- **Reviews analysiert:** {total_reviews}")
    lines.append(f"- **Aktive Regeln (high):** {len(active)}")
    lines.append(f"- **Emerging Patterns (medium):** {len(emerging)}")
    lines.append(f"- **Observations (low):** {len(observations)}")
    lines.append(f"- **Archiviert:** {len(archived)}")
    if avg_scores:
        lines.append(f"- **⌀ Quality Score:** {avg_scores.get('quality', 0):.1f}/10")
        lines.append(f"- **⌀ Leserwert:** {avg_scores.get('reader', 0):.1f}/10")
        lines.append(f"- **⌀ Kaufentscheidung:** {avg_scores.get('purchase', 0):.1f}/10")
    lines.append("")

    # Active Rules (5+ Vorkommen)
    lines.append("## 🛡️ Active Rules (hohe Confidence)")
    lines.append("Diese Regeln basieren auf 5+ Vorkommen und sollten aktiv beachtet werden.\n")
    if active:
        for l in active:
            lines.append(f"- **[{l.category}]** {l.rule} ({l.occurrences}x)")
    else:
        lines.append("(Noch keine stabilen Regeln – mehr Reviews sammeln)")
    lines.append("")

    # Emerging Patterns (3-4 Vorkommen)
    lines.append("## 🔄 Emerging Patterns (mittlere Confidence)")
    lines.append("Wiederkehrende Muster, aber noch nicht stabil genug für eine feste Regel.\n")
    if emerging:
        for l in emerging:
            lines.append(f"- **[{l.category}]** {l.rule} ({l.occurrences}x)")
    else:
        lines.append("(Keine wiederkehrenden Muster)")
    lines.append("")

    # Observations (1-2 Vorkommen)
    lines.append("## 👁️ Observations (niedrige Confidence)")
    lines.append("Einmalige oder seltene Hinweise – nicht als harte Regel behandeln.\n")
    if observations:
        for l in observations:
            lines.append(f"- **[{l.category}]** {l.rule} ({l.occurrences}x)")
    else:
        lines.append("(Keine Observations)")
    lines.append("")

    # Archived
    if archived:
        lines.append("## 🗄️ Archived ({}+ Tage nicht gesehen)".format(AGING_DAYS))
        lines.append("Alte Learnings, die länger nicht mehr aufgetreten sind.\n")
        for l in archived:
            lines.append(f"- **[{l.category}]** {l.rule} (zuletzt {l.last_seen[:10]})")
        lines.append("")

    lines.append("---")
    lines.append("*Automatisch generiert vom Learning Engine v2.*")
    return "\n".join(lines)

def render_performance_learnings(pmap: dict[str, Learning]) -> str:
    """Generiere performance_learnings.md – positive Muster."""
    active, emerging, observations, archived = format_learnings_by_status(pmap)

    lines = []
    lines.append("# Performance Learnings (Positive Muster)")
    lines.append(f"\n*Generiert am: {datetime.now().strftime('%d.%m.%Y %H:%M')}*\n")
    lines.append("---\n")

    lines.append("## ✅ Erfolgreiche Artikelmuster")
    for l in sorted(pmap.values(), key=lambda x: x.occurrences, reverse=True):
        if l.category == "erfolgreiche_artikel" and l.confidence != "low":
            lines.append(f"- ({l.occurrences}x) {l.rule}")
    lines.append("")

    lines.append("## 📈 Erfolgreiche Überschriften & Leserfragen")
    for l in sorted(pmap.values(), key=lambda x: x.occurrences, reverse=True):
        if l.category == "erfolgreiche_leserfrage" and l.confidence != "low":
            lines.append(f"- ({l.occurrences}x) {l.rule}")
    lines.append("")

    lines.append("## 💰 Erfolgreiche Kaufargumente")
    for l in sorted(pmap.values(), key=lambda x: x.occurrences, reverse=True):
        if l.category == "erfolgreiche_kaufargumente" and l.confidence != "low":
            lines.append(f"- ({l.occurrences}x) {l.rule}")
    lines.append("")

    lines.append("## 📐 Erfolgreiche Strukturen")
    for l in sorted(pmap.values(), key=lambda x: x.occurrences, reverse=True):
        if l.category == "erfolgreiche_struktur" and l.confidence != "low":
            lines.append(f"- ({l.occurrences}x) {l.rule}")
    lines.append("")

    lines.append("## 🏆 Allgemeine Erfolgsmuster")
    for l in sorted(pmap.values(), key=lambda x: x.occurrences, reverse=True):
        if l.category == "erfolgsmuster" and l.confidence != "low":
            lines.append(f"- ({l.occurrences}x) {l.rule}")
    lines.append("")

    lines.append("---")
    lines.append("*Automatisch generiert vom Learning Engine v2.*")
    return "\n".join(lines)

# ─── Haupt-Logik ──────────────────────────────────────────────────

def run():
    log("INFO", "LEARNING ENGINE V2 STARTED")

    reviews = load_reviews()
    if not reviews:
        log("INFO", "Learning Engine: No reviews found, skipping")
        print("  [INFO] Learning Engine: No reviews found, skipping")
        return

    log("INFO", f"REVIEWS ANALYZED: {len(reviews)}")

    if len(reviews) < MIN_REVIEWS_FOR_FULL:
        log("WARNING", f"Learning Engine: Only {len(reviews)} reviews (min {MIN_REVIEWS_FOR_FULL} for full analysis)")
        print(f"  [WARN] Learning Engine: Only {len(reviews)} reviews (min {MIN_REVIEWS_FOR_FULL} for full analysis)")

    # Durchschnittswerte
    n = max(len(reviews), 1)
    avg = {
        "reader": sum(r.get("reader_score", 0) or 0 for r in reviews) / n,
        "purchase": sum(r.get("purchase_clarity_score", 0) or 0 for r in reviews) / n,
        "quality": sum(r.get("overall_quality_score", 0) or 0 for r in reviews) / n,
    }

    # Learnings extrahieren (negativ + positiv)
    learning_map = extract_learnings(reviews)
    perf_map = extract_performance(reviews)
    total_patterns = len(learning_map) + len(perf_map)
    log("INFO", f"PATTERNS FOUND: {total_patterns}")

    # Quality Learnings schreiben
    ql = render_quality_learnings(learning_map, len(reviews), avg)
    try:
        os.makedirs(os.path.dirname(LEARNINGS_PATH), exist_ok=True)
        with open(LEARNINGS_PATH, "w") as f:
            f.write(ql)
        log("INFO", "QUALITY LEARNINGS UPDATED")
    except OSError as e:
        log("ERROR", f"Failed to write quality_learnings: {e}")

    # Performance Learnings schreiben
    pl = render_performance_learnings(perf_map)
    try:
        os.makedirs(os.path.dirname(PERF_PATH), exist_ok=True)
        with open(PERF_PATH, "w") as f:
            f.write(pl)
        log("INFO", "PERFORMANCE LEARNINGS UPDATED")
    except OSError as e:
        log("ERROR", f"Failed to write performance_learnings: {e}")

    print(f"  [OK] Learning Engine v2: {len(reviews)} reviews → {len(learning_map)} quality + {len(perf_map)} performance patterns")

if __name__ == "__main__":
    run()
