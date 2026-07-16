+++
title = "Fujitsu Futro S7010 als Homelab-Einstieg 2026: Der 40€-Thin-Client"
description = "Fujitsu Futro S7010 als günstigen Homelab-Server nutzen: Proxmox, Docker, Pi-hole und mehr auf einem Thin Client mit geringem Stromverbrauch – für Einsteiger mit 30–300 € Budget."
date = 2026-06-22
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
approved_for_publish = false
image = "featured.jpg"

[cover]
image = "featured.jpg"
alt = "Fujitsu Futro S7010 Thin Client als Homelab-Server"
relative = true

[taxonomies]
tags = ["fujitsu", "futro", "thin-client", "low-budget", "homelab", "home-assistant", "proxmox"]
categories = ["Hardware"]

[extra]
content_state = "draft"
audit_status = "pending"
user_approval_required = true
instagram_derivatives_required = true
instagram_derivatives_status = "planned"
content_cluster = "hardware"
content_role = "affiliate"
risk_level = "medium"
next_action = "review_before_publish"
related_articles = ["mini-pc-homelab-vergleich", "home-assistant-gebrauchter-mini-pc-2026"]
notes = [
  "Neuschrieb Juni 2026: Superlative reduziert, OPNSense-1-NIC-Einschränkung ergänzt, PVE04-Specs korrigiert auf 4GB/64GB, KI-Empfehlungen entfernt, Preise datiert."
]
+++

**Aktualisiert: Juli 2026 | Lesezeit: ca. 10 Minuten**

> **Hinweis:** Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision – für dich entstehen keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.

Du willst in die Welt der Homelabs einsteigen, aber kein großes Budget ausgeben? Der **Fujitsu Futro S7010** ist ein gebrauchter Thin Client, der für rund **30 bis 50 € (Stand: Juli 2026)** zu haben ist. Er läuft lüfterlos, zieht wenig Strom und eignet sich für Dienste wie Home Assistant, Pi-hole oder leichte Docker-Container.

Ich betreibe selbst einen S7010 seit einigen Monaten als OPNSense-Firewall mit AdGuard Home – lautlos, 24/7, ohne nennenswerte Probleme. Was der Thin Client kann, wo seine Grenzen liegen und was du für den Start brauchst, erkläre ich in diesem Artikel.

<!--more-->

---

## Kurzübersicht: Budget-Stufen

| Budget | Konfiguration | Geeignet für |
|--------|--------------|--------------|
| **~45 €** | Futro S7010 gebraucht (oft mit 4 GB RAM + 64 GB SSD) | Einstieg, Pi-hole, Home Assistant light |
| **~130 €** | S7010 + 8 GB RAM + 120 GB M.2 SATA SSD | Home Assistant, mehrere Docker-Container |
| **~210 €** | S7010 + 16 GB RAM + 500 GB M.2 SATA SSD | Firewall, Proxmox mit Containern, mehr Dienste |
| **ab ~80 €** | HP ProDesk 400 G3, Lenovo M720q (Alternativen) | Stärkere CPU, mehr RAM-Slots, PCIe |

> **Hinweis zum Monitor-Anschluss:** Der Futro S7010 hat **DisplayPort**, kein HDMI. Falls dein Monitor keinen DisplayPort-Eingang hat (erkennbar an der abgeschrägten Ecke), brauchst du einen **DisplayPort-auf-HDMI-Adapter (ca. 5–8 €, Stand: Juli 2026)**.

---

## Was ist der Fujitsu Futro S7010?

Der Futro S7010 ist ein **Thin Client** – ein kleiner Büro-Computer, der ursprünglich für Unternehmen gedacht war und dort Anwendungen vom Server aus ausgeführt hat. Nach der Ausmusterung landen diese Geräte oft für 30–50 € auf dem Gebrauchtmarkt (Stand: Juli 2026).

Das Gehäuse ist kompakt und aus Metall. Die Kühlung erfolgt **passiv** – es gibt keinen Lüfter, was den Betrieb komplett geräuschlos macht. Das ist praktisch, wenn das Gerät im Wohn- oder Schlafzimmer stehen soll.

Unterstützte Betriebssysteme: Ubuntu Server LTS, Debian, OPNSense, Proxmox VE, Home Assistant OS. Windows 10 funktioniert, Windows 11 nicht (kein TPM 2.0).

