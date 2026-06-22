---
title: "Fujitsu Futro S740 als Homelab-Einstieg 2026: Der 30€-Server"
date: 2026-06-22
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Fujitsu Futro S740 Thin Client – der ultimative 30€-Homelab-Server für 2026"
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
---

**Aktualisiert: Juni 2026 | Lesezeit: 9 Minuten**

Du möchtest in die Welt der Homelabs einsteigen, hast aber kein Budget für teure Server-Hardware? Dann ist der **Fujitsu Futro S740** genau das richtige Gerät für dich. Für gerade einmal **20 bis 60 Euro** bekommst du einen fertigen, extrem stromsparenden Server, der sich perfekt für Home Assistant, Pi-hole, Docker-Container und leichte Virtualisierung eignet.

In diesem Artikel zeige ich dir, was der kleine Thin Client kann, welche Use-Cases realistisch sind und welche Komponenten du für den Start benötigst.

<!--more-->

## Auf einen Blick: Budget-Stufen

| Budget | Konfiguration | Ideal für |
|--------|--------------|-----------|
| **~30 €** | Futro S740 pur (gebraucht, ohne Zubehör) | Wenn du SSD + RAM bereits hast |
| **50–80 €** | Futro S740 + 8 GB RAM + 120 GB SSD | Home Assistant, Pi-hole, leichte Dienste |
| **80–120 €** | Futro S740 + 16 GB RAM + 256 GB NVMe | Mehrere Docker-Container, NAS light |
| **120–250 €** | Alternativen: HP ProDesk 400 G3 oder Lenovo M720q | VMs mit Proxmox, PCIe-Erweiterungen |

> **💡 Einsteiger-Tipp:** Der Futro S740 wird oft **mit RAM und SSD** verkauft – achte beim Kauf auf die Angebotsbeschreibung (Links unten). **Achtung beim Monitor-Anschluss:** Der Futro hat **DisplayPort**, kein HDMI. Prüf kurz, ob dein Monitor einen DisplayPort-Eingang hat (runde Buchse mit abgeschrägter Ecke). Falls nicht: Du brauchst einen **DisplayPort-auf-HDMI-Adapter (ca. 5 €)** für die Ersteinrichtung.

## Was ist der Fujitsu Futro S740?

Der Fujitsu Futro S740 ist ein **Thin Client** – ein kleiner, stromsparender Büro-Computer, der ursprünglich für Terminalserver-Anbindungen entwickelt wurde. Nach der Ausmusterung aus Unternehmen landen diese Geräte für kleines Geld auf dem Gebrauchtmarkt. Und genau dort werden sie für Homelab-Einsteiger interessant.

**Kompatible Betriebssysteme:** Der Futro S740 läuft mit nahezu jedem gängigen Linux – besonders empfehlenswert sind **Ubuntu Server LTS** (einfachster Einstieg), **Debian 12** (ressourcenschonend), **Proxmox VE 8.x** (für Virtualisierung) oder **Home Assistant OS** (dedizierter Smarthome-Server). Windows 10 funktioniert ebenfalls, Windows 11 wird allerdings nicht unterstützt (siehe FAQ).

### Technische Daten (kanonisch)

| Komponente | Spezifikation |
|------------|--------------|
| **CPU** | Intel Celeron J4105 (4C/4T, 1.5–2.5 GHz, 10W TDP) oder J4125 (4C/4T, 2.0–2.7 GHz) |
| **RAM** | 2× DDR4 SODIMM, offiziell max. 16 GB (inoffiziell bis 32 GB getestet) |
| **Storage** | 1× M.2 2280 SATA/NVMe + 1× mSATA + 1× 2,5-Zoll-SATA-Bay |
| **Netzwerk** | 1× Realtek Gigabit Ethernet (optional zweiter Port) |
| **Video** | 2× DisplayPort |
| **USB** | 4× USB 3.0 |
| **Stromverbrauch** | 4–8 Watt im Leerlauf, 12–18 Watt unter Last |
| **Lautstärke** | Passiv gekühlt oder extrem leiser Lüfter |
| **Preis** | **20–60 € (gebraucht)** |

### Futro S740 vs. Futro S7010 – was ist der Unterschied?

Der neuere **Futro S7010** wird oft mit dem S740 verwechselt. Die wichtigsten Unterschiede:

