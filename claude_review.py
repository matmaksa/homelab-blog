#!/usr/bin/env python3
"""
Claude Sonnet 4.6 Review Pipeline + Geräte-Datenbank Faktencheck
Liest einen generierten SEO-Artikel, prüft mit YAML-Datenbank,
schickt an Claude zur Verbesserung, überschreibt die Datei.
"""
import json, urllib.request, urllib.error, sys, os, re, yaml

DEVICES_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "devices.yaml")

def load_device_database():
    """Load the canonical device specs from YAML."""
    if not os.path.exists(DEVICES_DB):
        print("⚠️  devices.yaml not found – skipping DB fact-check")
        return None
    with open(DEVICES_DB) as f:
        data = yaml.safe_load(f)
    return data.get("devices", {})

def format_db_for_prompt(devices):
    """Format device database compactly for the Claude prompt."""
    lines = []
    for key, dev in devices.items():
        lines.append(f"\n### {dev.get('brand','?')} {dev.get('model','?')}")
        lines.append(f"  CPU: {dev.get('cpu_options', dev.get('cpu','?'))}")
        lines.append(f"  RAM: {dev.get('ram_type','?')}, max {dev.get('ram_max_official','?')} official ({dev.get('ram_max_unofficial','?')})")
        lines.append(f"  Storage: {dev.get('storage','?')}")
        lines.append(f"  Netzwerk: {dev.get('network','?')}")
        lines.append(f"  PCIe: {dev.get('pcie_slots','Keine')}")
        lines.append(f"  Preis: {dev.get('price_range_german','?')}")
    return "\n".join(lines)

def get_anthropic_key():
    """Extract Anthropic API key from Hermes config."""
    with open("/root/.hermes/config.yaml") as f:
        for line in f:
            if line.strip().startswith("api_key:") and "sk-ant" in line:
                return line.split("api_key:")[1].strip()
    return None

def review_article(content):
    """Send article to Claude Sonnet 4.6 for critical review + improvement."""
    api_key = get_anthropic_key()
    if not api_key:
        print("ERROR: Could not find Anthropic API key")
        sys.exit(1)

    # Load device database
    devices = load_device_database()
    db_text = ""
    if devices:
        db_text = "\n\n### KANONISCHE GERÄTE-DATENBANK (Quelle der Wahrheit für Faktenchecks)\n" + format_db_for_prompt(devices)
        db_text += "\n\nPrüfe JEDE Hardware-Aussage im Artikel gegen diese Datenbank. Weiche NICHT von diesen Specs ab."

    print(f"📤 Sending article to Claude Sonnet 4.6...")

    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 8192,
        "system": f"""Du bist ein KRITISCHER deutschsprachiger Technik-Redakteur und Faktenprüfer.
Deine Aufgabe ist es, den folgenden Blog-Artikel über Homelab-Hardware GRÜNDLICH zu reviewen und zu verbessern.{db_text}

PFLICHT-CHECKLISTE (jeden Punkt prüfen!):
1. FAKTEN-CHECK mit Datenbank: Stimmen ALLE Hardware-Spezifikationen?
   - CPU-Modell, Kerne/Threads, Takt (z.B. i5-8500T = 6C/6T, KEIN Hyperthreading!)
   - RAM-Typ (DDR3/DDR4/DDR5) und Limits (offiziell UND inoffiziell)
   - Netzwerk-Spezifikationen exakt (1GbE/2,5GbE/10GbE)
   - Storage-Konfiguration (wie viele Slots, welcher Formfaktor)
   - Keine falschen oder geratenen Werte

2. WIDERSPRÜCHE: Gibt es im Artikel innere Widersprüche?
   - Wenn "2 Kerne minimum" gesagt wird, aber eine CPU 4 Kerne hat → korrigieren
   - Wenn eine CPU als "schwach" bezeichnet wird, aber mehr Kerne hat als eine andere als "stark" bezeichnete → prüfen

3. KLARHEIT: Ist die Preis-Range-Struktur klar?
   - Sind die Budget-Grenzen sinnvoll?
   - Passen die Empfehlungen zum Budget?

4. QUALITÄT: 
   - Rechtschreibung & Grammatik korrigieren
   - Satzfluss & Lesbarkeit verbessern
   - Call-to-Actions schärfer formulieren
   - Redundanzen entfernen

5. AMAZON-LINKS: Alle Links müssen ?tag=makmatas-homelab-21 enthalten.
   Keine Links entfernen oder ersetzen.

WICHTIG: Gib NUR den verbesserten vollständigen Artikel zurück (inkl. YAML-Frontmatter).
Keine Erklärungen, keine Zusammenfassung, kein "Ich habe folgendes geändert".
Wenn alles perfekt ist, gib den Artikel trotzdem zurück – aber korrigiere mindestens die kritischen Punkte.""",
        "messages": [{"role": "user", "content": f"Hier ist der SEO-Artikel zur Verbesserung:\n\n---\n{content}\n---\n\nBitte verbessere den Artikel und gib NUR den vollständigen verbesserten Artikel zurück."}]
    }

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode(),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read())
            for block in result.get("content", []):
                if block.get("type") == "text":
                    return block["text"]
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP {e.code}: {body[:300]}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    return None

def find_latest_article():
    """Find the most recently created article in the blog content directory."""
    blog_dir = "/root/homelab-blog/content/posts"
    if not os.path.exists(blog_dir):
        print(f"ERROR: {blog_dir} not found")
        sys.exit(1)

    # Find newest directory with index.md
    newest = None
    newest_time = 0
    for root, dirs, files in os.walk(blog_dir):
        for f in files:
            if f == "index.md":
                path = os.path.join(root, f)
                mtime = os.path.getmtime(path)
                if mtime > newest_time:
                    newest_time = mtime
                    newest = path

    if not newest:
        print("ERROR: No article found")
        sys.exit(1)

    print(f"📄 Found article: {newest}")
    return newest

def main():
    # Allow passing article path as argument, or find latest
    if len(sys.argv) > 1:
        article_path = sys.argv[1]
    else:
        article_path = find_latest_article()

    if not os.path.exists(article_path):
        print(f"ERROR: Article not found: {article_path}")
        sys.exit(1)

    # Read original
    with open(article_path) as f:
        original = f.read()

    print(f"📖 Original: {len(original)} chars")

    # Send to Claude for review
    improved = review_article(original)

    if not improved:
        print("ERROR: No response from Claude")
        sys.exit(1)

    # Clean up Claude's response - sometimes adds markdown code fences
    improved = improved.strip()
    if improved.startswith("```markdown"):
        improved = improved[11:]
    if improved.startswith("```"):
        improved = improved[3:]
    if improved.endswith("```"):
        improved = improved[:-3]
    improved = improved.strip()

    # Write improved version
    with open(article_path, "w") as f:
        f.write(improved + "\n")

    print(f"✅ Claude review complete: {len(improved)} chars")
    print(f"   +{len(improved) - len(original)} chars changed")
    print(f"   Saved to: {article_path}")

if __name__ == "__main__":
    main()