### Technische Daten im Überblick

| Komponente | Angabe |
|------------|--------|
| **Prozessor** | Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 Watt TDP) |
| **RAM** | 1 Steckplatz DDR4 SO-DIMM, offiziell max. 8 GB, 16 GB in der Praxis getestet |
| **Speicher** | 1× M.2 2280 – **nur SATA, kein NVMe** |
| **Netzwerk** | 1× Realtek Gigabit Ethernet |
| **Videoausgänge** | 2× DisplayPort 1.2a |
| **USB** | 2× USB 3.1 Gen1 (vorne), 4× USB 2.0 (hinten) |
| **Stromverbrauch** | ca. 4–8 Watt Leerlauf, ca. 10–14 Watt unter Last |
| **Kühlung** | Passiv – kein Lüfter |
| **Preis gebraucht** | ca. 30–50 € (Stand: Juli 2026) |

---

## S7010 vs. S740 – was ist der Unterschied?

Die beiden Modelle sind weitgehend baugleich. Der einzige relevante Unterschied liegt in der CPU:

| Merkmal | Futro S7010 | Futro S740 |
|---------|-------------|------------|
| **CPU** | Intel Celeron J4125 (4C, 2,0–2,7 GHz) | Intel Celeron J4105 (4C, 1,5–2,5 GHz) |
| RAM-Slots | 1 | 1 |
| SSD-Typ | M.2 SATA only | M.2 SATA only |
| Kühlung | Passiv | Passiv |
| Preis gebraucht | ~30–50 € | ~20–45 € (Stand: Juli 2026) |

Beide Modelle haben dieselben Einschränkungen: ein RAM-Slot, kein NVMe, kein 2,5-Zoll-Einbauschacht. Der S7010 hat den etwas neueren Prozessor – das macht sich bei dauerlaufenden Diensten wie einer Firewall oder mehreren Containern bemerkbar. Wenn der S740 günstig verfügbar ist, ist er ebenfalls eine überlegenswerte Option.

---

## Die Budget-Stufen im Detail

### ~45 €: Der Einstieg

Für **30–50 € (Stand: Juli 2026)** bekommst du das Basisgerät. Viele Angebote enthalten bereits RAM und eine kleine SSD – 4 GB RAM und 64 GB SSD sind üblich. Prüf die Beschreibung des Angebots sorgfältig.

**Was du zusätzlich brauchst:**
- ✅ Netzteil (12V Fujitsu-kompatibel, meist im Lieferumfang)
- ✅ DisplayPort-auf-HDMI-Adapter (~5–8 €) – nur falls kein DP-Monitor vorhanden
- Ggf. DDR4 SO-DIMM RAM (falls nicht enthalten)
- Ggf. M.2 SATA SSD (falls nicht enthalten – **kein NVMe kaufen!**)

