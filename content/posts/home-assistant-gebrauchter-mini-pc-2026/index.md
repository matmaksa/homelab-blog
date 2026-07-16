---
title: "Home Assistant auf dem Mini-PC: Smarthome-Zentrale ab 40€"
description: "Home Assistant auf einem gebrauchten Mini-PC: Hardware-Auswahl, Kosten, Grenzen und Kaufentscheidung für die Smarthome-Zentrale."
date: 2026-06-24
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Home Assistant auf einem Mini-PC – Smarthome-Zentrale für unter 100 Euro"
  relative: true
tags:
  - home-assistant
  - smart-home
  - mini-pc
  - low-budget
  - homelab
  - zigbee
  - docker
categories:
  - Smarthome

# Production State Flow
content_state: "published"
audit_status: "passed"
user_approval_required: false
approved_for_publish: true
instagram_derivatives_required: true
instagram_derivatives_status: "planned"
content_cluster: "home-assistant"
content_role: "pillar"
risk_level: "medium"
next_action: "complete_instagram_derivative_review_and_cta_utm_check"
related_articles:
  - "mini-pc-homelab-vergleich"
  - "fujitsu-futro-s7010-homelab-einstieg"
notes:
  - "Published Home Assistant pillar article."
  - "Instagram derivatives exist but still need review/CTA/UTM checks."
---
**Aktualisiert: Juni 2026 | Lesezeit: 6 Minuten**

Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.


Dein Zuhause soll intelligent werden: Licht schaltet sich automatisch aus, die Heizung regelt sich nach Anwesenheit und die Rollläden fahren bei Sonnenaufgang hoch. Dafür brauchst du eine Zentrale, die alle Geräte steuert.

**Home Assistant** ist die beste Lösung dafür – eine kostenlose Open-Source-Software, die über 2.000 verschiedene Geräte und Dienste miteinander verbindet. Raspberry Pi und Home Assistant Green sind einfacher Einstieg, ein gebrauchter Mini-PC bietet oft mehr Leistung fürs Geld – aber nicht jeder braucht das.

Dieser Artikel zeigt dir, welcher Mini-PC für dein Smart Home am besten geeignet ist und was du außer dem PC noch brauchst.

<!--more-->

---

## 🥇 Kurzempfehlung

| Kategorie | Empfehlung | Preis |
|-----------|-----------|-------|
| 🥇 Preis-Leistung | Fujitsu Futro S7010 + 8 GB RAM + Sonoff Zigbee-Stick | ~75 € |
| 🚀 Für große Installationen | HP ProDesk 400 G4 (i5, 2 RAM-Slots) | ~120 € |
| 🏠 Home Assistant + KI | Lenovo M720q Tiny (6 Kerne, PCIe-Slot) | ~150 € |
| 🔧 Für Einsteiger (Neugerät) | GMKtec G3S (Garantie, kein Gebrauchtkauf) | ~210 € |

---

## Warum ein Mini-PC statt Raspberry Pi?

Home Assistant läuft auch auf einem Raspberry Pi – ein **x86-Mini-PC** bietet jedoch mehr Reserve für aufwendigere Setups mit Kameras, KI oder mehreren parallelen Diensten. Wer nur ein paar Zigbee-Geräte und Automationen steuern will, kommt mit einem Raspberry Pi 5 oder Home Assistant Green ebenfalls gut zurecht.

| Kriterium | Mini-PC (Refurbished) | Raspberry Pi 5 (neu) |
|-----------|----------------------|----------------------|
| **Preis komplett** | 45–150 € (inkl. RAM, SSD, Netzteil) | ~120 € (nur Board + Gehäuse + SD-Karte + Netzteil) |
| **Speicher** | SSD – schnell, langlebig | SD-Karte – fällt bei Dauerbetrieb oft aus |
| **RAM** | 8–16 GB (aufrüstbar) | 4–8 GB (fest) |
| **Stromverbrauch** | 4–14 Watt | 8–15 Watt |
| **Erweiterbarkeit** | RAM+SSD wechselbar, PCIe bei Lenovo | Nur USB + GPIO |

**Einziger Vorteil Raspberry Pi:** Der GPIO-Anschluss. Für 99 % aller Home-Assistant-Nutzer ist das irrelevant – Zigbee, Z-Wave und WLAN-Geräte werden per USB-Stick angebunden.

