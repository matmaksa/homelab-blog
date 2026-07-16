+++
title = "Homelab unter 100€: Was du wirklich brauchst"
description = "Ein Homelab muss nicht teuer sein. Wer mit gebrauchter Business-Hardware startet, kommt schon für unter 100€ zu einem voll funktionsfähigen Server für Docker, Proxmox oder Pi-hole."
date = 2026-07-06
draft = false
ShowToc = true
ShowShareButtons = true
ShowBreadCrumbs = true
ShowPostNavLinks = true
ShowCodeCopyButtons = true

tags = ["homelab", "einsteiger", "thin-client", "proxmox", "docker", "sparen"]
categories = ["Homelab"]

content_intent = "pillar"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = true
risk_level = "low"

content_state = "published_ready"
audit_status = "passed"
user_approval_required = false
approved_for_publish = true
next_action = "monitor_and_promote"

instagram_derivatives_created = 5
instagram_derivatives_path = "instagram-derivate/unter-100-euro-5-derivate.md"
instagram_derivatives_status = "ready_for_review"

[cover]
  image = "featured.jpg"
  alt = "Fujitsu Futro Thin Client auf einem Schreibtisch als Homelab-Einstieg unter 100€"
  relative = true
  caption = "Ein Homelab muss nicht groß und teuer sein – ein gebrauchter Thin Client reicht für den Start."
+++

Viele denken bei einem Homelab sofort an teure Server-Racks, laute Lüfter und eine dreistellige Stromrechnung.  
Die Wahrheit: Für die ersten Schritte reichen oft **unter 100 Euro** – wenn man weiß, worauf es ankommt.

Dieser Artikel zeigt, was du wirklich brauchst, worauf du sparen kannst und wo sich eine etwas höhere Anfangsinvestition lohnt.

## Für wen ist dieser Artikel?

- Du willst zu Hause IT-Wissen praktisch aufbauen
- Du suchst einen leisen, stromsparenden Server für Docker, Pi-hole, [Home Assistant]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}}) oder einen VPN
- Du hast kein großes Budget, aber Lust, selbst zu bauen
- Du bist bereit, gebrauchte Business-Hardware statt neuer Verbrauchergeräte zu kaufen

## Das Herz: Ein gebrauchter Thin Client oder Mini-PC

Die wichtigste Komponente in einem Low-Budget-Homelab ist kein Serverschrank, sondern ein kleiner, gebrauchter Büro-Rechner.

**[Thin Clients]({{< relref "fujitsu-futro-s7010-homelab-einstieg" >}})** wie der Fujitsu Futro **S740** oder **S7010**, HP t730 oder Dell Wyse 5070 lassen sich gebraucht je nach Zustand, Ausstattung und Händler für **20–50 Euro** finden. Sie sind leise, klein und verbrauchen im Betrieb meist unter 20 Watt. Einsteiger-Modelle mit 4 GB RAM und einer kleinen SSD sind für erste Experimente ausreichend – wer mehr vorhat, greift zur Variante mit 8 GB RAM.

### Vergleich: Fujitsu Futro S740 vs S7010

| Feature | Fujitsu Futro S740 | Fujitsu Futro S7010 |
|---|---|---|
| CPU | Intel Celeron J4105, 4C/4T, 1,5–2,5 GHz | Intel Celeron J4125, 4C/4T, 2,0–2,7 GHz |
| RAM | DDR4 SO-DIMM, häufig 4–8 GB | DDR4 SO-DIMM, häufig 4–8 GB |
| Stromverbrauch | sehr sparsam, typischer Thin-Client-Bereich | sehr sparsam, typischer Thin-Client-Bereich |
| Video | 2x DisplayPort | 2x DisplayPort |
| Geeignet für | Pi-hole, Docker, erste Proxmox-/Linux-Tests | Pi-hole, Docker, Proxmox, mehrere kleine Dienste |
| Hinweis | gut für sehr günstigen Einstieg | oft der bessere Sweet Spot, wenn verfügbar |

**RAM-Hinweis**: Beim RAM immer das konkrete Angebot und Datenblatt prüfen. Viele S740/S7010-Angebote kommen mit 4–8 GB RAM; für erste Dienste reichen 8 GB oft aus. 16 GB können je nach Modell, BIOS und Modul möglich sein, sollten aber vor dem Kauf geprüft werden.

**[Mini-PCs]({{< relref "mini-pc-homelab-vergleich" >}})** der Serien Lenovo ThinkCentre M710q / M720q, HP ProDesk 400 G5 oder Dell OptiPlex 3070 Micro sind leistungsfähiger, liegen aber meist eher bei **100–130 Euro oder höher**. Sie sind als Upgrade-Option interessant, passen nicht immer in ein reines 100-Euro-Budget. Wer unter 100 Euro bleiben will, ist mit einem Thin Client realistischer unterwegs.

> **Preise schwanken – prüfe vor dem Kauf aktuelle Angebote.** Gerade bei Auktionen oder gewerblichen Rückläufern lassen sich gute Deals finden.

{{< ebay-link query="Thin Client gebraucht" text="🔍 Gebrauchte Thin Clients bei eBay durchsuchen" >}}

