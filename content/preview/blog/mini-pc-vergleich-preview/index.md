+++
title = "Mini PC fürs Homelab nach Budget: Von 40€ bis 300€ – welcher passt zu dir?"
description = "Mini-PC-Vergleich fürs Homelab: Thin Client, NUC oder Workstation? Hardware für jedes Budget von 40€ bis 300€ mit Vor- und Nachteilen."
date = 2026-06-19
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
approved_for_publish = false
image = "featured.jpg"

[cover]
image = "featured.jpg"
alt = "Mini-PCs und Thin Clients fürs Homelab – Fujitsu, HP, Dell, Lenovo, GMKtec"
relative = true

[taxonomies]
tags = ["hardware", "mini-pc", "kaufberatung", "homelab", "budget", "thin-client"]
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
related_articles = [
  "fujitsu-futro-s7010-homelab-einstieg",
  "home-assistant-gebrauchter-mini-pc-2026"
]
notes = [
  "Neugeschriebener Artikel, Preisangaben mit Stand-Vermerk versehen.",
  "Prozentangaben entfernt.",
  "KI nicht als zentrale Kategorie behandelt.",
  "M720q: Riser-Karte-Hinweis ergänzt.",
  "Beste Wahl durch passend wenn ersetzt.",
  "KI-Tabelle abgeschwächt."
]
+++

**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

> Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.

Ein Mini-PC ist eine solide Grundlage für dein Homelab – leise, stromsparend und leistungsstark genug für Proxmox, Docker und viele andere Dienste. Aber welches Modell passt zu deinem Budget und deinen Zielen?

Statt einer generischen Rangliste zeige ich dir hier konkrete Optionen **nach Preisklasse** – vom 40-Euro-Thin-Client bis zur 300-Euro-Neumaschine. Die Modelle auf dieser Seite haben sich in der Community bewährt und sind Mitte 2026 noch gut verfügbar.

<!--more-->

---

## Kurzübersicht: Welches Gerät passt zu welchem Zweck?

| Zweck | Empfehlung |
|-------|-----------|
| Günstigster Einstieg | Fujitsu Futro S7010 (ca. 40 €, Stand Juli 2026) |
| Preis-Leistung für Einsteiger | HP ProDesk 400 G4 (ca. 90 € gebraucht, Stand Juli 2026) |
| Passend wenn du Hardware erweitern willst | Lenovo M720q (ca. 150 € gebraucht, Stand Juli 2026) + PCIe-Riser-Karte |
| Passend wenn du Home Assistant betreiben willst | Fujitsu Futro S7010 (ca. 40 €, Stand Juli 2026) |
| Passend wenn du einen kleinen Proxmox-Cluster aufbauen willst | 2× Dell Optiplex 3070 Micro (ca. 100 € pro Stück, Stand Juli 2026) |

---

## Drei Fragen, die Einsteiger häufig stellen

Bevor es zu den Modellen geht, kurz die drei Punkte, die am meisten Verwirrung stiften.

### „Reicht ein alter i5 gegen einen modernen N100 oder N95?"

Die kurze Antwort: Ein i5-8500T (6 Kerne, 8. Generation) aus 2018 hat in typischen Homelab-Aufgaben mehr Rechenleistung als ein Intel N95 (4 Kerne) aus 2023. Der N95 verbraucht dafür im Leerlauf deutlich weniger Strom.

Für viele gleichzeitige Dienste – etwa Proxmox mit mehreren Containern – ist der i5 meist die bessere Wahl. Für einen einzelnen 24/7-Dauerläufer wie Pi-hole oder Home Assistant genügt ein N95 oder N100 gut.

### „Was ist ein Barebone? Muss ich löten?"

Ein Barebone ist ein PC, bei dem **Arbeitsspeicher (RAM) und Festplatte (SSD) fehlen** – das Gehäuse mit Mainboard und CPU ist bereits vorhanden. Du musst nicht löten.

Die SSD wird in einen Steckplatz gesteckt und mit einer kleinen Schraube gesichert. Der RAM wird in seinen Steckplatz gedrückt, bis er einrastet. Das dauert wenige Minuten, Spezialwerkzeug brauchst du keines.

Plane beim Kauf eines Barebone etwa 40–100 € für gebrauchten RAM sowie 50–100 € für eine SSD ein (Preise Stand Juli 2026 – Marktpreise können schwanken, gebrauchte Komponenten sind oft günstiger).