---

## 💰 Bis 60 € – Fujitsu Futro S7010 (Der 40-Euro-Held)

**Ich betreibe genau dieses 40-Euro-Modell in meinem eigenen Setup.** Der Fujitsu Futro S7010 ist der absolute Preis-Leistungs-Champion: Er ist **lüfterlos** (absolut lautlos), verbraucht kaum Strom und kostet mit Gebraucht-Glück schon **unter 40 €**.

| Komponente | Spezifikation |
|------------|--------------|
| **CPU** | Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 W) |
| **RAM** | 1 Slot DDR4 – offiziell max. 8 GB, **16 GB getestet** |
| **SSD** | 1× M.2 2280 – **nur SATA** (kein NVMe!) |
| **Netzwerk** | 1× Realtek Gigabit Ethernet |
| **Kühlung** | **Lüfterlos** – absolut lautlos |
| **Strom (Idle)** | 4–8 Watt |
| **Preis** | **30–50 € gebraucht** |
| **HA OS** | ✅ Ja – läuft flüssig |
| **Optimal für** | HA OS, Zigbee, Shelly, ESPHome, Automationen |
| **Add-ons** | Zigbee2MQTT, Node-RED, ESPHome |
| **KI-Sprache** | ❌ Nicht empfohlen |

**Aus meiner Erfahrung:** Der S7010 läuft seit Monaten stabil mit Home Assistant OS, 16 GB RAM und einer 64 GB M.2 SATA SSD. Über 20 Zigbee-Geräte, mehrere Shelly-WLAN-Steckdosen und diverse Automationen – alles flüssig, keine Verzögerungen. Der einzige Moment, wo er nachdenkt: Beim Start von Home Assistant nach einem Update.

**Zur Einordnung:** Reine Zigbee- und Shelly-Geräte sind für den Futro kein Problem – die Home-Assistant-Automation läuft flüssig, auch mit vielen Sensoren und Aktoren. Der wahre Hardware-Fresser sind **Kameras (Frigate)** und **lokale KI-Sprachassistenten**. Wer diese zusätzlich betreiben will, braucht ein Upgrade-Modell.

**Orientierung – welcher PC für welches Setup:**
- Nur HA + Zigbee/Shelly → **Futro S7010** reicht völlig
- HA + 2–4 Kameras (Frigate) → **HP ProDesk 400 G4** oder **Dell OptiPlex 3070**
- HA + Proxmox + viele VMs + Frigate + lokale KI → **Lenovo M720q** oder **GMKtec G3S**

**⚠️ Dual-Rank-Riegel nötig:** Für 16 GB brauchst du zwingend einen **Dual-Rank-Riegel (2Rx8)**. Single-Rank wird nicht erkannt – der Futro bootet dann nicht. Geprüfter Riegel: Samsung M471A2K43BB1-CRC.

**💡 DisplayPort:** Der Futro hat DisplayPort, nicht HDMI. Falls du nur einen HDMI-Monitor hast, brauchst du einen Adapter (~5–7 €).

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

## 💰 Upgrade-Modelle auf einen Blick

Wer mehr Leistung braucht (Kameras mit Frigate, lokale KI-Sprachassistenten, Parallelbetrieb mehrerer Dienste), findet hier die Alternativen:

