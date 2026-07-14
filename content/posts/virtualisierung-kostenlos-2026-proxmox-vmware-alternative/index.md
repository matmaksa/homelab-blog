---
title: "Virtualisierung kostenlos 2026: Proxmox VE als VMware-Alternative im Homelab"
date: 2026-06-17
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Proxmox VE Dashboard auf einem Server – Virtualisierung kostenlos und Open Source"
  relative: true
tags:
  - proxmox
  - virtualisierung
  - vmware-alternative
  - homelab
  - open-source
categories:
  - Virtualisierung

# Production State Flow
content_state: "published"
audit_status: "passed"
user_approval_required: false
approved_for_publish: true
instagram_derivatives_required: true
instagram_derivatives_status: "planned"
content_cluster: "proxmox"
content_role: "pillar"
risk_level: "low"
next_action: "manual_duplicate_check_before_additional_proxmox_instagram_derivatives"
related_articles:
  - "mini-pc-homelab-vergleich"
notes:
  - "Published Proxmox pillar article."
  - "Additional Proxmox Instagram derivatives need duplicate-risk check."
---
**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.


Stell dir vor, du hast zu Hause einen kleinen Server – einen Mini-PC, der leise in der Ecke steht und Tag und Nacht läuft. Darauf sollen mehrere Dienste gleichzeitig laufen: Pi-hole (ein Werbeblocker fürs ganze Heimnetz), Jellyfin (ein Medienserver für Filme und Serien), Nextcloud (eine private Cloud für deine Fotos und Dokumente) und vielleicht noch ein Game-Server für dich und deine Freunde.

Müsstest du für jeden Dienst einen eigenen Rechner kaufen, wärst du schnell bei 500–1.000 € und einem Berg Kabelgewirr.

**Virtualisierung** löst genau dieses Problem – und Proxmox VE ist der einfachste Weg, das kostenlos umzusetzen.

Dieser Artikel richtet sich an **Homelab-Einsteiger ohne Vorkenntnisse**, die eine günstige Alternative zu VMware suchen. Fachbegriffe? Erklären wir kurz und mit einem Bild im Kopf.

<!--more-->

---

## 🥇 Kurzempfehlung: Welcher Weg passt zu dir?

| Kategorie | Empfehlung |
|-----------|-----------|
| 🥇 Beste Preis-Leistung | Proxmox VE auf gebrauchtem HP ProDesk 400 G4 (~90 €) |
| 💰 Günstigster Einstieg | Proxmox VE auf Fujitsu Futro S7010 (~40 €) |
| 🚀 Beste Wahl für lokale KI | Proxmox auf Lenovo M720q (~120 €) + 32 GB RAM |
| 🏠 Beste Wahl für Home Assistant | Proxmox LXC-Container (2 GB RAM reichen) |
| 🔧 Beste Wahl für Proxmox Cluster | 2× Dell Optiplex 3070 Micro (~100 €/Stück) |

---

## Was ist Virtualisierung? (Einfach erklärt)

Stell dir vor, dein Computer ist ein **Mehrfamilienhaus** mit einem einzigen großen Raum. Virtualisierung baut **Zwischenwände ein** – plötzlich können mehrere Familien (das sind deine Dienste) gleichzeitig im selben Haus wohnen, ohne sich gegenseitig zu stören. Jede Familie hat ihren eigenen Bereich, ihr eigenes Inventar und kann unabhängig ein- und ausziehen.

Es gibt zwei Bauarten für diese "Zwischenwände":

| Typ | Beschreibung | Beispiel |
|-----|-------------|----------|
| **Typ 1 (Bare Metal)** | Läuft direkt auf der Hardware – wie ein Vermieter, der im Erdgeschoss wohnt | Proxmox VE, VMware ESXi |
| **Typ 2 (Gehostet)** | Läuft als Programm in Windows oder Linux – wie ein Untermieter | VirtualBox, VMware Workstation |

Proxmox VE ist ein **Typ-1-Hypervisor** – eine Spezial-Software, die direkt auf dem Rechner sitzt und die Ressourcen (Rechenleistung, Arbeitsspeicher, Festplatte) gerecht an alle virtuellen Maschinen verteilt.

### Was bringt dir das konkret?

