---
title: "Homelab unter 100€: Was du wirklich brauchst"
date: 2026-07-06
draft: false
description: "Ein Homelab muss nicht teuer sein. Wer mit gebrauchter Business-Hardware startet, kommt schon für unter 100€ zu einem voll funktionsfähigen Server für Docker, Proxmox oder Pi-hole."
tags:
  - homelab
  - einsteiger
  - thin-client
  - proxmox
  - docker
  - sparen
categories:
  - Homelab
content_state: published
audit_status: passed
user_approval_required: false
approved_for_publish: true
content_intent: pillar
monetization_intent: soft_affiliate
affiliate_disclosure_required: true
price_research_required: false
price_research_done: 2026-07-06
price_research_notes: >
  Typische Gebrauchtpreise Juli 2026 recherchiert: Thin Clients 20–50€ bei eBay/gewerblichen Rückläufern,
  Mini-PCs 50–80€, SSDs 10–15€, DDR3L-RAM 8–12€, 5-Port-Switch 15–20€ (gebraucht 8–12€).
  Preise schwanken saisonal. Keine festen Zusagen.
product_recommendation_allowed: true
instagram_derivatives_required: true
risk_level: low
next_action: user_review_before_publish
cover:
    image: featured.jpg
    alt: "Thin Client auf einem Schreibtisch als Homelab-Einstieg unter 100€"
    relative: true
    caption: "Ein Homelab muss nicht groß und teuer sein – ein gebrauchter Thin Client reicht für den Start."
---

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

**[Thin Clients](/fujitsu-futro-s7010-homelab-einstieg/)** wie der Fujitsu Futro S920 oder S740, HP t730 oder Dell Wyse 5070 lassen sich gebraucht oft für **20–50 Euro** finden. Sie sind leise, klein und verbrauchen im Betrieb meist unter 20 Watt. Einsteiger-Modelle mit 4 GB RAM und einer kleinen SSD sind für erste Experimente ausreichend – wer mehr vorhat, greift zur Variante mit 8 GB RAM.

**[Mini-PCs](/mini-pc-homelab-vergleich/)** der Serien Lenovo ThinkCentre M710q / M720q, HP ProDesk 400 G5 oder Dell OptiPlex 3070 Micro sind etwas teurer, bieten aber oft mehr CPU-Leistung und Erweiterbarkeit. Ein gebrauchtes Gerät mit Intel Core i5 der 8. Generation und 8 GB RAM liegt meist zwischen **50 und 80 Euro**.

> **Preise schwanken – prüfe vor dem Kauf aktuelle Angebote.** Gerade bei Auktionen oder gewerblichen Rückläufern lassen sich gute Deals finden.

## Speicher: SSD und RAM clever kombinieren

- Eine gebrauchte **[120–240 GB SATA-SSD](https://www.amazon.de/dp/B0B25RNBNS?tag=matmaksa-homelab-21)** reicht für die ersten Projekte völlig aus (ca. 10–15 Euro gebraucht).
- Mehr **RAM** ist wichtiger als eine große SSD. 8 GB sind das empfohlene Minimum, 16 GB der Komfortbereich für mehrere Dienste gleichzeitig.
- Thin Clients nutzen oft günstigen DDR3L-SO-DIMM-Speicher – ein gebrauchter 8-GB-Riegel kostet ca. 8–12 Euro.

## Netzwerk: LAN reicht

Ein Homelab unter 100 € braucht kein Wifi 7 und keinen 10-Gbit-Switch. Ein einfacher **[TP-Link oder Netgear Switch mit 5 Ports](https://www.amazon.de/dp/B0000E5N9B?tag=matmaksa-homelab-21)** für 15–20 Euro (gebraucht oft unter 10 Euro) ist völlig ausreichend.

Einzige Empfehlung: Verwende **[Cat‑6 Patchkabel](https://www.amazon.de/dp/B078WPTBPP?tag=matmaksa-homelab-21)** – die sind nicht teuer, ersparen aber später Ärger mit Fehlersuche.

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

| Komponente | Gebrauchtpreis (ca.) |
|---|---|
| Fujitsu Futro S920, 8 GB RAM, 120 GB SSD | 45 € |
| 8 GB RAM zusätzlich (bei Bedarf) | 10 € |
| TP-Link 5-Port Switch (gebraucht) | 8 € |
| 2x Cat‑6 Patchkabel, 1–2 m | 6 € |
| **Gesamt** | **ca. 69 €** |

Mit dem verbleibenden Budget lassen sich eine zweite SSD für Backups oder ein günstiger USB-Stick für erste ISO-Experimente finanzieren.

## Fazit

Ein Homelab unter 100 Euro ist kein Kompromiss – es ist ein cleverer Einstieg.  
Du lernst die gleichen Konzepte wie mit teurer Hardware, aber ohne finanzielles Risiko.  

Starte mit einem gebrauchten Thin Client, installiere [Proxmox](/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) oder Debian, und arbeite dich Schritt für Schritt vor.  
Der Rest wächst von allein – genau wie bei den meisten, die heute mehrere Server betreiben.

---

*Dieser Artikel enthält Affiliate-Links zu externen Marktplätzen und Händlern. Für dich entstehen keine zusätzlichen Kosten, aber wir können eine kleine Provision erhalten, wenn du über diese Links einkaufst. Alle Produktempfehlungen basieren auf eigener Erfahrung und praktischer Eignung für das beschriebene Einsatzszenario.*
