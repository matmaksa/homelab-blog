---
title: "Mini PC fürs Homelab nach Budget: Von 50€ bis 650€ – welcher passt zu dir?"
date: 2026-06-18
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Gebrauchte Business-Mini-PCs fürs Homelab – HP, Lenovo, Dell, Fujitsu"
  relative: true
# cover image entfernt (KI-Bild zeigte falsche Modelle)
tags:
  - hardware
  - mini-pc
  - kaufberatung
  - homelab
categories:
  - Hardware
---

**Aktualisiert: Juni 2026 | Lesezeit: 7 Minuten**

Ein Mini-PC ist die ideale Grundlage für dein Homelab – leise, stromsparend und leistungsstark genug für Proxmox, Docker und erste KI-Experimente. Doch welches Modell lohnt sich wirklich für dein Budget?

Statt einer generischen Rangliste zeige ich dir hier die besten Mini-PCs **nach Preisklasse** – vom 50-Euro-Gebrauchtkauf bis zur 650-Euro-Proxmox-Maschine.

<!--more-->

## Auf einen Blick

| Budget | Modell | Zustand | Ideal für |
|--------|--------|---------|-----------|
| **Bis 100 €** | HP ProDesk 400 G3 Mini | Gebraucht | **Homelab-Einstieg** – Proxmox, Pi-hole, Docker |
| **100–200 €** | Lenovo ThinkCentre M720q Tiny | Gebraucht | **Erweiterbares Homelab** – PCIe-Slot für NICs |
| **200–300 €** | GMKtec G3 Pro | Neu | **Neugerät mit Garantie** – Office, Docker, Medien |
| **Über 300 €** | Minisforum MS-01 | Neu | **Proxmox-Spitzenklasse** – 10GbE, viele Kerne |

---

## Bis 100 €: HP ProDesk 400 G3 Mini – Der perfekte Homelab-Einstieg

{{< figure src="/homelab-blog/images/products/hp-prodesk-400-g3.jpg" alt="HP ProDesk 400 G3 Mini" width="400" >}}

Der HP ProDesk 400 G3 Mini ist der absolute Budget-König fürs Homelab. Gebraucht bekommst du ihn bereits ab **50–100 €** – und er ist dabei vollkommen ausreichend für die ersten Schritte im Homelab.

- **CPU:** Intel Core i5-6500T / i5-7500T (je 4 Kerne / 4 Threads)
- **RAM:** Bis zu 32 GB DDR4
- **Storage:** 1× M.2 NVMe + 1× SATA
- **Netzwerk:** 1× 1GbE
- **Preis gebraucht:** 50–100 €
- **Stromverbrauch:** ca. 15–20 W im Betrieb

**👍 Vorteile:** Extrem günstig. Riesiges Angebot auf dem Gebrauchtmarkt. Sehr stromsparend. Leise und gut aufrüstbar.

**👎 Nachteile:** Nur 4 Kerne. Kein 10GbE. Maximal 32 GB RAM. Gebrauchtkauf ohne Herstellergarantie.

**Ideal für:** Proxmox mit 2–3 VMs, Pi-hole, Docker und leichte NAS-Aufgaben. Perfekt als **erster Homelab-Server** zum Ausprobieren ohne großes Risiko.

🔍 [HP ProDesk 400 G3 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G3+Mini&tag=makmatas-homelab-21)

---

## 100–200 €: Lenovo ThinkCentre M720q Tiny – Der Erweiterbare

{{< figure src="/homelab-blog/images/products/lenovo-m720q-tiny.jpg" alt="Lenovo ThinkCentre M720q Tiny" width="400" >}}

Der Lenovo ThinkCentre M720q Tiny ist die Geheimwaffe für Homelab-Betreiber, die mehr wollen: **Er verfügt über einen PCIe-Slot.** Das bedeutet, du kannst eine 10GbE-Netzwerkkarte, eine SATA-Erweiterungskarte oder sogar eine kompakte GPU einbauen – eine Möglichkeit, die kaum ein anderer Mini-PC dieser Preisklasse bietet.

- **CPU:** Intel Core i5-8500T (6 Kerne / 6 Threads) oder i7-8700T (6 Kerne / 12 Threads)
- **RAM:** Bis zu 32 GB DDR4
- **Storage:** 1× M.2 NVMe + **PCIe-Slot für Erweiterungen**
- **Netzwerk:** 1× 1GbE (über PCIe auf 10GbE erweiterbar)
- **Preis gebraucht:** 100–200 €
- **Besonderheit:** **PCIe x8-Slot** – in dieser Geräteklasse äußerst selten

