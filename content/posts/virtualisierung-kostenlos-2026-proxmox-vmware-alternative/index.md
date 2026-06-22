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
---

**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

Stell dir vor, du hast zu Hause einen kleinen Server – einen Mini-PC, der leise in der Ecke steht und Tag und Nacht läuft. Darauf sollen mehrere Dienste gleichzeitig laufen: Pi-hole als Werbeblocker fürs ganze Netz, ein Medienserver für Filme (Jellyfin), eine Cloud für deine Fotos (Nextcloud) und vielleicht noch ein Game-Server. Müsstest du für jeden Dienst einen eigenen Rechner kaufen, wärst du schnell bei 500–1.000 € und einem Berg Kabelgewirr.

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

Stell dir vor, dein Computer ist ein **Mehrfamilienhaus** mit einem einzigen großen Raum. Virtualisierung baut **Zwischenwände ein** – plötzlich können mehrere Familien (VMs oder Container) gleichzeitig im selben Haus wohnen, ohne sich gegenseitig zu stören. Jede Familie hat ihren eigenen Bereich, ihr eigenes Inventar und kann unabhängig ein- und ausziehen.

Es gibt zwei Bauarten für diese "Zwischenwände":

| Typ | Beschreibung | Beispiel |
|-----|-------------|----------|
| **Typ 1 (Bare Metal)** | Läuft direkt auf der Hardware – wie ein Vermieter, der im Erdgeschoss wohnt | Proxmox VE, VMware ESXi |
| **Typ 2 (Gehostet)** | Läuft als Programm in Windows oder Linux – wie ein Untermieter | VirtualBox, VMware Workstation |

Proxmox VE ist ein **Typ-1-Hypervisor**: Er sitzt direkt auf der Hardware und verteilt die Ressourcen (CPU, RAM, Festplatte) effizient auf alle virtuellen Maschinen.

### Was bringt dir das konkret?

- **Isolation:** Ein abgestürzter Dienst reißt die anderen nicht mit – dein Medienserver läuft weiter, auch wenn Pi-hole gerade neu startet
- **Snapshots:** Bevor du eine riskante Änderung machst, knipst du einen Schnappschuss. Läuft was schief? Ein Klick und alles ist wie vorher
- **Kosteneffizienz:** Ein Server ersetzt fünf – weniger Strom, weniger Platz, weniger Lärm
- **Flexibilität:** Du kannst verschiedene Betriebssysteme parallel fahren – Linux für Docker, Windows für bestimmte Anwendungen

---

## Proxmox VE – Die kostenlose Lösung für dein Homelab

Proxmox Virtual Environment (VE) ist eine **komplett kostenlose Virtualisierungsplattform** auf Debian-Basis. Sie vereint zwei Technologien unter einer Weboberfläche:

### KVM-VMs (der "Gästeraum mit eigenem Eingang")

Virtuelle Maschinen mit eigenem BIOS, eigener CPU und eigenem RAM. Ideal, wenn du Windows Server, Ubuntu, Rocky Linux und FreeBSD **gleichzeitig** auf einem Rechner betreiben willst.

### LXC-Container (die "WG mit geteilter Küche")

Container teilen sich den Linux-Kernel des Hosts – das spart enorm Ressourcen. Ein LXC-Container mit Ubuntu braucht nur **~100 MB RAM** statt 2 GB für eine vollständige VM. Das ist der Unterschied zwischen einer möblierten Wohnung (LXC) und einem kompletten Hausbau (KVM).

**Perfekt für:** Docker-Hosts, Pi-hole, n8n, Home Assistant – alles, was schlank laufen soll.

### Die wichtigsten Funktionen auf einen Blick

| Funktion | Beschreibung |
|----------|-------------|
| **Web-UI** | Verwaltung über den Browser – keine Linux-Kenntnisse nötig |
| **Snapshots** | Zustand der VM einfrieren und bei Bedarf zurückrollen |
| **Backup** | Komplettes VM-Backup mit einem Klick (VZDump) |
| **Cluster** | Mehrere Rechner als einen großen Server verwalten |
| **Live-Migration** | VM umziehen, während sie läuft – keine Ausfallzeit |
| **REST API** | Automatisierung per Skript – für Fortgeschrittene |

