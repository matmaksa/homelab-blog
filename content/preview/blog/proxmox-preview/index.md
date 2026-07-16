+++
title = "Virtualisierung kostenlos 2026: Proxmox VE als VMware-Alternative im Homelab"
description = "Proxmox VE als kostenlose VMware-Alternative: Virtualisierung fürs Homelab mit VMs, LXC-Containern und integriertem Backup – für Einsteiger erklärt."
date = 2026-07-01
draft = true
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
approved_for_publish = false
image = "featured.jpg"

[cover]
image = "featured.jpg"
alt = "Proxmox VE Dashboard auf einem Server – Virtualisierung kostenlos und Open Source"
relative = true

[taxonomies]
tags = ["proxmox", "virtualisierung", "vmware-alternative", "homelab", "open-source"]
categories = ["Virtualisierung"]

[extra]
content_state = "draft"
audit_status = "pending"
user_approval_required = true
instagram_derivatives_required = false
instagram_derivatives_status = "not_planned"
content_cluster = "proxmox"
content_role = "pillar"
risk_level = "low"
next_action = "review_before_publish"
related_articles = ["mini-pc-homelab-vergleich"]

[[extra.notes]]
text = "Vollständige Neufassung: Community-Repo-Hinweis, Snapshot != Backup, Live-Migration-Voraussetzungen, KI als optionaler Zusatz, keine Token-Angaben."
+++

**Stand: Juli 2026 | Lesezeit: ca. 10 Minuten**

> Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.

Stell dir vor, du hast zu Hause einen kleinen Server – einen Mini-PC, der leise in der Ecke steht und rund um die Uhr läuft. Darauf sollen gleichzeitig mehrere Dienste laufen: Pi-hole (Werbeblocker fürs Heimnetz), Jellyfin (Medienserver für Filme und Serien), Nextcloud (private Cloud für Fotos und Dokumente) und vielleicht noch ein Game-Server.

Für jeden Dienst einen eigenen Rechner zu kaufen, wäre teuer und unpraktisch. **Virtualisierung** löst genau dieses Problem – und Proxmox VE ist ein bewährter Weg, das ohne Lizenzkosten umzusetzen.

Dieser Artikel richtet sich an **Homelab-Einsteiger ohne Vorkenntnisse**, die eine günstige Alternative zu VMware suchen. Fachbegriffe werden kurz erklärt, damit du weißt, worum es geht.

<!--more-->

---

## 🥇 Kurzempfehlung: Welcher Weg passt zu dir?

| Kategorie | Empfehlung |
|-----------|-----------|
| 💰 Günstigster Einstieg | Proxmox VE auf Fujitsu Futro S7010 (gebraucht, ca. 30–50 €, Stand Juli 2026) |
| 🥇 Beste Preis-Leistung | Proxmox VE auf HP ProDesk 400 G4 (gebraucht, ca. 80–120 €, Stand Juli 2026) |
| 🚀 Maximale Erweiterbarkeit | Lenovo M720q Tiny (gebraucht, ca. 130–180 €, Stand Juli 2026) + PCIe-Slot für Zusatzkarten |
| 🏠 Beste Wahl für Home Assistant | Proxmox LXC-Container (2 GB RAM reichen) |
| 🔧 Einstieg in Proxmox-Cluster | 2× Dell Optiplex 3070 Micro (gebraucht, je ca. 80–130 €, Stand Juli 2026) |

---

## Was ist Virtualisierung? (Einfach erklärt)

Stell dir deinen Computer als **Mehrfamilienhaus** mit einem einzigen großen Raum vor. Virtualisierung baut **Zwischenwände ein** – mehrere Familien (deine Dienste) können gleichzeitig im selben Haus wohnen, ohne sich zu stören. Jede Familie hat ihren eigenen Bereich und kann unabhängig ein- und ausziehen.

Es gibt zwei grundlegende Bauarten dieser „Zwischenwände":