**👍 Vorteile:** PCIe-Erweiterbarkeit (10GbE, GPU, SATA). 6 Kerne beim i5-8500T. Sehr kompaktes Design. Große und aktive Lenovo-Community.

**👎 Nachteile:** Nur 1GbE onboard. Gebrauchtkauf. Unter Last etwas lauter als der HP ProDesk.

**Ideal für:** Homelab mit **10GbE-Ambitionen** (NIC via PCIe-Slot), Proxmox-Cluster und fortgeschrittene Docker-Setups.

🔍 [Lenovo ThinkCentre M720q bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+ThinkCentre+M720q+Tiny&tag=makmatas-homelab-21)

---

## 200–300 €: GMKtec G3 Pro – Neugerät mit Garantie

{{< figure src="/homelab-blog/images/products/gmktec-g3-pro.jpg" alt="GMKtec G3 Pro Mini PC" width="400" >}}

Der GMKtec G3 Pro ist die beste Wahl, wenn du ein **Neugerät mit Garantie** möchtest und nicht auf dem Gebrauchtmarkt suchen willst. Mit einem Intel Core i3-10110U und 16 GB RAM ist er ein solider Allrounder für den Homelab-Alltag – und der 2,5GbE-Anschluss hebt ihn klar von den günstigeren Gebrauchtmodellen ab.

- **CPU:** Intel Core i3-10110U (2 Kerne / 4 Threads, bis 4,1 GHz)
- **RAM:** 16 GB DDR4
- **Storage:** 512 GB M.2 NVMe
- **Netzwerk:** **1× 2,5GbE** + Wi-Fi 6
- **Preis neu:** ca. 230–280 €
- **Besonderheit:** 2× HDMI, 3× USB 3.2, Windows 11 Pro vorinstalliert

**👍 Vorteile:** Neugerät mit Herstellergarantie. 2,5GbE – schnelleres Netzwerk als bei den Gebrauchtmodellen. Kompakt und leise. Windows 11 Pro inklusive.

**👎 Nachteile:** Nur 2 Kerne / 4 Threads (i3-10110U) – weniger als beim Lenovo M720q. Kein PCIe-Erweiterungsslot. RAM bei einigen Varianten verlötet – vor dem Kauf prüfen.

**Ideal für:** **Docker-Server**, Office-Homelab, Mediencenter und Home Assistant. Optimal für alle, die Neuware und Garantie priorisieren und den Gebrauchtmarkt meiden möchten.

