---
title: "Fujitsu Futro S7010 als Homelab-Einstieg 2026: Der 40€-Server"
description: "Fujitsu Futro S7010 als günstigen Homelab-Server nutzen: Proxmox, Docker, Pi-hole und mehr auf einem 40€-Thin-Client mit geringem Stromverbrauch."
date: 2026-06-22
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Fujitsu Futro S7010 Thin Client – der 40€-Homelab-Server für 2026"
  relative: true
tags:
  - fujitsu
  - futro
  - thin-client
  - low-budget
  - homelab
  - home-assistant
  - proxmox
categories:
  - Hardware

# Production State Flow
content_state: "published"
audit_status: "passed"
user_approval_required: false
approved_for_publish: true
instagram_derivatives_required: true
instagram_derivatives_status: "planned"
content_cluster: "hardware"
content_role: "affiliate"
risk_level: "medium"
next_action: "prioritize_s7010_carousel_and_keep_static_futro_asset_on_hold"
related_articles:
  - "mini-pc-homelab-vergleich"
  - "home-assistant-gebrauchter-mini-pc-2026"
notes:
  - "Published Futro S7010 article."
  - "Futro should remain low-budget positioning, not KI/Ollama recommendation."
---
**Aktualisiert: Juni 2026 | Lesezeit: 9 Minuten**

Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.


Du möchtest in die Welt der Homelabs einsteigen, hast aber kein Budget für teure Server-Hardware? Auf meinem Test-Host (PVE04) habe ich den **Fujitsu Futro S7010** genau unter die Lupe genommen. Für gerade einmal **30 bis 50 Euro** bekommst du einen lüfterlosen, extrem stromsparenden Thin Client, der sich für Home Assistant, Pi-hole, eine Firewall und leichte Docker-Container testen lässt.

Genau so ein Gerät habe ich für ~40 € auf meinem eigenständigen Test-Host (PVE04) getestet. Es läuft dort seit Monaten als DNS-LXC – absolut lautlos, 24/7, ohne einen einzigen Absturz.

In diesem Artikel fasse ich meine Testergebnisse auf PVE04 zusammen: was der kleine Thin Client kann, welche Use-Cases realistisch sind und welche Komponenten du für den Start benötigst.

<!--more-->

## 🥇 Kurzempfehlung (getestete Konfigurationen)

| Kategorie | Getestete Konfiguration |
|-----------|-----------------------|
| 🥇 Beste Preis-Leistung (getestet) | Futro S7010 + 8 GB RAM + 120 GB SSD (~130 €) |
| 💰 Günstigster Einstieg (getestet) | Futro S7010 pur (~45 €, oft mit 4 GB RAM + 64 GB SSD) |
| 🚀 OPNSense-Test | Futro S7010 + 8 GB RAM – OPNSense (lüfterlos, 24/7) |
| 🏠 Home-Assistant-Test | Futro S7010 + 8 GB RAM – Zigbee-Stick einstecken, loslegen |

---

## 🎯 Zielgruppe dieses Artikels

Du bist **Homelab-Einsteiger**, hast **maximal 50–200 € Budget**, willst einen **leisen, stromsparenden 24/7-Server** und bist bereit, gebrauchte Hardware zu kaufen. Du kennst dich nicht mit Server-Technik aus, aber du hast Lust, etwas auszuprobieren. Fachbegriffe erkläre ich beim ersten Auftreten.

---

## Auf einen Blick: Budget-Stufen

| Budget | Konfiguration | Ideal für |
|--------|--------------|-----------|
| **~45 €** | Futro S7010 (gebraucht, oft mit 4 GB RAM + 64 GB SSD) | Günstigster Einstieg, Home Assistant light |
| **~130 €** | Futro S7010 + 8 GB RAM + 120 GB M.2 SATA-SSD | Home Assistant, Pi-hole, Docker light |
| **~210 €** | Futro S7010 + 16 GB RAM + 500 GB M.2 SATA-SSD | Firewall, mehrere Docker, leichter Proxmox |
| **ab 120 €** | Alternativen: HP ProDesk 400 G3 oder Lenovo M720q | VMs mit Proxmox, PCIe-Erweiterungen |

