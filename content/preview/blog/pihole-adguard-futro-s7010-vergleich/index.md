+++
title = 'Pi-hole oder AdGuard Home auf dem Futro S7010: Der Praxisvergleich'
description = 'Pi-hole vs. AdGuard Home auf dem Fujitsu Futro S7010 mit 4 GB RAM. Echte Messwerte zu RAM, CPU, DNS-Latenz und Blockabdeckung unter identischen Testbedingungen. cgroup-Speichermessung, dnsperf-Lasttest, Browser-Vergleich.'
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
| Stabilisierung | 5 Minuten vor Messbeginn |

**Standardkonfiguration:** Beide Systeme liefen mit Out-of-the-box-Einstellungen. Keine Cache-Optimierung, kein Deaktivieren von Logging, keine hinzugefügten Filterlisten.

**LXC-Übersicht:**

| Container | CTID | Status | IP |
|-----------|------|--------|----|
| docs-pihole | 100 | gestoppt (behalten) | 192.168.20.12 |
| docs-adguard | 102 | gestoppt (behalten) | 192.168.20.13 |
| docs-dnsclient | 103 | gestoppt (behalten) | 192.168.20.14 |

## Filtermengen

| System | Quelle | Aktive Regeln |
|--------|--------|--------------|
| Pi-hole v6.4.3 | StevenBlack (Standard-Gravity) | ~78.451 |
| AdGuard Home v0.107.78 | AdGuard DNS Filter | ~157.206 |

Die Filtermengen sind **nicht identisch.** AdGuard startet mit etwa doppelt so vielen Regeln. Ein direkter Blockabdeckungs-Vergleich auf Augenhöhe ist daher nicht möglich. `FILTER_COUNTS_COMPARABLE=no`

## Ressourcenverbrauch

### Speichermessung (cgroup)

Drei Messungen im 30-Sekunden-Abstand nach 5 Minuten Stabilisierung. Alle Werte vom Host (PVE04) aus `/sys/fs/cgroup/lxc/{CTID}/` erfasst.

| Metrik | Pi-hole v6.4.3 | AdGuard Home v0.107.78 | Differenz |
|--------|---------------|----------------------|-----------|
| cgroup memory.current | ~110,5 MB | ~117,6 MB | +7 MB |
| anon (Prozesse/RSS) | ~11,2 MB | ~47,3 MB | +36 MB (×4,2) |
| file (Dateicache) | ~92,9 MB | ~65,0 MB | −28 MB |
| Dienst-RSS (ps aux) | ~10,6 MB | ~56,8 MB | +46 MB (×5,4) |

**Einordnung:** Der cgroup-Wert enthält Page Cache und LXC-Overhead. Der **anon-Speicher** zeigt die echte Prozessbelastung: AdGuards Go-Binary belegt ~47 MB, Pi-holes C-basierter pihole-FTL nur ~11 MB. Pi-hole baut mehr Dateicache auf (~93 MB vs. 65 MB), sodass der Gesamteffekt auf dem Host ähnlich ist. Der Dienst-RSS (resident set size) bestätigt: AdGuardHome ist ~5,4× größer als pihole-FTL.

**Host-Effekt auf PVE04:** Verfügbarer RAM von ~2.091 MB fällt bei beiden Systemen um ca. 120–125 MB. Kein signifikanter Unterschied in der Host-Belastung.

## DNS-Lasttest

Testtool: **dnsperf v2.10.0** (Debian 12, offizielles Paket) auf docs-dnsclient (CT103)
Dataset: 500 eindeutige Domains (250 allowed + 95 blocked + 155 NXDOMAIN) im Format `domain A`
SHA256: `e86ec701e0e5e9eadc43f2dc8d059187140b129aa6fb184153498f08ed01d69b`

**Kein selbstgebauter Benchmark, keine Python-Threads.** dnsperf v2.10.0 kann auf Debian 12 maximal ~500 eindeutige Abfragen pro Lauf zuverlässig verarbeiten (Message-ID-Konflikte bei Wiederholungen → REFUSED). Daher zehn sequenzielle Läufe à 500 queries, dazwischen FTL-Neustart. Parallelitätstests (C10/C50) als `not_run` markiert.

### Pi-hole — Sequential Cold Cache (Mittelwert 3 Läufe)

| Metrik | Wert |
|--------|------|
| QPS | **91,0** |
| Ø Latenz | 10,6 ms |
| Min Latenz | 0,43 ms |
| Max Latenz | 385 ms |
| Fehler | 0 |

### AdGuard Home — Sequential Cold Cache (Lauf 1)

| Metrik | Wert |
|--------|------|
| QPS | **43,5** |
| Ø Latenz | 23,0 ms |
| Min Latenz | 0,16 ms |
| Max Latenz | 2.064 ms |
| Fehler | 0 |

