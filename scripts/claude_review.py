#!/usr/bin/env python3
"""
Claude Quality Review – consolidated pipeline.
Replaces 3 separate Claude calls (fact-check, reader review, decision check)
with a SINGLE API call returning structured JSON.

Output JSON schema:
{
  "facts_ok": true/false,
  "spec_errors": [],
  "reader_score": 1-10,
  "reader_feedback": "",
  "purchase_clarity_score": 1-10,
  "purchase_feedback": "",
  "required_changes": []
}
"""
import json, urllib.request, urllib.error, sys, os, re, time

# Pipeline utilities
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from pipeline_utils import retry_api, log
from context_loader import get_claude_context

ANTHROPIC_KEY = None
DEVICES_PATH = "/root/homelab-blog/devices.yaml"

def get_anthropic_key() -> str:
    global ANTHROPIC_KEY
    if ANTHROPIC_KEY:
        return ANTHROPIC_KEY
    env_path = "/root/.hermes/.env"
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if "CUSTOM_PROVIDER_1_KEY" in line and not line.startswith("#"):
                    parts = line.split("=", 1)
                    if len(parts) == 2 and len(parts[1]) > 20:
                        ANTHROPIC_KEY = parts[1]
                        return ANTHROPIC_KEY
    # Fallback: config.yaml
    cfg_path = "/root/.hermes/config.yaml"
    if os.path.exists(cfg_path):
        with open(cfg_path) as f:
            for line in f:
                if "api_key:" in line and "sk-ant" in line:
                    ANTHROPIC_KEY = line.split("api_key:")[1].strip().strip("'\"")
                    return ANTHROPIC_KEY
    return None

def load_devices() -> str:
    if os.path.exists(DEVICES_PATH):
        with open(DEVICES_PATH) as f:
            return f.read()
    return ""