## Speicher: SSD und RAM clever kombinieren

- Eine gebrauchte **120–240 GB SATA-SSD** reicht für die ersten Projekte völlig aus. Die Preise variieren je nach Zustand und Händler – regelmäßig prüfen lohnt sich.
- Mehr **RAM** ist wichtiger als eine große SSD. 8 GB sind das empfohlene Minimum, 16 GB der Komfortbereich für mehrere Dienste gleichzeitig.
- **RAM-Typ und Aufrüstbarkeit** hängen stark vom konkreten Thin-Client-Modell ab. Manche Geräte nutzen Laptop-Speicher (SO-DIMM), andere sind fest verlötet oder begrenzt aufrüstbar. Vor dem Kauf immer das Datenblatt und die vorhandene Ausstattung prüfen.

## Netzwerk: LAN reicht

Ein Homelab unter 100 € braucht kein Wifi 7 und keinen 10-Gbit-Switch. Ein einfacher **TP-Link oder Netgear Switch mit 5 Ports** (neu 15–20 Euro, gebraucht oft günstiger) ist völlig ausreichend.

Einzige Empfehlung: Verwende **Cat‑6 Patchkabel** – die sind nicht teuer, ersparen aber später Ärger mit Fehlersuche.

## Stromverbrauch – der oft unterschätzte Posten

Ein Thin Client mit typisch 15–20 Watt (je nach Ausstattung) kostet bei 24/7-Betrieb etwa **30–45 Euro pro Jahr** (bei 30 Cent/kWh). Im Idle ist der Verbrauch oft noch niedriger. Ein Desktop-Rechner mit 80–100 Watt käme dagegen schnell auf 200 Euro pro Jahr – das sprengt das Budget nicht nur einmal, sondern dauerhaft.

## Was du nicht brauchst

Manche Dinge klingen wichtig, sind aber für den Start überflüssig:

- **USV** – sinnvoll, aber kein Pflichtkauf fürs erste Jahr.
- **Rack** – ein Mini-PC steht unsichtbar neben dem Router.
- **Enterprise-Switch** – ein einfacher unmanaged Switch tut es.
- **NAS** – für den Start reicht auch eine externe 2,5-Zoll-HDD, eine USB-SSD oder ein zweiter Mini-PC als Backup-Ziel. Wichtig ist nicht SSD um jeden Preis, sondern dass Backups regelmäßig erstellt und testweise wiederhergestellt werden. Für viele Homelab-Backups ist eine günstige HDD völlig ausreichend, weil Restore-Test und Regelmäßigkeit wichtiger sind als maximale Geschwindigkeit.
- **Tailscale** – einfacher Einstieg für den sicheren Fernzugriff von unterwegs. Für Einsteiger die richtige Wahl. **Headscale** (selbst gehostet) ist ein fortgeschrittenes Projekt für später.
- **Teure Domain- oder Hosting-Setups** brauchst du am Anfang nicht. Für die Lernphase reicht entweder lokaler Zugriff, Tailscale (einfacher Einstieg) oder Headscale (fortgeschritten) oder eine kostenlose DynDNS-Adresse mit Let's Encrypt, wenn du bewusst mit HTTPS üben möchtest. Wichtig ist: keine Dienste unüberlegt offen ins Internet stellen.

## Beispiel-Setup unter 100€

Die folgende Zusammenstellung ist eine **beispielhafte Orientierung**. Die tatsächlichen Preise hängen stark von Verfügbarkeit, Zustand und Händler ab – regelmäßiges Prüfen und Vergleichen lohnt sich. Unter 100 € ist möglich, wenn Gebrauchtpreis, RAM/SSD und Zubehör passen.

| Komponente | Geschätzter Gebrauchtpreis |
|---|---|
| Thin Client (z. B. Fujitsu Futro S740 oder S7010, 4–8 GB RAM, kleine SSD) | 20–50 € |
| Gebrauchte SSD – je nach Angebot | variabel |
| 5-Port Gigabit Switch (gebraucht) | ca. 8–15 € |
| 2x Cat‑6 Patchkabel | ca. 5–10 € |
| **Gesamt (optimistisch)** | **unter 100 € möglich, wenn Preise passen** |

Mit dem verbleibenden Budget lassen sich eine zweite HDD/SSD für Backups oder ein günstiger USB-Stick für erste ISO-Experimente finanzieren.

## Fazit

Ein Homelab unter 100 Euro ist ein sinnvoller Einstieg mit klaren Grenzen.  
Du lernst die gleichen Konzepte wie mit teurer Hardware, aber ohne finanzielles Risiko.

Starte mit einem gebrauchten Thin Client, installiere [Proxmox]({{< relref "virtualisierung-kostenlos-2026-proxmox-vmware-alternative" >}}) oder Debian, und arbeite dich Schritt für Schritt vor.

Wenn du nach dem Hardware-Kauf nicht planlos weitermachen willst, lies als Nächstes den Proxmox-Einstieg oder nutze die kommende Homelab-Checkliste, um Hardware, Backup und erste Dienste sauber zu planen.