| Typ | Beschreibung | Beispiel |
|-----|-------------|----------|
| **Typ 1 (Bare Metal)** | Läuft direkt auf der Hardware – kein Betriebssystem dazwischen | Proxmox VE, VMware ESXi |
| **Typ 2 (Gehostet)** | Läuft als Programm in Windows oder Linux | VirtualBox, VMware Workstation |

Proxmox VE ist ein **Typ-1-Hypervisor** – eine Spezialsoftware, die direkt auf dem Rechner sitzt und Ressourcen (CPU, RAM, Festplatte) an virtuelle Maschinen und Container verteilt.

### Was bringt dir das konkret?

- **Isolation:** Ein abgestürzter Dienst reißt die anderen nicht mit – dein Medienserver läuft weiter, auch wenn der Werbeblocker gerade neu startet.
- **Snapshots:** Vor einer riskanten Änderung kannst du den aktuellen Zustand einer VM oder eines Containers als Snapshot speichern. Läuft etwas schief, stellst du den Zustand per Klick wieder her. **Wichtig:** Ein Snapshot ist kein Backup. Snapshots sind differenzielle Momentaufnahmen, die auf demselben Speicher liegen – fällt die Festplatte aus, sind Snapshot und Daten weg. Für echte Datensicherheit brauchst du regelmäßige, separate Backups (mehr dazu weiter unten).
- **Kosteneffizienz:** Ein Server ersetzt mehrere – weniger Strom, weniger Platz, weniger Lärm.
- **Flexibilität:** Linux für Docker, Windows für bestimmte Anwendungen – alles auf einem Rechner.

---

## Proxmox VE – Die Community-Version für dein Homelab

Proxmox Virtual Environment (VE) ist eine **kostenlos nutzbare Virtualisierungsplattform** auf Open-Source-Basis. Der Quellcode ist öffentlich einsehbar, und die Software darf ohne Lizenzgebühren eingesetzt werden.

### Community-Repository vs. Enterprise-Repository

Nach der Installation fragt Proxmox, welches Update-Repository du nutzen möchtest. Hier ein wichtiger Punkt, den viele Anleitungen überspringen:

- **Enterprise-Repository:** Enthält besonders getestete, stabile Updates – gedacht für Produktionsumgebungen in Unternehmen. Voraussetzung ist eine kostenpflichtige Subscription (ab ca. 95 €/Jahr pro Node, Stand Juli 2026).
- **Community-Repository (No-Subscription):** Enthält aktuelle Updates ohne Subscription-Pflicht – für Homelabs absolut geeignet. Sicherheitsupdates sind enthalten. Du siehst nach dem Login eine Hinweismeldung ohne Subscription, die dich aber nicht einschränkt.

Für dein Homelab nimmst du das **Community-Repository** – das ist kostenlos und für private Nutzung mehr als ausreichend. Die optionalen Subscriptions sind für Unternehmen gedacht, die Support und besonders getestete Update-Pfade benötigen.

### KVM-VMs (der „Gästeraum mit eigenem Eingang")

Virtuelle Maschinen haben ein eigenes BIOS, eine eigene CPU und eigenen Arbeitsspeicher. Ideal, wenn du verschiedene Betriebssysteme **gleichzeitig** auf einem Rechner betreiben willst – zum Beispiel Windows, Ubuntu und FreeBSD nebeneinander.

### LXC-Container (die „WG mit geteilter Küche")

Container teilen sich den Linux-Kernel des Hosts – das spart erheblich Ressourcen. Ein LXC-Container mit Ubuntu benötigt deutlich weniger RAM als eine vollständige VM. Das ist der Unterschied zwischen einer möblierten Wohnung (LXC) und einem kompletten Hausbau (KVM).

**Gut geeignet für:** Docker, Pi-hole, n8n, Home Assistant, Nextcloud – alles, was schlank laufen soll.

---

