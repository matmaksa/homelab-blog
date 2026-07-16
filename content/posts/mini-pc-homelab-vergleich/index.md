---
title: "Mini PC fürs Homelab nach Budget: Von 40€ bis 300€ – welcher passt zu dir?"
description: "Mini-PC-Vergleich fürs Homelab: Thin Client, NUC oder Workstation? Die beste Hardware für jedes Budget von 40€ bis 300€ mit Vor- und Nachteilen."
date: 2026-06-19
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Mini-PCs und Thin Clients fürs Homelab – Fujitsu, HP, Dell, Lenovo, GMKtec"
  relative: true
tags:
  - hardware
  - mini-pc
  - kaufberatung
  - homelab
  - budget
  - thin-client
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
next_action: "maintain_price_affiliate_and_derivative_gates"
related_articles:
  - "fujitsu-futro-s7010-homelab-einstieg"
  - "home-assistant-gebrauchter-mini-pc-2026"
notes:
  - "Published hardware comparison article."
  - "Affiliate and price freshness gates remain relevant."
---
**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.


Ein Mini-PC ist die ideale Grundlage für dein Homelab – leise, stromsparend und leistungsstark genug für Proxmox, Docker und erste KI-Experimente. Aber welches Modell lohnt sich wirklich für dein Budget?

Statt einer generischen Rangliste zeige ich dir hier die besten Optionen **nach Preisklasse** – vom 40-Euro-Thin-Client bis zur 300-Euro-Neumaschine. Die Modelle auf dieser Seite haben sich über Jahre bewährt und sind auch Mitte 2026 noch die ersten Wahl – in vielen Fällen wurden sie erst 2023/2024 auf den Markt gebracht und sind technisch topaktuell.

<!--more-->

## 🥇 Kurzempfehlung: Welcher Mini-PC passt zu dir?

| Kategorie | Empfehlung |
|-----------|-----------|
| 🥇 Beste Preis-Leistung | HP ProDesk 400 G4 (~90 € gebraucht) |
| 💰 Günstigster Einstieg | Fujitsu Futro S7010 (~40 € gebraucht) |
| 🚀 Beste Wahl für maximale Erweiterbarkeit | Lenovo M720q (~150 €) + 32 GB RAM |
| 🏠 Beste Wahl für Home Assistant | Fujitsu Futro S7010 (~40 €) |
| 🔧 Beste Wahl für Proxmox Cluster | 2× Dell Optiplex 3070 (~100 €/Stück) |

---

## Worauf du achten solltest – drei häufige Anfänger-Fragen

Bevor es zu den Modellen geht, kurz die drei Dinge, die Einsteiger am meisten verunsichern:

### "Reicht ein alter i5 gegen einen modernen N100/N95?"
Die kurze Antwort: **Der alte i5 (8. Gen) ist meist stärker** – trotz des größeren Modellnamens. Ein i5-8500T (6 Kerne) aus 2018 hat in der Regel mehr Rechenleistung als ein aktueller Intel N95 (4 Kerne) aus 2023. Dafür verbraucht der N95 deutlich weniger Strom (~10 W vs. ~15-25 W im Leerlauf). **Faustregel:** Für viele gleichzeitige Dienste (Proxmox mit 5+ Containern) nimm den i5. Für einen einzelnen 24/7-Dauerläufer (Pi-hole, Home Assistant) reicht der N95/N100 völlig.

Der i5-8500T (älterer Sechskern) hat Reserven bei parallelen Diensten, der N95 ist häufig sparsamer und einfacher als Neugerät erhältlich.

