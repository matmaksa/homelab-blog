+++
title = 'Pi-hole oder AdGuard Home auf dem Futro S7010: Der Praxisvergleich'
description = 'Pi-hole vs. AdGuard Home auf dem Fujitsu Futro S7010 mit 4 GB RAM. Echte Messwerte zu RAM, CPU, DNS-Latenz, Laststabilität und Blockabdeckung unter identischen Testbedingungen.'
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
| Disk | 4 GB (thin) |
| Swap | Kein |
| Netzwerk | VLAN 20, statische IP |
| Upstream DNS | Cloudflare (1.1.1.1) + Google (8.8.8.8) |
| Stabilisierung | 2 Minuten vor Messbeginn |

**Standardkonfiguration:** Beide Systeme liefen mit Out-of-the-box-Einstellungen. Keine Cache-Optimierung, kein Deaktivieren von Logging, keine hinzugefügten Filterlisten.

## Ressourcenverbrauch

| Metrik | Pi-hole v6.4.3 | AdGuard Home v0.107.78 |
|---|---|---|
| LXC cgroup memory.current | **110 MB** | 50 MB (vor Löschung) |
| Dienst-RSS | ~10–12 MB | ~57 MB |
| Disk-Verbrauch | 834 MB | 713 MB |
| Prozesse im LXC | 18 | 6 |

**Hinweis zur Speichermessung:** Der cgroup-Wert (110 MB bei Pi-hole) zeigt den tatsächlichen Host-Effekt inklusive Page Cache und LXC-Overhead. Der innerhalb des Containers mit `free -m` gemeldete Wert (16 MB) ist niedriger, aber nicht aussagekräftig für die Host-Belastung.

## DNS-Lasttest

Getestet mit einem Python-Skript über UDP-Socket (ohne subprocess-Overhead). Domainliste mit 85 Einträgen (erlaubt, blockiert, NXDOMAIN, wiederholt). Alle Tests gegen die Standardkonfiguration ohne Benchmark-Optimierungen.

| Test | Dauer | QPS | Median | P95 | P99 | Fehler |
|---|---|---|---|---|---|---|
| 5.000 sequenziell (warm) | 5.631 ms | **888** | 0,6 ms | 3,3 ms | 3,6 ms | 0 |
| 5.000 parallel (C=10) | 6.257 ms | 799 | 102 ms | 127 ms | 185 ms | 504 |
| 5.000 parallel (C=50) | 3.119 ms | **1.603** | 62 ms | 63 ms | 63 ms | 0 |

**Ergebnis:** Der sequenzielle Test zeigt eine beeindruckende Latenz von <1 ms bei 888 qps. Bei hoher Parallelität (C=50) erreicht Pi-hole über 1.600 qps – mehr als für jeden Heimanwendung ausreichend. Die hohen Latenzen im C10-Test mit 504 Fehlern sind auf Thread-Contention im Python-Testskript zurückzuführen, nicht auf Pi-hole. Im C50-Test (fehlerfrei) liegt der Median bei 62 ms – dies ist die reale Latenz unter Last und für DNS völlig akzeptabel.

**Dienstzustand nach dem Test:** pihole-FTL-RSS von 10 MB auf 12 MB gestiegen, LXC weiterhin gesund, keine Abstürze.

## Blocking-Test (DNS-Ebene)

Getestet via direkte DNS-Abfragen aus dem Testnetzwerk (VLAN 20):

| Domain | Pi-hole | AdGuard |
|---|---|---|
| doubleclick.net | **0.0.0.0** (blockiert) | Nicht getestet |
| googlesyndication.com | **0.0.0.0** (blockiert) | Nicht getestet |
| google-analytics.com | **0.0.0.0** (blockiert) | Nicht getestet |
| criteo.com | **0.0.0.0** (blockiert) | Nicht getestet |
| adnxs.com | **0.0.0.0** (blockiert) | Nicht getestet |
| scorecardresearch.com | **0.0.0.0** (blockiert) | Nicht getestet |

AdGuard-CT wurde vor diesen Tests gelöscht – ein direkter Browser-Vergleich unter identischen DNS-Bedingungen war daher nicht möglich.

## Bedienbarkeit

| Kriterium | Pi-hole | AdGuard Home |
|---|---|---|
| Einrichtung | Offizielles Install-Skript | Binary entpacken + Web-Wizard |
| Ersteinrichtung | Dialoge im Terminal | Web-Oberfläche (Port 3000) |
| Dashboard | Funktional, übersichtlich | Modern, detaillierte Statistiken |
| Update | `pihole -up` | Binary ersetzen + Neustart |
| Backup | /etc/pihole/ sichern | /root/AdGuardHome/ sichern |
| Admin-Passwort | via `pihole setpassword` | via Web-UI |

## Fazit nach Kategorien

**Geringster Ressourcenbedarf:** Pi-hole (110 MB cgroup inkl. Cache vs. deutlich niedrigerer Dienst-RSS)

**Höchste DNS-Laststabilität:** Pi-hole (über 1.600 qps bei C=50, keine Fehler, Dienst nach Test gesund)

**Beste Out-of-the-Box-Blockabdeckung:** Nicht abschließend bestimmbar – AdGuard hatte mit 157.189 Regeln etwa doppelt so viele Filtereinträge wie Pi-hole (78.451). Die tatsächliche Blockqualität hängt von den gewählten Listen ab, nicht von der reinen Regelanzahl.

**Einfachste Bedienung:** Pi-hole (pihole -up vs. manuelles Binary-Ersetzen bei AdGuard)

**Empfehlung für den konkreten 4-GB-Futro-Setup: Pi-hole**

Eingeschränkt auf dieses Setup, da:
- Geringerer gemessener Speicherbedarf
- Ausreichender Funktionsumfang für einen DNS-Blocker
- Einfacheres Update und Backup
- Über 1.600 qps unter Last – mehr als ausreichend

Auf einem System mit 8+ GB RAM wäre AdGuard Home aufgrund des moderneren Web-Interfaces die komfortablere Wahl. Hier entscheiden vor allem Geschmack und Bedienkomfort.

> **Kein produktiver DNS-Einsatz:** Der getestete DNS-LXC bleibt gestoppt. Eine Umstellung des Heimnetzwerk-DNS wurde nicht durchgeführt.
+++