- **Isolation:** Ein abgestürzter Dienst reißt die anderen nicht mit – dein Medienserver läuft weiter, auch wenn der Werbeblocker gerade neu startet
- **Snapshots (Schnappschüsse):** Bevor du eine riskante Änderung machst, knipst du einen Schnappschuss. Läuft was schief? Ein Klick und alles ist wie vorher
- **Kosteneffizienz:** Ein Server ersetzt fünf – weniger Strom, weniger Platz, weniger Lärm
- **Flexibilität:** Linux für Docker, Windows für bestimmte Anwendungen – alles auf einem Rechner

---

## Proxmox VE – Die kostenlose Lösung für dein Homelab

Proxmox Virtual Environment (VE) ist eine **komplett kostenlose Virtualisierungsplattform**. Sie vereint zwei Technologien unter einer übersichtlichen Weboberfläche – also einer Benutzeroberfläche, die du ganz normal im Browser bedienst:

### KVM-VMs (der "Gästeraum mit eigenem Eingang")

Virtuelle Maschinen mit eigenem BIOS (Startprogramm), eigener CPU und eigenem Arbeitsspeicher. Ideal, wenn du verschiedene Betriebssysteme **gleichzeitig** auf einem Rechner betreiben willst – zum Beispiel Windows, Ubuntu und FreeBSD nebeneinander.

### LXC-Container (die "WG mit geteilter Küche")

Container teilen sich den Linux-Kernel (den Betriebssystemkern) des Hosts – das spart enorm Ressourcen. Ein LXC-Container mit Ubuntu braucht nur **~100 MB RAM** statt 2 GB für eine vollständige VM. Das ist der Unterschied zwischen einer möblierten Wohnung (LXC) und einem kompletten Hausbau (KVM).

**Perfekt für:** Docker (eine Plattform für Kleinst-Anwendungen), Pi-hole (Werbeblocker), n8n (Automatisierungs-Tool), Home Assistant (Smart-Home-Zentrale) – alles, was schlank laufen soll.

---

## Proxmox vs. VMware ESXi – Der Vergleich 2026

Seit Broadcom VMware übernommen hat (November 2023) gibt es keine kostenlose Version mehr. Wer VMware weiternutzen will, zahlt **mindestens ~500 € pro Jahr**.

| Kriterium | Proxmox VE | VMware vSphere (Broadcom) |
|-----------|-----------|--------------------------|
| **Preis** | **0 €** – komplett kostenlos | **Ab ~500 €/Jahr** |
| **Container** | LXC inkludiert (schlanke Virt. ohne Voll-OS) | Nicht vorhanden (nur VMs) |
| **Datenhaltung (ZFS)** | Ja, integriert (effiziente Snapshots) | Nur mit Zusatzkosten |
| **Verteilter Speicher** | Ceph integriert (für Cluster-Betrieb) | vSAN ab **~2.000 €/Jahr** |
| **Updates** | Kostenlos (Community-Version) | Nur mit gültigem Support-Vertrag |

**Die Botschaft:** Proxmox bietet mehr Funktionen als der alte ESXi Free – und das völlig kostenlos.

---

## Wie viel Hardware brauchst du für Proxmox?

Proxmox läuft auch auf älteren Rechnern und unterstützt praktisch jeden handelsüblichen Prozessor (x86_64 – das ist der Standard bei Intel und AMD). Anders als VMware musst du keine teure Spezial-Hardware kaufen.

### Minimal-Ausstattung

| Komponente | Minimal | Empfohlen |
|-----------|---------|-----------|
| **CPU (Prozessor)** | 4 Kerne (z. B. Intel Core i5-6500) | 8+ Kerne (Intel i7/i9 oder AMD Ryzen) |
| **RAM (Arbeitsspeicher)** | 8 GB | 32–64 GB |
| **Festplatte (Storage)** | 256 GB SSD | 1 TB NVMe + HDD für Backups |
| **Netzwerk** | 1 Gigabit-Anschluss | 2,5 oder 10 Gigabit |

> **Gut zu wissen:** Zum Zeitpunkt dieses Artikels ist Proxmox VE 9.2 die aktuelle Version. Sie bringt einen automatischen Lastausgleich zwischen mehreren Servern, ein für Mobilgeräte optimiertes Web-Interface und aktuelle Versionen aller enthaltenen Komponenten. Wichtig für dich als Einsteiger: **Die Installation und Bedienung ändert sich kaum von Version zu Version** – du kannst diese Anleitung auch in zwei Jahren noch nutzen.