### „Brauche ich für 2,5 GbE ein neues Netzwerk?"

Nein. Ein 2,5-Gigabit-Anschluss verhandelt automatisch die Geschwindigkeit mit deiner vorhandenen Hardware. An einer normalen FRITZ!Box mit 1 Gigabit läuft er problemlos mit 1 Gigabit.

Der Vorteil von 2,5 GbE zeigt sich erst bei mehreren gleichzeitig stark belasteten Geräten im Netzwerk. Für die ersten Schritte ist 1 GbE vollkommen ausreichend.

---

## Auf einen Blick

| Budget | Modell(e) | Zustand | Highlight |
|--------|-----------|---------|-----------|
| **Bis 50 €** | Fujitsu Futro S7010 | Gebraucht | Günstigster Einstieg – 4 Kerne, lüfterlos |
| **80–150 €** | HP ProDesk 400 G3/G4 Mini **oder** Dell OptiPlex 3060/3070 Micro | Gebraucht | Je nach aktuellem Angebot wählen |
| **150–200 €** | Lenovo ThinkCentre M720q Tiny | Gebraucht | PCIe-Slot über Riser-Karte nachrüstbar |
| **200–300 €** | GMKtec G3S (Intel N95) | Neu | Neugerät mit Garantie |

---

## Bis 50 €: Fujitsu Futro S7010 – Der günstigste Einstieg

{{< figure src="/images/products/fujitsu-s7010.jpg" alt="Fujitsu Futro S7010 Thin Client" width="400" >}}

Der Fujitsu Futro S7010 ist gebraucht regelmäßig für 30–50 € (Stand Juli 2026) zu finden, oft bereits mit 8 GB RAM und 64 GB SSD. Für seinen Preis ist er erstaunlich brauchbar.

Die CPU ist ein **Intel Celeron J4125** mit 4 Kernen und maximal 2,7 GHz. Das reicht für leichte Dienste gut, aber nicht für aufwendigere Workloads.

**Technische Daten im Überblick:**

- **CPU:** Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 W TDP)
- **RAM:** 8 GB DDR4 offiziell, 16 GB in der Praxis getestet – nur 1 Steckplatz
- **SSD:** 64 GB M.2 SATA (austauschbar, aber **kein NVMe-Support**)
- **Netzwerk:** 1 Gigabit Ethernet
- **Stromverbrauch (Leerlauf):** ca. 3–7 W
- **Kühlung:** Passiv, lüfterlos – absolut geräuschlos
- **Erweiterbarkeit:** Nur 1 RAM-Slot, nur M.2 SATA, kein PCIe-Slot
- **USB-C:** Nein

**Passend wenn** du Pi-hole, Home Assistant oder einzelne leichte Docker-Container betreiben willst. Auch gut geeignet als allererster Server zum Ausprobieren, ohne viel Geld zu riskieren.

Nicht geeignet für mehrere gleichzeitige VMs, aufwendige Docker-Stacks oder rechen­intensive Aufgaben.

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=matmaksa-homelab-21)

---

## 80–150 €: HP ProDesk G3/G4 Mini oder Dell OptiPlex 3060/3070 Micro

In dieser Preisklasse hast du freie Wahl – nimm schlicht das Modell, das du gerade günstiger findest. Leistung und Ausstattung sind ähnlich.

**Hinweis zur SSD:** Diese Geräte unterstützen NVMe-SSDs (der schnelle aktuelle Standard). Wenn du eine SSD nachkaufst, lohnt sich eine NVMe – nicht die langsamere SATA-Variante.

### HP ProDesk 400 G3 Mini (ca. 50–100 € gebraucht, Stand Juli 2026)

- **CPU:** Intel Core i5-6500T oder i5-7500T (je 4 Kerne)
- **RAM:** Bis zu 32 GB DDR4 – zwei Steckplätze, nicht verlötet
- **Speicher:** 1× M.2 NVMe oder SATA + 1× 2,5-Zoll-SATA-Schacht
- **Netzwerk:** 1 Gigabit (Intel)
- **Stromverbrauch (Leerlauf):** ca. 12–18 W
- **Erweiterbarkeit:** RAM nachrüstbar, zweiter Speicherschacht vorhanden. Kein PCIe-Slot.

**Passend wenn** du einen ersten Proxmox-Server, Pi-hole oder einen Docker-Stack mit mehreren Containern betreiben willst.

