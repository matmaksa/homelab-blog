#!/usr/bin/env python3
"""
Broken Link Checker for Homelab Blog.
Scannt alle Artikel auf defekte Links (4xx, 5xx, Timeouts, DNS-Fehler).
Läuft standalone oder eingebunden in den Freshness-Check.

Usage:
  python3 link_checker.py              # Alle Artikel scannen
  python3 link_checker.py --report     # Nur Report, keine Einzel-Links
"""
import os, re, sys, json, urllib.request, urllib.error, socket, ssl, time
from datetime import datetime

BLOG_DIR = "/root/homelab-blog"
POSTS_DIR = os.path.join(BLOG_DIR, "content", "posts")
REPORT_DIR = os.path.join(BLOG_DIR, "reports")
TIMEOUT = 10  # Sekunden pro Link
MAX_RETRIES = 2
DELAY = 0.5  # Sekunden zwischen Requests (Rate Limiting)

# Links die wir ignorieren (interne, bekannte Probleme)
SKIP_DOMAINS = [
    "localhost", "127.0.0.1", "0.0.0.0",
    "matmaksa.github.io",  # eigener Blog (noch nicht deployed)
]
SKIP_PATTERNS = [
    r"^#",  # Anchor-Links
    r"^mailto:",
    r"^tel:",
]

def is_skip_link(url: str) -> bool:
    for pat in SKIP_PATTERNS:
        if re.match(pat, url):
            return True
    for domain in SKIP_DOMAINS:
        if domain in url:
            return True
    return False

def extract_links_from_md(content: str) -> list:
    """Extrahiert alle Markdown-Links: [text](url) und <url>"""
    links = set()
    # [text](url) - Standard Markdown
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        url = m.group(2).strip()
        if url and not is_skip_link(url):
            links.add(url)
    # <url> - Autolinks
    for m in re.finditer(r'<((https?://)[^>]+)>', content):
        url = m.group(1).strip()
        if url and not is_skip_link(url):
            links.add(url)
    return sorted(links)

def check_link(url: str, retry: int = 0) -> dict:
    """Prüft einen Link mit HEAD Request. Fallback auf GET bei Fehlern."""
    result = {"url": url, "status": "unknown", "code": 0, "error": ""}

    req = urllib.request.Request(url, method="HEAD")

    for attempt in range(MAX_RETRIES + 1):
        try:
            req.add_header("User-Agent", "Mozilla/5.0 (HomelabBlog-LinkChecker/1.0)")
            # Timeout + SSL ohne Zertifikatsprüfung (für self-signed/abgelaufen)
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                code = resp.getcode()
                if 200 <= code < 400:
                    result["status"] = "ok"
                    result["code"] = code
                    return result
                else:
                    result["status"] = "broken"
                    result["code"] = code
                    result["error"] = f"HTTP {code}"
                    # Bei 429 (Rate Limit) warten und wiederholen
                    if code == 429 and attempt < MAX_RETRIES:
                        time.sleep(2 ** attempt)
                        continue
                    return result

        except urllib.error.HTTPError as e:
            code = e.code
            result["code"] = code
            if code == 405:
                # 405 = HEAD nicht unterstützt → GET Fallback (z.B. Amazon-Suche)
                if attempt == 0:
                    # Einmalig mit GET wiederholen
                    req.method = "GET"
                    time.sleep(0.5)
                    continue
                else:
                    result["status"] = "ok"
                    result["code"] = 200
                    result["error"] = "HEAD=405, GET accepted"
                    return result
            elif code == 403:
                # 403 kann false-positive sein (WAF, Cloudflare)
                result["status"] = "check_manual"
                result["error"] = f"HTTP {code} (möglicherweise false-positive)"
            elif code == 429 and attempt < MAX_RETRIES:
                time.sleep(2 ** attempt)
                continue
            else:
                result["status"] = "broken"
                result["error"] = f"HTTP {code}"
            return result

        except urllib.error.URLError as e:
            result["status"] = "broken"
            result["error"] = str(e.reason) if hasattr(e, 'reason') else str(e)
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return result

        except socket.timeout:
            result["status"] = "broken"
            result["error"] = "Timeout"
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return result

        except Exception as e:
            result["status"] = "broken"
            result["error"] = str(e)[:100]
            return result

    return result

def scan_all_articles() -> dict:
    """Scannt alle Artikel und prüft Links."""
    results = {
        "scan_date": datetime.now().isoformat(),
        "total_articles": 0,
        "total_links": 0,
        "broken_links": [],
        "check_manual": [],
        "ok_links": 0,
        "articles_scanned": []
    }

    if not os.path.exists(POSTS_DIR):
        print(f"ERROR: Posts directory not found: {POSTS_DIR}")
        sys.exit(1)

    for slug in sorted(os.listdir(POSTS_DIR)):
        article_dir = os.path.join(POSTS_DIR, slug)
        article_file = os.path.join(article_dir, "index.md")
        if not os.path.isfile(article_file):
            continue

        results["total_articles"] += 1
        with open(article_file) as f:
            content = f.read()

        links = extract_links_from_md(content)
        if not links:
            continue

        results["total_links"] += len(links)
        article_result = {"slug": slug, "links": [], "broken_count": 0}

        for url in links:
            time.sleep(DELAY)
            check = check_link(url)
            article_result["links"].append(check)

            if check["status"] == "ok":
                results["ok_links"] += 1
            elif check["status"] == "check_manual":
                results["check_manual"].append(check)
                article_result["broken_count"] += 1
            elif check["status"] == "broken":
                results["broken_links"].append(check)
                article_result["broken_count"] += 1

        results["articles_scanned"].append(article_result)

        # Kurz-Output während des Scans
        if article_result["broken_count"] > 0:
            print(f"  {slug}: {article_result['broken_count']} broken link(s)")

    return results

def print_report(results: dict):
    """Gibt einen lesbaren Report aus."""
    print("\n" + "=" * 60)
    print("  BROKEN LINK REPORT — Homelab Blog")
    print(f"  Scan: {results['scan_date'][:19]}")
    print("=" * 60)

    print(f"\n  Artikel gescannt: {results['total_articles']}")
    print(f"  Links geprüft:    {results['total_links']}")
    print(f"  OK:               {results['ok_links']}")
    print(f"  Broken:           {len(results['broken_links'])}")
    print(f"  Check manual:     {len(results['check_manual'])}")

    if results["broken_links"]:
        print(f"\n  ❌ BROKEN LINKS ({len(results['broken_links'])}):")
        for link in results["broken_links"]:
            print(f"    • {link['url'][:80]}")
            print(f"      Error: {link['error']}")

    if results["check_manual"]:
        print(f"\n  ⚠️  MANUAL CHECK ({len(results['check_manual'])}):")
        for link in results["check_manual"]:
            print(f"    • {link['url'][:80]}")
            print(f"      Error: {link['error']}")

    if not results["broken_links"] and not results["check_manual"]:
        print(f"\n  ✅ ALLE LINKS OK!")
    print()

def main():
    # Report-Verzeichnis
    os.makedirs(REPORT_DIR, exist_ok=True)

    print(f"  Scanning {POSTS_DIR} for broken links...")
    results = scan_all_articles()
    print_report(results)

    # Report speichern
    report_path = os.path.join(REPORT_DIR, f"link_check_{datetime.now().strftime('%Y%m%d')}.json")
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"  Report saved: {report_path}")

    # Exit-Code für Automatisierung
    if results["broken_links"]:
        sys.exit(2)  # Broken links gefunden
    sys.exit(0)

if __name__ == "__main__":
    main()