> 👉 [Proxmox VE bei Amazon suchen (Bücher & Hardware)](https://www.amazon.de/s?k=Proxmox+VE+Virtualisierung&tag=makmatas-homelab-21)

---

## Proxmox vs. VMware ESXi – Der Vergleich 2026

Seit Broadcom VMware übernommen hat, ist Schluss mit der kostenlosen ESXi-Version. Wer VMware weiternutzen will, zahlt **mindestens ~500 € pro Jahr** (vSphere Foundation) – und das ohne Storage-Funktionen wie ZFS oder Ceph.

| Kriterium | Proxmox VE | VMware vSphere (Broadcom) |
|-----------|-----------|--------------------------|
| **Preis** | **0 €** – komplett kostenlos | **Ab ~500 €/Jahr** – nur mit Support-Lizenz |
| **Container** | LXC inkludiert | Nicht vorhanden (nur VMs) |
| **ZFS / Snapshots** | Ja, integriert | Nur mit Zusatzkosten |
| **Ceph Storage** | Integriert (Hochverfügbarkeit) | vSAN ab **~2.000 €/Jahr** |
| **Community** | Aktiv, deutschsprachig | Stark geschrumpft seit Broadcom |
| **Updates** | Kostenlos (Community-Repo) | Nur mit gültigem Support-Vertrag |

**Die Botschaft:** Proxmox bietet mehr Funktionen als der alte ESXi Free – und das völlig kostenlos.

---

## Wie viel Hardware brauchst du für Proxmox?

Proxmox läuft auch auf älteren Rechnern. Anders als VMware (das eine strikte Hardware-Kompatibilitätsliste hat) unterstützt Proxmox praktisch jeden x86_64-Prozessor.

### Minimal-Ausstattung (Tabellen-Struktur)

| Komponente | Minimal | Empfohlen |
|-----------|---------|-----------|
| **CPU** | 4 Kerne (z. B. Intel Core i5-6500, 4C/4T) | 8+ Kerne (Intel i7/i9 oder AMD Ryzen) |
| **RAM** | 8 GB | 32–64 GB |
| **Storage** | 256 GB SSD | 1 TB NVMe + HDD für Backups |
| **Netzwerk** | 1 GbE | 2,5 GbE oder 10 GbE |

> **Tipp:** Proxmox VE 9.2 (basierend auf Debian 13.5 „Trixie“) bringt den modernen Linux-Kernel 7.0, QEMU 11.0, LXC 7.0 sowie ZFS 2.4 – die neueste Version mit Dynamic Load Balancer, erweitertem SDN, HA-Arm/Disarm und verwaltbaren CPU-Profilen.

---

## Gute Hardware für dein Proxmox-Homelab – nach Budget

### 💰 Bis 50 € – Fujitsu Futro S7010

- **CPU:** Intel J4125 (4 Kerne, 4 Threads) – lüfterlos, 10 Watt Leerlauf
- **RAM:** 8 GB offiziell, 16 GB getestet – ein RAM-Slot, DDR4-SODIMM
- **Storage:** 64 GB M.2 SATA – kein zweiter Slot, Upgrade auf größere SSD nötig
- **Netzwerk:** 1× GbE
- **Upgrade-Fähigkeit:** ❌ RAM verlötet? Nein – aber nur ein Slot. SSD austauschbar, aber M.2 SATA only.
- **KI-Potenzial:** ❌ Kein lokales KI-Modell möglich (4 Kerne, 8–16 GB RAM). Für Ollama nicht geeignet.
- **Betriebssystem-Empfehlung:** Proxmox VE mit LXC-Containern (Pi-hole, AdGuard, einfacher Webserver)
- **Stromverbrauch Idle:** ca. 6–8 Watt – damit günstiger im Dauerbetrieb als jede Glühbirne
- **Praxis-Tipp:** Läuft bei mir seit Monaten als OPNSense-Firewall und AdGuard-DNS – absolut lautlos, kein Lüftergeräusch

**Ideal für:** Erste Proxmox-Experimente, DNS/DHCP, Monitoring, Backup-Ziel (PBS)

👉 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21)

