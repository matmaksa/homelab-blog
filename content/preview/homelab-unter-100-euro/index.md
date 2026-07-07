+++
title = "Homelab unter 100€: Was du wirklich brauchst"
description = "Ein Homelab muss nicht teuer sein. Wer mit gebrauchter Business-Hardware startet, kommt schon für unter 100€ zu einem voll funktionsfähigen Server für Docker, Proxmox oder Pi-hole."
date = 2026-07-06
draft = false
robotsNoIndex = true
preview = true
draft_banner = true
status = "draft"
noindex = true
sitemap = { exclude = true }
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
ShowToc = true
comments = false
editPost = []

tags = ["homelab", "einsteiger", "thin-client", "proxmox", "docker", "sparen"]
categories = ["Homelab"]

# Preview-Metadaten
source_draft = "content/posts/homelab-unter-100-euro-was-du-brauchst/index.md"
content_state = "revision_required"
audit_status = "failed"
instagram_derivatives_created = 5
instagram_derivatives_path = "instagram-derivate/unter-100-euro-5-derivate.md"

[cover]
  image = "featured.jpg"
  alt = "Thin Client auf einem Schreibtisch als Homelab-Einstieg unter 100€"
  relative = true
  caption = "PREVIEW: Ein Homelab muss nicht groß und teuer sein – ein gebrauchter Thin Client reicht für den Start."
+++

# Homelab unter 100€: Was du wirklich brauchst

Viele denken bei einem Homelab sofort an teure Server-Racks, laute Lüfter und eine dreistellige Stromrechnung.  
Die Wahrheit: Für die ersten Schritte reichen oft **unter 100 Euro** – wenn man weiß, worauf es ankommt.

Dieser Artikel zeigt, was du wirklich brauchst, worauf du sparen kannst und wo sich ein geringerer Invest trotzdem lohnt.

## Für wen ist dieser Artikel?

- Du willst zu Hause IT-Wissen praktisch aufbauen
- Du suchst einen leisen, stromsparenden Server für Docker, Pi-hole, [Home Assistant](/home-assistant-gebrauchter-mini-pc-2026/) oder einen VPN
- Du hast kein großes Budget, aber Lust, selbst zu bauen
- Du bist bereit, gebrauchte Business-Hardware statt neuer Verbrauchergeräte zu kaufen

## Das Herz: Ein gebrauchter Thin Client oder Mini-PC

Die wichtigste Komponente in einem Low-Budget-Homelab ist kein Serverschrank, sondern ein kleiner, gebrauchter Büro-Rechner.

**[Thin Clients](/fujitsu-futro-s7010-homelab-einstieg/)** wie der Fujitsu Futro S920 oder S740, HP t730 oder Dell Wyse 5070 lassen sich gebraucht je nach Zustand, Ausstattung und Händler für **20–50 Euro** finden. Sie sind leise, klein und verbrauchen im Betrieb meist unter 20 Watt. Einsteiger-Modelle mit 4 GB RAM und einer kleinen SSD sind für erste Experimente ausreichend – wer mehr vorhat, greift zur Variante mit 8 GB RAM.

**[Mini-PCs](/mini-pc-homelab-vergleich/)** der Serien Lenovo ThinkCentre M710q / M720q, HP ProDesk 400 G5 oder Dell OptiPlex 3070 Micro sind leistungsfähiger, liegen aber meist eher bei **100–130 Euro oder höher**. Sie sind als Upgrade-Option interessant, passen nicht immer in ein reines 100-Euro-Budget. Wer unter 100 Euro bleiben will, ist mit einem Thin Client realistischer unterwegs.

> **Preise schwanken – prüfe vor dem Kauf aktuelle Angebote.** Gerade bei Auktionen oder gewerblichen Rückläufern lassen sich gute Deals finden.

## Speicher: SSD und RAM clever kombinieren

- Eine gebrauchte **120–240 GB SATA-SSD** reicht für die ersten Projekte völlig aus. Die Preise variieren je nach Zustand und Händler – regelmäßig prüfen lohnt sich.
- Mehr **RAM** ist wichtiger als eine große SSD. 8 GB sind das empfohlene Minimum, 16 GB der Komfortbereich für mehrere Dienste gleichzeitig.
- **RAM-Typ und Aufrüstbarkeit** hängen stark vom konkreten Thin-Client-Modell ab. Manche Geräte nutzen Laptop-Speicher (SO-DIMM), andere sind fest verlötet oder begrenzt aufrüstbar. Vor dem Kauf immer das Datenblatt und die vorhandene Ausstattung prüfen.

## Netzwerk: LAN reicht

Ein Homelab unter 100 € braucht kein Wifi 7 und keinen 10-Gbit-Switch. Ein einfacher **TP-Link oder Netgear Switch mit 5 Ports** (neu 15–20 Euro, gebraucht oft günstiger) ist völlig ausreichend.

Einzige Empfehlung: Verwende **Cat‑6 Patchkabel** – die sind nicht teuer, ersparen aber später Ärger mit Fehlersuche.

## Stromverbrauch – der oft unterschätzte Posten

Ein Thin Client mit 15–20 Watt kostet bei 24/7-Betrieb etwa **30–45 Euro pro Jahr** (bei 30 Cent/kWh). Das ist günstiger als viele Streaming-Geräte. Ein Desktop-Rechner mit 80–100 Watt käme dagegen schnell auf 200 Euro pro Jahr – das sprengt das Budget nicht nur einmal, sondern dauerhaft.

## Was du nicht brauchst

Manche Dinge klingen wichtig, sind aber für den Start überflüssig:

- **USV** – sinnvoll, aber kein Pflichtkauf fürs erste Jahr.
- **Rack** – ein Mini-PC steht unsichtbar neben dem Router.
- **Enterprise-Switch** – ein einfacher unmanaged Switch tut es.
- **NAS** – eine externe USB-SSD oder ein zweiter Mini-PC als Backup-Ziel reichen anfangs.
- **Domain mit eigenem SSL-Zertifikat** – Tailscale oder eine lokale IP reichen für die Lernphase völlig.

## Beispiel-Setup unter 100€

Die folgende Zusammenstellung ist eine **beispielhafte Orientierung**. Die tatsächlichen Preise hängen stark von Verfügbarkeit, Zustand und Händler ab – regelmäßiges Prüfen und Vergleichen lohnt sich.

| Komponente | Geschätzter Gebrauchtpreis |
|---|---|
| Thin Client (z. B. Futro S920, 4–8 GB RAM, SSD) | 20–50 € |
| Gebrauchte SSD – je nach Angebot | variabel |
| 5-Port Gigabit Switch (gebraucht) | ca. 8–15 € |
| 2x Cat‑6 Patchkabel | ca. 5–10 € |
| **Gesamt (optimistisch)** | **unter 100 € möglich** |

Mit dem verbleibenden Budget lassen sich eine zweite SSD für Backups oder ein günstiger USB-Stick für erste ISO-Experimente finanzieren.

## Fazit

Ein Homelab unter 100 Euro ist kein Kompromiss – es ist ein cleverer Einstieg.  
Du lernst die gleichen Konzepte wie mit teurer Hardware, aber ohne finanzielles Risiko.

Starte mit einem gebrauchten Thin Client, installiere [Proxmox](/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) oder Debian, und arbeite dich Schritt für Schritt vor.  
Der Rest wächst von allein – genau wie bei den meisten, die heute mehrere Server betreiben.