def run_review(article_content: str) -> dict:
    api_key = get_anthropic_key()
    if not api_key:
        print("ERROR: No Anthropic API key found")
        sys.exit(1)

    devices_yaml = load_devices()

    system_prompt = (
        "Du bist Chefredakteur eines technischen Homelab-Blogs. "
        "Deine Aufgabe ist NICHT Textverschönerung, "
        "sondern Qualitätskontrolle aus Sicht eines Käufers.\n\n"
        "=== Blog Kontext ===\n"
        f"{get_claude_context()}\n"
        "=== Ende Blog Kontext ===\n\n"
        "Prüfe den Artikel in EINEM Durchlauf auf drei Ebenen:\n"
        "1. FAKTEN: Stimmen Hardwaredaten gegen devices.yaml? Gibt es Widersprüche? "
        "Erfundene Angaben?\n"
        "2. LESERWERT: Wird die eigentliche Suchintention beantwortet? "
        "Gibt der Artikel eine echte Entscheidungshilfe?\n"
        "3. KAUFENTSCHEDUNG: Ist klar formuliert: Kaufen wenn... / Nicht kaufen wenn...?\n\n"
        "publish_ready=false setzen WENN:\n"
        "- wichtige Specs falsch sind\n"
        "- der Artikel nur Technik beschreibt ohne Bewertung\n"
        "- keine klare Zielgruppe erkennbar ist\n"
        "- keine echte Kaufentscheidung getroffen wird\n\n"
        "Ein schöner Text ist nicht automatisch ein guter Artikel.\n\n"
        "Antworte AUSSCHLIESSLICH mit einem validen JSON-Objekt. "
        "KEIN Markdown, KEINE Erklärungen, KEINE Codeblöcke. Nur das JSON."
    )

    user_prompt = (
        "Prüfe den folgenden SEO-Artikel.\n\n"
        f"--- DEVICES YAML (Referenz für Faktencheck) ---\n{devices_yaml}\n\n"
        f"--- ARTIKEL ---\n{article_content}\n\n"
        "--- AUFGABE ---\n"
        "Prüfe auf drei Ebenen und antworte NUR mit JSON:\n\n"
        "1. FAKTENCHECK: Stimmen CPU-Kerne, RAM, Netzwerk, Speicher-Pfade?\n"
        "2. LESER-REVIEW: Beantwortet der Artikel eine klare Leserfrage? (Score 1-10)\n"
        "3. KAUFENTSCHEDUNG: Ist die Empfehlung eindeutig? (Score 1-10)\n\n"
        'ERWARTETES JSON-SCHEMA:\n'
        '{\n'
        '  "facts_ok": true/false,\n'
        '  "spec_errors": [\n'
        '    {\n'
        '      "field": "ram",\n'
        '      "article_claim": "16GB",\n'
        '      "source_value": "8GB",\n'
        '      "source": "devices.yaml"\n'
        '    }\n'
        '  ],\n'
        '  "reader_score": 1-10,\n'
        '  "reader_feedback": "Kurze Begründung",\n'
        '  "purchase_clarity_score": 1-10,\n'
        '  "purchase_feedback": "Kurze Begründung",\n'
        '  "overall_quality_score": 1-10,\n'
        '  "publish_ready": true/false,\n'
        '  "required_changes": ["Liste der notwendigen Änderungen"]\n'
        '}\n\n'
        "Wichtig: Gib NUR das JSON zurück. Kein Markdown, kein Präfix, kein Suffix."
    )

    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 4096,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_prompt}],
        "temperature": 0.1,
    }

    @retry_api(max_attempts=3)
    def _call_claude(payload, api_key):
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps(payload).encode(),
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            }
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read())

    try:
        result = _call_claude(payload, api_key)
        text = ""
        for block in result.get("content", []):
            if block.get("type") == "text":
                text += block["text"]

        # Strip markdown code fences
        text = re.sub(r'^```(?:json)?\s*|\s*```$', '', text.strip(), flags=re.MULTILINE)
        parsed = json.loads(text)

        # Validate schema
        required_keys = ["facts_ok", "reader_score", "purchase_clarity_score",
                         "overall_quality_score", "publish_ready"]
        for key in required_keys:
            if key not in parsed:
                raise ValueError(f"Missing required key: {key}")

        return parsed

    except json.JSONDecodeError as e:
        print(f"ERROR: Claude returned invalid JSON: {e}")
        print(f"Raw: {text[:500]}")
        return {
            "facts_ok": False,
            "spec_errors": [{"field": "json", "article_claim": "parse_error", "source_value": f"JSON: {e}", "source": "claude_review.py"}],
            "reader_score": 0,
            "reader_feedback": "JSON parse error",
            "purchase_clarity_score": 0,
            "purchase_feedback": "JSON parse error",
            "overall_quality_score": 0,
            "publish_ready": False,
            "required_changes": ["Claude review failed - manual check required"]
        }
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP Error {e.code}: {body[:300]}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    article_path = sys.argv[1] if len(sys.argv) > 1 else None
    if not article_path:
        blog_dir = "/root/homelab-blog/content/posts"
        newest, newest_time = None, 0
        for root, dirs, files in os.walk(blog_dir):
            for f in files:
                if f == "index.md":
                    p = os.path.join(root, f)
                    mt = os.path.getmtime(p)
                    if mt > newest_time:
                        newest_time = mt
                        newest = p
        article_path = newest

    if not article_path or not os.path.exists(article_path):
        print("ERROR: No article found")
        sys.exit(1)

    with open(article_path) as f:
        content = f.read()

    print(f"  Article: {os.path.basename(os.path.dirname(article_path))}")
    print(f"  Size: {len(content)} chars")
    result = run_review(content)

    print(f"\n  Results:")
    print(f"    Facts OK:       {'✅' if result.get('facts_ok') else '❌'}")
    if result.get("spec_errors"):
        for err in result["spec_errors"]:
            if isinstance(err, dict):
                print(f"      Spec error: {err.get('field','?')} - Artikel: {err.get('article_claim','?')} / Soll: {err.get('source_value','?')} ({err.get('source','?')})")
            else:
                print(f"      Spec error: {err}")
    print(f"    Reader Score:   {result.get('reader_score', '?')}/10")
    print(f"    Purchase Score: {result.get('purchase_clarity_score', '?')}/10")
    print(f"    Overall Quality: {result.get('overall_quality_score', '?')}/10")
    print(f"    Publish Ready:  {'✅' if result.get('publish_ready') else '❌'}")
    if result.get("required_changes"):
        print(f"    Required changes:")
        for c in result["required_changes"]:
            print(f"      - {c}")

    # Save result next to article for deploy.py
    result_path = os.path.join(os.path.dirname(article_path), "review_result.json")
    with open(result_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n  Result saved: {result_path}")

if __name__ == "__main__":
    main()