### AdGuard Home — Sequential Warm Cache (Läufe 2+3)

| Metrik | Wert |
|--------|------|
| QPS | ~3.666 (Durchschnitt) |
| Ø Latenz | 0,19 ms |
| Min Latenz | 0,13 ms |
| Max Latenz | 7 ms |

**Fazit Lasttest:** Pi-hole ist auf kaltem Cache etwa **doppelt so schnell** (~91 vs. ~43 QPS). AdGuards C++ (Pi-hole) vs. Go (AdGuard) zeigt sich hier deutlich. AdGuards Warm-Cache-Performance ist exzellent (~3.666 QPS), aber für einen Heim-DNS-Blocker sind 43 QPS auf kaltem Cache völlig ausreichend.

## Browser-Adblock-Test

Testtool: Node.js + Playwright v1.61.1 + Chromium (headless) auf docs-dnsclient
Browser: Frisches Profil pro Lauf, kein DoH, keine Extensions, kein Browser-Cache über Läufe hinweg
DNS-Proof: Vor jedem Testlauf per `dig +short` an den Ziel-DNS bestätigt
Vorherige Browser-Tests: `INVALID_BROWSER_TEST_WRONG_DNS=yes` (liefen über Router-DNS)

### adblock.turtlecute.org

| DNS-System | Lauf | Blockiert | Nicht blockiert | Quote |
|-----------|------|-----------|----------------|-------|
| Pi-hole | 1 | 94 | 39 | **70,7 %** |
| AdGuard Home | 1 | 107 | 26 | **80,5 %** |
| AdGuard Home | 2 | 107 | 26 | **80,5 %** |

**AdGuard blockiert 13 zusätzliche Domains,** darunter Amazon S3, Adcolony, LinkedIn, TikTok, Pinterest, YouTube, MouseFlow, LuckyOrange, Hotjar, FreshWorks, Realme und Oppo — alles Tracking-Domains, die Pi-hole mit der reinen Hosts-basierten StevenBlack-Liste nicht erfasst.

**Cosmetic Filtering** ist auf DNS-Ebene nicht möglich und wird nicht bewertet.

### superadblocktest.com

Seite geladen (DNS funktioniert), Scores nicht automatisiert extrahierbar (JavaScript-Interaktion erforderlich). Screenshots zur visuellen Prüfung vorhanden.

## Fairness des Vergleichs

- **Filtermengen:** AdGuard (~157K Regeln) vs. Pi-hole (~78K) — nicht vergleichbar. Der Browsertest zeigt die Out-of-the-box-Realität, nicht die maximale Blockfähigkeit jedes Systems.
- **dnsperf-Limit:** Zehn separate 500er-Läufe simulieren nicht exakt einen einzelnen 5.000er-Durchlauf. Der Neustart zwischen Läufen kann kälteren Cache bewirken.
- **Sprache:** Pi-hole ist in C geschrieben, AdGuard in Go. Go-Binaries haben grundsätzlich einen höheren Speicher-Fußabdruck.

## Fazit nach Kategorien

### Ressourcenbedarf → **Pi-hole**
Anon-Speicher 11 vs. 47 MB, Dienst-RSS 11 vs. 57 MB. Der cgroup-Gesamtwert liegt nah beieinander (110 vs. 118 MB), aber der anon-Unterschied ist auf dem 4-GB-Futro relevant.

### DNS-Laststabilität → **Pi-hole**
Cold Cache QPS 91 vs. 43. Pi-hole verarbeitet sequenzielle Abfragen etwa doppelt so schnell. Beide 0 Fehler bei 500 Abfragen.

### Out-of-the-Box-Blockabdeckung → **AdGuard Home**
80,5 % vs. 70,7 %. Die größere Filterliste blockiert 13 zusätzliche Tracking-Kategorien. Einschränkung: bei identischer Liste wahrscheinlich annähernd gleich.

### Bedienbarkeit → **AdGuard Home**
Moderneres Web-Interface, detailliertere Statistiken, integrierte Filterlisten-Verwaltung. Pi-hole erfordert TOML-Edit für erweiterte Einstellungen.

> Dieser Vergleich bewertet die Out-of-the-box-Konfigurationen auf genau diesem Futro. Er beweist nicht, dass eine Lösung auf jeder Hardware oder mit jeder Filterliste grundsätzlich besser ist.

**Empfehlung für den 4-GB-Futro: Pi-hole** — geringerer Speicherbedarf (anon), schnellere DNS-Verarbeitung, ausreichend für einen reinen DNS-Blocker. AdGuard Home empfiehlt sich bei 8+ GB RAM oder wenn das Web-Interface und die größere Standard-Filterliste gewünscht sind.