| Gerät | CPU | RAM | SSD | Lüfterlos? | Idle (W) | Preis | Amazon |
|-------|-----|-----|-----|-----------|----------|-------|--------|
| **Futro S7010** | J4125 (4C) | 1 Sl. max 16 GB | M.2 SATA only | ✅ Ja | 4–8 | ~45 € | 🔍 [Suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| **HP ProDesk 400 G4** | i5-8500T (6C) | 2 Sl. max 32 GB | NVMe + SATA | ❌ Nein | 8–14 | ~120 € | 🔍 [Suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=matmaksa-homelab-21) |
| **Dell OptiPlex 3070** | i5-9500T (6C) | 2 Sl. max 32 GB | NVMe + SATA | ❌ Nein | 6–12 | ~130 € | 🔍 [Suchen](https://www.amazon.de/s?k=Dell+OptiPlex+3070+Micro&tag=matmaksa-homelab-21) |
| **Lenovo M720q Tiny** | i5-8500T (6C) | 2 Sl. max 64 GB | NVMe + SATA | ❌ Nein | 6–12 | ~150 € | 🔍 [Suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=matmaksa-homelab-21) |
| **GMKtec G3S** (neu) | N95 (4C) | 1 Sl. max 16 GB | M.2 NVMe | ❌ Nein | 5–8 | ~210 € | 🔍 [Suchen](https://www.amazon.de/s?k=GMKtec+G3S+N95&tag=matmaksa-homelab-21) |

**Kurz gesagt:** Der HP ProDesk ist der beste Allrounder (6 Kerne, 2 RAM-Slots, günstig). Der Lenovo M720q hat den seltenen PCIe-Slot für Erweiterungen. Der GMKtec G3S ist das Neugerät mit Garantie.

**Bezugsquellen für Refurbished-Mini-PCs:** Gute Angebote findest du auf **eBay** und **Kleinanzeigen**. Spezialisierte Händler mit Gewährleistung sind **AfB** (Social Green IT), **ITSCO** und **GreenPanda** – dort bekommst du geprüfte Business-Geräte oft mit 12 Monaten Garantie.

| Dauerverbrauch | Stromkosten / Jahr (bei 35 ct/kWh) |
|----------------|-----------------------------------|
| 5 W (Futro S7010) | ~15 € |
| 10 W (HP/Dell) | ~31 € |
| 15 W (Lenovo M720q) | ~46 € |

---

## Was brauchst du außer dem Mini-PC?

### 1. Zigbee-USB-Stick (nur nötig, wenn du Zigbee-Geräte verwendest)

| Stick | Preis | Besonderheit |
|-------|-------|-------------|
| **Sonoff Zigbee 3.0 USB Dongle P** | ~15–20 € | Günstig, zuverlässig, große Community – die erste Wahl |
| **Home Assistant Connect ZBT-2** | ~35 € | Offizielles HA-Zubehör, matter-kompatibel |
| **Conbee II** | ~30–35 € | Sehr ausgereift |
| **TubeZB PoE** | ~40 € | Mit PoE – per LAN-Kabel statt USB |

🔍 [Sonoff Zigbee 3.0 USB Dongle P bei Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21)

### 2. Empfohlene Sensoren für den Start

| Gerät | Preis | Wofür? |
|-------|-------|--------|
| **Aqara Temperatursensor** | ~12 € | Raumtemperatur + Luftfeuchtigkeit |
| **Aqara Bewegungsmelder** | ~15 € | Licht automatisch schalten |
| **Aqara Fenster-/Türkontakt** | ~10 € | Fenster offen? Heizung aus |
| **Sonoff Smart Plug S40** | ~10 € | Steckdose schalten + Strom messen |

> **💡 Meiner Erfahrung nach:** Fang mit einem **Bewegungsmelder** und einem **Temperatursensor** an. Licht schaltet sich automatisch an, wenn du den Raum betrittst – das motiviert ungemein.

### 3. Speicher (SSD) – Achtung Kompatibilität!

| Gerät | SSD-Typ | Empfehlung |
|-------|---------|------------|
| **Futro S7010** | **M.2 SATA only** – kein NVMe! | WD Blue SA510 |
| **HP, Dell, Lenovo, GMKtec** | M.2 NVMe (schnell) | Kingston NV3 |

> **Wichtig:** Der Futro akzeptiert **keine NVMe-SSD**. Sie passt mechanisch, wird aber nicht erkannt.

---

## Installation

Die ausführliche Installationsanleitung findest du im separaten Artikel:
👉 [Home Assistant OS auf einem Mini-PC installieren]({{< relref "home-assistant-os-mini-pc-installieren" >}})

Dieser Artikel konzentriert sich auf die Hardware-Auswahl und Kaufentscheidung.

---

## Drei häufige Fehler beim Start

**1. "Bootet nicht vom USB-Stick"** → Direkt nach Einschalten **mehrmals schnell** F2/F10/F12 drücken.

**2. "Zigbee-Stick wird nicht erkannt"** → Stick erst **nach** der Installation einstecken. Bei Problemen: USB-2.0-Port probieren (schwarz, nicht blau).

**3. "Kein Zugriff auf die Weboberfläche"** → Mini-PC und Computer im selben Netzwerk. Browser → http://homeassistant.local:8123

---

## FAQ

**Kann Home Assistant auch mit WLAN-Geräten umgehen?** Ja. WLAN-Geräte (TP-Link, Shelly) werden direkt per Netzwerk eingebunden – kein Zigbee-Stick nötig.

**Wie viel RAM brauche ich?** HA selbst: 1–2 GB. Mit Add-ons: 4 GB komfortabel. Ab 8 GB Reserven für Kameras (Frigate) oder KI.

**Kann ich meinen Raspberry Pi umziehen?** Ja. Backup exportieren, auf Mini-PC installieren, Backup wiederherstellen – alle Geräte und Automationen sind sofort da.

---

## Ausblick: Wenn dein Smart Home größer wird

Frigate, Immich und lokale KI sind mögliche spätere Ausbauoptionen – für den Start nicht nötig.

Viele Nutzer starten mit Home Assistant und merken schnell, dass ihr Mini-PC noch mehr kann. Irgendwann kommen weitere Self-Hosting-Dienste dazu – und aus der Smarthome-Zentrale wird ein kleiner Heimserver.

**Typische Dienste, die auf dem gleichen Rechner laufen können:**

* **AdGuard Home** – Werbeblocker fürs ganze Netzwerk
* **Paperless-ngx** – Dokumentenverwaltung, digitales Archiv
* **Immich** – Self-hosted Google-Fotos-Alternative
* **Jellyfin** – eigener Streaming-Server für Filme und Serien
* **Frigate** – Kamera-Überwachung mit KI-Objekterkennung

**Welches Setup passt zu deinem geplanten Ausbau?**

| Geplante Nutzung | Empfehlung |
|-----------------|------------|
| Nur Home Assistant | Futro-Setup |
| Home Assistant + einige zusätzliche Dienste | HP-Setup |
| Proxmox, mehrere Container/VMs, Frigate | Lenovo-Setup |

---

## 🛒 Drei Starter-Konfigurationen – von Budget bis Homelab

Je nach Budget und Zielsetzung gibt es drei klare Pfade.

### Das 80€-Budget-Setup (für Einsteiger)
| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC** | Fujitsu Futro S7010 (gebraucht) | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| **RAM** | 8 GB DDR4 SO-DIMM | ~15 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DDR4+8GB+SO-DIMM&tag=matmaksa-homelab-21) |
| **SSD** | 64 GB M.2 SATA | ~10 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=M.2+SATA+64GB+SSD&tag=matmaksa-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |

### Das 150€-Power-Setup (für Smarthome-Fans)
| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC** | HP ProDesk 400 G4 (gebraucht) | ~100 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=matmaksa-homelab-21) |
| **RAM** | 16 GB DDR4 SO-DIMM | ~25 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=16GB+DDR4+SO-DIMM&tag=matmaksa-homelab-21) |
| **SSD** | 256 GB M.2 NVMe | ~25 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=256GB+M.2+NVMe+SSD&tag=matmaksa-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |

