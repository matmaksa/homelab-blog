+++
title = "Home Assistant auf dem Mini-PC: Smarthome-Zentrale ab 40€"
description = "Home Assistant auf einem gebrauchten Mini-PC einrichten: Smarthome-Zentrale für unter 40€ mit Zigbee, Docker und tausenden kompatiblen Geräten."
date = 2026-06-24
draft = true
robotsNoIndex = true
sitemap = { exclude = true }
image = "featured.jpg"

[cover]
image = "featured.jpg"
alt = "Home Assistant auf einem Mini-PC – Smarthome-Zentrale für unter 100 Euro"
relative = true

[taxonomies]
tags = ["home-assistant", "smart-home", "mini-pc", "low-budget", "homelab", "zigbee", "docker"]
categories = ["Smarthome"]

[extra]
preview = true
draft = true
approved_for_publish = false
content_state = "draft"
audit_status = "pending"
user_approval_required = true
instagram_derivatives_required = true
instagram_derivatives_status = "planned"
content_cluster = "home-assistant"
content_role = "pillar"
risk_level = "medium"
next_action = "complete_instagram_derivative_review_and_cta_utm_check"
related_articles = ["mini-pc-homelab-vergleich", "fujitsu-futro-s7010-homelab-einstieg"]
notes = ["Neugeschrieben nach Redaktions-Feedback Juni 2026.", "Superlative entfernt, Raspberry Pi fair eingeordnet, Zigbee-Stick-Formulierung angepasst."]
+++
**Aktualisiert: Juni 2026 | Lesezeit: 6 Minuten**

Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.


Dein Zuhause soll intelligent werden: Licht schaltet sich automatisch aus, die Heizung regelt sich nach Anwesenheit und die Rollläden fahren bei Sonnenaufgang hoch. Dafür brauchst du eine Zentrale, die alle Geräte steuert.

**Home Assistant** ist eine kostenlose Open-Source-Software, die über 2.000 verschiedene Geräte und Dienste miteinander verbindet. Ein refurbished Mini-PC bietet dabei deutlich mehr Leistung als eine Fertig-Box wie der HA Green – und oft auch mehr als ein Raspberry Pi zum vergleichbaren Preis.

Dieser Artikel zeigt dir, welcher Mini-PC für dein Smart Home passt, was du außer dem PC noch brauchst und wie du alles zum Laufen bringst.

<!--more-->

---

## Kurzempfehlung

| Kategorie | Empfehlung | Preis |
|-----------|-----------|-------|
| Günstiger Einstieg | Fujitsu Futro S7010 + 8 GB RAM + Sonoff Zigbee-Stick | ~75 € |
| Passend für größere Installationen | HP ProDesk 400 G4 (i5, 2 RAM-Slots) | ~120 € |
| Passend für Home Assistant + KI | Lenovo M720q Tiny (6 Kerne, PCIe-Slot) | ~150 € |
| Passend für Einsteiger (Neugerät) | GMKtec G3S (Garantie, kein Gebrauchtkauf) | ~210 € |

---

## Warum ein Mini-PC – und was ist mit dem Raspberry Pi?

Der **Raspberry Pi** ist eine solide Wahl für Home Assistant, gerade wenn du GPIO-Pins nutzen möchtest oder bereits einen besitzt. Für die meisten Zigbee- und WLAN-Setups reicht er aus. Seine Schwäche zeigt sich, wenn zusätzliche Dienste wie Frigate (Kameraerkennung) oder lokale KI-Sprachassistenten dazukommen – dann stoßen 4–8 GB RAM und die ARM-CPU schneller an ihre Grenzen.

Ein **x86-Mini-PC** hat andere Stärken: SSD statt SD-Karte (zuverlässiger im Dauerbetrieb), aufrüstbarer RAM und in der Regel mehr CPU-Reserven. Refurbished Business-Geräte kosten dabei oft weniger als ein Raspberry Pi 5 mit allem Zubehör.