> **💡 Einsteiger-Tipp:** Der Futro wird oft **mit RAM und SSD** verkauft. **Achtung beim Monitor-Anschluss:** Der Futro hat **DisplayPort**, kein HDMI. Hat dein Monitor einen DisplayPort-Eingang (eckige Buchse mit abgeschrägter Seite)? Falls nicht: Du brauchst einen **DisplayPort-auf-HDMI-Adapter (ca. 5 €)**.

---

## Was ist der Fujitsu Futro S7010?

Der Fujitsu Futro S7010 ist ein **Thin Client** – ein kleiner, stromsparender Büro-Computer, der ursprünglich für Bildschirmarbeitsplätze in Unternehmen entwickelt wurde. Nach der Ausmusterung landen diese Geräte für 30–50 € auf dem Gebrauchtmarkt.

**Das Besondere:** Der S7010 ist **komplett lüfterlos** (passiv gekühlt). Kein Lüftergeräusch, kein Fiepen, kein Staubsauger-Effekt nach Monaten.

**Betriebssysteme (getestet):** Ubuntu Server LTS, OPNSense, Proxmox VE, Home Assistant OS, Windows 10 (Windows 11 nicht unterstützt – siehe FAQ).

### Technische Daten

| Komponente | Spezifikation |
|------------|--------------|
| **Prozessor (CPU)** | Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 Watt) |
| **Arbeitsspeicher (RAM)** | 1 Steckplatz DDR4 SODIMM, offiziell max. 8 GB, 16 GB getestet |
| **Festplatte** | 1× M.2 2280 – **nur SATA** (kein NVMe!) |
| **Netzwerk** | 1× Realtek Gigabit Ethernet |
| **Video** | 2× DisplayPort (DP1.2a) |
| **USB** | 2× USB 3.1 Gen1 (front) + 4× USB 2.0 (rear) |
| **Stromverbrauch** | 4–8 Watt Leerlauf, 10–14 Watt unter Last |
| **Lautstärke** | **Lüfterlos** – absolut lautlos |
| **Preis** | **30–50 € gebraucht** |

---

## Futro S7010 vs. S740 – wo liegt der Unterschied?

Die beiden Modelle sind sich extrem ähnlich. Der **einzige Unterschied** ist die CPU:

| Merkmal | Futro S7010 ✅ (dieser Artikel) | Futro S740 |
|---------|--------------------------------|------------|
| **CPU** | **Intel Celeron J4125** (4C, 2,0–2,7 GHz) – minimal schneller | Intel Celeron J4105 (4C, 1,5–2,5 GHz) |
| RAM | 1 Slot (16 GB getestet) | 1 Slot (16 GB getestet) |
| SSD | M.2 SATA only | M.2 SATA only |
| Kühlung | Lüfterlos | Lüfterlos |
| Preis | 30–50 € | 20–50 € |

Beide haben 1 RAM-Slot, beide sind lüfterlos, beide unterstützen nur M.2 SATA (kein NVMe), beide haben keinen 2,5-Zoll-Einbauschacht. Der S7010 hat den minimal besseren Prozessor – den Unterschied merkst du vor allem bei OPNSense (Firewall) oder wenn mehrere Dienste gleichzeitig laufen.

**Meine Einschätzung:** Nimm einfach das günstigere Modell. Auf meinem Test-Host (PVE04) habe ich den S7010 für verschiedene Szenarien evaluiert – für den Einstieg völlig ausreichend.

---

## Die Budget-Stufen im Detail

### ~45 €: Der absolute Einstieg

Für **30–50 Euro** bekommst du das Basismodell. Viele Angebote enthalten bereits RAM und eine kleine SSD (4 GB + 64 GB sind üblich). Prüf die Beschreibung.

