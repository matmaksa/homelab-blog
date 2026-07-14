+++
title = 'Fujitsu Futro S7010 im Kaufzustand: Was geht mit 4 GB RAM und 64 GB SSD?'
description = 'Der Fujitsu Futro S7010 für 40 Euro: Was leistet der Thin Client mit 4 GB RAM und 64 GB SSD als Proxmox-Host wirklich? Echte Messwerte statt Werbeversprechen.'
date = 2026-07-14
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false

# Preview Classification
preview_content_type = "article_draft"
publish_eligible = false
user_visual_approval_required = true
fact_check_required = true
link_check_required = true
price_check_required = false
recommended_action = "pending_visual_approval_and_fact_check"
content_intent = "pillar"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = true
risk_level = "medium"
+++

## Hardware

| Komponente | Detail |
|---|---|
| Modell | Fujitsu Futro S7010 |
| CPU | AMD GX-217GA (2 Kerne, ~1,6 GHz) |
| RAM | 4 GB DDR3 (3,6 GiB nutzbar) |
| SSD | 64 GB intern |
| Netzteil | Externes 19V-Netzteil |
| Preis (gebraucht) | ca. 40–50 Euro |

## Proxmox-Baseline (Leerlauf, keine Gäste)

| Metrik | Wert |
|---|---|
| Proxmox-Version | 9.2.4 (Kernel 7.0.14-4-pve) |
| RAM gesamt | 3.730.072 kB (3,6 GiB) |
| RAM belegt (Host) | **1,3 GiB** |
| RAM verfügbar | 2,2 GiB |
| Swap | 7,2 GiB (0 B genutzt) |
| Load Average | 0,09 / 0,04 / 0,08 |
| SSD belegt | 5,4 GB von 25 GB (root) |
| SSD thin-pool | 17,2 GB für Gäste |
| USB-Backup-HDD | 931 GB (870 GB frei) |

**Wichtig:** Proxmox allein beansprucht bereits ~1,3 GB RAM. Für Gäste bleiben effektiv **2,2 GB**. Das ist nicht viel.

## Sinnvolle Dienste im Kaufzustand

- **Ein DNS-Blocker** (Pi-hole oder AdGuard Home, ~16–50 MB)
- **Ein kleiner Test-LXC** (zeitweise, ~256–512 MB)
- **USB-Backups** der Gäste
- **Lern- und Experimentierplattform**

## Grenzen des Kaufzustands

> **Nicht möglich / nicht empfohlen im Kaufzustand:**
> - KI-/Ollama-Modelle
> - Immich (Foto-Management mit ML)
> - Produktive Nextcloud-Instanz
> - Mehrere parallele VMs
> - NAS-Ersatz
> - Media-Transcoding

## Upgrade-Pfad

### Empfohlen: 8 GB RAM (~15–20 Euro)

- Mehrere kleine LXC gleichzeitig
- Reverse Proxy als Zusatzprojekt
- Nextcloud-Testinstanz
- Deutlich bessere Reserve für Dateicache

### Separates Datenlaufwerk

- Notwendig für dauerhafte Fotoablage
- 500 GB – 2 TB interne 2,5"-HDD oder USB 3.0
- Die vorhandene USB-Backup-HDD bleibt **ausschließlich Backup**
- Originaldaten und einziges Backup niemals auf derselben HDD

## Fazit

Der Fujitsu Futro S7010 ist ein **sparsamer Einsteiger-Proxmox-Host** für 40 Euro. Im Kaufzustand mit 4 GB RAM laufen **ein bis zwei kleine LXC** stabil. Wer mehrere Dienste betreiben will, sollte **8 GB RAM** nachrüsten. Ein **separates Datenlaufwerk** ist für jede Form der Datenablage Pflicht.

Kein Wunder-Server, aber ein **ehrliches Lernsystem** für den Homelab-Einstieg.
+++