| Kriterium | Mini-PC (Refurbished) | Raspberry Pi 5 (neu) |
|-----------|----------------------|----------------------|
| **Preis komplett** | 45–150 € (inkl. RAM, SSD, Netzteil) | ~120 € (nur Board + Gehäuse + SD-Karte + Netzteil) |
| **Speicher** | SSD – schnell, langlebig | SD-Karte – fällt bei Dauerbetrieb öfter aus |
| **RAM** | 8–16 GB (aufrüstbar) | 4–8 GB (fest verlötet) |
| **Stromverbrauch** | 4–14 Watt | 8–15 Watt |
| **Erweiterbarkeit** | RAM + SSD wechselbar, PCIe bei Lenovo | Nur USB + GPIO |
| **GPIO** | ❌ Nicht vorhanden | ✅ Vorhanden |

**Fazit:** Für GPIO-Projekte ist der Raspberry Pi sinnvoll. Für reine Smarthome-Zentralen mit Zigbee, Z-Wave und WLAN ist ein Mini-PC oft die praktischere Wahl.

---

## Bis 60 € – Fujitsu Futro S7010

**Ich betreibe genau dieses Modell in meinem eigenen Setup.** Der Fujitsu Futro S7010 ist **lüfterlos** (absolut lautlos), verbraucht wenig Strom und ist gebraucht schon ab rund 30–40 € zu finden.

| Komponente | Spezifikation |
|------------|--------------|
| **CPU** | Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 W) |
| **RAM** | 1 Slot DDR4 – offiziell max. 8 GB, **16 GB getestet** |
| **SSD** | 1× M.2 2280 – **nur SATA** (kein NVMe!) |
| **Netzwerk** | 1× Realtek Gigabit Ethernet |
| **Kühlung** | **Lüfterlos** – absolut lautlos |
| **Strom (Idle)** | 4–8 Watt |
| **Preis** | **30–50 € gebraucht** |
| **HA OS** | ✅ Ja – läuft flüssig |
| **Optimal für** | HA OS, Zigbee, Shelly, ESPHome, Automationen |
| **Add-ons** | Zigbee2MQTT, Node-RED, ESPHome |
| **KI-Sprache** | ❌ Nicht empfohlen |

**Aus meiner Erfahrung:** Der S7010 läuft seit Monaten stabil mit Home Assistant OS, 16 GB RAM und einer 64 GB M.2 SATA SSD. Über 20 Zigbee-Geräte, mehrere Shelly-WLAN-Steckdosen und diverse Automationen laufen flüssig ohne spürbare Verzögerungen. Der einzige Moment, wo er kurz nachdenkt: beim Start nach einem Update.

**Zur Einordnung:** Zigbee- und Shelly-Geräte sind für den Futro kein Problem. Der wahre Hardware-Fresser sind **Kameras (Frigate)** und **lokale KI-Sprachassistenten**. Wer diese zusätzlich betreiben will, braucht ein leistungsstärkeres Modell.

**Orientierung – welcher PC für welches Setup:**
- Nur HA + Zigbee/Shelly → **Futro S7010** reicht
- HA + 2–4 Kameras (Frigate) → **HP ProDesk 400 G4** oder **Dell OptiPlex 3070**
- HA + Proxmox + viele VMs + Frigate + lokale KI → **Lenovo M720q** oder **GMKtec G3S**

**⚠️ Dual-Rank-Riegel nötig:** Für 16 GB brauchst du einen **Dual-Rank-Riegel (2Rx8)**. Single-Rank wird nicht erkannt – der Futro bootet dann nicht. Geprüfter Riegel: Samsung M471A2K43BB1-CRC.

**💡 DisplayPort:** Der Futro hat DisplayPort, nicht HDMI. Falls du nur einen HDMI-Monitor hast, brauchst du einen Adapter (~5–7 €).

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