---

## Gute Hardware für dein Proxmox-Homelab – nach Budget

### 💰 1–50 € – Fujitsu Futro S740 oder S7010

Was du auf dem Gebrauchtmarkt findest: meist mit 8 GB RAM und 64 GB SSD.

- **Prozessor (CPU):** Intel J4125 (S7010, 4 Kerne) oder Intel J4105 (S740, 4 Kerne) – **beide lüfterlos** (kein Lüftergeräusch)
- **Arbeitsspeicher (RAM):** 8 GB offiziell, 16 GB getestet – ein einzelner Steckplatz
- **Festplatte:** 64 GB M.2 SATA – austauschbar, aber **nur für SATA-SSDs** (kein NVMe, siehe SSD-Warnung unten)
- **Netzwerk:** 1 Gigabit-Anschluss (GbE)
- **Erweiterbarkeit:** ❌ Nur ein RAM-Steckplatz, kein zweiter SSD-Slot, kein PCIe-Slot für Zusatzkarten
- **KI-Tauglichkeit:** ❌ Für lokale KI-Modelle (Ollama) nicht geeignet – Prozessor zu schwach, RAM zu knapp
- **Stromverbrauch (Leerlauf):** ca. 6–8 Watt – günstiger als jede Glühbirne
- **USB-C?** Nein

**Ideal für:** Erste Proxmox-Experimente, Pi-hole (Werbeblocker), AdGuard (DNS-Filter), Netzwerk-Monitoring

👉 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

### 💰 100–150 € – HP ProDesk 400 G3/G4 oder Dell Optiplex 3060/3070 Micro

- **Prozessor (CPU):** Intel Core i5 der 7.–9. Generation (4–6 Kerne)
- **Arbeitsspeicher (RAM):** Bis zu 32 GB DDR4 – **zwei Steckplätze, nicht fest verlötet**
- **Festplatte:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA – zwei Plätze, gut erweiterbar
- **Netzwerk:** 1 Gigabit-Anschluss
- **Erweiterbarkeit:** ✅ RAM nachrüstbar, zweiter SSD-Platz vorhanden. Kein PCIe-Slot im Innern.
- **KI-Tauglichkeit:** ⚠️ Basis möglich. Phi-3-mini (ein kleines KI-Modell) läuft mit über 10 Tokens/s auf der CPU – flüssig für Texte. Größere Modelle (Llama-3-8B) werden langsamer. 16+ GB RAM empfohlen.
- **Stromverbrauch (Leerlauf):** ca. 12–18 Watt
- **USB-C?** Nein (nur USB-A, der rechteckige Standard-Anschluss)

**Ideal für:** Einen vollwertigen Proxmox-Host für viele Container und 3–5 virtuelle Maschinen, Home Assistant (Smart Home), Jellyfin (Medienserver)

**Wichtiger Hinweis zur SSD-Kompatibilität:** Dieses Gerät unterstützt **NVMe-SSDs** (den schnellen Standard mit bis zu 6.000 MB/s). Der günstigere Fujitsu Futro weiter oben unterstützt **nur SATA-SSDs** (langsamer, ~560 MB/s, aber für Proxmox völlig ausreichend). Wenn du beide Komponenten kaufst, achte darauf, dass die SSD zum PC passt!

- 🔍 [HP ProDesk 400 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=matmaksa-homelab-21)
- 🔍 [Dell Optiplex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+Optiplex+3070+Micro&tag=matmaksa-homelab-21)

---

### 💰 150–200 € – Lenovo M720q Tiny

- **Prozessor (CPU):** Intel Core i5-8500T oder i7-8700T (6 Kerne)
- **Arbeitsspeicher (RAM):** Bis zu 32 GB DDR4 – zwei Steckplätze
- **Festplatte:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1 Gigabit-Anschluss
- **Erweiterbarkeit:** ✅ RAM und SSD nachrüstbar. **Pluspunkt:** Ein PCIe-Slot im Innern – damit kannst du eine 10-Gigabit-Netzwerkkarte oder eine kleine Grafikkarte einbauen. Das hat kein anderer Mini-PC in dieser Preisklasse.
- **KI-Tauglichkeit:** ✅ Phi-3-mini läuft mit über 10 Tokens/s. Mit 32 GB RAM auch Llama-3-8B nutzbar.
- **Stromverbrauch (Leerlauf):** ca. 12–20 Watt
- **USB-C?** **Ja** – einmal USB-C. Das ist selten in dieser Klasse.