| Merkmal | Futro S740 | Futro S7010 |
|---------|-----------|-------------|
| CPU | Celeron J4105 (älter) | Celeron J4125 (neuer, minimal schneller) |
| Preis | 20–50 € | 30–60 € |
| Verbrauch | 4–8 W | 4–8 W |
| Ideal für | Home Assistant, Pi-hole, Docker light | OPNSense, AdGuard Home, leichte VMs |

Der S7010 hat den minimal besseren J4125-Prozessor und eignet sich besonders gut als **dedizierte Firewall** (OPNSense) – genau das, wofür ich meinen eigenen S7010 einsetze. Der S740 ist jedoch häufiger und günstiger verfügbar.

## Die Budget-Stufen im Detail

### Bis 30 €: Der absolute Einstieg

Für **20–60 Euro** bekommst du das Basismodell. Viele Angebote enthalten bereits RAM und eine kleine SSD (4 GB + 16–32 GB sind üblich) – prüf einfach die Beschreibung. Das senkt deine Einstiegskosten deutlich.

**Was du brauchst:**
- ✅ Netzteil (meist Fujitsu Original-12V-Netzteil, oft dabei)
- ✅ **DisplayPort-auf-HDMI-Adapter (ca. 5 €) falls nötig** – der Futro hat DisplayPort, kein HDMI. Check: Hat dein Monitor einen DisplayPort-Eingang (eckige Buchse mit abgeschrägter Seite)? Dann brauchst du keinen Adapter. Sieht er nur HDMI-Buchsen? Dann Adapter besorgen.
- ❌ DDR4 SODIMM RAM (falls nicht im Angebot enthalten – oft ist RAM dabei)
- ❌ SSD (M.2 NVMe oder 2,5-Zoll-SATA, falls nicht im Angebot enthalten)

