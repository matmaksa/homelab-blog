---
title: "Mini PC fürs Homelab nach Budget: Von 40€ bis 300€ – welcher passt zu dir?"
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
---

**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

Ein Mini-PC ist die ideale Grundlage für dein Homelab – leise, stromsparend und leistungsstark genug für Proxmox, Docker und erste KI-Experimente. Aber welches Modell lohnt sich wirklich für dein Budget?

Statt einer generischen Rangliste zeige ich dir hier die besten Optionen **nach Preisklasse** – vom 40-Euro-Thin-Client bis zur 300-Euro-Neumaschine.

<!--more-->

## Auf einen Blick

| Budget | Modell(e) | Zustand | Highlight |
|--------|-----------|---------|-----------|
| **Bis 50 €** | Fujitsu Futro S7010 | Gebraucht | **Günstigster Einstieg** – 4 Kerne, extrem sparsam |
| **50–150 €** | HP ProDesk 400 G3/G4 Mini **oder** Dell OptiPlex 3060/3070 Micro | Gebraucht | **Freie Wahl** – nimm was günstiger ist |
| **150–200 €** | Lenovo ThinkCentre M720q Tiny | Gebraucht | **PCIe-Slot** – erweiterbar wie kein anderer |
| **200–300 €** | GMKtec G3S (Intel N95) | Neu | **Neugerät** – Alder Lake, Garantie, 16 GB |

---

## Bis 50 €: Fujitsu Futro S7010 – Der 40-Euro-Server

{{< figure src="/homelab-blog/images/products/fujitsu-s7010.jpg" alt="Fujitsu Futro S7010 Thin Client" width="400" >}}

Der Fujitsu Futro S7010 ist der absolute Budget-Champion. Gebraucht bekommst du ihn mit 4 GB RAM und 64 GB SSD bereits ab **30–50 €** – und er ist erstaunlich brauchbar für seinen Preis.

Die CPU ist ein **Intel Celeron J4125** (4 Kerne / 4 Threads, 2,0–2,7 GHz). Das ist ein Gemini-Lake-Refresh aus dem Jahr 2019 mit nur 10 Watt TDP – also extrem stromsparend.

- **CPU:** Intel Celeron J4125 (4C/4T, 2,0–2,7 GHz, 10 W TDP)
- **RAM:** 4–8 GB DDR4 (1 Slot, max. 8 GB offiziell)
- **Storage:** 64 GB M.2 SATA (aufrüstbar)
- **Netzwerk:** 1× Realtek Gigabit Ethernet
- **Stromverbrauch:** ca. 4–7 W im Leerlauf – **kaum messbar**
- **Kühlung:** Passiv (lüfterlos) – absolut lautlos
- **Abmessungen:** Winzig – passt in jede Tasche

**👍 Vorteile:** Extrem günstig (ab 30 €). Lüfterlos – absolut lautlos. Sehr stromsparend. 4 Kerne – erstaunlich brauchbar. Kompakte Bauweise. 16 GB RAM möglich (getestet).

**👎 Nachteile:** Nur 1 RAM-Slot (max. 8 GB offiziell). Realtek-NIC (kein Intel – kann bei Proxmox Probleme machen). Kein separater SATA-Port.

**Ideal für:** Pi-hole, Home Assistant, einfache Docker-Container, leichter Dateiserver. Perfekt als **erster Server** zum Ausprobieren, ohne Geld zu verbrennen.

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21)

---

## 50–150 €: HP ProDesk G3/G4 Mini oder Dell OptiPlex 3060/3070 Micro

In dieser Preiskategorie hast du die **freie Wahl** – nimm einfach das Modell, das du gerade günstiger findest. Beide Hersteller liefern solide Business-Mini-PCs, die sich perfekt fürs Homelab eignen.

### HP ProDesk 400 G3 Mini

{{< figure src="/homelab-blog/images/products/hp-prodesk-400-g3.jpg" alt="HP ProDesk 400 G3 Mini" width="400" >}}

Den **HP ProDesk 400 G3 Mini** bekommst du gebraucht für **50–100 €**. Mit Intel Core i5-6500T oder i5-7500T (je 4 Kerne / 4 Threads, kein Hyperthreading), bis zu 32 GB DDR4 und 1× M.2 NVMe/SATA + 1× 2,5"-SATA ist er ein solider Allrounder.

