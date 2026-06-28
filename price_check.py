#!/usr/bin/env python3
"""
Preis-Checker für den Homelab-Blog.
Öffnet Browser-Tabs für Amazon, Geizhals und Kleinanzeigen
zu jedem Gerät, damit aktuelle Preise ermittelt werden können.

Usage:
  python3 price_check.py --device hp_prodesk_400_g3
  python3 price_check.py --all          # Alle Geräte
  python3 price_check.py --report       # Nur Report alter Preise
"""
import os, sys, json, re, urllib.parse
from datetime import datetime, timedelta

BLOG_DIR = "/root/homelab-blog"
DEVICES_PATH = os.path.join(BLOG_DIR, "devices.yaml")
REPORTS_DIR = os.path.join(BLOG_DIR, "reports")
MAX_AGE_DAYS = 45  # Nach 45 Tagen als "veraltet" markieren

def load_devices():
    """Lädt devices.yaml und parst die Geräte."""
    try:
        import yaml
        with open(DEVICES_PATH) as f:
            data = yaml.safe_load(f)
        return data.get("devices", {})
    except ImportError:
        # Fallback: Manuelles Parsen
        return _parse_devices_fallback()

def _parse_devices_fallback():
    """Simple Fallback-Parsing ohne yaml-Lib."""
    devices = {}
    current = None
    with open(DEVICES_PATH) as f:
        for line in f:
            m = re.match(r'^\s+(\w+):$', line)
            if m and not line.startswith('  ' * 4):
                current = m.group(1)
                devices[current] = {"id": current}
            if current and 'price_range_german:' in line:
                devices[current]['price_range_german'] = line.split(':', 1)[1].strip().strip('"')
            if current and 'amazon_link:' in line:
                devices[current]['amazon_link'] = line.split(':', 1)[1].strip().strip('"')
    return devices

def get_search_urls(device_id, device):
    """Erzeugt Such-URLs für jedes Gerät."""
    name = device.get("model", device_id.replace("_", " "))
    brand = device.get("brand", "")
    search_terms = [brand, name] if brand else [name]
    query = " ".join(search_terms)

    return {
        "amazon": f"https://www.amazon.de/s?k={urllib.parse.quote(query)}&tag=matmaksa-homelab-21",
        "geizhals": f"https://geizhals.de/?fs={urllib.parse.quote(query)}&hloc=de",
        "kleinanzeigen": f"https://www.kleinanzeigen.de/s-{urllib.parse.quote(query.replace(' ', '-').lower())}/k0",
        "ebay": f"https://www.ebay.de/sch/i.html?_nkw={urllib.parse.quote(query)}&_sop=15",
    }

def check_price_age(device):
    """Prüft wie alt die Preisangabe ist."""
    price_date_str = device.get("price_date", "")
    if not price_date_str:
        return {"status": "missing", "days_old": None}

    try:
        price_date = datetime.strptime(price_date_str, "%Y-%m-%d")
        days_old = (datetime.now() - price_date).days
        if days_old > MAX_AGE_DAYS:
            return {"status": "stale", "days_old": days_old}
        return {"status": "fresh", "days_old": days_old}
    except ValueError:
        return {"status": "invalid_date", "days_old": None}

def main():
    devices = load_devices()
    if not devices:
        print("ERROR: No devices found in devices.yaml")
        sys.exit(1)

    os.makedirs(REPORTS_DIR, exist_ok=True)

    # Nur ein Gerät?
    target = None
    if "--device" in sys.argv:
        idx = sys.argv.index("--device")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]

    results = []
    for device_id, device in devices.items():
        if target and device_id != target:
            continue

        price_age = check_price_age(device)
        urls = get_search_urls(device_id, device)

        entry = {
            "id": device_id,
            "name": f"{device.get('brand', '')} {device.get('model', device_id)}",
            "current_price": device.get("price_range_german", "unbekannt"),
            "price_date": device.get("price_date", "nie geprüft"),
            "price_source": device.get("price_source", "unbekannt"),
            "price_age": price_age,
            "urls": urls,
        }
        results.append(entry)

        # Ausgabe
        age_icon = "🟢" if price_age["status"] == "fresh" else "🟡" if price_age["status"] == "stale" else "🔴"
        print(f"\n{age_icon} {entry['name']}")
        print(f"   Aktuell: {entry['current_price']} (Stand: {entry['price_date']})")
        print(f"   Quellen:")
        print(f"     Amazon:      {urls['amazon'][:80]}")
        print(f"     Geizhals:    {urls['geizhals'][:80]}")
        print(f"     Kleinanzeigen: {urls['kleinanzeigen'][:80]}")
        print(f"     eBay:        {urls['ebay'][:80]}")

    # Report speichern
    now = datetime.now()
    report = {
        "scan_date": now.isoformat(),
        "total_devices": len(results),
        "fresh": sum(1 for r in results if r["price_age"]["status"] == "fresh"),
        "stale": sum(1 for r in results if r["price_age"]["status"] == "stale"),
        "missing": sum(1 for r in results if r["price_age"]["status"] == "missing"),
        "devices": results,
    }
    report_path = os.path.join(REPORTS_DIR, f"price_check_{now.strftime('%Y%m%d')}.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport: {report_path}")

    # Nur Report-Modus
    if "--report" in sys.argv:
        print(f"\nPreis-Status: {report['fresh']} 🟢 frisch | {report['stale']} 🟡 veraltet | {report['missing']} 🔴 nie geprüft")
        return

    print(f"\n💡 Zum Prüfen der Preise die URLs im Browser öffnen.")
    print(f"   Nach Prüfung in devices.yaml aktualisieren: price_date und price_range_german.")

if __name__ == "__main__":
    main()