## Upgrade-Modelle auf einen Blick

Wer mehr Leistung braucht (Kameras mit Frigate, lokale KI-Sprachassistenten, Parallelbetrieb mehrerer Dienste), findet hier die Alternativen:

| Gerät | CPU | RAM | SSD | Lüfterlos? | Idle (W) | Preis | Amazon |
|-------|-----|-----|-----|-----------|----------|-------|--------|
| **Futro S7010** | J4125 (4C) | 1 Sl. max 16 GB | M.2 SATA only | ✅ Ja | 4–8 | ~45 € | 🔍 [Suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| **HP ProDesk 400 G4** | i5-8500T (6C) | 2 Sl. max 32 GB | NVMe + SATA | ❌ Nein | 8–14 | ~120 € | 🔍 [Suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=matmaksa-homelab-21) |
| **Dell OptiPlex 3070** | i5-9500T (6C) | 2 Sl. max 32 GB | NVMe + SATA | ❌ Nein | 6–12 | ~130 € | 🔍 [Suchen](https://www.amazon.de/s?k=Dell+OptiPlex+3070+Micro&tag=matmaksa-homelab-21) |
| **Lenovo M720q Tiny** | i5-8500T (6C) | 2 Sl. max 64 GB | NVMe + SATA | ❌ Nein | 6–12 | ~150 € | 🔍 [Suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=matmaksa-homelab-21) |
| **GMKtec G3S** (neu) | N95 (4C) | 1 Sl. max 16 GB | M.2 NVMe | ❌ Nein | 5–8 | ~210 € | 🔍 [Suchen](https://www.amazon.de/s?k=GMKtec+G3S+N95&tag=matmaksa-homelab-21) |

**Kurz gesagt:** Der HP ProDesk ist ein solider Allrounder mit 6 Kernen und 2 RAM-Slots. Der Lenovo M720q hat den seltenen PCIe-Slot für Erweiterungen. Der GMKtec G3S ist das Neugerät mit Garantie – passend für alle, die keinen Gebrauchtkauf möchten.

**Bezugsquellen für Refurbished-Mini-PCs:** Gute Angebote findest du auf **eBay** und **Kleinanzeigen**. Spezialisierte Händler mit Gewährleistung sind **AfB** (Social Green IT), **ITSCO** und **GreenPanda** – dort bekommst du geprüfte Business-Geräte oft mit 12 Monaten Garantie.

| Dauerverbrauch | Stromkosten / Jahr (bei 35 ct/kWh) |
|----------------|-----------------------------------|
| 5 W (Futro S7010) | ~15 € |
| 10 W (HP/Dell) | ~31 € |
| 15 W (Lenovo M720q) | ~46 € |

---

## Was brauchst du außer dem Mini-PC?

### 1. Zigbee-USB-Stick (wenn du Zigbee-Geräte nutzen möchtest)

Für WLAN-Geräte wie Shelly brauchst du keinen Stick – die werden direkt per Netzwerk eingebunden. Wenn du Zigbee-Sensoren oder Aktoren verwenden willst, empfiehlt sich einer der folgenden Sticks:

| Stick | Preis | Besonderheit |
|-------|-------|-------------|
| **Sonoff Zigbee 3.0 USB Dongle P** | ~15–20 € | Günstig, zuverlässig, große Community |
| **Home Assistant Connect ZBT-2** | ~35 € | Offizielles HA-Zubehör, Matter-kompatibel |
| **Conbee II** | ~30–35 € | Ausgereift, breite Geräteunterstützung |
| **TubeZB PoE** | ~40 € | Per LAN-Kabel statt USB eingebunden |

🔍 [Sonoff Zigbee 3.0 USB Dongle P bei Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21)

### 2. Empfohlene Sensoren für den Start

| Gerät | Preis | Wofür? |
|-------|-------|--------|
| **Aqara Temperatursensor** | ~12 € | Raumtemperatur + Luftfeuchtigkeit |
| **Aqara Bewegungsmelder** | ~15 € | Licht automatisch schalten |
| **Aqara Fenster-/Türkontakt** | ~10 € | Fenster offen? Heizung aus |
| **Sonoff Smart Plug S40** | ~10 € | Steckdose schalten + Strom messen |

> **💡 Aus meiner Erfahrung:** Fang mit einem **Bewegungsmelder** und einem **Temperatursensor** an. Licht schaltet sich automatisch an, wenn du den Raum betrittst – das motiviert für weitere Automatisierungen.

### 3. Speicher (SSD) – Achtung Kompatibilität!

| Gerät | SSD-Typ | Empfehlung |
|-------|---------|------------|
| **Futro S7010** | **M.2 SATA only** – kein NVMe! | WD Blue SA510 |
| **HP, Dell, Lenovo, GMKtec** | M.2 NVMe (schnell) | Kingston NV3 |

> **Wichtig:** Der Futro akzeptiert **keine NVMe-SSD**. Sie passt mechanisch, wird aber nicht erkannt.

---

## Installation: So richtest du Home Assistant ein

### Weg 1: Home Assistant OS (empfohlen)

1. **Image laden:** [home-assistant.io/installation](https://www.home-assistant.io/installation/) → "Home Assistant OS" für x86_64
2. **Auf USB schreiben:** Mit **Balena Etcher** (kostenlos) auf einen USB-Stick (mind. 4 GB)
3. **Booten:** Monitor (DisplayPort), Tastatur, LAN-Kabel anschließen, USB-Stick einstecken. Beim Einschalten **F2/F10/F12** drücken → USB als Boot-Laufwerk wählen
4. **Warten:** Nach ~5–10 Minuten ist die Installation fertig
5. **Öffnen:** Browser → **http://homeassistant.local:8123**
6. **Zigbee-Stick einstecken:** HA erkennt ihn automatisch (sofern vorhanden)

### Weg 2: Home Assistant Container (für Fortgeschrittene)

Linux installieren (Ubuntu Server LTS), dann Home Assistant als Docker-Container. So laufen Pi-hole, Paperless-ngx und andere Dienste parallel auf demselben Gerät.

> **💡 Starte mit Home Assistant OS.** Du kannst später auf Container umsteigen – deine Konfiguration bleibt erhalten.

---

## Drei häufige Fehler beim Start

**1. "Bootet nicht vom USB-Stick"** → Direkt nach Einschalten **mehrmals schnell** F2/F10/F12 drücken.

**2. "Zigbee-Stick wird nicht erkannt"** → Stick erst **nach** der Installation einstecken. Bei Problemen: USB-2.0-Port probieren (schwarz, nicht blau).

**3. "Kein Zugriff auf die Weboberfläche"** → Mini-PC und Computer müssen im selben Netzwerk sein. Browser → http://homeassistant.local:8123

---

## FAQ

**Kann Home Assistant auch mit WLAN-Geräten umgehen?** Ja. WLAN-Geräte (TP-Link, Shelly) werden direkt per Netzwerk eingebunden – kein Zigbee-Stick nötig.

**Wie viel RAM brauche ich?** HA selbst benötigt 1–2 GB. Mit Add-ons sind 4 GB komfortabel. Ab 8 GB hast du Reserven für Kameras (Frigate) oder lokale KI.

**Kann ich meinen Raspberry Pi umziehen?** Ja. Backup exportieren, auf Mini-PC installieren, Backup wiederherstellen – alle Geräte und Automationen sind sofort da.

---

## Ausblick: Wenn dein Smart Home größer wird

Viele Nutzer starten mit Home Assistant und merken, dass ihr Mini-PC noch mehr kann. Irgendwann kommen weitere Self-Hosting-Dienste dazu – und aus der Smarthome-Zentrale wird ein kleiner Heimserver.

**Typische Dienste, die auf dem gleichen Rechner laufen können:**

* **AdGuard Home** – Werbeblocker fürs ganze Netzwerk
* **Paperless-ngx** – Dokumentenverwaltung, digitales Archiv
* **Immich** – Self-hosted Foto-Verwaltung als Alternative zu Google Photos
* **Jellyfin** – eigener Streaming-Server für Filme und Serien
* **Frigate** – Kamera-Überwachung mit KI-Objekterkennung

Wer Frigate, Immich oder lokale KI-Modelle in Home Assistant einsetzen möchte, sollte das bei der Hardware-Wahl einplanen. Für diese Ausbaustufe reicht der Futro S7010 nicht mehr aus – hier sind der HP ProDesk oder Lenovo M720q die passenden Optionen.

**Welches Setup passt zu deinem geplanten Ausbau?**

| Geplante Nutzung | Empfehlung |
|-----------------|------------|
| Nur Home Assistant | Futro-Setup |
| Home Assistant + einige zusätzliche Dienste | HP-Setup |
| Proxmox, mehrere Container/VMs, Frigate, KI | Lenovo-Setup |

---

## Drei Starter-Konfigurationen – von Budget bis Homelab

Je nach Budget und Zielsetzung gibt es drei klare Pfade.

### Das 80€-Budget-Setup (für Einsteiger)
| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC** | Fujitsu Futro S7010 (gebraucht) | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| **RAM** | 8 GB DDR4 SO-DIMM | ~15 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DDR4+8GB+SO-DIMM&tag=matmaksa-homelab-21) |
| **SSD** | 64 GB M.2 SATA | ~10 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=M.2+SATA+64GB+SSD&tag=matmaksa-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |

### Das 150€-Power-Setup (für Smarthome-Fans)
| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC** | HP ProDesk 400 G4 (gebraucht) | ~100 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=matmaksa-homelab-21) |
| **RAM** | 16 GB DDR4 SO-DIMM | ~25 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=16GB+DDR4+SO-DIMM&tag=matmaksa-homelab-21) |
| **SSD** | 256 GB M.2 NVMe | ~25 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=256GB+M.2+NVMe+SSD&tag=matmaksa-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |

### Das 250€-Homelab-Setup (für Enthusiasten)
| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC** | Lenovo M720q Tiny (gebraucht) | ~150 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=matmaksa-homelab-21) |
| **RAM** | 32 GB DDR4 SO-DIMM | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=32GB+DDR4+SO-DIMM&tag=matmaksa-homelab-21) |
| **SSD** | 512 GB M.2 NVMe | ~40 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=512GB+M.2+NVMe+SSD&tag=matmaksa-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |

---

## Fazit

| Budget | Empfehlung |
|--------|-----------|
| **~45–75 €** | Fujitsu Futro S7010 + Sonoff-Stick – günstiger Einstieg |
| **~120–150 €** | HP ProDesk 400 G4 – solide Leistung für Frigate und mehrere Dienste |
| **~150–200 €** | Lenovo M720q + 32 GB RAM – passend für KI-Erweiterungen und Proxmox |

Home Assistant auf einem Mini-PC bietet mehr Leistung als ein Raspberry Pi, kostet weniger als Fertig-Boxen und lässt sich später aufrüsten. Wer mit Zigbee-Sensoren und Shelly-Steckdosen starten möchte, ist mit dem Fujitsu Futro S7010 für rund 45 € gut aufgestellt.

**Konkrete Empfehlung für den Einstieg:** Fujitsu Futro S7010 (~45 €) und – wenn du Zigbee-Geräte nutzen möchtest – einen Sonoff Zigbee-Stick (~18 €) dazu. Zusammen unter 65 € für eine leise, stromsparende Smarthome-Zentrale. Das gesparte Geld investierst du in die ersten Sensoren.