## Proxmox vs. VMware ESXi – Der Vergleich 2026

Seit Broadcom VMware übernommen hat (November 2023), gibt es keine kostenlose Version mehr. Wer VMware weiternutzt, zahlt Lizenzgebühren, die für Privatanwender kaum vertretbar sind.

| Kriterium | Proxmox VE | VMware vSphere (Broadcom) |
|-----------|-----------|--------------------------|
| **Preis** | **0 €** (Community-Repo) | Kostenpflichtig, keine freie Version mehr |
| **Container** | LXC integriert | Nicht vorhanden (nur VMs) |
| **ZFS-Dateisystem** | Integriert (effiziente Snapshots) | Nur mit Zusatzkosten |
| **Verteilter Speicher** | Ceph integriert | Kostenpflichtige Zusatzlizenz |
| **Updates** | Kostenlos via Community-Repo | Nur mit gültigem Support-Vertrag |

Proxmox bietet damit mehr Funktionen als der frühere ESXi Free – ohne Lizenzgebühren.

---

## Ein wichtiges Thema vorab: Snapshots und Backups sind nicht dasselbe

Das ist einer der häufigsten Irrtümer beim Einstieg in die Virtualisierung – deshalb sprechen wir es früh an.

**Snapshots** speichern den Zustand deiner VM oder deines Containers zu einem bestimmten Zeitpunkt. Sie liegen auf demselben Speicher wie die VM selbst. Wenn die Festplatte ausfällt, ist beides weg. Snapshots schützen dich vor versehentlichen Konfigurationsfehlern – aber nicht vor Hardwareausfällen oder Datenverlust durch Diebstahl oder Feuer.

**Backups** kopieren deine Daten auf einen anderen Speicherort – idealerweise physisch getrennt. Proxmox hat dafür eine eigene Lösung: den **Proxmox Backup Server (PBS)**. Er erstellt inkrementelle, platzsparende Backups deiner VMs und Container und lässt sich auf einem zweiten Mini-PC oder einer externen Festplatte betreiben.

Die Faustregel lautet: **Snapshots für schnelle Rollbacks, Backups für echte Datensicherheit.** Beides ergänzt sich, ersetzt sich aber nicht.

---

## Live-Migration: Was sie ist und was sie voraussetzt

In vielen Proxmox-Artikeln liest man von „Live-Migration" – also dem Verschieben einer laufenden VM von einem Host auf einen anderen, ohne Unterbrechung. Das klingt beeindruckend, und das ist es auch. Aber es gibt klare Voraussetzungen, die für Einsteiger wichtig sind:

- **Proxmox-Cluster:** Mindestens zwei Proxmox-Hosts müssen zu einem Cluster zusammengeschlossen sein. Das geht nicht mit einem einzelnen Server.
- **Gemeinsamer Speicher:** Beide Hosts müssen auf denselben Speicher zugreifen können – entweder über ein Netzwerk-Dateisystem (NFS, Ceph) oder einen anderen gemeinsam genutzten Storage. Haben beide Hosts nur ihre eigene lokale SSD, ist Live-Migration nicht möglich.

Für einen **einzelnen Proxmox-Host** (der typische Homelab-Einstieg) ist Live-Migration schlicht nicht relevant. Sie wird interessant, wenn du zwei oder mehr Mini-PCs zu einem Cluster verbindest – und dann brauchst du auch gemeinsamen Speicher. Für die meisten Einsteiger-Setups reicht ein einzelner Host vollkommen aus.

---

## Wie viel Hardware brauchst du für Proxmox?

Proxmox läuft auf älteren Rechnern und unterstützt praktisch jeden handelsüblichen x86_64-Prozessor (der Standard bei Intel und AMD). Teure Spezial-Hardware ist nicht notwendig.

### Übersicht: Minimal- und Empfehlungswerte