- **CPU:** i5-6500T (4C/4T, 2,5–3,1 GHz) oder i5-7500T (4C/4T, 2,7–3,3 GHz)
- **RAM:** Bis 32 GB DDR4 SODIMM
- **Storage:** 1× M.2 2280 NVMe/SATA + 1× 2,5" SATA
- **Netzwerk:** 1× Intel I219-LM Gigabit Ethernet
- **Preis:** 50–100 € gebraucht

**Ideal für:** Erster Proxmox-Server, Pi-hole, Docker, leichte NAS-Aufgaben.

🔍 [HP ProDesk 400 G3 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G3+Mini&tag=makmatas-homelab-21)

### HP ProDesk 600 G4 Mini

Der **HP ProDesk 600 G4 Mini** ist die leistungsstärkere Business-Linie mit neueren CPUs der 8. Intel-Generation. Hier bekommst du oft den **i5-8500T (6 Kerne / 6 Threads, kein Hyperthreading)** – also spürbar mehr Leistung als beim G3. Ein besonderer Vorteil: Der RAM-Ausbau ist inoffiziell auf bis zu **64 GB** getestet worden.

- **CPU:** i5-8500T (6C/6T, 2,1–3,5 GHz) oder i7-8700T (6C/12T, 2,4–4,0 GHz)
- **RAM:** Bis 32 GB DDR4 SODIMM offiziell (64 GB inoffiziell getestet)
- **Storage:** 1× M.2 2280 NVMe/SATA + 1× 2,5" SATA
- **Netzwerk:** 1× Intel I219-LM Gigabit Ethernet
- **Preis:** 100–180 € gebraucht

**Ideal für:** Mehrere VMs unter Proxmox, Docker-Stack mit 5+ Containern.

🔍 [HP ProDesk 600 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+600+G4+Mini&tag=makmatas-homelab-21)

### Dell OptiPlex 3060 Micro

Der **Dell OptiPlex 3060 Micro** ist die direkte Konkurrenz zum HP ProDesk. Identisches Preisniveau, ähnliche Specs.
- **CPU:** i5-8500T (6C/6T, kein Hyperthreading) oder i3-8100T (4C/4T)
- **RAM:** Bis 32 GB DDR4 SODIMM
- **Netzwerk:** 1× Intel I219-LM Gigabit Ethernet
- **Preis:** 80–150 € gebraucht

### Dell OptiPlex 3070 Micro

Der **Dell OptiPlex 3070 Micro** bringt die 9. Intel-Generation (i5-9500T mit bis zu **6 Kernen**). Preislich liegt er meist etwas über dem 3060er, aber die neuere CPU-Generation macht einen spürbaren Unterschied.

- **CPU:** i5-9500T (6C/6T) oder i3-9100T (4C/4T, 3,1–3,7 GHz)
- **RAM:** Bis 64 GB DDR4 SODIMM (offiziell max. 32 GB)
- **Storage:** 1× M.2 2230/2280 NVMe + 1× 2,5" SATA
- **Netzwerk:** 1× Intel I219-LM Gigabit Ethernet
- **Preis:** 100–180 € gebraucht