---

### 💰 50–100 € – HP ProDesk 400 G4 Mini / Dell Optiplex 3060 Micro

- **CPU:** Intel Core i5-8500T (6 Kerne, 6 Threads) – mit Lüfter, ~15 Watt Leerlauf
- **RAM:** 32 GB DDR4 möglich – zwei RAM-Slots (kein verlöteter RAM)
- **Storage:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA – zweiter Platz vorhanden
- **Netzwerk:** 1× GbE
- **Upgrade-Fähigkeit:** ✅ RAM auf 32 GB erweiterbar. Platz für zweite SSD (2,5 Zoll). Kein PCIe-Slot.
- **KI-Potenzial:** ⚠️ Basis möglich. Llama-3-8B via CPU (ohne GPU) läuft langsam (~2-3 Tokens/s). Für Phi-3-mini (3,8B) reicht es flüssig mit 16+ GB RAM.
- **Betriebssystem-Empfehlung:** Proxmox VE + Docker-LXC + Home Assistant VM + Jellyfin
- **Stromverbrauch Idle:** ca. 12–18 Watt – je nach verbauter SSD und RAM-Bestückung
- **USB-C?** Nein. Nur USB 3.0 (Typ A). Kein DisplayPort über USB-C.

**Ideal für:** Vollwertigen Proxmox-Host für 3–5 VMs/Container, Home Assistant, Medienserver

- 🔍 [HP ProDesk 400 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=makmatas-homelab-21)
- 🔍 [Dell Optiplex 3060 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+Optiplex+3060+Micro&tag=makmatas-homelab-21)

---

### 💰 100–150 € – Dell Optiplex 3070 Micro / Lenovo M720q Tiny

- **CPU:** Intel Core i5-9500T (6 Kerne, 6 Threads) – mit Lüfter
- **RAM:** Bis zu 32 GB DDR4 – zwei RAM-Slots (SODIMM)
- **Storage:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1× GbE
- **Upgrade-Fähigkeit:** ✅ RAM erweiterbar, zweiter SSD-Slot vorhanden. **Lenovo M720q:** zusätzlicher PCIe-Slot (Riser-Karte) für 10GbE oder GPU
- **KI-Potenzial:** ✅ Phi-3-mini und Llama-3-8B via CPU nutzbar (4-5 Tokens/s). 32 GB RAM empfohlen. Reine CPU-Inferenz ohne dedizierte GPU.
- **Betriebssystem-Empfehlung:** Proxmox VE mit Ollama-LXC + Open WebUI + Home Assistant + Nextcloud
- **USB-C?** Dell Optiplex 3070: **Nein**. Lenovo M720q: **Ja** – einmal USB-C (DisplayPort-alt)
- **Stromverbrauch Idle:** ca. 12–20 Watt

**Ideal für:** Den ersten "richtigen" Homelab-Server mit KI-Spielerei. Lenovo M720q für Cluster-Bau mit PCIe-Anbindung.

- 🔍 [Dell Optiplex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+Optiplex+3070+Micro&tag=makmatas-homelab-21)
- 🔍 [Lenovo M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=makmatas-homelab-21)

---

### 💰 150–300 € – Lenovo M720q / GMKtec G3S (neu)

**Lenovo M720q (gebraucht, ~90–150 €)**
- Wie oben, **aber mit PCIe-Slot** – du kannst eine 10GbE-Karte oder eine kleine GPU einbauen
- **Upgrade-Fähigkeit:** ✅ Einziger 1L-PC mit PCIe-Slot. RAM + Dual-Storage + GPU/10GbE = maximale Flexibilität