🔍 [HP ProDesk 400 G3 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G3+Mini&tag=matmaksa-homelab-21)

---

### HP ProDesk 600 G4 Mini (ca. 100–180 € gebraucht, Stand Juli 2026)

Der G4 bringt CPUs der 8. Intel-Generation und damit mehr Kerne. Ein **i5-8500T** hat 6 Kerne statt 4 beim G3 – das macht sich bei gleichzeitigen VMs oder Containern bemerkbar.

- **CPU:** i5-8500T (6 Kerne) oder i7-8700T (6 Kerne, 12 Threads)
- **RAM:** Bis zu 32 GB offiziell (64 GB in der Praxis getestet, ohne Herstellergarantie)
- **Speicher:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA-Schacht
- **Netzwerk:** 1 Gigabit (Intel)
- **Erweiterbarkeit:** RAM + doppelter Speicher. Kein PCIe-Slot.

**Passend wenn** du mehrere VMs unter Proxmox oder einen Docker-Stack mit fünf oder mehr Containern betreiben willst.

🔍 [HP ProDesk 600 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+600+G4+Mini&tag=matmaksa-homelab-21)

---

### Dell OptiPlex 3060/3070 Micro (ca. 80–180 € gebraucht, Stand Juli 2026)

Die direkte Konkurrenz zu HP in dieser Klasse. Ähnliches Preisniveau, ähnliche Spezifikationen. Der **3070** bringt die 9. Intel-Generation.

- **CPU:** i5-8500T (3060, 6 Kerne) oder i5-9500T (3070, 6 Kerne)
- **RAM:** Bis zu 32 GB DDR4 (64 GB in der Praxis getestet, ohne Herstellergarantie)
- **Speicher:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA-Schacht
- **Netzwerk:** 1 Gigabit (Intel)
- **USB-C:** Nein (beim OptiPlex nicht vorhanden; Lenovo M720q hat USB-C)

**Passend wenn** du auf dem Gebrauchtmarkt einen Dell günstiger findest als HP – die Leistung ist vergleichbar.