🔍 [Dell OptiPlex 3060/3070 bei Amazon suchen](https://www.amazon.de/s?k=Dell+OptiPlex+Micro&tag=makmatas-homelab-21)

**Meine Meinung zur Kategorie 50–150 €:** Egal ob HP oder Dell – nimm das Modell, das du gerade günstiger siehst. Ein ProDesk 600 G4 mit i5-8500T für 110 € ist genauso gut wie ein OptiPlex 3060 für 100 €. Kauf nach Angebotslage.

---

## 150–200 €: Lenovo ThinkCentre M720q Tiny – Der Erweiterbare

{{< figure src="/homelab-blog/images/products/lenovo-m720q-tiny.jpg" alt="Lenovo ThinkCentre M720q Tiny" width="400" >}}

Der Lenovo ThinkCentre M720q Tiny ist die Geheimwaffe für Homelab-Betreiber, die mehr wollen: **Er verfügt über einen PCIe-Slot.** Das bedeutet, du kannst eine 10GbE-Netzwerkkarte, eine SATA-Erweiterungskarte oder sogar eine kompakte GPU nachrüsten – eine Möglichkeit, die kaum ein anderer Mini-PC dieser Preisklasse bietet.

- **CPU:** Intel Core i5-8500T (6C/6T, 2,1–3,5 GHz, kein Hyperthreading) oder i7-8700T (6C/12T, 2,4–4,0 GHz)
- **RAM:** Bis zu 32 GB DDR4 SODIMM offiziell (64 GB inoffiziell getestet)
- **Storage:** 1× M.2 2280 NVMe + 1× 2,5" SATA (Adapter erforderlich)
- **Netzwerk:** 1× Intel I219-V Gigabit Ethernet (über PCIe-Riser auf 10GbE erweiterbar)
- **Anschlüsse:** 1× USB 3.1 Typ-C + 4× USB 3.1 + 2× USB 2.0
- **Besonderheit:** **PCIe x8-Slot (Riser-kompatibel)** – in dieser Geräteklasse äußerst selten
- **Preis gebraucht:** 90–200 €

**👍 Vorteile:** PCIe-Erweiterbarkeit (10GbE, GPU, SATA). USB-C Anschluss. 6 Kerne beim i5-8500T. Sehr kompaktes Design. Große und aktive Lenovo-Community.

**👎 Nachteile:** Nur 1 GbE onboard. Gebrauchtkauf.

**Ideal für:** Homelab mit **10GbE-Ambitionen** (NIC via PCIe-Slot), Proxmox-Cluster, fortgeschrittene Docker-Setups.

🔍 [Lenovo ThinkCentre M720q bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+ThinkCentre+M720q+Tiny&tag=makmatas-homelab-21)

---

## 200–300 €: GMKtec G3S – Neugerät mit Garantie

{{< figure src="/homelab-blog/images/products/gmktec-g3s.jpg" alt="GMKtec G3S Intel N95 Mini PC" width="400" >}}

Der GMKtec G3S ist die beste Wahl, wenn du ein **Neugerät mit Garantie** möchtest und nicht auf dem Gebrauchtmarkt suchen willst. Mit dem **Intel N95** (Alder Lake, 4 Kerne / 4 Threads, bis 3,4 GHz, 15 W TDP) und 16 GB DDR4 ist er moderner als viele gebrauchte Business-PCs und für den Homelab-Alltag bestens geeignet.

- **CPU:** Intel Alder Lake N95 (4C/4T, bis 3,4 GHz, 15 W TDP)
- **RAM:** 8 oder 16 GB DDR4 (1 Slot)
- **Storage:** M.2 SSD (PCIe & SATA, bis 8 TB)
- **Netzwerk:** 1× Gigabit Ethernet
- **Video:** 2× HDMI 2.0 (4K)
- **Preis neu:** ca. 200–230 €

**👍 Vorteile:** Neugerät mit Herstellergarantie. Aktuelle Alder-Lake-Architektur. Bis 8 TB Speicher erweiterbar. Sehr niedriger Stromverbrauch (15 W TDP).

**👎 Nachteile:** Nur 1 RAM-Slot. Kein PCIe-Erweiterungsslot. Nur Gigabit Ethernet. Schwächere CPU als gebrauchte i5-8500T-Geräte in ähnlicher Preislage.

**Ideal für:** Docker-Server, Home Assistant, Office-Homelab, Mediencenter. Optimal für alle, die Neuware mit Garantie bevorzugen.

👉 [GMKtec G3S bei GMKtec ansehen](https://de.gmktec.com/products/gmktec-g3s-intel-alder-lake-n95-mini-pc)

---

## Preis-Leistungs-Vergleich aller Modelle

| Modell | Preis | CPU | RAM max. (offiziell) | Netzwerk | Besonderheit |
|--------|-------|-----|----------------------|----------|--------------|
| Fujitsu Futro S7010 | **~40 €** | J4125 (4C/4T) | 8 GB DDR4 | 1 GbE | Günstigster Einstieg |
| HP ProDesk 400 G3 | **~80 €** | i5-7500T (4C/4T) | 32 GB DDR4 | 1 GbE (Intel) | Riesiges Angebot |
| HP ProDesk 600 G4 | **~120 €** | i5-8500T (6C/6T) | 32 GB DDR4 | 1 GbE (Intel) | 6 Kerne, 64 GB inoffiziell |
| Dell OptiPlex 3060 | **~120 €** | i5-8500T (6C/6T) | 32 GB DDR4 | 1 GbE (Intel) | – |
| Dell OptiPlex 3070 | **~150 €** | i5-9500T (6C/6T) | 32 GB DDR4 | 1 GbE (Intel) | 9. Gen Intel |
| Lenovo M720q Tiny | **~150 €** | i5-8500T (6C/6T) | 32 GB DDR4 | 1 GbE (Intel) | **PCIe x8-Slot + USB-C** |
| GMKtec G3S | **~220 €** | Intel N95 (4C/4T) | 16 GB DDR4 | 1 GbE | Neugerät + Garantie |

---

## Lohnt sich ein gebrauchter Mini-PC fürs Homelab?

**Ja, absolut!** Gerade für den Einstieg sind gebrauchte Business-Mini-PCs von HP, Lenovo und Dell die beste Wahl:

- **Preis:** Bis zu 80–90 % günstiger als Neugeräte
- **Verfügbarkeit:** Riesiges Angebot durch Unternehmens-Ausmusterungen
- **Haltbarkeit:** Business-Geräte sind für den 24/7-Dauerbetrieb ausgelegt
- **Stromverbrauch:** Meist unter 25 W – ideal für den dauerhaften Betrieb

### Worauf du beim Gebrauchtkauf achten solltest

- SSD und RAM sind meistens nachrüstbar – lieber ein günstiges Basismodell kaufen und selbst aufrüsten
- Bei Thin Clients (Fujitsu Futro): RAM ist oft auf 1 Slot begrenzt – vorher prüfen!
- Auf die CPU-Generation achten: Ab Intel der 6./7. Generation ist die Leistung für Proxmox ausreichend
- Bevorzugt bei gewerblichen Händlern kaufen – diese bieten häufig 12 Monate Gewährleistung

---

## Mini-PC für KI-Modelle – Was ist in welcher Preisklasse möglich?

Lokale KI-Modelle sind 2026 auch im Homelab längst angekommen:

| Budget | KI-Nutzung |
|--------|------------|
| **Bis 50 €** | Ollama auf CPU, kleine Modelle (1–3B Parameter) |
| **50–150 €** | Ollama + Open WebUI, 7B-Modelle (langsam) |
| **150–200 €** | 7B-Modelle nutzbar, GPU via PCIe-Riser (M720q) |
| **200–300 €** | 7B-Modelle auf CPU, effizienter durch Alder-Lake-Architektur |

---

## Fazit: Welcher Mini-PC passt zu deinem Budget?

| Dein Budget | Unsere Empfehlung |
|-------------|-------------------|
| **40–50 €** | 👉 **Fujitsu Futro S7010** – günstigster Einstieg überhaupt |
| **50–150 €** | 👉 **HP ProDesk 400 G3/600 G4** oder **Dell OptiPlex 3060/3070** – je nach Angebot |
| **150–200 €** | 👉 **Lenovo M720q Tiny** – PCIe macht den Unterschied |
| **200–300 €** | 👉 **GMKtec G3S** – Neugerät mit Garantie |

**Meine persönliche Empfehlung:** Wer **unter 100 €** bleiben will, greift zum Fujitsu Futro S7010 (ab 40 €) für leichte Dienste oder spart auf 80–120 € für einen HP/Dell mit 6 Kernen. Der **Lenovo M720q Tiny** ist der interessanteste Allrounder – der PCIe x8-Slot hebt ihn klar von allen anderen ab. Wer dagegen einfach ein **Neugerät mit Garantie** will, ist mit dem GMKtec G3S für ~220 € gut bedient – muss aber wissen, dass der N95 CPU-seitig schwächer ist als ein gebrauchter i5-8500T.

**Jetzt bist du dran:** Welches Budget hast du für dein Homelab eingeplant? Schreib es in die Kommentare!



---

## Weiterführende Artikel

- 🔗 [Proxmox Cluster selber bauen: 3 gebrauchte Mini-PCs im Benchmark-Vergleich ab 42 €](/homelab-blog/posts/proxmox-cluster-mini-pc-benchmark-vergleich/) — *(Thema: proxmox,hardware)*
- 🔗 [Fujitsu Futro S740 als Homelab-Einstieg 2026: Der 30€-Server](/homelab-blog/posts/fujitsu-futro-s740-homelab-einstieg/) — *(Thema: fujitsu,futro)*
- 🔗 [Virtualisierung kostenlos 2026: Proxmox VE als VMware-Alternative im Homelab](/homelab-blog/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) — *(Thema: proxmox,virtualisierung)*

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Für dich ändert sich der Preis dadurch nicht.*