### "Was ist ein Barebone? Muss ich löten?"
Ein Barebone ist ein PC, bei dem **Arbeitsspeicher (RAM) und Festplatte (SSD) fehlen** – quasi ein Auto ohne Räder. Du musst nicht löten, sondern nur **zwei Teile einclipsen** (wie Lego): Die SSD wird in einen Schlitz gesteckt und festgeschraubt, der RAM wird in einen Steckplatz gedrückt, bis er einrastet. Das sind 5 Minuten Arbeit, kein Spezialwerkzeug nötig. **Kosten extra:** 32 GB DDR4 RAM (gebraucht) + 500 GB NVMe SSD = ca. 150–200 € zusätzlich. Achtung: Aktuell (2026) sind RAM-Preise stark gestiegen – ein neues 32-GB-Kit kostet schnell 200+ €. Auf dem Gebrauchtmarkt oder bei Refurbished-Händlern findest du oft günstigere Angebote.

### "Brauche ich für 2,5 GbE ein neues Netzwerk?"
**Nein.** Ein 2,5-Gigabit-Anschluss funktioniert auch an deiner normalen FRITZ!Box mit 1 Gigabit – er passt sich automatisch an die langsamere Geschwindigkeit an. Der Vorteil von 2,5 GbE zeigt sich erst, wenn du **mehrere Geräte gleichzeitig stark belastest** (z. B. Medienserver + Cloud + Backup parallel). Für die ersten Schritte reicht 1 GbE völlig.

---

## Auf einen Blick

| Budget (Stand: Juli 2026) | Modell(e) | Zustand | Highlight |
|--------|-----------|---------|-----------|
| **Bis 50 €** | Fujitsu Futro S7010 | Gebraucht | **Günstigster Einstieg** – 4 Kerne, extrem sparsam |
| **80–150 €** | HP ProDesk 400 G3/G4 Mini **oder** Dell OptiPlex 3060/3070 Micro | Gebraucht | **Freie Wahl** – was du günstiger findest |
| **150–200 €** | Lenovo ThinkCentre M720q Tiny | Gebraucht | **PCIe-Slot** – erweiterbar wie kein anderer |
| **200–300 €** | GMKtec G3S (Intel N95) | Neu | **Neugerät** – Alder Lake, 16 GB RAM, Garantie |

---

## 💰 Bis 50 €: Fujitsu Futro S7010 – Der 40-Euro-Server

{{< figure src="/images/products/fujitsu-s7010.jpg" alt="Fujitsu Futro S7010 Thin Client" width="400" >}}

Der Fujitsu Futro S7010 ist der absolute Budget-Champion. Gebraucht bekommst du ihn mit 8 GB RAM und 64 GB SSD bereits ab **30–50 €** – und er ist erstaunlich brauchbar für seinen Preis.

Die CPU ist ein **Intel Celeron J4125** (4 Kerne, 2,0–2,7 GHz). Das klingt nach nicht viel, reicht aber für leichte Dienste problemlos.

{{< ebay-link query="Fujitsu Futro S7010 8GB" text="🔍 Fujitsu Futro S7010 mit 8 GB RAM bei eBay suchen" >}}

- **Prozessor (CPU):** Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 W)
- **Arbeitsspeicher (RAM):** 8 GB DDR4 offiziell, 16 GB getestet – 1 Slot (kein zweiter)
- **Festplatte (SSD):** 64 GB M.2 SATA (austauschbar, aber **kein NVMe**)
- **Netzwerk:** 1 Gigabit-Anschluss (GbE)
- **Stromverbrauch (Leerlauf):** ca. 3–7 W – extrem stromsparend
- **Kühlung:** Passiv (lüfterlos) – absolut lautlos
- **Erweiterbarkeit:** ❌ Nur 1 RAM-Slot. Nur M.2 SATA (kein NVMe). Kein PCIe-Slot.
- **USB-C?** Nein
- **KI-Tauglichkeit:** ❌ Für Ollama nicht geeignet

**Ideal für:** Pi-hole (Werbeblocker), Home Assistant (Smart Home), leichte Docker-Container, kleiner Dateiserver. Perfekt als **erster Server** zum Ausprobieren, ohne Geld zu verbrennen.

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

## 💰 80–150 €: HP ProDesk G3/G4 Mini oder Dell OptiPlex 3060/3070 Micro