### Das 250€-Homelab-Setup (für Enthusiasten)
| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC** | Lenovo M720q Tiny (gebraucht) | ~150 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=matmaksa-homelab-21) |
| **RAM** | 32 GB DDR4 SO-DIMM | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=32GB+DDR4+SO-DIMM&tag=matmaksa-homelab-21) |
| **SSD** | 512 GB M.2 NVMe | ~40 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=512GB+M.2+NVMe+SSD&tag=matmaksa-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=matmaksa-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |

---

## Fazit

| Budget | Empfehlung |
|--------|-----------|
| **~45–75 €** | Fujitsu Futro S7010 + Sonoff-Stick – günstigster Einstieg |
| **~120–150 €** | HP ProDesk 400 G4 – solide Leistung für Frigate und mehrere Dienste |
| **~150–200 €** | Lenovo M720q + 32 GB RAM – KI + Erweiterbarkeit |

Home Assistant auf einem Mini-PC ist **der beste Weg ins Smart Home**: Mehr Leistung als ein Raspberry Pi, günstiger als Fertig-Boxen und die Freiheit, später aufzurüsten.

**Meine Klartext-Empfehlung:** Kauf einen Fujitsu Futro S7010 für ~45 € und einen Sonoff Zigbee-Stick für ~18 €. Zusammen 63 € für eine leise, stromsparende Smart-Home-Zentrale. Investiere das gesparte Geld in ein paar Sensoren für den Start.