| Komponente | Minimal | Empfohlen |
|-----------|---------|-----------|
| **CPU** | 4 Kerne (z. B. Intel Core i5-6500) | 6–8 Kerne (i7/i9 oder AMD Ryzen) |
| **RAM** | 8 GB | 32–64 GB |
| **Speicher** | 256 GB SSD | 1 TB NVMe + separate HDD für Backups |
| **Netzwerk** | 1 Gigabit | 2,5 oder 10 Gigabit |

> **Hinweis zur Version:** Zum Zeitpunkt dieses Artikels ist Proxmox VE 8.x die aktuelle stabile Version. Die grundlegende Bedienung ändert sich zwischen Versionen kaum – diese Anleitung ist auch für zukünftige Versionen größtenteils gültig.

---

## Gute Hardware für dein Proxmox-Homelab – nach Budget

### 💰 30–50 € – Fujitsu Futro S740 oder S7010

Auf dem Gebrauchtmarkt meist mit 8 GB RAM und 64 GB SSD zu finden (Preise Stand Juli 2026).

- **CPU:** Intel J4125 (S7010) oder J4105 (S740) – 4 Kerne, **lüfterlos** (kein Lüftergeräusch)
- **RAM:** 8 GB offiziell, bis 16 GB getestet – nur ein Steckplatz
- **Speicher:** 64 GB M.2 SATA – **nur SATA-SSDs**, kein NVMe (siehe SSD-Hinweis unten)
- **Netzwerk:** 1 Gigabit
- **Erweiterbarkeit:** ❌ Ein RAM-Steckplatz, kein zweiter SSD-Slot, kein PCIe-Slot
- **Stromverbrauch (Leerlauf):** ca. 6–8 Watt

**Ideal für:** Erste Proxmox-Experimente, Pi-hole, AdGuard, Netzwerk-Monitoring

👉 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

### 💰 80–130 € – HP ProDesk 400 G3/G4 oder Dell Optiplex 3060/3070 Micro

- **CPU:** Intel Core i5 der 7.–9. Generation, 4–6 Kerne
- **RAM:** Bis zu 32 GB DDR4 – zwei Steckplätze, nicht fest verlötet
- **Speicher:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA – gut erweiterbar
- **Netzwerk:** 1 Gigabit
- **Erweiterbarkeit:** ✅ RAM nachrüstbar, zweiter SSD-Platz vorhanden. Kein PCIe-Slot im Innern.
- **Stromverbrauch (Leerlauf):** ca. 12–18 Watt

**Ideal für:** Einen vollwertigen Proxmox-Host für viele Container und 3–5 virtuelle Maschinen, Home Assistant, Jellyfin

> **SSD-Kompatibilität:** Dieser PC unterstützt **NVMe-SSDs** (schneller Standard). Der Fujitsu Futro weiter oben unterstützt **nur SATA-SSDs**. Achte beim Kauf darauf, dass die SSD zum PC passt – mehr dazu im SSD-Abschnitt.

- 🔍 [HP ProDesk 400 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=matmaksa-homelab-21)
- 🔍 [Dell Optiplex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+Optiplex+3070+Micro&tag=matmaksa-homelab-21)

---

### 💰 130–180 € – Lenovo M720q Tiny

- **CPU:** Intel Core i5-8500T oder i7-8700T, 6 Kerne
- **RAM:** Bis zu 32 GB DDR4 – zwei Steckplätze
- **Speicher:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1 Gigabit
- **Erweiterbarkeit:** ✅ RAM und SSD nachrüstbar. **Pluspunkt:** Ein PCIe-Slot im Innern – damit lässt sich eine 10-Gigabit-Netzwerkkarte einbauen. Das bietet kaum ein anderer Mini-PC in dieser Preisklasse.
- **Stromverbrauch (Leerlauf):** ca. 12–20 Watt
- **USB-C:** Ja – einmal vorhanden, selten in dieser Klasse