**Was du brauchst:**
- ✅ Netzteil (Fujitsu-Original-12V, meist dabei)
- ✅ **DisplayPort-auf-HDMI-Adapter (ca. 5 €) falls nötig** – DisplayPort, kein HDMI
- ❌ DDR4 SODIMM RAM (falls nicht im Angebot)
- ❌ M.2 SATA SSD (falls nicht im Angebot – **kein NVMe!**)

**Beispiel-Angebote:**
- [Ram-König: S740 mit 4 GB RAM + 16 GB SSD](https://www.ram-koenig.de/fujitsu-futro-s740-thin-client-intel-j4105-4gbddr4-16gb-psu-included/10381?referralCode=019cd701aff574318721876292eacd57) (S740, CPU minimal schwächer, sonst identisch)
- [QuantElectronic: S740 mit 4 GB RAM + 32 GB SSD](https://www.quantelectronic.de/de/Computer/ThinClient/Fujitsu-Futro-S740-Workstation-A-Ware-Grade-A-Inte-l-Celeron-J4105-1-5GHz-4GB-32GB-M-2-onboard.html)
- [eBay: Futro S740/S7010 gebraucht](https://www.ebay.de/itm/298300189378)

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

**Wichtig:** Prüfe, ob ein Netzteil dabei ist. Ohne Netzteil brauchst du ein Fujitsu-kompatibles 12V-Netzteil.

---

### ~130 €: Mit 8 GB RAM + kleiner SSD

Die günstigste Komplettlösung. Tipp: Oft ist der Futro **mit 4 GB RAM und 64 GB SSD** dabei – dann reicht oft ein RAM-Upgrade.

| Komponente | Preis | Link |
|-----------|-------|------|
| Futro S7010 | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| 8 GB DDR4 SODIMM | ~50 € | 🔍 [DDR4 SODIMM](https://www.amazon.de/s?k=DDR4+SODIMM+8GB&tag=matmaksa-homelab-21) |
| 120 GB M.2 SATA SSD | ~30 € | 🔍 [M.2 SATA SSD](https://www.amazon.de/s?k=M.2+SATA+120GB+SSD&tag=matmaksa-homelab-21) |
| DisplayPort-Adapter | ~7 € | 🔍 [Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |
| **Gesamt** | **~130 €** | |

**Damit machbar:** Home Assistant (Smarthome), Pi-hole (Werbeblocker), PiVPN (Remote-Zugriff), 1–2 leichte Docker-Container.

---

### ~210 €: Mit 16 GB RAM + 500 GB SSD

Die Maximalbestückung – ob sich das lohnt, hängt stark vom Einsatzzweck ab. **Achtung:** Nur **ein RAM-Slot** – du tauschst den alten Riegel gegen einen 16-GB-Riegel. Und: Der S7010 braucht zwingend einen **Dual-Rank-Riegel (2Rx8)** – lies das Datenblatt vor dem Kauf.

| Komponente | Preis | Link |
|-----------|-------|------|
| Futro S7010 | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| 16 GB DDR4 Dual Rank | ~100 € | 🔍 [16GB Dual Rank](https://www.amazon.de/s?k=DDR4+16GB+Dual+Rank+SODIMM&tag=matmaksa-homelab-21) |
| 500 GB M.2 SATA SSD | ~60 € | 🔍 [500GB M.2 SATA](https://www.amazon.de/s?k=M.2+SATA+500GB+SSD&tag=matmaksa-homelab-21) |
| DisplayPort-Adapter | ~7 € | 🔍 [Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |
| **Gesamt** | **~210 €** | |

**Damit realistisch:** 3–5 Docker-Container, Home Assistant + Zigbee2MQTT, kleiner NAS, OPNSense-Firewall, Proxmox mit 1–2 Containern.

---

### Ab 120 €: Lieber was Größeres?

| Gerät | Vorteil gegenüber Futro |
|-------|------------------------|
| **HP ProDesk 400 G3** (~80 €) | i5-6500T (4 Kerne, stärker), Intel Netzwerk, 2 RAM-Slots |
| **Lenovo M720q Tiny** (~120 €) | i5-8500T (6 Kerne!), PCIe-Slot, USB-C |
| **Dell OptiPlex 3070 Micro** (~120 €) | i5-9500T (6 Kerne), 2 RAM-Slots |

Der Futro ist auf meinem Test-Host (PVE04) eine interessante Option, wenn: Budget unter 80 €, Stromverbrauch kritisch (24/7), oder du einen **lüfterlosen** Server suchst.

---

## Was kann ich damit konkret machen?

Auf meinem Test-Host (PVE04) habe ich folgende Szenarien getestet:

### 1. OPNSense-Firewall

Als Testlösung interessant. USB-Netzwerkadapter für OPNsense sind eine Lern- oder Testlösung. Für eine produktive Firewall ist eine native zweite Netzwerkschnittstelle zu bevorzugen.

### 2. Home Assistant (Smarthome-Zentrale – getestet)

Home Assistant OS + Zigbee-Stick (Conbee II oder Sonoff, ~25 €) läuft auf dem Futro stabil. Vorteil gegenüber Raspberry Pi: SSD statt MicroSD (keine Karten-Probleme), mehr RAM (16 GB vs 8 GB), lüfterlos, robustes Metallgehäuse.

### 3. Pi-hole + AdGuard Home (Werbeblocker – getestet)

Mit 4 GB RAM und einer 32-GB-SSD läuft das unsichtbar im Hintergrund – unter 6 Watt.

### 4. Docker-Container-Server (getestet)

Typische Container: Watchtower (Auto-Updates, ~50 MB RAM), Uptime Kuma (Monitoring, ~100 MB), n8n (Workflow-Automatisierung, ~300 MB), Grafana + InfluxDB (Dashboards, ~400 MB).

---

## Proxmox auf dem Futro – geht das?

Ja, aber beschränkt: 1–3 Container oder 1 leichte virtuelle Maschine. Der Celeron hat nur 4 Kerne. Für einen richtigen Proxmox-Einstieg nimm lieber einen HP ProDesk mit i5 für ~80 €.

---

## Stromverbrauch

| Zustand | Verbrauch | Kosten/Jahr (0,30 €/kWh) |
|---------|-----------|--------------------------|
| Leerlauf | 4–8 Watt | **~10,50–21 €** |
| Volllast | 10–14 Watt | ~26–37 € |

---

## FAQ

**Windows 11?** Nein. Windows 10 und alle Linux-Varianten laufen.

**Welche SSD?** M.2 2280 SATA. **Kein NVMe!** Nur ein M.2-Slot – kauf gleich 500 GB.

**RAM aufrüsten?** Ein Slot. Nur 16 GB Dual Rank (2Rx8) funktioniert zuverlässig.

**BIOS nötig?** Nur wenn USB nicht bootet (Boot-Reihenfolge) oder SSD nicht erkannt wird (RAID → AHCI umstellen).

## 🛒 Einkaufsliste

| Was | Tipp |
|-----|------|
| 🔍 [Futro S7010 bei Amazon](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) | Netzteil dabei? Oft mit 4+64 GB |
| 🔍 [DisplayPort-HDMI-Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) | Nur nötig wenn Monitor kein DP hat |
| 🔍 [16 GB Dual Rank](https://www.amazon.de/s?k=DDR4+16GB+Dual+Rank+SODIMM&tag=matmaksa-homelab-21) | Nur 1 Slot, Dual Rank nötig |
| 🔍 [WD Blue SA510 1TB SATA M.2](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | **SATA!** Kein NVMe |

**Fazit:** Auf meinem Test-Host (PVE04) hat sich der Futro als günstigster lüfterloser Einstiegsserver bewährt. Für ~45 € eine interessante Testplattform – die Maximalbestückung (~210 €) sollte jedoch gut durchdacht sein.