In dieser Preiskategorie hast du die **freie Wahl** – nimm einfach das Modell, das du gerade günstiger findest. Egal ob HP oder Dell: Die Leistung ist nahezu identisch.

**Wichtiger Hinweis zur SSD:** Im Gegensatz zum Fujitsu Futro unterstützen diese Geräte **NVMe-SSDs** (den schnellen Standard). Wenn du eine SSD dazukaufst, achte darauf, dass es eine NVMe ist – nicht die günstigere SATA-Variante.

### HP ProDesk 400 G3 Mini (~50–100 € gebraucht)

- **Prozessor (CPU):** Intel Core i5-6500T oder i5-7500T (je 4 Kerne)
- **Arbeitsspeicher (RAM):** Bis zu 32 GB DDR4 – zwei Steckplätze (nicht verlötet)
- **Festplatte:** 1× M.2 NVMe/SATA + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1 Gigabit (Intel)
- **Stromverbrauch (Leerlauf):** ca. 12–18 Watt
- **Erweiterbarkeit:** ✅ RAM nachrüstbar, zweiter SSD-Platz. Kein PCIe-Slot.

**Ideal für:** Ersten Proxmox-Server, Pi-hole, Docker, leichte NAS-Aufgaben.

🔍 [HP ProDesk 400 G3 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G3+Mini&tag=matmaksa-homelab-21)

### HP ProDesk 600 G4 Mini (~100–180 € gebraucht)

Der schnellere Bruder mit neueren CPUs der 8. Generation. Der **i5-8500T (6 Kerne)** hat spürbar mehr Leistung als der G3.

- **Prozessor (CPU):** i5-8500T (6 Kerne) oder i7-8700T (6 Kerne, 12 Threads)
- **Arbeitsspeicher (RAM):** Bis zu 32 GB offiziell (64 GB inoffiziell getestet)
- **Festplatte:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1 Gigabit (Intel)
- **Erweiterbarkeit:** ✅ RAM + Dual-Storage

**Ideal für:** Mehrere VMs unter Proxmox, Docker-Stack mit 5+ Containern.

🔍 [HP ProDesk 600 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+600+G4+Mini&tag=matmaksa-homelab-21)

### Dell OptiPlex 3060/3070 Micro (~80–180 € gebraucht)

Die direkte Konkurrenz zu HP. Identisches Preisniveau, ähnliche Specs. Der **3070** bringt die 9. Intel-Generation (i5-9500T).

- **Prozessor (CPU):** i5-8500T (6 Kerne) oder i5-9500T (6 Kerne)
- **Arbeitsspeicher (RAM):** Bis zu 32 GB DDR4 (64 GB inoffiziell getestet)
- **Festplatte:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1 Gigabit (Intel)
- **USB-C?** Nein (nur Dell Optiplex, Lenovo M720q hat USB-C)