**Ideal für:** Einen leistungsfähigen Proxmox-Host, der sich mit einer Netzwerkkarte gut erweitern lässt, oder als Cluster-Node

- 🔍 [Lenovo M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=matmaksa-homelab-21)

---

### 💰 200 € und mehr – Minisforum MS-01 (neu)

- **CPU:** Intel Core i9-13900H, 14 Kerne
- **RAM:** Bis zu 96 GB DDR5
- **Speicher:** 3× M.2 NVMe
- **Netzwerk:** 2× 10 Gigabit (SFP+) + 2× 2,5 Gigabit
- **Erweiterbarkeit:** ✅ Drei NVMe-Slots, zwei DDR5-Slots

**Ideal für:** Leistungshungrige Anwendungen, Cluster-Betrieb mit schnellem Netzwerk – wenn das Budget es hergibt

👉 [Preis bei Geizhals prüfen](https://geizhals.de/minisforum-ms-01-a3260346.html)

---

## 💾 SSD-Empfehlung – Auf Kompatibilität achten!

High-End-SSDs lohnen sich im Homelab selten. Viel wichtiger ist, dass die SSD zum PC passt:

- **Fujitsu Futro S7010/S740** unterstützt **nur M.2 SATA** – hier ist die WD Blue SA510 die richtige Wahl.
- **HP ProDesk, Dell Optiplex, Lenovo M720q** unterstützen **NVMe** – hier passt die Kingston NV3.

| Modell | Preis (ca., Stand Juli 2026) | Typ | Passt zu |
|--------|------------|-----|----------|
| [Kingston NV3 1 TB](https://geizhals.de/kingston-nv3-nvme-pcie-4-0-ssd-1tb-snv3s-1000g-a3248579.html?hloc=de) | ca. 60–80 € | NVMe PCIe 4.0 | HP, Dell, Lenovo |
| [WD Blue SA510 1 TB](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | ca. 60–80 € | M.2 SATA | Fujitsu Futro (und HP/Dell/Lenovo als SATA-Slot) |

---

## Proxmox einrichten – Schritt für Schritt

Die Installation von Proxmox ist für eine Serverlösung überraschend unkompliziert. Hier der genaue Ablauf.

### Was du brauchst

- Den Mini-PC (deine zukünftige Proxmox-Maschine)
- Einen zweiten Computer, von dem aus du die Installation vorbereitest
- Einen USB-Stick (mindestens 4 GB)
- Monitor und Tastatur (nur für die Installation, danach nicht mehr nötig)

### Die 5 Schritte

**1. ISO herunterladen**

Gehe auf [proxmox.com/downloads](https://www.proxmox.com/downloads) und lade die Installations-Datei (ISO) herunter. Kostenlos, keine Registrierung nötig.

**2. Auf USB-Stick schreiben**

Mit [Rufus](https://rufus.ie/de/) (Windows) oder Balena Etcher (Mac/Linux) überträgst du die ISO auf den USB-Stick. Der Stick wird dabei gelöscht – vorher Daten sichern.

**3. Alles anschließen und booten**

Schließe Monitor, Tastatur, LAN-Kabel und USB-Stick an den Mini-PC an. Dann einschalten und mehrfach F2, F10 oder F12 drücken (je nach Hersteller), bis das Boot-Menü erscheint. Dort den USB-Stick als Startlaufwerk auswählen.

**4. Dem Installations-Assistenten folgen**

Nach dem Booten erscheint ein Textbildschirm. Du wirst nach folgenden Angaben gefragt:

- **Festplatte:** Wähle die SSD des Mini-PCs aus. Alle Daten werden dabei gelöscht.
- **Passwort:** Vergib ein sicheres Passwort für den Administrator-Zugang.
- **IP-Adresse:** Proxmox braucht eine feste IP im Heimnetz. Schau auf deinem Router nach der Gateway-Adresse (oft auf einem Aufkleber: z. B. 192.168.1.1). Wähle eine freie Nummer im selben Bereich (z. B. 192.168.1.99). Die Subnetzmaske ist fast immer 255.255.255.0.
- **Update-Repository:** Wähle hier das **No-Subscription-Repository (Community)** – das ist kostenlos und für Homelabs geeignet.

**5. Fertig – loslegen ohne Monitor**

Nach der Installation startet der Mini-PC neu. USB-Stick abziehen, wenn er dazu auffordert. Danach kannst du Monitor und Tastatur abstecken. Der Mini-PC läuft von jetzt an nur mit Strom und LAN-Kabel.

Öffne auf deinem normalen Laptop oder PC den Browser und gib ein:
`https://192.168.1.99:8006` (mit deiner gewählten IP).

Es erscheint eine Sicherheitswarnung wegen des selbst erstellten Zertifikats – das ist normal. Klicke auf „Trotzdem fortfahren" oder „Erweitert" → „Weiter zur Website".

Du siehst jetzt das Proxmox-Dashboard. Dein Homelab läuft.

---

## Das solltest du vor dem Kauf wissen

Einige praktische Punkte aus der Erfahrung mit Homelab-Hardware:

- **RAM richtig planen:** Proxmox selbst benötigt kaum RAM (ca. 2 GB). Ein LXC-Container braucht je nach Anwendung 0,5–4 GB (Pi-hole: ca. 0,5 GB, Nextcloud: ca. 2–4 GB). Eine vollständige VM startet bei mindestens 2–4 GB. Mit 32 GB bist du für die meisten Homelab-Szenarien gut aufgestellt.
- **Eine SSD reicht zum Einstieg:** Zwei SSDs im Verbund (ZFS Mirror) sind sicherer, aber für den Einstieg tut es auch eine. Wichtiger ist ein regelmäßiges Backup auf externen Speicher.
- **Netzwerk:** Ein Gigabit-Anschluss reicht für die ersten Schritte gut aus. Schnelleres Netzwerk wird erst interessant, wenn mehrere Dienste gleichzeitig stark belastet werden.
- **Gebraucht oft sinnvoller als neu:** Business-Mini-PCs von HP, Dell und Lenovo sind für den Dauerbetrieb ausgelegt. Ein gebrauchtes Modell für 80–150 € läuft oft jahrelang stabil und kostet einen Bruchteil des ursprünglichen Preises.

---

## Drei Tools, die dein Homelab sinnvoll ergänzen

### 1. Proxmox Backup Server (PBS) – Echte Datensicherung

PBS erstellt inkrementelle, platzsparende Backups deiner VMs und Container – auf einem zweiten Rechner oder einer externen Festplatte. Das ist die einfachste Möglichkeit, echte Backups (nicht nur Snapshots) in dein Homelab zu integrieren. PBS läuft gut als eigene VM auf demselben Host oder auf einem günstigen Zweit-PC.

### 2. Home Assistant via LXC – Smart-Home-Zentrale

Licht, Heizung, Kameras – alles von einer Oberfläche steuern. Home Assistant in einem LXC-Container braucht nur rund 2 GB RAM und ist in kurzer Zeit eingerichtet.

### 3. Lokale KI – Optionaler Zusatz

Wer möchte, kann auf einem Proxmox-Host auch lokale KI-Sprachmodelle betreiben – zum Beispiel mit **Ollama** und **Open WebUI** in einem LXC-Container oder einer VM. Das funktioniert ohne Internet und ohne Abo.

Das ist aber kein Kernmerkmal von Proxmox, sondern ein optionaler Zusatz. Die Einrichtung erfordert einige Terminal-Befehle, und sinnvolle Ergebnisse bekommst du erst ab etwa 16–32 GB RAM. Ob das für dich interessant ist, hängt von deinen Zielen ab – es ist keine Voraussetzung für ein funktionierendes Homelab.

---

## Häufig gestellte Fragen

### Ist Proxmox VE wirklich kostenlos nutzbar?

Ja. Proxmox ist Open Source und darf ohne Lizenzgebühren genutzt werden. Über das kostenlose **No-Subscription-Repository** bekommst du aktuelle Updates inklusive Sicherheitspatches. Nach dem Login erscheint ein Hinweis, dass keine Subscription hinterlegt ist – das schränkt die Funktionen aber nicht ein.

Es gibt kostenpflichtige Subscriptions (ab ca. 95 €/Jahr pro Node, Stand Juli 2026), die Zugang zum Enterprise-Repository und kommerziellen Support bieten. Für Homelabs ist das in den meisten Fällen nicht notwendig.

### Was unterscheidet Snapshot und Backup in Proxmox?

Ein Snapshot speichert den Zustand einer VM oder eines Containers zu einem Zeitpunkt – auf demselben Speicher. Er hilft bei schnellen Rollbacks nach Konfigurationsfehlern. Fällt die Festplatte aus, ist der Snapshot weg.

Ein Backup kopiert die Daten auf einen anderen Speicherort und schützt vor Hardwareausfällen. Beides hat seinen Platz, und beides ersetzt das andere nicht.

### Was brauche ich für Live-Migration?

Live-Migration (eine laufende VM ohne Unterbrechung auf einen anderen Host verschieben) setzt zwei Dinge voraus: einen **Proxmox-Cluster** aus mindestens zwei Hosts und **gemeinsam genutzten Speicher** (z. B. über Ceph oder NFS). Mit einem einzelnen Proxmox-Host und je einer lokalen SSD pro Gerät ist Live-Migration nicht möglich. Für den typischen Homelab-Einstieg ist das kein Thema.

### Kann ich VMware-VMs zu Proxmox migrieren?

Ja. Gängige Wege sind: Export aus VMware als OVF/OVA und Import in Proxmox, Konvertierung mit `qemu-img convert` oder das automatisierte Tool `virt-v2v`. Die meisten Betriebssysteme (Windows, Linux) laufen danach ohne große Anpassungen.

### Brauche ich Linux-Kenntnisse?

Für die **grundlegende Nutzung** nein. Die Weboberfläche erlaubt die Verwaltung per Mausklick – VMs anlegen, starten, stoppen, Snapshots erstellen. Für **fortgeschrittene Setups** (z. B. Cluster, PBS, lokale KI) sind gelegentlich Terminal-Befehle nötig. Die lernst du aber gezielt dann, wenn du sie brauchst.

---

## Fazit: Welcher Weg ist der richtige für dich?

| Budget (Stand Juli 2026) | Empfehlung | Ideal für |
|--------|-----------|-----------|
| **30–50 €** | Fujitsu Futro S740/S7010 (gebraucht) | Erste Experimente, Werbeblocker, Netzwerk-Dienste |
| **80–130 €** | HP ProDesk 400 G4 oder Dell Optiplex 3070 Micro (gebraucht) | Vollwertiger Homelab-Server für viele Dienste |
| **130–180 €** | Lenovo M720q Tiny (gebraucht) | Erweiterbarkeit, PCIe-Slot, Cluster-Node |
| **200 € und mehr** | Minisforum MS-01 (neu) | High-End: 10-Gigabit-Netzwerk, Profi-Homelab |

Proxmox VE ist eine solide, kostenlos nutzbare Alternative zu VMware – mit LXC-Containern, ZFS, integriertem Backup-Tool und einer übersichtlichen Weboberfläche. Auf gebrauchter Business-Hardware bekommst du ein leistungsfähiges Homelab für einen Bruchteil des Preises kommerzieller Lösungen.

Wichtig für den Start: Community-Repository wählen, regelmäßige Backups einrichten (nicht nur Snapshots), und mit einem einzelnen Host beginnen – Live-Migration und Cluster kommen später, wenn du weißt, ob du sie brauchst.