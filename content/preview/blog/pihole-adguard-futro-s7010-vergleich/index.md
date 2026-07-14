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
| RAM (konfiguriert) | 512 MB |
| RAM (cgroup memory.current) | Siehe Tabelle |
| Disk | 4 GB (thin) |
| Swap | Kein |
| Netzwerk | VLAN 20, statische IP |
| Upstream | Cloudflare (1.1.1.1) + Google (8.8.8.8) |
| Stabilisierung | 2 Minuten vor Messbeginn |
| Testabfragen | 30 pro System (google.com, warm) |

**Hinweis zur Messmethodik:** Angegeben wird der cgroup memory.current (tatsächlicher Speicher aus Host-Sicht, inkl. Page Cache und LXC-Overhead) sowie der Dienst-RSS (resident set size des Hauptprozesses). Beide Werte wurden nach 2 Minuten Stabilisierung mit `cat /sys/fs/cgroup/lxc/{CTID}/memory.current` und `ps aux` erhoben.

## Messergebnisse

| Metrik | Pi-hole v6.4.3 | AdGuard Home v0.107.78 |
|---|---|---|
| LXC cgroup memory.current | **110 MB** | 50 MB (gemessen vor Löschung) |
| Dienst-RSS | ~10 MB | ~57 MB |
| Host-RAM-Effekt | +110 MB | +100 MB |
| Disk-Verbrauch | 834 MB | 713 MB |
| Filterregeln | 78.451 | 157.189 |
| DNS-Latenz (Median) | < 1 ms | < 1 ms |
| DNS-Latenz (Max) | 1 ms | 2 ms |
| Fehlerrate | 0 % | 0 % |
| Startzeit | ~5 s | ~3 s |
| Prozesse im LXC | 18 | 6 |
| Web-Interface | Port 80/443 | Port 80 |

**Anmerkung zu Pi-hole LXC-RAM:** Der innerhalb des Containers mit `free -m` gemeldete Wert (16 MB) zeigt nur den vom Kernel als "used" ausgewiesenen Speicher. Der cgroup-Wert (110 MB) ist der tatsächliche Host-Effekt inklusive Page Cache. Bei AdGuard wurde nur der cgroup-Wert von 50 MB notiert (LXC-intern nicht erneut erfasst).

**DNS-Latenz:** Alle gemessenen Werte liegen unter der Millisekunden-Auflösung von `dig`. Für die Praxis sind beide Systeme gleich schnell.

## Fairness des Vergleichs

Die Filterregelmengen waren **nicht identisch**:
- Pi-hole: ~78.451 Regeln (Standard-Gravity)
- AdGuard Home: ~157.189 Regeln (AdGuard DNS Filter)

AdGuard hatte im Test etwa **doppelt so viele Filterregeln** wie Pi-hole. Der höhere Dienst-RSS von AdGuard (~57 MB vs. ~10 MB) könnte teilweise durch die größere Filterliste bedingt sein. Ein direkter Ressourcenvergleich bei identischer Regelanzahl wurde nicht durchgeführt.

**Fazit zur Fairness:** In diesem Test auf dem Futro S7010 benötigte Pi-hole weniger Arbeitsspeicher. Beide Lösungen beantworteten lokale DNS-Anfragen unterhalb der Messauflösung. Da AdGuard Home mit deutlich mehr Filterregeln getestet wurde, lässt sich daraus **kein allgemeiner Ressourcen-Sieger** ableiten.

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

**Empfehlung für den konkreten 4-GB-Futro-Setup: Pi-hole**

Begründung:
- Geringerer gemessener Speicherbedarf (110 MB vs. 50 MB cgroup, wobei die Filteranzahl unterschiedlich war)
- Ausreichender Funktionsumfang für den Einsatz als DNS-Blocker
- Einfacheres Update via `pihole -up`

**Einschränkung:** Die Unterschiede in der DNS-Latenz sind nicht signifikant. Auf einem System mit 8+ GB RAM wäre AdGuard Home aufgrund des moderneren Web-Interfaces die komfortablere Wahl. Hier entscheiden **Geschmack und Bedienkomfort** mehr als die wenigen MB RAM-Unterschied.

> **Kein produktiver DNS-Einsatz:** Der getestete DNS-LXC bleibt gestoppt. Eine Umstellung des Heimnetzwerk-DNS wurde nicht durchgeführt.
+++