👉 [GMKtec G3 Pro jetzt bei Amazon ansehen](https://www.amazon.de/dp/B0F9FS819H/?tag=makmatas-homelab-21)

---

## Über 300 €: Minisforum MS-01 – Der Proxmox-König

{{< figure src="/homelab-blog/images/products/minisforum-ms01.jpg" alt="Minisforum MS-01 Mini Workstation" width="400" >}}

Der Minisforum MS-01 ist 2026 der unangefochtene Spitzenreiter für Homelab-Betreiber, die maximale Leistung im kompakten Format suchen. Mit **10GbE onboard** und einem Intel Core i9-13900H ist er eine vollwertige Workstation im Mini-Format.

- **CPU:** Intel Core i9-13900H (14 Kerne / 20 Threads)
- **RAM:** Bis zu 96 GB DDR5
- **Storage:** 2× M.2 NVMe + 1× SATA
- **Netzwerk:** **2× 10GbE SFP+** + 2× 2,5GbE
- **Preis neu:** ca. 600–700 €
- **Besonderheit:** Zwei PCIe-Slots + USB4

**👍 Vorteile:** 10GbE onboard – kein teures Switch-Upgrade erforderlich. 14 Kerne für anspruchsvolle Proxmox-VMs. Zukunftssicher dank DDR5 und PCIe 4.0.

**👎 Nachteile:** Hoher Anschaffungspreis. Wird unter Volllast spürbar warm.

**Ideal für:** **Anspruchsvolle Proxmox-Umgebungen**, viele parallele VMs, KI-Experimente und 10GbE-Cluster-Setups.

👉 [Minisforum MS-01 jetzt bei Amazon ansehen](https://www.amazon.de/dp/B0D45JQCN7/?tag=makmatas-homelab-21)

---

## Preis-Leistungs-Vergleich aller Modelle

| Modell | Preis | CPU | RAM max. | Netzwerk | Besonderheit |
|--------|-------|-----|----------|----------|--------------|
| HP ProDesk 400 G3 | **~80 €** | i5-7500T (4C/4T) | 32 GB | 1GbE | Günstigster Einstieg |
| Lenovo M720q Tiny | **~150 €** | i5-8500T (6C/6T) | 32 GB | 1GbE + PCIe | **PCIe-Slot** |
| GMKtec G3 Pro | **~260 €** | i3-10110U (2C/4T) | 16 GB | **2,5GbE** | Neugerät + Garantie |
| Minisforum MS-01 | **~650 €** | i9-13900H (14C/20T) | **96 GB** | **2× 10GbE** | Absolute Spitzenklasse |

---

## Lohnt sich ein gebrauchter Mini-PC fürs Homelab?

**Ja, absolut!** Gerade für den Einstieg sind gebrauchte Business-Mini-PCs von HP, Lenovo und Dell die beste Wahl:

- **Preis:** Bis zu 80–90 % günstiger als Neugeräte
- **Verfügbarkeit:** Riesiges Angebot durch Unternehmens-Ausmusterungen
- **Haltbarkeit:** Business-Geräte sind für den 24/7-Dauerbetrieb ausgelegt
- **Stromverbrauch:** Meist unter 25 W – ideal für den dauerhaften Betrieb

### Worauf du beim Gebrauchtkauf achten solltest

- SSD und RAM sind meistens nachrüstbar – lieber ein günstiges Basismodell kaufen und selbst aufrüsten
- Auf die CPU-Generation achten: Ab Intel der 6. / 7. Generation (Skylake / Kaby Lake) ist die Leistung für Proxmox ausreichend
- Bevorzugt bei gewerblichen Händlern kaufen – diese bieten häufig 12 Monate Gewährleistung

---

## Mini-PC für KI-Modelle – Was ist in welcher Preisklasse möglich?

Lokale KI-Modelle sind 2026 auch im Homelab längst angekommen:

| Budget | KI-Nutzung |
|--------|------------|
| **Bis 100 €** | Ollama auf CPU, kleine Modelle (1–3B Parameter) |
| **100–200 €** | Ollama + Open WebUI, 7B-Modelle (langsam) |
| **200–300 €** | 7B-Modelle nutzbar, aber durch nur 2 Kerne begrenzt – Bildgenerierung kaum möglich |
| **Über 300 €** | 7B+-Modelle, NPU-Beschleunigung, GPU via PCIe (M720q) |

---

## Fazit: Welcher Mini-PC passt zu deinem Budget?

| Dein Budget | Unsere Empfehlung |
|-------------|-------------------|
| **50–100 €** | 👉 **HP ProDesk 400 G3 Mini** – günstiger Homelab-Einstieg ohne Risiko |
| **100–200 €** | 👉 **Lenovo ThinkCentre M720q Tiny** – erweiterbar per PCIe-Slot |
| **200–300 €** | 👉 **GMKtec G3 Pro** – Neugerät mit Garantie und 2,5GbE |
| **300–650 €** | 👉 **Minisforum MS-01** – 10GbE, 14 Kerne, absolute High-End-Lösung |

**Meine persönliche Empfehlung:** Der **Lenovo M720q Tiny** ist der interessanteste Allrounder in dieser Liste – vor allem wegen des PCIe-Slots, der ihn klar von allen anderen Modellen abhebt. Wer 10GbE ins Homelab bringen möchte, findet hier die günstigste Einstiegsmöglichkeit. Und der **HP ProDesk für rund 80 €** ist ideal, um ohne großen Einsatz einfach loszulegen.

**Jetzt bist du dran:** Welches Budget planst du für dein Homelab ein? Schreib es in die Kommentare – ich freue mich auf den Austausch!



---

## Weiterführende Artikel

- 🔗 [Virtualisierung kostenlos 2026: Proxmox VE als VMware-Alternative im Homelab](/homelab-blog/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) — *(Thema: proxmox,virtualisierung)*

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Für dich ändert sich der Preis dadurch nicht.*