**Beispiel-Angebote (Stand: Juli 2026):**
- [Ram-König: S740 mit 4 GB RAM + 16 GB SSD](https://www.ram-koenig.de/fujitsu-futro-s740-thin-client-intel-j4105-4gbddr4-16gb-psu-included/10381?referralCode=019cd701aff574318721876292eacd57)
- [QuantElectronic: S740 mit 4 GB RAM + 32 GB SSD](https://www.quantelectronic.de/de/Computer/ThinClient/Fujitsu-Futro-S740-Workstation-A-Ware-Grade-A-Inte-l-Celeron-J4105-1-5GHz-4GB-32GB-M-2-onboard.html)
- [eBay: Futro S740/S7010 gebraucht](https://www.ebay.de/itm/298300189378)
- 🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

### ~130 €: Mit 8 GB RAM und kleiner SSD

Diese Kombination reicht für Home Assistant, Pi-hole und zwei bis drei Docker-Container. Falls das Gerät bereits mit 4 GB RAM und 64 GB SSD geliefert wird, kannst du je nach Bedarf gezielt aufrüsten.

| Komponente | Preis (ca., Stand: Juli 2026) | Link |
|-----------|-------------------------------|------|
| Futro S7010 gebraucht | ~45 € | 🔍 [Amazon](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| 8 GB DDR4 SO-DIMM | ~20–30 € | 🔍 [DDR4 SO-DIMM](https://www.amazon.de/s?k=DDR4+SODIMM+8GB&tag=matmaksa-homelab-21) |
| 120 GB M.2 SATA SSD | ~20–30 € | 🔍 [M.2 SATA SSD](https://www.amazon.de/s?k=M.2+SATA+120GB+SSD&tag=matmaksa-homelab-21) |
| DisplayPort-Adapter | ~5–8 € | 🔍 [DP-Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |
| **Gesamt ca.** | **~100–115 €** | |

**Damit realistisch:** Home Assistant (Smarthome), Pi-hole oder AdGuard Home (DNS-Werbeblocker), Uptime Kuma (Monitoring), ein leichter weiterer Dienst.

---

### ~210 €: Mit 16 GB RAM und 500 GB SSD

Diese Ausbaustufe ist für ein etwas umfangreicheres Homelab sinnvoll. **Wichtig:** Der S7010 hat nur **einen RAM-Slot** – du tauschst den vorhandenen Riegel gegen einen 16-GB-Riegel. Achte dabei auf einen **Dual-Rank-Riegel (2Rx8)**, da Single-Rank-16-GB-Riegel auf diesem Mainboard erfahrungsgemäß nicht immer stabil laufen.

| Komponente | Preis (ca., Stand: Juli 2026) | Link |
|-----------|-------------------------------|------|
| Futro S7010 gebraucht | ~45 € | 🔍 [Amazon](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) |
| 16 GB DDR4 Dual Rank SO-DIMM | ~45–60 € | 🔍 [16 GB Dual Rank](https://www.amazon.de/s?k=DDR4+16GB+Dual+Rank+SODIMM&tag=matmaksa-homelab-21) |
| 500 GB M.2 SATA SSD | ~40–55 € | 🔍 [500 GB M.2 SATA](https://www.amazon.de/s?k=M.2+SATA+500GB+SSD&tag=matmaksa-homelab-21) |
| DisplayPort-Adapter | ~5–8 € | 🔍 [DP-Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) |
| **Gesamt ca.** | **~135–170 €** | |

**Damit realistisch:** Drei bis fünf Docker-Container, Home Assistant mit Zigbee2MQTT, OPNSense-Firewall, Proxmox VE mit LXC-Containern.

---

### Ab ~80 €: Lieber eine Alternative?

Wenn du von Anfang an Proxmox mit mehreren VMs oder rechenintensivere Aufgaben planst, kann eine alternative Plattform sinnvoller sein:

| Gerät | Vorteil gegenüber dem Futro |
|-------|-----------------------------|
| **HP ProDesk 400 G3** (~80 €) | i5-6500T, Intel-Netzwerkkarte, 2 RAM-Slots |
| **Lenovo M720q Tiny** (~120 €) | i5-8500T (6 Kerne), PCIe-Slot, USB-C |
| **Dell OptiPlex 3070 Micro** (~120 €) | i5-9500T (6 Kerne), 2 RAM-Slots, breite Ersatzteil-Verfügbarkeit |

Der Futro bleibt interessant, wenn: Budget unter ~80 €, der Stromverbrauch im Dauerbetrieb eine Rolle spielt oder du gezielt ein lüfterloses Gerät benötigst.

---

## Was kann ich damit konkret machen?

### 1. OPNSense-Firewall

Der S7010 eignet sich gut als Firewall-Appliance für den Heimbereich. Ich betreibe OPNSense zusammen mit AdGuard Home seit einigen Monaten – bei ca. 6–8 Watt Verbrauch.

**Wichtiger Hinweis zu OPNSense und einer einzelnen Netzwerkkarte:** OPNSense benötigt im Normalbetrieb **zwei Netzwerkschnittstellen** – eine für das WAN (Richtung Internet/Router) und eine für das LAN (dein Heimnetz). Der S7010 hat von Haus aus **nur eine Netzwerkkarte**.

Es gibt zwei Wege, das zu lösen:

- **USB-Netzwerkadapter:** Ein USB-3.0-Gigabit-Adapter (ca. 10–15 €, Stand: Juli 2026) dient als zweite Schnittstelle. Das ist die einfachste Lösung, aber USB-Netzwerkadapter können unter OPNSense je nach Chipsatz unterschiedlich gut unterstützt werden – prüf vorher, ob der Chipsatz kompatibel ist (z. B. ASIX AX88179 gilt als weitgehend stabil unter FreeBSD).
- **VLAN-Trunk am Switch:** Wenn du einen managed Switch mit VLAN-Unterstützung hast, kannst du WAN und LAN über VLANs auf der einzelnen physischen Netzwerkkarte trennen. Das setzt etwas Netzwerkkenntnisse voraus und ist keine Anfänger-Konfiguration.

Für einen einfachen Start empfehle ich den USB-Adapter-Weg. Wer OPNSense mit nur einer NIC ohne zweite Schnittstelle plant, sollte wissen, dass das **nicht** dem Standard-Deployment entspricht.

---

### 2. Home Assistant (Smarthome-Zentrale)

Home Assistant OS lässt sich direkt auf die M.2-SSD installieren. Mit einem USB-Zigbee-Adapter (z. B. Sonoff Zigbee 3.0 Dongle Plus oder Conbee II, ca. 20–30 €, Stand: Juli 2026) kannst du Zigbee-Geräte direkt einbinden.

Vorteil gegenüber einem Raspberry Pi: SSD statt MicroSD-Karte (keine Kartenkorruption nach Monaten), Metallgehäuse, kein Lüfter.

---

### 3. Pi-hole oder AdGuard Home (Netzwerk-Werbeblocker)

Diese Dienste laufen auch auf 4 GB RAM und einer kleinen SSD problemlos. Der Verbrauch im Leerlauf bleibt unter 6 Watt.

Pi-hole und AdGuard Home blocken Werbung und Tracking auf DNS-Ebene – für alle Geräte im Netz gleichzeitig, ohne dass du auf jedem Gerät etwas installieren musst.

---

### 4. Docker-Container-Server

Typische Container und ihr ungefährer RAM-Bedarf:

| Container | Aufgabe | RAM ca. |
|-----------|---------|---------|
| Watchtower | Automatische Container-Updates | ~50 MB |
| Uptime Kuma | Monitoring / Verfügbarkeit | ~100 MB |
| Vaultwarden | Passwortmanager (Bitwarden-kompatibel) | ~50 MB |
| Grafana + InfluxDB | Dashboards und Metriken | ~400 MB |
| n8n | Workflow-Automatisierung | ~300 MB |

Mit 8 GB RAM lassen sich drei bis vier dieser Dienste gleichzeitig betreiben. Mit 16 GB ist mehr Spielraum vorhanden.

---

## Proxmox VE auf dem Futro S7010

Proxmox lässt sich installieren und läuft stabil. Der Celeron J4125 hat vier Kerne und unterstützt Hardware-Virtualisierung (Intel VT-x). Damit sind LXC-Container und leichte VMs möglich.

**Realistisches Szenario (PVE04: 4 GB RAM / 64 GB SSD):** Mit dieser Basisausstattung bleibt wenig Spielraum. Zwei bis drei LXC-Container sind machbar, zum Beispiel Pi-hole, Uptime Kuma und ein kleiner Dienst. Eine vollwertige VM mit Ubuntu oder Debian lässt sich starten, ist aber bei 4 GB RAM knapp bemessen.

Mit **8 GB RAM** ist Proxmox deutlich komfortabler – du kannst drei bis vier Container parallel betreiben. Für ernsthafte VM-Arbeit mit mehreren Gästen ist ein Gerät mit stärkerer CPU und mehr RAM-Slots (z. B. HP ProDesk, Lenovo M720q) sinnvoller.

---

## Stromverbrauch und Betriebskosten

| Zustand | Verbrauch | Kosten/Jahr bei 0,30 €/kWh (ca.) |
|---------|-----------|----------------------------------|
| Leerlauf | 4–8 Watt | ~10–21 € |
| Mittellast | 8–10 Watt | ~21–26 € |
| Volllast | 10–14 Watt | ~26–37 € |

Die Werte sind Richtwerte – der tatsächliche Verbrauch hängt von der SSD, dem RAM-Typ und der laufenden Software ab. Ein Energiemessgerät (Steckdosenmessgerät, ca. 10–15 €) gibt Aufschluss über den tatsächlichen Verbrauch deines Setups.

---

## Häufige Fragen (FAQ)

**Funktioniert Windows 11?**
Nein. Der J4125 hat kein TPM 2.0. Windows 10 funktioniert, alle gängigen Linux-Varianten ebenso.

**Welche SSD passt?**
M.2 2280 SATA. **Kein NVMe** – der Slot unterstützt nur SATA. Da nur ein Slot vorhanden ist, lohnt es sich, direkt eine größere SSD zu kaufen (z. B. 500 GB), statt später tauschen zu müssen.

**Wieviel RAM ist sinnvoll?**
Für Pi-hole oder Home Assistant: 4–8 GB. Für mehrere Docker-Container oder Proxmox: 8–16 GB. Achte bei 16-GB-Riegeln auf **Dual Rank (2Rx8)** – Single-Rank-Riegel berichten manche Nutzer als instabil auf diesem Board.

**Muss ich ins BIOS?**
Nur wenn der USB-Stick nicht bootet (Boot-Reihenfolge anpassen) oder die SSD nicht erkannt wird (SATA-Modus von RAID auf AHCI umstellen). Beides ist selten, aber möglich.

**OPNSense mit nur einer Netzwerkkarte – geht das?**
Nicht ohne Zusatzmaßnahmen. Du brauchst entweder einen zweiten Netzwerkadapter (USB) oder einen managed Switch mit VLAN-Unterstützung. Details dazu stehen weiter oben im Abschnitt zu OPNSense.

---

## Alternativen auf einen Blick

Wenn der Futro für dein Vorhaben nicht passt:

| Gerät | Ungefährer Preis (Stand: Juli 2026) | Besonderheit |
|-------|--------------------------------------|--------------|
| **HP ProDesk 400 G3 Mini** | ~70–90 € | i5-6500T, 2 RAM-Slots, Intel-NIC |
| **Lenovo ThinkCentre M720q** | ~110–130 € | i5-8500T (6 Kerne), PCIe-Slot |
| **Dell OptiPlex 3070 Micro** | ~110–130 € | i5-9500T (6 Kerne), breite Ersatzteilversorgung |
| **Raspberry Pi 5 (4 GB)** | ~70–90 € | ARM, sehr kompakt, MicroSD oder USB-SSD |

Der Futro ist bei einem Budget unter ~80 € und dem Wunsch nach lüfterlosem Betrieb eine überlegenswerte Option. Für rechenintensivere Aufgaben oder Proxmox mit mehreren VMs bieten die Mini-PCs mit i5-CPU mehr Spielraum.

---

## Einkaufsliste

| Was | Hinweis |
|-----|---------|
| 🔍 [Futro S7010 bei Amazon](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21) | Oft mit 4 GB + 64 GB – Netzteil im Angebot prüfen |
| 🔍 [DisplayPort-HDMI-Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=matmaksa-homelab-21) | Nur nötig, wenn Monitor kein DisplayPort hat |
| 🔍 [16 GB Dual Rank SO-DIMM](https://www.amazon.de/s?k=DDR4+16GB+Dual+Rank+SODIMM&tag=matmaksa-homelab-21) | Dual Rank (2Rx8) beachten – nur ein Slot |
| 🔍 [M.2 SATA SSD](https://www.amazon.de/s?k=M.2+SATA+SSD&tag=matmaksa-homelab-21) | **Nur SATA** – kein NVMe |
| [WD Blue SA510 SATA M.2 (Geizhals)](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wdbb8h0010bnc-a2736547.html?hloc=de) | Bewährte SATA-SSD für diesen Formfaktor |

---

## Fazit

Der Fujitsu Futro S7010 ist ein günstiger Einstiegspunkt ins Homelab, wenn die Anforderungen zur Hardware passen. Lüfterlos, niedriger Stromverbrauch, ausreichend Leistung für Dienste wie Pi-hole, Home Assistant oder eine Handvoll Docker-Container – das sind seine Stärken.

Die Einschränkungen solltest du kennen: nur ein RAM-Slot, kein NVMe, eine einzelne Netzwerkkarte (relevant für OPNSense), begrenzte CPU-Leistung für viele parallele VMs. Wer von Anfang an mehr plant, ist mit einem gebrauchten Mini-PC mit i5-CPU oft besser beraten.

Für ~45 € ein einsteigerfreundliches 24/7-Gerät. Mit 8 GB RAM und einer 500-GB-SSD liegt man bei rund 120–150 € und hat ein solides kleines Homelab.