🔍 [Dell OptiPlex 3060/3070 bei Amazon suchen](https://www.amazon.de/s?k=Dell+OptiPlex+Micro&tag=matmaksa-homelab-21)

---

## 💰 150–200 €: Lenovo ThinkCentre M720q Tiny – Der Erweiterbare

{{< figure src="/images/products/lenovo-m720q-tiny.jpg" alt="Lenovo ThinkCentre M720q Tiny" width="400" >}}

Der Lenovo ThinkCentre M720q Tiny ist die Geheimwaffe für Homelab-Betreiber, die mehr wollen: **Er verfügt über einen PCIe-Slot im Innern.** Dafür wird allerdings eine PCIe-Riser-Karte (FRU 01AJ940) benötigt, die den Steckplatz bereitstellt – ohne diese Karte ist kein PCIe-Anschluss vorhanden. Das Gehäuse sollte entweder die Tiny-in-One-Variante sein oder der Standard-Tiny mit der passenden PCIe-Slot-Blende. Mit Riser-Karte kannst du dann eine 10-Gigabit-Netzwerkkarte, eine SATA-Erweiterungskarte oder sogar eine kompakte Grafikkarte nachrüsten – eine Möglichkeit, die kaum ein anderer Mini-PC dieser Preisklasse bietet.

- **Prozessor (CPU):** Intel Core i5-8500T (6 Kerne) oder i7-8700T (6 Kerne, 12 Threads)
- **Arbeitsspeicher (RAM):** Bis zu 32 GB DDR4 (64 GB inoffiziell getestet)
- **Festplatte:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1 Gigabit (Intel) – über PCIe auf 10 Gigabit erweiterbar
- **Erweiterbarkeit:** ✅ RAM + Dual-Storage + **PCIe-Slot** (Riser-Karte nötig)
- **USB-C?** **Ja** – einmal USB-C (selten in dieser Klasse!)
- **Stromverbrauch (Leerlauf):** ca. 12–20 Watt
- **KI-Tauglichkeit:** ✅ Phi-3-mini mit >10 Tokens/s, 32 GB RAM empfohlen

**Ideal für:** Homelab mit Erweiterungsplänen (10GbE, GPU), Proxmox-Cluster, KI-Spielereien.

🔍 [Lenovo ThinkCentre M720q bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+ThinkCentre+M720q+Tiny&tag=matmaksa-homelab-21)

---

## 💰 200–300 €: GMKtec G3S – Neugerät mit Garantie

{{< figure src="/images/products/gmktec-g3s.jpg" alt="GMKtec G3S Intel N95 Mini PC" width="400" >}}

Der GMKtec G3S ist die beste Wahl, wenn du ein **Neugerät mit Garantie** möchtest und nicht auf dem Gebrauchtmarkt suchen willst.

- **Prozessor (CPU):** Intel N95 (4 Kerne, Alder Lake 2023, 15 W)
- **Arbeitsspeicher (RAM):** 8 oder 16 GB DDR4 – **verlötet (nicht erweiterbar)** ⚠️
- **Festplatte:** 1× M.2 NVMe (bis 8 TB)
- **Netzwerk:** 1 Gigabit Ethernet
- **Stromverbrauch (Leerlauf):** ca. 10–15 Watt
- **Erweiterbarkeit:** ❌ RAM verlötet, nur 1 SSD-Slot. Kein PCIe.
- **KI-Tauglichkeit:** ❌ 16 GB RAM für KI zu knapp

**Wichtiger Hinweis für Käufer:** Der Intel N95 (4 Kerne) ist leistungsmäßig **schwächer** als ein gebrauchter i5-8500T (6 Kerne) aus dem HP oder Dell für 100–120 €. Dafür bekommst du ein Neugerät mit Garantie und extrem niedrigem Stromverbrauch – perfekt für den 24/7-Dauerbetrieb.

**Ideal für:** Wer Neugerät mit Garantie will, Docker-Server, Home Assistant, Mediencenter.

👉 [GMKtec G3S bei Amazon suchen](https://www.amazon.de/s?k=GMKtec+G3S&tag=matmaksa-homelab-21)

---

## 💾 Wohin mit den ganzen Daten? (Storage-Frage)

Die Mini-PCs haben oft nur Platz für 1–2 SSDs intern. Wenn du größere Datenmengen speichern willst (Nextcloud-Fotos, Filme, Backups), hast du mehrere Möglichkeiten:

- **Externe USB-Festplatte** – Einfachste Lösung. Ein 4 TB USB-3.0-Laufwerk (ca. 100–120 €) wird per USB eingesteckt und läuft stabil. Für Medienserver und Backups völlig ausreichend.
- **NAS (Network Attached Storage)** – Ein separater kleiner Server, der nur für Festplatten zuständig ist. Die Profi-Lösung, aber ab 200–300 € aufwärts.
- **Interne 2,5-Zoll-SSD** – Viele Modelle (HP, Dell, Lenovo) haben einen zweiten Slot für eine 2,5-Zoll-SSD. Da passen bis zu 4 TB rein – genug für die meisten Homelabs.

**Mein Tipp für Einsteiger:** Starte mit dem internen Speicher + einer externen USB-Festplatte für Backups. Ein NAS kannst du später immer noch nachrüsten.

---

## 💾 Günstige SSD-Empfehlung

| Modell | Preis (ca.) | Typ | Passt zu |
|--------|------------|-----|----------|
| [Kingston NV3 1 TB](https://geizhals.de/kingston-nv3-nvme-pcie-4-0-ssd-1tb-snv3s-1000g-a3248579.html?hloc=de) | ~139 € | NVMe PCIe 4.0 (schnell) | HP, Dell, Lenovo (nicht Futro!) |
| [WD Blue SA510 1 TB](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | ~135 € | SATA M.2 (langsamer) | Fujitsu Futro, HP, Dell, Lenovo |

---

## Lohnt sich ein gebrauchter Mini-PC fürs Homelab?

**Ja, absolut!** Gerade für den Einstieg sind gebrauchte Business-Mini-PCs von HP, Lenovo und Dell die beste Wahl:

- **Preis:** Bis zu 80–90 % günstiger als Neugeräte
- **Verfügbarkeit:** Riesiges Angebot durch Unternehmens-Ausmusterungen
- **Haltbarkeit:** Business-Geräte sind für den 24/7-Dauerbetrieb ausgelegt
- **Stromverbrauch:** Meist unter 25 W – ideal für den Dauerbetrieb

---

## Preis-Leistungs-Vergleich aller Modelle

| Modell | Preis | CPU | RAM max. | Netzwerk | Besonderheit |
|--------|-------|-----|----------|----------|--------------|
| Fujitsu Futro S7010 | **~40 €** | J4125 (4C) | 8 GB | 1 GbE | Günstigster Einstieg, lüfterlos |
| HP ProDesk 400 G3 | **~80 €** | i5-7500T (4C) | 32 GB | 1 GbE | Riesiges Angebot |
| HP ProDesk 600 G4 | **~120 €** | i5-8500T (6C) | 32 GB | 1 GbE | 6 Kerne, 64 GB inoffiziell |
| Dell OptiPlex 3060 | **~120 €** | i5-8500T (6C) | 32 GB | 1 GbE | – |
| Dell OptiPlex 3070 | **~150 €** | i5-9500T (6C) | 32 GB | 1 GbE | 9. Gen Intel |
| Lenovo M720q Tiny | **~150 €** | i5-8500T (6C) | 32 GB | 1 GbE | **PCIe-Slot + USB-C** |
| GMKtec G3S | **~220 €** | Intel N95 (4C) | 16 GB | 1 GbE | Neugerät + Garantie |

---

> ⚠️ **Lokale KI ist auf diesen Geräten ohne dedizierte GPU nur eingeschränkt sinnvoll.** Kleinere Modelle wie Phi-3-mini laufen auf CPUs mit 16+ GB RAM, aber für größere Modelle oder flüssige Nutzung ist eine GPU nötig.

---

## Fazit: Welcher Mini-PC passt zu deinem Budget?

| Dein Budget | Unsere Empfehlung |
|-------------|-------------------|
| **40–50 €** | 👉 **Fujitsu Futro S7010** – günstigster Einstieg überhaupt |
| **80–150 €** | 👉 **HP ProDesk 400 G3/600 G4** oder **Dell OptiPlex 3060/3070** – je nach Angebot |
| **150–200 €** | 👉 **Lenovo M720q Tiny** – PCIe macht den Unterschied |
| **200–300 €** | 👉 **GMKtec G3S** – Neugerät mit Garantie (aber CPU-seitig schwächer als gebrauchte i5) |

**Passend für Einsteiger, wenn …:** Hol dir einen **HP ProDesk 400 G4** gebraucht für ~90 €. Dazu nachrüstbar: 16–32 GB RAM (gebraucht oft günstiger) und eine 500 GB NVMe-SSD. Der Rechner hat 6 Kerne, läuft leise und stromsparend – und du kannst später bei Bedarf die zweite SSD nachrüsten.