**Ideal für:** KI-Spielereien (Ollama für lokale KI-Modelle), Cluster-Node mit PCIe-Erweiterung, Home Assistant + Nextcloud + KI alles in einem

- 🔍 [Lenovo M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=matmaksa-homelab-21)

---

### 💰 > 200 € – Minisforum MS-01 (neu)

- **Prozessor (CPU):** Intel Core i9-13900H (14 Kerne) – ein sehr leistungsstarker Prozessor
- **Arbeitsspeicher (RAM):** Bis zu 96 GB DDR5 – der neueste, schnelle RAM-Standard
- **Festplatte:** 3× M.2 NVMe – extrem erweiterbar
- **Netzwerk:** 2× 10 Gigabit (SFP+) + 2× 2,5 Gigabit
- **Erweiterbarkeit:** ✅ Drei NVMe-Slots, zwei DDR5-Slots
- **KI-Tauglichkeit:** ✅ Ja, mit 64+ GB RAM sind auch größere KI-Modelle möglich
- **Stromverbrauch (Leerlauf):** Keine exakten Daten vorhanden

**Ideal für:** Leistungshungrige Anwendungen, Cluster mit schnellem Netzwerk, KI-Workloads – wenn das Budget es hergibt.

👉 [Preis bei Geizhals prüfen](https://geizhals.de/minisforum-ms-01-a3260346.html)

---

## 💾 Günstige SSD-Empfehlung (Achtung Kompatibilität!)

High-End-SSDs wie die Samsung 990 Pro (150+ €) lohnen sich im Homelab selten. Allerdings: **Nicht jede SSD passt in jeden PC.** Bitte beachten:

- **Fujitsu Futro S7010/S740** unterstützt **nur M.2 SATA** (langsamerer Standard, ~560 MB/s). Hier ist die **WD Blue SA510** (SATA) die richtige Wahl.
- **HP ProDesk, Dell Optiplex und Lenovo M720q** unterstützen **NVMe** (schneller Standard, bis 6.000 MB/s). Hier passt die **Kingston NV3**.

| Modell | Preis (ca.) | Typ | Passt zu | Besonderheit |
|--------|------------|-----|----------|-------------|
| [Kingston NV3 1 TB](https://geizhals.de/kingston-nv3-nvme-pcie-4-0-ssd-1tb-snv3s-1000g-a3248579.html?hloc=de) | ~139 € | NVMe PCIe 4.0 (sehr schnell) | HP, Dell, Lenovo ab 100€ | Nur für Geräte mit NVMe-Support |
| [WD Blue SA510 1 TB](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | ~135 € | SATA (M.2, langsamer) | Fujitsu Futro (passt auch in HP/Dell) | ⬅️ **Genau diese brauchst du für den Fujitsu Futro!** |

---

## Proxmox einrichten – Schritt für Schritt (auch für absolute Einsteiger)

Die Installation von Proxmox ist überraschend einfach – eine der großen Stärken der Plattform. Hier der genaue Ablauf:

### Was du brauchst
- Den Mini-PC (deine zukünftige Proxmox-Maschine)
- Einen zweiten Computer (Laptop oder PC), von dem aus du die Installation machst
- Einen USB-Stick (mindestens 4 GB)
- Einen Monitor und eine Tastatur (nur für die Installation, danach nicht mehr nötig)

### Die 5 Schritte (mit allen praktischen Details)

1. **ISO herunterladen** – Gehe auf [proxmox.com](https://www.proxmox.com/downloads) und lade die Installations-Datei (ISO) herunter. Das ist kostenlos, keine Registrierung nötig.

2. **Auf USB-Stick schreiben** – Mit [Rufus](https://rufus.ie/de/) (Windows) oder Balena Etcher (Mac/Linux) wird die ISO-Datei auf den USB-Stick übertragen. Der Stick wird dabei komplett gelöscht, also vorher leeren, wenn noch Daten drauf sind.

3. **Vorbereitung: Alles anschließen** – Bevor du den PC einschaltest:
   - **Monitor** an den Mini-PC anschließen (HDMI oder DisplayPort)
   - **Tastatur** an den Mini-PC anschließen (USB)
   - **LAN-Kabel** vom Mini-PC zum Router (WLAN haben die meisten Mini-PCs nicht)
   - USB-Stick mit der Proxmox-Installation einstecken
   - **Dann** den Mini-PC einschalten und mehrfach F2, F10 oder F12 drücken (je nach Hersteller), bis ein Menü erscheint. Dort den USB-Stick als Startlaufwerk auswählen.

4. **Dem Installations-Assistenten folgen** – Nach dem Booten erscheint ein Text-Bildschirm. Folgende Angaben werden abgefragt:
   - **Festplatte auswählen:** Hier die SSD des Mini-PCs auswählen (Vorsicht: alle Daten werden gelöscht)
   - **Passwort vergeben:** Ein sicheres Passwort für den Administrator-Zugang
   - **IP-Adresse eingeben:** Proxmox braucht eine feste IP-Adresse im Heimnetz. Du musst sie dir nicht ausdenken – so findest du die richtige: Schau auf deinem Router nach (meist auf einem Aufkleber auf der Unterseite: "IP-Adresse: 192.168.X.X" oder "Gateway: 192.168.X.1"). Merke dir die ersten drei Zahlen (z. B. 192.168.1). Dann gib in Proxmox eine Nummer zwischen 2 und 254 ein, die noch kein anderes Gerät im Haus hat – z. B. **192.168.1.99**. Die "Subnetzmaske" ist fast immer **255.255.255.0** und das "Gateway" ist die Adresse deines Routers (meist 192.168.1.1 oder 192.168.0.1).

5. **Fertig – umstecken und loslegen** – Nach der Installation (dauert ca. 5 Minuten) passiert Folgendes:
   - Der Mini-PC startet neu (USB-Stick abziehen, wenn er dazu auffordert)
   - Jetzt kannst du **Monitor und Tastatur vom Mini-PC abstecken**
   - Der Mini-PC bleibt mit **Strom und LAN-Kabel** verbunden – stell ihn in den Keller, Schrank oder unters Bett. Er läuft von jetzt an ohne Monitor und Tastatur.
   - Setz dich an **deinen normalen Laptop oder PC**, öffne den Browser und gib ein: `https://192.168.1.99:8006` (die IP, die du in Schritt 4 eingetragen hast, plus :8006).
   - Es erscheint eine Sicherheitswarnung (Zertifikat-Warnung) – das ist normal, weil Proxmox ein selbst erstelltes Zertifikat verwendet. Klicke auf "Trotzdem fortfahren" oder "Erweitert" → "Weiter zur Website".
   - **Herzlichen Glückwunsch!** Du siehst jetzt das Proxmox-Dashboard. Dein Homelab läuft!

---

## Das solltest du vor dem Kauf wissen

Bevor du Hardware kaufst, hier ein paar praktische Fallstricke aus meiner Erfahrung:

- **RAM richtig planen:** Proxmox selbst braucht kaum Arbeitsspeicher (~2 GB). Ein LXC-Container (schlanke Virtualisierung) benötigt je nach Anwendung 0,5–4 GB (Pi-hole: ~0,5 GB, Nextcloud: ~2–4 GB). Eine vollständige VM startet bei mindestens 4 GB. Mit **32 GB** bist du für die meisten Homelabs gut aufgestellt.
- **Eine SSD reicht:** Zwei SSDs im Verbund sind sicherer, aber fürs Homelab tut es auch eine. Wichtiger sind regelmäßige Backups auf eine externe Festplatte.
- **Netzwerk nicht vergessen:** Ein einfacher Gigabit-Anschluss reicht für die ersten Schritte völlig. Erst wenn du mehrere Dienste gleichzeitig stark belastest (z. B. Medienserver + Cloud + Game-Server), wird ein schnellerer Anschluss interessant.
- **Gebraucht ist oft besser als neu:** Business-Mini-PCs (HP, Dell, Lenovo) sind für den Dauerbetrieb (24/7) ausgelegt. Ein gebrauchtes Modell für 100–150 € läuft meist jahrelang problemlos und hat vor ein paar Jahren noch das Zehnfache gekostet.

---

## Drei Tools, die dein Homelab auf das nächste Level bringen

### 1. Proxmox Backup Server (PBS) – Sicherungen leicht gemacht

Automatische, platzsparende Backups deiner VMs und Container. Ideal als zweite virtuelle Maschine auf demselben Host oder auf einem günstigen Zweit-Rechner.

### 2. Ollama + Open WebUI für lokale KI

Ab 32 GB RAM kannst du kleine KI-Modelle direkt auf deinem Proxmox-Host laufen lassen – ohne Internet, ohne Abo, ohne dass deine Daten nach extern gehen. **Phi-3-mini** (ein kompaktes Sprachmodell von Microsoft) läuft mit über 10 Tokens/s auf der CPU – völlig flüssig für Chat und Textaufgaben.

**Ehrliche Ansage zur Einrichtung:** Die Installation von Ollama erfordert ein paar Schritte im Terminal (dem schwarzen Fenster mit weißer Schrift). Du musst Docker in einem LXC-Container einrichten, was das Setzen von "Root-Rechten" und das Anpassen von Konfigurationsdateien bedeutet. Das ist machbar, aber nicht in 15 Minuten und nicht rein per Mausklick. Such einfach nach "Ollama Proxmox LXC installieren" – es gibt gute Schritt-für-Schritt-Anleitungen. Sobald es einmal läuft, steuerst du alles übers Web-Interface (Open WebUI) – dann wieder ohne Terminal.

### 3. Home Assistant via LXC – Smart Home Zentrale

Licht, Heizung, Kameras – alles von einer Oberfläche aus steuern. Home Assistant in einem LXC-Container braucht nur ~2 GB RAM und ist in 10 Minuten eingerichtet.

---

## Häufig gestellte Fragen

### Ist Proxmox VE wirklich komplett kostenlos?

Ja. Proxmox ist Open Source – der Quellcode ist öffentlich einsehbar und darf von jedem kostenlos genutzt werden. Es gibt zwar ein kostenpflichtiges Enterprise-Repository mit getesteten Updates, aber die **kostenlose Community-Version reicht fürs Homelab völlig aus** (Sicherheitsupdates inklusive).

### Kann ich meine bestehenden VMware-VMs zu Proxmox migrieren?

Ja. Du hast drei Wege: Export aus VMware als OVF/OVA und Import in Proxmox, Konvertierung mit dem Tool `qemu-img convert` oder das automatisierte `virt-v2v`-Tool. Die meisten Betriebssysteme (Windows, Linux, FreeBSD) laufen ohne Anpassungen.

### Brauche ich Linux-Kenntnisse für Proxmox?

Für die **grundlegende Nutzung**: nein. Die Weboberfläche erlaubt die Verwaltung per Mausklick – VMs anlegen, starten, stoppen, Snapshots erstellen. Für **fortgeschrittene Themen wie die KI-Einrichtung (Ollama) oder Cluster-Verwaltung** sind ein paar Terminal-Befehle nötig. Aber diese speziellen Dinge lernst du gezielt dann, wenn du sie brauchst – du musst nicht vorher Linux-Profi sein.

---

## Fazit: Welcher Weg ist der richtige für dich?

| Budget | Empfehlung | Ideal für |
|--------|-----------|-----------|
| **1–50 €** | Fujitsu Futro S740/S7010 (gebraucht) | Erste Experimente, Werbeblocker, Netzwerk-Dienste |
| **100–150 €** | HP ProDesk 400 G4 oder Dell Optiplex 3070 (gebraucht) | Den "richtigen" Homelab-Server für viele Dienste |
| **150–200 €** | Lenovo M720q Tiny (gebraucht) | KI-Spielereien, maximale Erweiterbarkeit, Cluster |
| **> 200 €** | Minisforum MS-01 (neu) | High-End: 10 Gigabit, große KI-Modelle, Profi-Homelab |

Die VMware-Ära im Homelab ist vorbei. Proxmox ist die logische, kostenlose und leistungsfähigere Alternative – und mit gebrauchter Business-Hardware kommst du günstiger weg als mit jedem Fertig-NAS oder Mini-PC aus dem Laden.