🔍 [Dell OptiPlex 3060/3070 bei Amazon suchen](https://www.amazon.de/s?k=Dell+OptiPlex+Micro&tag=matmaksa-homelab-21)

---

## 150–200 €: Lenovo ThinkCentre M720q Tiny – Der Erweiterbare

{{< figure src="/images/products/lenovo-m720q-tiny.jpg" alt="Lenovo ThinkCentre M720q Tiny" width="400" >}}

Der Lenovo ThinkCentre M720q Tiny hebt sich durch seinen PCIe-Anschluss im Innern von der Konkurrenz ab. Über eine passende **Riser-Karte** (separat erhältlich, ca. 20–40 €, Stand Juli 2026) lässt sich dieser Anschluss nutzen, um zum Beispiel eine 10-Gigabit-Netzwerkkarte, eine SATA-Erweiterungskarte oder eine kompakte Grafikkarte einzubauen.

Wichtig: Die Riser-Karte ist kein Zubehör, das im Lieferumfang enthalten ist. Du musst sie separat beschaffen. Prüfe beim Kauf, welche PCIe-Riser-Karte zum M720q kompatibel ist.

**Technische Daten im Überblick:**

- **CPU:** Intel Core i5-8500T (6 Kerne) oder i7-8700T (6 Kerne, 12 Threads)
- **RAM:** Bis zu 32 GB DDR4 (64 GB in der Praxis getestet, ohne Herstellergarantie)
- **Speicher:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA-Schacht
- **Netzwerk:** 1 Gigabit (Intel) – über PCIe-Riser auf 10 Gigabit erweiterbar
- **Erweiterbarkeit:** RAM + doppelter Speicher + **PCIe-Slot via Riser-Karte**
- **USB-C:** Ja – einmal USB-C (in dieser Klasse ungewöhnlich)
- **Stromverbrauch (Leerlauf):** ca. 12–20 W

**Passend wenn** du dein Homelab nach und nach erweitern möchtest – zum Beispiel später eine 10-GbE-Karte oder eine GPU nachrüsten willst.

🔍 [Lenovo ThinkCentre M720q bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+ThinkCentre+M720q+Tiny&tag=matmaksa-homelab-21)

---

## 200–300 €: GMKtec G3S – Neugerät mit Garantie

{{< figure src="/images/products/gmktec-g3s.jpg" alt="GMKtec G3S Intel N95 Mini PC" width="400" >}}

Der GMKtec G3S ist eine Option, wenn du ein **Neugerät mit Herstellergarantie** bevorzugst und nicht auf dem Gebrauchtmarkt suchen möchtest.

**Technische Daten im Überblick:**

- **CPU:** Intel N95 (4 Kerne, Alder Lake Architektur 2023, 15 W TDP)
- **RAM:** 8 oder 16 GB DDR4 – **verlötet, nicht erweiterbar** ⚠️
- **Speicher:** 1× M.2 NVMe (bis zu 8 TB möglich)
- **Netzwerk:** 1 Gigabit Ethernet
- **Stromverbrauch (Leerlauf):** ca. 10–15 W
- **Erweiterbarkeit:** RAM verlötet, nur 1 SSD-Schacht, kein PCIe
- **USB-C:** Ja

**Wichtiger Hinweis:** Der Intel N95 (4 Kerne) hat in typischen Homelab-Aufgaben weniger Rechenleistung als ein gebrauchter i5-8500T (6 Kerne) aus dem HP oder Dell für 100–120 €. Der Vorteil des GMKtec G3S liegt in der neuen Hardware mit Garantie und dem niedrigen Stromverbrauch.

Das verlötete RAM ist ein spürbarer Nachteil: Mit 16 GB maximal ist kaum Spielraum für Erweiterungen. Wer später mehr als fünf bis sechs Docker-Container oder mehrere VMs betreiben will, könnte mit 16 GB schnell an Grenzen stoßen.

**Passend wenn** du ein Neugerät mit Garantie für leichte Dauerdienste wie Docker, Home Assistant oder einen Medienserver suchst.

👉 [GMKtec G3S bei Amazon suchen](https://www.amazon.de/s?k=GMKtec+G3S&tag=matmaksa-homelab-21)

---

## Wohin mit größeren Datenmengen?

Die Mini-PCs bieten intern meist Platz für eine oder zwei SSDs. Für größere Datenmengen – Nextcloud-Fotos, Mediensammlung, Backups – gibt es drei gängige Wege:

**Externe USB-Festplatte:** Einfachste Lösung. Ein 4-TB-USB-3.0-Laufwerk (ca. 80–120 €, Stand Juli 2026) wird einfach eingesteckt und läuft stabil. Für Medienserver und Backups gut geeignet.

**Interne 2,5-Zoll-SSD:** HP, Dell und Lenovo haben meist einen zweiten Einbauplatz für eine 2,5-Zoll-SATA-SSD. Dort passen bis zu 4 TB rein – für viele Homelabs ausreichend.

**Separates NAS:** Ein eigener kleiner Server nur für Festplatten. Das ist die flexibelste Lösung, aber auch die teuerste – ab etwa 200–300 € aufwärts (Stand Juli 2026).

Für den Einstieg empfiehlt sich: internen Speicher nutzen und eine externe USB-Festplatte für Backups dazunehmen. Ein NAS lässt sich später immer noch ergänzen.

---

## SSD-Empfehlung für den Einstieg

| Modell | Preis (ca.) | Typ | Passt zu |
|--------|------------|-----|----------|
| [Kingston NV3 1 TB](https://geizhals.de/kingston-nv3-nvme-pcie-4-0-ssd-1tb-snv3s-1000g-a3248579.html?hloc=de) | ~60–80 € (Stand Juli 2026) | NVMe PCIe 4.0 | HP, Dell, Lenovo (nicht Futro – kein NVMe) |
| [WD Blue SA510 1 TB](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | ~55–75 € (Stand Juli 2026) | SATA M.2 | Fujitsu Futro, HP, Dell, Lenovo |

---

## Lohnen sich gebrauchte Business-Mini-PCs?

Für den Einstieg ins Homelab sind gebrauchte Business-Mini-PCs von HP, Lenovo und Dell aus mehreren Gründen interessant:

- **Preis:** Deutlich günstiger als Neugeräte mit vergleichbarer Leistung
- **Verfügbarkeit:** Großes Angebot durch Unternehmens-Ausmusterungen, oft mit kurzer Restgarantie
- **Auslegung:** Business-Geräte sind für den Dauerbetrieb konzipiert und entsprechend gebaut
- **Stromverbrauch:** Meist unter 25 W im Leerlauf – für den 24/7-Betrieb gut geeignet

Worauf du beim Kauf achten solltest: Prüfe den Zustand sorgfältig, frage nach Garantie-Restlaufzeit und kauf wenn möglich bei verifizierten Refurbished-Händlern.

---

## Vergleichstabelle aller Modelle

| Modell | Preis (Stand Juli 2026) | CPU | RAM max. | Netzwerk | Besonderheit |
|--------|------------------------|-----|----------|----------|--------------|
| Fujitsu Futro S7010 | ~40 € | J4125 (4C) | 8 GB | 1 GbE | Lüfterlos, sehr sparsam |
| HP ProDesk 400 G3 | ~80 € | i5-7500T (4C) | 32 GB | 1 GbE | Großes Angebot |
| HP ProDesk 600 G4 | ~120 € | i5-8500T (6C) | 32 GB (64 GB inoff.) | 1 GbE | 6 Kerne, 8. Gen |
| Dell OptiPlex 3060 | ~120 € | i5-8500T (6C) | 32 GB (64 GB inoff.) | 1 GbE | Alternative zu HP |
| Dell OptiPlex 3070 | ~150 € | i5-9500T (6C) | 32 GB (64 GB inoff.) | 1 GbE | 9. Gen Intel |
| Lenovo M720q Tiny | ~150 € | i5-8500T (6C) | 32 GB (64 GB inoff.) | 1 GbE | PCIe via Riser-Karte + USB-C |
| GMKtec G3S | ~220 € | N95 (4C) | 16 GB (verlötet) | 1 GbE | Neugerät mit Garantie |

---

## KI-Modelle lokal betreiben – was ist realistisch?

Lokale KI-Modelle (z. B. über Ollama) sind auf Mini-PCs ohne dedizierte GPU grundsätzlich möglich, aber mit Einschränkungen verbunden. Die Tabelle zeigt, was in welcher Preisklasse erprobt wurde – ohne Garantie, da Ergebnisse je nach Modell, Einstellungen und System variieren.

| Budget | KI-Nutzung auf der CPU |
|--------|------------------------|
| **Bis 50 €** | Für Ollama und vergleichbare Tools nicht sinnvoll nutzbar – CPU und RAM zu begrenzt |
| **80–150 €** | Kleine Modelle wie Phi-3-mini (3,8B) laufen in Tests brauchbar. Größere Modelle wie Llama-3-8B sind sehr langsam. Mindestens 16 GB RAM werden empfohlen. |
| **150–200 €** | Phi-3-mini läuft flüssiger. Mit 32 GB RAM auch Llama-3-8B nutzbar, aber kein flüssiges Erlebnis. Der M720q ermöglicht über PCIe-Riser eine kompakte GPU – das verändert das Bild erheblich. |
| **200–300 €** | Der N95 (GMKtec G3S) ist für KI-Aufgaben auf der CPU schwächer als ein i5-8500T trotz neuerer Architektur. RAM ist auf 16 GB begrenzt. |

Wer KI-Modelle regelmäßig und flüssig nutzen möchte, sollte langfristig über eine dedizierte GPU nachdenken. Die Mini-PCs hier sind für gelegentliches Ausprobieren gedacht, nicht als primäre KI-Workstation.

---

## Fazit: Welcher Mini-PC passt zu deinem Budget?

| Budget | Empfehlung |
|--------|-----------|
| **40–50 €** | **Fujitsu Futro S7010** – günstigster Einstieg, lüfterlos, gut für einzelne Dauerdienste |
| **80–150 €** | **HP ProDesk 400 G3/600 G4** oder **Dell OptiPlex 3060/3070** – je nach aktuellem Angebot |
| **150–200 €** | **Lenovo M720q Tiny** – passend wenn du Erweiterungen planst (PCIe via Riser-Karte) |
| **200–300 €** | **GMKtec G3S** – passend wenn du ein Neugerät mit Garantie bevorzugst (CPU-seitig schwächer als gebrauchte i5-Geräte) |

**Persönliche Einschätzung für Einsteiger:** Ein **HP ProDesk 600 G4** gebraucht für etwa 90–120 € (Stand Juli 2026) ist ein solider Startpunkt. Mit nachrüstbarem RAM (16–32 GB, gebraucht oft günstiger) und einer NVMe-SSD hast du 6 Kerne, ordentliche Laufruhe und die Möglichkeit, später einen zweiten Speicher einzubauen. Ein guter Kompromiss, ohne zu viel Geld zu riskieren.
