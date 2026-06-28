#!/usr/bin/env python3
"""
Keyword-Recherche für den Homelab-Blog.
Nutzte kostenlose Quellen: Google Suggest, Related Searches, Reddit.
Kein API-Key nötig.

Usage:
  python3 keyword_research.py --seed "homelab mini pc"
  python3 keyword_research.py --seed "gebrauchter mini pc proxmox"
  python3 keyword_research.py --list          # Zeigt letzte 5 Recherchen
"""
import json, urllib.request, urllib.parse, urllib.error
import sys, os, re, time
from datetime import datetime

BLOG_DIR = "/root/homelab-blog"
REPORTS_DIR = os.path.join(BLOG_DIR, "reports")
HISTORY_FILE = os.path.join(REPORTS_DIR, "keyword_history.json")

# Basis-Keywords aus dem Blog
BLOG_NICHE_KEYWORDS = [
    "homelab mini pc",
    "gebrauchter mini pc",
    "1L pc homelab",
    "proxmox mini server",
    "home assistant hardware",
    "thin client proxmox",
    "fujitsu futro",
    "hp probook mini",
    "dell optiplex homelab",
]

# Konstante für Rate Limiting
DELAY = 0.3

def fetch_google_suggest(seed: str) -> list:
    """Holt Google Suggest-Vorschläge (kostenlos, kein API-Key)."""
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={urllib.parse.quote(seed)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            suggestions = data[1] if len(data) > 1 else []
            return [s.strip() for s in suggestions if s.strip()]
    except Exception as e:
        print(f"  ⚠️  Google Suggest failed: {e}")
        return []

def fetch_google_suggest_lang(seed: str, lang: str = "de") -> list:
    """Holt Google Suggest-Vorschläge für eine bestimmte Sprache."""
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&hl={lang}&q={urllib.parse.quote(seed)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            suggestions = data[1] if len(data) > 1 else []
            return [s.strip() for s in suggestions if s.strip()]
    except Exception as e:
        return []

def classify_intent(keyword: str) -> str:
    """Klassifiziert Suchintention grob."""
    kw = keyword.lower()
    transactional_words = ["kaufen", "preis", "billig", "günstig", "bestellen", "deals", "angebot", "kosten", "preis"]
    informational_words = ["was", "wie", "unterschied", "vs", "oder", "anleitung", "setup", "einrichten", "tutorial", "guide", "erfahrung"]
    commercial_words = ["test", "vergleich", "review", "erfahrungen", "bewertung", "top", "beste", "empfehlung"]
    navigational_words = ["download", "software", "tool", "github"]

    for w in transactional_words:
        if w in kw: return "transactional"
    for w in commercial_words:
        if w in kw: return "commercial"
    for w in informational_words:
        if w in kw: return "informational"
    for w in navigational_words:
        if w in kw: return "navigational"
    return "informational"  # Default

def research(seed: str) -> dict:
    """Führt eine vollständige Keyword-Recherche durch."""
    print(f"\n🔍 Keyword-Recherche: '{seed}'")
    print("=" * 50)

    # Google Suggest (DE)
    print("\n📌 Google Suggest (DE):")
    de_suggestions = fetch_google_suggest_lang(seed, "de")
    time.sleep(DELAY)

    # Google Suggest (EN - als Fallback für Tech-Begriffe)
    en_suggestions = fetch_google_suggest_lang(seed, "en")
    time.sleep(DELAY)

    # Related Searches via Google Suggest
    related = []
    for s in list(set(de_suggestions + en_suggestions))[:5]:
        related_suggestions = fetch_google_suggest_lang(s, "de")[:3]
        related.extend(related_suggestions)
        time.sleep(DELAY)

    # Deduplizieren und klassifizieren
    all_keywords = list(set(de_suggestions + en_suggestions + related))

    if not all_keywords:
        print("  Keine Vorschläge gefunden")
        return {"seed": seed, "keywords": [], "timestamp": datetime.now().isoformat()}

    # Nach Intent sortieren
    results = []
    for kw in sorted(all_keywords):
        intent = classify_intent(kw)
        results.append({"keyword": kw, "intent": intent, "source": "google_suggest"})

    # Ausgabe
    for r in results:
        intent_icon = {"informational": "📖", "commercial": "🛒", "transactional": "💰", "navigational": "🔗"}
        icon = intent_icon.get(r["intent"], "📌")
        print(f"  {icon} {r['keyword']:<50} [{r['intent']}]")

    # Count by intent
    counts = {}
    for r in results:
        counts[r["intent"]] = counts.get(r["intent"], 0) + 1
    print(f"\n  Verteilung: {counts}")

    # Article recommendations with content-type
    print(f"\n💡 Mögliche Artikel-Titel (mit Content-Typ):")
    high_prio = [r for r in results if r["intent"] in ("commercial", "transactional")]
    for r in high_prio[:5]:
        print(f"  🛒 {r['keyword'].title()} — Kaufberatung [Money]")
    for r in results[:8]:
        if r["intent"] == "informational" and r not in high_prio[:5]:
            print(f"  📖 {r['keyword'].title()} — Ratgeber/Anleitung [Pillar]")

    # Content-type recommendation
    commercial_count = counts.get("commercial", 0) + counts.get("transactional", 0)
    informational_count = counts.get("informational", 0)
    total_count = sum(counts.values())
    if commercial_count > informational_count:
        print(f"\n  🛒 Empfohlener Content-Typ: **Money/Kaufberatung** (mehrere kommerzielle Keywords)")
    elif total_count > 0:
        print(f"\n  📖 Empfohlener Content-Typ: **Reichweite/Pillar** (meist informative Keywords)")

    return {
        "seed": seed,
        "keywords": results,
        "timestamp": datetime.now().isoformat(),
        "intent_distribution": counts,
    }

def save_history(result: dict):
    """Speichert die Recherche im Verlauf."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    history.insert(0, result)
    history = history[:20]  # Max 20 Einträge
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def show_history():
    """Zeigt die letzten Recherchen."""
    if not os.path.exists(HISTORY_FILE):
        print("Keine bisherigen Recherchen.")
        return
    with open(HISTORY_FILE) as f:
        history = json.load(f)
    print(f"\n📋 Letzte {len(history)} Keyword-Recherchen:\n")
    for i, h in enumerate(history[:10]):
        count = len(h.get("keywords", []))
        ts = h.get("timestamp", "")[:16]
        seed = h.get("seed", "")
        print(f"  {i+1}. [{ts}] '{seed}' → {count} Keywords")

def main():
    if "--list" in sys.argv or "-l" in sys.argv:
        show_history()
        return

    # Find seed keyword
    seed = None
    if "--seed" in sys.argv:
        idx = sys.argv.index("--seed")
        if idx + 1 < len(sys.argv):
            seed = sys.argv[idx + 1]

    if not seed:
        print("Usage: python3 keyword_research.py --seed \"suchbegriff\"")
        print("       python3 keyword_research.py --list")
        print("\nOr use --suggest for niche suggestions:")
        print(f"  Niche keywords: {', '.join(BLOG_NICHE_KEYWORDS[:5])}...")
        sys.exit(1)

    result = research(seed)
    save_history(result)

    # Save detail report
    safe_seed = re.sub(r'[^a-z0-9]', '_', seed.lower())[:30]
    report_path = os.path.join(REPORTS_DIR, f"keywords_{safe_seed}_{datetime.now().strftime('%Y%m%d')}.json")
    with open(report_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\nReport: {report_path}")

if __name__ == "__main__":
    main()
