+++
title = 'Pi-hole oder AdGuard Home auf dem Futro S7010: Der Praxisvergleich'
description = 'Pi-hole vs. AdGuard Home auf dem Fujitsu Futro S7010 mit 4 GB RAM. Echte Messwerte zu RAM, CPU, DNS-Latenz und Bedienung – unter identischen Testbedingungen.'
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
content_intent = "supporting"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = true
risk_level = "low"
+++

## Testaufbau

Beide DNS-LXC unter identischen Bedingungen auf dem Futro S7010 (PVE04):

| Parameter | Wert |
|---|---|
| LXC-Basis | Debian 12 Bookworm |
| CPU | 1 vCore |
| RAM | 512 MB |
| Disk | 4 GB (thin) |
| Swap | Kein |
| Netzwerk | VLAN 20, statische IP |
| Upstream | Cloudflare (1.1.1.1) + Google (8.8.8.8) |
| Stabilisierung | 2 Minuten vor Messbeginn |
| Testabfragen | 30 pro System (google.com, warm) |

## Messergebnisse

| Metrik | Pi-hole v6.4.3 | AdGuard Home v0.107.78 |
|---|---|---|
| LXC-RAM genutzt | **16 MB** | 50 MB |
| Dienst-RSS | ~10 MB | ~57 MB |
| Host-RAM-Effekt | +100 MB | +100 MB |
| Disk-Verbrauch | 818 MB | 713 MB |
| Filterregeln | 78.451 | 157.189 |
| DNS-Latenz (Median) | < 1 ms | < 1 ms |
| DNS-Latenz (Max) | 1 ms | 2 ms |
| Fehlerrate | 0 % | 0 % |
| Startzeit | ~5 s | ~3 s |
| Prozesse im LXC | 18 | 6 |
| Web-Interface | Port 80/443 | Port 80 |

**Hinweis zur DNS-Latenz:** Alle gemessenen Werte liegen unter der Millisekunden-Auflösung von `dig`. Für die Praxis sind beide Systeme gleich schnell.

## Filtervergleich

Beide Systeme nutzen standardmäßig unterschiedliche Blocklisten:
- **Pi-hole:** Standard-Gravity (Default Blocklisten)
- **AdGuard Home:** AdGuard DNS Filter (AdGuardteam Hostlists Registry)

AdGuard hat mit 157.189 Regeln etwa doppelt so viele Einträge wie Pi-hole mit 78.451. Die höhere Regelanzahl bedeutet nicht automatisch besseren Schutz – entscheidend ist die Qualität und Aktualität der Listen.

## Bedienbarkeit

| Kriterium | Pi-hole | AdGuard Home |
|---|---|---|
| Einrichtung | Offizielles Install-Skript | Binary entpacken + Web-Wizard |
| Ersteinrichtung | Dialoge im Terminal | Web-Oberfläche (Port 3000) |
| Dashboard | Funktional, übersichtlich | Modern, detaillierte Statistiken |
| Update | `pihole -up` | Binary ersetzen + Neustart |
| Backup | /etc/pihole/ sichern | /root/AdGuardHome/ sichern |
| Admin-Passwort | via `pihole setpassword` | via Web-UI |

## Fazit

**Für den Futro S7010 im Kaufzustand (4 GB RAM) empfiehlt sich Pi-hole.**

Begründung:
- **Ressourcenschonung:** 16 MB LXC-RAM vs. 50 MB – bei 4 GB Gesamt-RAM ist das relevant
- **DNS-Performance:** Identisch – beide unter 1 ms
- **Update-Komfort:** `pihole -up` ist einfacher als manuelles Binary-Ersetzen

**Einschränkung:** Die Unterschiede in der DNS-Latenz sind **nicht signifikant**. Auf einem System mit 8+ GB RAM wäre AdGuard Home aufgrund des moderneren Web-Interfaces und der umfangreicheren Statistiken die komfortablere Wahl. Hier entscheiden **Geschmack und Bedienkomfort** mehr als die wenigen MB RAM-Unterschied.

> **Kein produktiver DNS-Einsatz:** Der getestete DNS-LXC bleibt gestoppt. Eine Umstellung des Heimnetzwerk-DNS auf diesen Testcontainer wurde nicht durchgeführt.
+++