**Beispiel-Angebote (oft mit RAM + SSD):**
- [Ram-König: Futro S740 mit 4 GB RAM + 16 GB SSD](https://www.ram-koenig.de/fujitsu-futro-s740-thin-client-intel-j4105-4gbddr4-16gb-psu-included/10381?referralCode=019cd701aff574318721876292eacd57)
- [QuantElectronic: Futro S740 mit 4 GB RAM + 32 GB SSD](https://www.quantelectronic.de/de/Computer/ThinClient/Fujitsu-Futro-S740-Workstation-A-Ware-Grade-A-Inte-l-Celeron-J4105-1-5GHz-4GB-32GB-M-2-onboard.html)
- [eBay: Futro S740 gebraucht](https://www.ebay.de/itm/298300189378?var=0&mkevt=1&mkcid=1&mkrid=707-53477-19255-0&toolid=20006&campid=5338791727&customid=sPeA6HLykEYp7nQp1loxbg)

🔍 [Fujitsu Futro S740 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S740&tag=makmatas-homelab-21)

Besonders wichtig: **Prüfe vor dem Kauf, ob ein Netzteil dabei ist.** Ohne Netzteil brauchst du ein Fujitsu-kompatibles 12V-Netzteil mit 4-Pin- oder Rundstecker.

### 30–70 €: Futro S740 mit 8 GB RAM + kleiner SSD

Die günstigste Komplettlösung für einen lauffähigen Server:

| Komponente | Ungefährer Preis | Link |
|-----------|-----------------|------|
| Fujitsu Futro S740 | 20–40 € | 🔍 [Suche bei Amazon](https://www.amazon.de/s?k=Fujitsu+Futro+S740&tag=makmatas-homelab-21) |
| 8 GB DDR4 SODIMM | ~10–15 € | 🔍 [DDR4 SODIMM bei Amazon](https://www.amazon.de/s?k=DDR4+SODIMM+8GB&tag=makmatas-homelab-21) |
| 120 GB SATA SSD 2,5" | ~15–20 € | 🔍 [Günstige SSD bei Amazon](https://www.amazon.de/s?k=120+GB+SATA+SSD+2.5+Zoll&tag=makmatas-homelab-21) |
| **Gesamt** | **~50–75 €** | |

Damit betreibst du komfortabel:
- **Home Assistant** (inkl. zigbee-Gateway über USB)
- **Pi-hole** zur Werbeblockade im ganzen Netzwerk
- **PiVPN** für sicheren Remote-Zugriff
- **1–2 leichte Docker-Container** (z. B. n8n, Watchtower, Uptime Kuma)

### 70–120 €: Futro S740 mit 16 GB RAM + NVMe SSD

Die optimale Ausbaustufe für dein erstes richtiges Homelab:

| Komponente | Ungefährer Preis | Link |
|-----------|-----------------|------|
| Fujitsu Futro S740 | 20–40 € | 🔍 [Suche bei Amazon](https://www.amazon.de/s?k=Fujitsu+Futro+S740&tag=makmatas-homelab-21) |
| 16 GB DDR4 SODIMM (2×8 GB) | ~20–30 € | 🔍 [DDR4 SODIMM 16 GB Kit bei Amazon](https://www.amazon.de/s?k=DDR4+SODIMM+16GB+Kit&tag=makmatas-homelab-21) |
| 256 GB M.2 NVMe SSD | ~25–35 € | 🔍 [M.2 NVMe SSD 256GB bei Amazon](https://www.amazon.de/s?k=M.2+NVMe+256GB+SSD&tag=makmatas-homelab-21) |
| **Gesamt** | **~65–105 €** | |

Damit sind folgende Szenarien realistisch:
- **3–5 Docker-Container** parallel (Postgres, n8n, Jellyfin light, Grafana, Node-RED)
- **Home Assistant + Zigbee2MQTT + InfluxDB + Grafana**
- **Leichter NAS-Server** über Samba (für kleine Dateien, Backups)
- **AdGuard Home + Unbound** als DNS-Resolved
- **Proxmox VE** mit 1–2 LXCs (mehr dazu unten)

### Ab 120 €: Lieber einen HP ProDesk oder Lenovo Tiny kaufen?

Ab etwa 120 Euro Gesamtbudget solltest du über Alternativen nachdenken. Ein **HP ProDesk 400 G3** (50–100 €) oder ein **Lenovo ThinkCentre M720q Tiny** (90–200 €) bieten:

| Gerät | Vorteil gegenüber Futro |
|-------|------------------------|
| **HP ProDesk 400 G3** | i5-6500T (4 Kerne, stärker als Celeron), Intel NIC |
| **Lenovo M720q Tiny** | i5-8500T (6 Kerne!), **PCIe-Slot** für 10GbE oder SATA-Erweiterung |
| **Dell OptiPlex 3070 Micro** | i5-9500T (6 Kerne), USB-C, extrem stromsparend |

Der Futro bleibt die Nummer 1, wenn:
- Dein Budget **unter 80 €** liegt
- Stromverbrauch **absolut kritisch** ist (24/7-Betrieb)
- Du **Home Assistant oder Pi-hole** als primären Use-Case hast
- Du **leise** oder **lüfterlose** Hardware brauchst

👉 [HP ProDesk 400 G3 bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G3+Mini&tag=makmatas-homelab-21)
👉 [Lenovo ThinkCentre M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+ThinkCentre+M720q+Tiny&tag=makmatas-homelab-21)

## Proxmox auf dem Futro S740 – geht das?

Ja, **Proxmox VE** läuft auf dem Futro S740, aber mit Einschränkungen:

**✅ Was funktioniert:**
- 1–3 leichte LXC-Container (z. B. Pi-hole, Home Assistant, Unbound)
- 1 leichte VM (z. B. Ubuntu Server mit 1 GB RAM)
- Snapshots, Backups via Proxmox Backup Server

**⚠️ Was du beachten musst:**
- **Realtek NIC:** Der integrierte Realtek-Chip (RTL8111G) wird von Proxmox standardmäßig erkannt, aber einige Nutzer berichten von sporadischen Verbindungsabbrüchen. **Fix:** `ethtool -K vmbr0 gro on lro on` oder ein Intel-basiertes USB-Ethernet-Adapter (~15€) als Alternative.
- **CEPH oder ZFS sind zu heavy:** Der Celeron hat zu wenig Leistung für CEPH oder dedupliziertes ZFS. Verwende ext4 oder einfaches LVM-Thin.
- **Max 2 VMs realistisch:** Bei mehr als 2 VMs wird der Celeron zum Flaschenhals.

**Meine Empfehlung:** Nutze den Futro als **dedizierten Home-Assistant-Host** unter Proxmox, oder betreibe ihn **ohne Proxmox** als reinen Docker-Host mit Ubuntu Server LTS. Das spart Overhead und läuft butterweich.

## Die besten Use-Cases für den Futro S740

### 1. Home Assistant (perfekt!)

Der Futro S740 ist **der ideale Home Assistant Server**. Mit 8–16 GB RAM und einer kleinen SSD betreibst du Home Assistant OS, Zigbee2MQTT und Node-RED absolut problemlos. Ein USB-Zigbee-Stick (Conbee II oder Sonoff) wird sofort erkannt.

**Vorteile gegenüber Raspberry Pi 5:**
- Keine SD-Karten-Probleme (SATA-SSD statt MicroSD)
- x86-Architektur (keine ARM-Inkompatibilitäten)
- Mehr RAM möglich (16 GB vs 8 GB beim Pi 5)
- Robusteres Gehäuse, kein Hitzestau

🔍 [Home Assistant (gelb) bei Amazon suchen](https://www.amazon.de/s?k=Home+Assistant+Gelb&tag=makmatas-homelab-21)

### 2. Pi-hole + Unbound DNS

Mit 4 GB RAM und einer 32-GB-SSD läuft Pi-hole + Unbound nahezu unsichtbar im Hintergrund. Der Futro verbraucht dabei **unter 6 Watt** – weniger als eine durchschnittliche LED-Lampe.

### 3. Docker-Container-Server

Betreibe einen Ubuntu-Server als Docker-Host. Typische Container:

| Container | RAM | Sinn |
|-----------|-----|------|
| Watchtower | ~50 MB | Automatische Updates |
| Uptime Kuma | ~100 MB | Monitoring + Status-Seite |
| n8n | ~300 MB | Workflow-Automatisierung |
| Grafana + InfluxDB | ~400 MB | Metriken-Dashboard |
| Jellyfin (light) | ~500 MB | Medien-Streaming (nur Audio/leichte Videos) |

### 4. OPNSense / pfSense Firewall (S7010 besser geeignet)

Der Futro S7010 (mit J4125) ist besser für OPNSense geeignet, da er die minimal bessere CPU hat. Der S740 kann als Einsteiger-Firewall für 500 Mbit/s-Leitungen dienen.

> **📱 Einsteiger-Tipp: Von unterwegs auf dein Homelab zugreifen**
> 
> Wenn du deinen Futro als Home Assistant oder NAS nutzt, willst du auch von unterwegs darauf zugreifen. Die sicherste und einfachste Methode: **Tailscale**. Installiere Tailscale auf dem Futro (1 Befehl: `curl -fsSL https://tailscale.com/install.sh | sh`) und auf deinem Handy. Dann verbindest du dich per Tailscale-IP – verschlüsselt, ohne Port-Freigaben, ohne Cloud-Dienst. Funktioniert auf Android und iOS mit der offiziellen Tailscale-App. Alternativ: WireGuard über PiVPN (etwas mehr Einrichtung, aber ebenfalls top).

## Stromverbrauch – die große Stärke des Futro

Der Futro S740 glänzt vor allem durch seinen extrem niedrigen Stromverbrauch:

| Zustand | Verbrauch | Kosten pro Jahr (bei 0,30 €/kWh) |
|---------|-----------|----------------------------------|
| Idle (Leerlauf) | 4–8 Watt | **~10,50–21 €** |
| Leichte Last | 8–12 Watt | ~21–31,50 € |
| Volllast | 12–18 Watt | ~31,50–47 € |

Zum Vergleich: Ein ausgemusterter Tower-Server (Dell PowerEdge T320) zieht im Idle 80–120 Watt – das sind **210–315 € pro Jahr** allein für den Strom. Der Futro spart dir also potenziell **bis zu 290 € pro Jahr** an Stromkosten (bei 24/7-Betrieb und 0,30 €/kWh, Stand 2026).

> 💡 **Wer den Futro 3 Jahre betreibt, hat die Anschaffungskosten (30 €) oft bereits nach 2–3 Monaten allein durch die Stromersparnis gegenüber einem älteren Tower-Server wieder drin – bei aktuellen Strompreisen eine realistische Größenordnung.**

## Preis-Leistungs-Vergleich: Futro vs. andere Mini-PCs

| Modell | Preis | CPU-Kerne | RAM max. | Idle-Strom | PCIe-Slot |
|--------|-------|-----------|----------|------------|-----------|
| **Fujitsu Futro S740** | **20–60 €** | **4 Cores** | **16–32 GB** | **4–8 W** | ❌ |
| HP ProDesk 400 G3 | 50–100 € | 4 Cores | 32 GB | 8–12 W | ❌ |
| HP ProDesk 600 G4 | 100–180 € | **6 Cores** | 32–64 GB | 8–14 W | ❌ |
| Lenovo M720q Tiny | 90–200 € | **6 Cores** | 32–64 GB | 6–12 W | ✅ (PCIe x8) |
| Dell OptiPlex 3070 Micro | 100–180 € | **6 Cores** | 32–64 GB | 6–12 W | ❌ |
| GMKtec G3 Pro (neu) | 200–280 € | 2 Cores | 16–32 GB | 6–10 W | ❌ |
| Minisforum MS-01 (neu) | 550–700 € | **14 Cores** | 96 GB | 15–25 W | ✅ (USB4) |

**Fazit der Tabelle:** Der Futro S740 ist unschlagbar günstig und stromsparend. Sobald du mehr als 2 VMs betreiben willst oder PCIe-Erweiterungen brauchst, lohnt sich der Aufstieg zum Lenovo M720q oder HP ProDesk.

## FAQ

### Kann ich mit dem Futro S740 Windows 11 nutzen?
Nein, der Celeron J4105/J4125 wird von Microsoft nicht für Windows 11 unterstützt (kein TPM 2.0 / kein Intel 8. Gen). Windows 10 läuft hingegen problemlos. Für ein Homelab empfehle ich aber Linux (Ubuntu Server LTS oder Debian).

### Passt eine 2,5-Zoll-SSD in den Futro?
Ja, der Futro S740 hat drei Storage-Optionen: (1) einen **M.2-2280-Slot** für NVMe-SSDs (empfohlen fürs Betriebssystem), (2) einen **mSATA-Slot** für zusätzliche SSDs, und (3) einen **internen 2,5-Zoll-SATA-Bay** für klassische SATA-SSDs. Die 120-GB-SATA-SSD aus der 50–80-€-Budgetstufe kommt in den 2,5-Zoll-Bay. Wer schnelleren Speicher will, nutzt den M.2-Slot für eine NVMe-SSD.

### Kann ich den Arbeitsspeicher aufrüsten?

Ja, der Futro hat zwei DDR4 SODIMM-Slots. Offiziell unterstützt Fujitsu 16 GB, in der Community wurden aber auch 32 GB (2× 16 GB) erfolgreich getestet.

**Wichtiger Hinweis zur RAM-Kompatibilität:** Der Futro ist wählerisch bei 16-GB-Riegeln. Nicht jeder 16-GB-DDR4-SODIMM funktioniert – es muss ein **Dual-Rank**-Riegel sein (das steht im Datenblatt). Single-Rank-Riegel mit 16GB werden oft nicht erkannt. **Mein Tipp:** Kauf gebrauchte 8-GB-Riegel (2 Stück für 16 GB), die sind günstiger und laufen garantiert. Oder such gezielt nach "16GB DDR4 SODIMM Dual Rank" für den Futro.

### Wie laut ist der Futro S740?
Sehr leise. Viele Versionen sind passiv gekühlt (völlig lautlos), andere haben einen kleinen Lüfter, der im Leerlauf kaum hörbar ist (< 20 dB).

### Muss ich das BIOS updaten oder Einstellungen ändern?

In den meisten Fällen: **nein.** Der Futro startet direkt von SSD oder USB-Stick, sobald du ihn einschaltest. Nur in zwei Fällen musst du ins BIOS (beim Start F2 drücken):

1. **Wenn der USB-Stick nicht bootet:** Gehe ins BIOS → "Boot" → "Boot Priority" und stelle USB an die erste Stelle. Das war's.
2. **Wenn eine neue SSD nicht erkannt wird:** Gehe ins BIOS → "Advanced" → "SATA Configuration" und stelle den Modus von "RAID" auf "AHCI". Das ist der einzige Schalter, den du umlegen musst.

**Keine Angst:** Das BIOS des Futro sieht aus wie ein blauer Bildschirm aus den 90ern, aber du kannst außer diesen beiden Einstellungen nichts kaputt machen. Wenn du dich verirrst: Einfach "Exit → Load Default Settings" wählen und ohne Speichern beenden.

### Gibt es Bastel-Möglichkeiten für später? (NVMe-Adapter)

Erfahrene Bastler bauen die interne WLAN-Karte aus und nutzen den Steckplatz mit einem Adapter für eine zweite NVMe-SSD. **[NUR FÜR BASTLER]** – als Anfänger solltest du das sein lassen. Der normale M.2-Slot und der 2,5-Zoll-Bay reichen für jeden Homelab völlig aus. Wenn du später mehr Speicher brauchst, kauf lieber eine größere SSD oder hänge eine externe USB-Festplatte an.

### Ist der Futro S740 für Proxmox geeignet?
Ja, aber beschränkt auf 1–3 LXCs oder 1–2 leichte VMs. Für einen reinen Proxmox-Einstieg reicht es völlig, aber für einen Mehrzweck-Cluster ist ein gebrauchter HP ProDesk mit i5-8500T die bessere Wahl.

### Wo kaufe ich den Futro S740 am besten?
Gebraucht bei Amazon Warehouse Deals, eBay Kleinanzeigen oder Refurbished-Händlern. Achte auf den Zustand "Generalüberholt" oder "Geprüft funktionsfähig" – und ob Netzteil und DisplayPort-Kabel dabei sind.

🔍 [Fujitsu Futro S740 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S740&tag=makmatas-homelab-21)

## Fazit – Für wen lohnt sich der Futro S740?

**Kaufen, wenn:**
- Du unter 80 € Gesamtbudget für dein erstes Homelab hast
- Stromverbrauch deine Hauptsorge ist (24/7-Betrieb)
- Du Home Assistant, Pi-hole oder leichte Docker-Container betreiben willst
- Du einen leisen, unauffälligen Server suchst

**Lieber sparen und größer kaufen, wenn:**
- Du mehrere VMs parallel betreiben willst
- Du PCIe-Erweiterungen (10GbE, SATA-Controller) brauchst
- Du Proxmox mit ZFS/Ceph planst
- Mehrere Docker-Container mit rechenintensiven Workloads (z. B. KI-Inferenz, Transkodierung)

**Meine persönliche Empfehlung:** Starte mit einem Futro S740 oder S7010 für 30–50 € und einer kleinen SSD. Betreibe Home Assistant + Pi-hole + einen n8n-Workflow-Automaten darauf. Sobald du mehr brauchst, holst du dir einen HP ProDesk 400 G4 (mit i5-8500T ebenfalls sehr günstig) als zweiten Cluster-Node. Zwei Mini-PCs im Cluster sind besser und günstiger als ein großer Server.

---

## 🛒 Idiotensichere Einkaufsliste für den Futro S740

Damit du am Ende genau weißt, was du bestellen musst:

| Was | Wofür? | Tipp |
|-----|--------|------|
| 🔍 [Fujitsu Futro S740 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S740&tag=makmatas-homelab-21) | Das Gerät selbst | Achte auf "Netzteil dabei" im Angebot |
| 🔍 [DisplayPort-auf-HDMI-Adapter](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=makmatas-homelab-21) | Monitor-Anschluss | **Pflicht!** Der Futro hat kein HDMI – ca. 5 € |
| 🔍 [DDR4 SODIMM 8 GB](https://www.amazon.de/s?k=DDR4+SODIMM+8GB&tag=makmatas-homelab-21) | Arbeitsspeicher | Lieber 2× 8 GB (16 GB) kaufen – Dual-Rank-Probleme vermeiden |
| 🔍 [WD Blue SA510 1 TB (SATA M.2)](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | SSD fürs Betriebssystem | **SATA-Version**, nicht NVMe! Oder günstiger: kleine 120 GB SATA-SSD für den Start |

**Gesamtkosten (mit 8 GB RAM + 120 GB SSD): ca. 50–75 €** – der günstigste Homelab-Einstieg überhaupt.

*Hinweis: RAM und SSD sind auf dem Gebrauchtmarkt oft viel günstiger. Frag bei eBay Kleinanzeigen oder schau bei Refurbed-Händlern.*

| Budget | Meine Empfehlung |
|--------|-----------------|
| **Bis 60 €** | Fujitsu Futro S740 + 8 GB RAM + kleine SSD |
| **60–150 €** | HP ProDesk 400 G3 (i5) + 8–16 GB RAM |
| **150–250 €** | Lenovo M720q Tiny (i5) + 16 GB RAM → PCIe-Upgrade möglich |
| **250–400 €** | Dell OptiPlex 7070 Micro (i7, 8 Kerne) |

> **🔗 Weiterlesen:** Du willst mehr über die anderen Mini-PC-Kandidaten erfahren? Dann schau dir unseren [Mini-PC-Vergleich fürs Homelab 2026](/homelab-blog/posts/mini-pc-homelab-vergleich/) an – mit HP ProDesk, Dell OptiPlex und Lenovo ThinkCentre im Direktvergleich.

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.*