**GMKtec G3S (neu, ~200–230 €)**
- **CPU:** Intel N95 Alder Lake (4 Kerne, 4 Threads, 2023) – lüfterlos? Nein, mit Lüfter, ~10–15 Watt Leerlauf
- **RAM:** 16 GB DDR4 verlötet – **nicht erweiterbar** ⚠️
- **Storage:** 1× M.2 NVMe – kein zweiter Slot
- **Upgrade-Fähigkeit:** ❌ RAM verlötet, nur ein SSD-Slot. Kaufentscheidung: direkt mit genug RAM kaufen
- **KI-Potenzial:** ❌ 16 GB RAM für KI zu knapp, CPU zu schwach für flüssige Modelle
- **Betriebssystem-Empfehlung:** Proxmox VE für leichte Dienste (Pi-hole, AdGuard, kleiner Webserver)

**Ideal für:** Wer Neugerät mit Garantie will (GMKtec) oder maximale Erweiterbarkeit braucht (Lenovo).

- 🔍 [Lenovo M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=makmatas-homelab-21)
- 🔍 [GMKtec G3S bei Amazon suchen](https://www.amazon.de/s?k=GMKtec+G3S&tag=makmatas-homelab-21)

---

## 💾 Günstige SSD-Empfehlung

High-End-SSDs wie die Samsung 990 Pro (150+ €) lohnen sich im Homelab selten. Dein ZFS-Root-Pool wird auch mit einer günstigen NVMe flott:

| Modell | Preis (ca.) | Typ | Besonderheit |
|--------|------------|-----|-------------|
| [Kingston NV3 1 TB](https://geizhals.de/kingston-nv3-nvme-pcie-4-0-ssd-1tb-snv3s-1000g-a3248579.html?hloc=de) | ~139 € | NVMe PCIe 4.0 | Solide Allround-SSD, 6.000 MB/s lesend |
| [WD Blue SA510 1 TB](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | ~135 € | SATA (M.2) | Günstiger, aber SATA-Limit (560 MB/s) – fürs Boot-Laufwerk völlig ausreichend |

---

## Proxmox einrichten – Die ersten Schritte (auch für Einsteiger)

Die Installation ist erstaunlich einfach – eine der großen Stärken von Proxmox:

1. **ISO herunterladen** von [proxmox.com](https://www.proxmox.com/downloads) (kostenlos, keine Registrierung nötig)
2. **Auf USB-Stick schreiben** – mit [Rufus](https://rufus.ie/de/) (Windows) oder Balena Etcher (Mac/Linux)
3. **Vom USB-Stick booten** – den Rechner starten, F2/F12 drücken, USB als Boot-Laufwerk auswählen
4. **Installations-Assistent folgen** – dauert etwa 5 Minuten, nur: Festplatte auswählen, Passwort setzen, IP-Adresse eingeben
5. **Web-UI aufrufen:** `https://deine-ip:8006` im Browser – fertig!

> **Keine Linux-Kenntnisse nötig?** Für die Grundnutzung: ja. Das Web-UI ist übersichtlich und selbsterklärend. Erst wenn du ZFS-Tuning, Ceph-Cluster oder Kommandozeilen-Backups machen willst, helfen Linux-Grundlagen.

---

## Das solltest du vor dem Kauf wissen

Bevor du Hardware kaufst, hier ein paar **praktische Fallstricke** aus meiner Erfahrung:

- **RAM nicht unterschätzen:** Proxmox selbst braucht kaum RAM (~2 GB), aber jede VM will ihren eigenen Speicher. Faustregel: 8 GB Basis + 2 GB pro LXC + 4 GB pro VM. 32 GB sind ein guter Startwert.
- **Eine SSD reicht:** ZFS mag zwei SSDs im Mirror, aber fürs Homelab tut es auch eine. Mach regelmäßige Backups auf eine externe HDD oder einen zweiten Rechner.
- **Netzwerk nicht vergessen:** Ein GbE-Anschluss reicht für die ersten Schritte. Erst wenn du mehrere VMs gleichzeitig stark belastest (z. B. Jellyfin + Nextcloud + Game-Server), wird 2,5 GbE interessant.
- **Gebraucht ist oft besser als neu:** Für 100–150 € bekommst du einen Business-1L-PC, der vor 5 Jahren noch 1.000 € gekostet hat. Die Dinger sind für 24/7-Betrieb ausgelegt und laufen Jahre ohne Probleme.

---

## Drei Tools, die dein Homelab auf das nächste Level bringen

### 1. Proxmox Backup Server (PBS) – Kostenlose Backups

Sicherungen deiner VMs und Container – dedupliziert, verschlüsselt, mit Bandbreiten-Limit. Ideal als zweiter LXC-Container auf demselben Host oder einem günstigen Futro.

### 2. Home Assistant via LXC

Home Assistant in einem LXC-Container braucht nur ~2 GB RAM und lässt sich in 10 Minuten einrichten. Perfekt für Smart-Home-Steuerung (Licht, Heizung, Kameras) direkt auf deinem Proxmox-Host.

### 3. Ollama + Open WebUI für lokale KI

Ab 32 GB RAM kannst du kleine KI-Modelle wie **Phi-3-mini (3,8B Parameter)** oder **Llama-3-8B** direkt auf deinem Proxmox-Host laufen lassen. Einrichtung per LXC-Container mit Docker – in 15 Minuten erledigt. Die Modelle laufen rein über die CPU (keine GPU nötig), aber erwarte ~2–5 Tokens pro Sekunde, nicht ChatGPT-Tempo.

---

## Häufig gestellte Fragen

### Ist Proxmox VE wirklich komplett kostenlos?

Ja. Proxmox VE ist Open Source (GPLv2). Du kannst es unbegrenzt nutzen, ohne zu bezahlen. Es gibt ein Enterprise-Repository (kostenpflichtig), aber das **Community-Repository reicht fürs Homelab völlig aus** – Updates und Sicherheits-Patches inklusive.

### Kann ich meine bestehenden VMware-VMs zu Proxmox migrieren?

Ja. Du hast drei Wege: Export aus VMware als OVF/OVA und Import in Proxmox, Konvertierung per `qemu-img convert` oder das automatisierte `virt-v2v`-Tool. Die meisten Betriebssysteme laufen ohne Anpassungen.

### Brauche ich Linux-Kenntnisse für Proxmox?

Für die ersten Schritte: nein. Die Weboberfläche erlaubt die vollständige Verwaltung per Mausklick. Für Fortgeschrittenes (ZFS-Tuning, Cluster, Kommandozeile) helfen Grundkenntnisse, aber die lernst du mit der Zeit von selbst.

---

## Fazit: Welcher Weg ist der richtige für dich?

| Budget | Empfehlung | Kosten (ca.) | Ideal für |
|--------|-----------|-------------|-----------|
| **Bis 50 €** | Fujitsu Futro S7010 + 16 GB RAM | ~50 € | Erste Schritte, Pi-hole, DNS, Monitoring |
| **~100 €** | HP ProDesk 400 G4 oder Dell Optiplex 3060 | ~90–120 € | Vollwertiger Homelab-Host, Home Assistant, Jellyfin |
| **~150 €** | Lenovo M720q + PCIe-Erweiterung | ~130–180 € | KI-Spielereien, 10GbE, Cluster-Node |
| **~250 €** | Lenovo M720q + 32 GB RAM + SSD | ~200–250 € | KI + Home Assistant + Nextcloud + Backup alles in einem |

**Meine klare Empfehlung für Einsteiger:** Hol dir einen **HP ProDesk 400 G4 Mini gebraucht für ~90 €**, pack 16–32 GB RAM rein, eine günstige 500 GB NVMe und installiere Proxmox. Damit hast du für unter **150 € Gesamtkosten** eine Plattform, die dich die nächsten Jahre begleitet.

Die VMware-Ära im Homelab ist vorbei. Proxmox ist die logische, kostenlose und leistungsfähigere Alternative – und mit gebrauchter Business-Hardware kommst du günstiger weg als mit jedem Fertig-NAS oder Mini-PC aus dem Laden.

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.*
