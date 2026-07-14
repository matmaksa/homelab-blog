+++
title = 'Pi-hole oder AdGuard Home auf einem Futro S7010: Was läuft mit 256 MB RAM?'
description = 'Pi-hole und AdGuard Home im Vergleich auf dem Fujitsu Futro S7010 mit 4 GB RAM. Getestet mit 256 und 512 MB – echte Messwerte zu Speicher, DNS-Latenz, WebUI und Blockabdeckung.'
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

## 1. Einleitung

Der Fujitsu Futro S7010 ist ein typisches Einsteiger-System fürs Homelab. Gebraucht oft für etwa 40 Euro zu haben, mit 4 GB RAM und einer 64-GB-SSD im Kaufzustand – kein High-End-Server, aber eine solide Basis für erste Gehversuche mit Proxmox und kleinen Diensten.

Was ist mit so einem schmalen System realistisch möglich? Welche DNS-Werbeblocker laufen darauf stabil? Und reichen 256 MB RAM für einen LXC-Container mit Pi-hole oder AdGuard Home, oder muss es mehr sein?

Dieser Test vergleicht Pi-hole v6.4.3 und AdGuard Home v0.107.78 unter identischen Bedingungen auf einem Futro S7010 – mit 512 MB und mit 256 MB RAM. Ziel ist nicht, einen allgemeingültigen Sieger zu küren, sondern eine datenbasierte Orientierung für Einsteiger mit schmalem Budget zu geben.

## 2. Testaufbau

**Hardware:** Fujitsu Futro S7010 mit 4 GB DDR3-RAM, 64-GB-SSD und Proxmox VE 9.2.4 als Standalone-Host. Eine USB-HDD dient als separates Backup-Ziel.

Beide DNS-Systeme liefen in vergleichbaren Debian-12-LXC-Containern:

| Parameter | Wert |
|---|---|
| LXC-Basis | Debian 12 Bookworm |
| CPU | 1 vCore |
| Disk | 4 GB (thin) |
| Swap | Kein |
| Netzwerk | VLAN 20, statische IP |
| Upstream DNS | Cloudflare (1.1.1.1) + Google (8.8.8.8) |

Getestet wurde mit zwei RAM-Profilen: 512 MB und 256 MB. Der DNS-Lasttest nutzte 1.000 Abfragen bei 10 Queries pro Sekunde (dnsperf v2.10.0). Die WebUI wurde mit Playwright + Chromium geprüft.

Es fand keine produktive Routerumstellung statt – die Container blieben im isolierten Lab-Netz.

## 3. Pi-hole und AdGuard Home kurz erklärt

Beide Systeme sind DNS-Werbeblocker: Sie filtern unerwünschte Domains auf DNS-Ebene heraus, bevor Werbung oder Tracker den Browser erreichen.

**Gemeinsamkeiten:** Beide laufen als lokaler DNS-Server, blockieren Domains anhand von Filterlisten und bieten eine Weboberfläche zur Verwaltung.

**Unterschiede:** Pi-hole setzt auf eine schlanke C-Binary (pihole-FTL) und eine übersichtliche, minimalistische Oberfläche. AdGuard Home ist in Go geschrieben, bietet ein moderneres Web-Interface mit mehr integrierten Einstellungen und bringt eine größere Standard-Filterliste mit.

## 4. Speicherverbrauch

Der Speicherverbrauch wurde per cgroup erfasst (`memory.current`). Dieser Wert umfasst den gesamten vom LXC allokierten Speicher – Prozesse, Dateicache und Kernel-Overhead. Der Dateicache kann vom Host bei Bedarf freigegeben werden, zählt aber zum cgroup-Verbrauch.

| System | RAM-Profil | cgroup Peak | Gast-Reserve |
|---|---|---|---|
| Pi-hole v6.4.3 | 512 MB | ~113,4 MB | 96,1 % |
| Pi-hole v6.4.3 | 256 MB | ~114,1 MB | 91,8 % |
| AdGuard Home v0.107.78 | 512 MB | ~117,7 MB | 89,8 % |
| AdGuard Home v0.107.78 | 256 MB | ~119,5 MB | 79,7 % |

Pi-hole hat einen geringeren tatsächlichen Prozessspeicher (anon: ~11 MB vs. ~47 MB bei AdGuard). Der cgroup-Gesamtwert liegt jedoch nah beieinander, weil Pi-hole mehr Dateicache aufbaut. Auf dem Host sind beide Belastungen praktisch identisch.

## 5. DNS-Antwortzeiten

Der Latenztest nutzte 1.000 DNS-Abfragen bei begrenzten 10 Queries pro Sekunde – eine realistischere Last für ein Heimnetz als ein maximaler Durchsatztest.

| System | RAM | Ø Antwortzeit | Min | Max | Fehler |
|---|---|---|---|---|---|
| Pi-hole v6.4.3 | 512 MB | 1,53 ms | 0,32 ms | 29,94 ms | 0 |
| Pi-hole v6.4.3 | 256 MB | 1,54 ms | 0,30 ms | 29,83 ms | 0 |
| AdGuard Home v0.107.78 | 512 MB | 3,03 ms | 0,48 ms | 106,25 ms | 0 |
| AdGuard Home v0.107.78 | 256 MB | 3,15 ms | — | — | 0 |

Pi-hole war in diesem Test etwa doppelt so schnell wie AdGuard Home – ein Unterschied, der sich durch die unterschiedlichen Programmiersprachen (C vs. Go) und Architekturen erklären lässt.

**Einordnung:** Im praktischen Heimnetzbetrieb sind beide Werte schnell. Der Unterschied zwischen 1,5 ms und 3,0 ms ist für einen menschlichen Nutzer nicht spürbar. AdGuards höhere Max-Latenz (~106 ms) deutet auf Go-Garbage-Collection-Pausen hin, bleibt aber weit unter jeder kritischen Schwelle.

Es gibt keinen allgemeinen Performance-Sieger – die Unterschiede sind im Heimnetz praktisch egal.

## 6. Funktionieren 256 MB wirklich?

Kurze Antwort: Ja. Beide Systeme liefen im Test mit 256 MB RAM vollständig und stabil.

| Kriterium | Pi-hole 256 MB | AdGuard 256 MB |
|---|---|---|
| DNS-Test (1.000 Queries) | ✅ bestanden | ✅ bestanden |
| WebUI | ✅ bestanden | ✅ bestanden |
| Filterupdate | ✅ bestanden | ✅ bestanden |
| Neustart | ✅ bestanden | ✅ bestanden |
| OOM-Ereignisse | 0 | 0 |

Die cgroup-Reserve lag bei Pi-hole bei 55,5 %, bei AdGuard bei 53,3 %. Das ist ausreichend, aber nicht üppig. Die Gast-Reserve (MemAvailable im Container) betrug bei Pi-hole 91,8 % und bei AdGuard 79,7 %.

Für den reinen DNS-Betrieb mit den getesteten Filterlisten waren 256 MB in beiden Fällen ausreichend.

## 7. WebUI und Bedienung

Mit 256 MB RAM wurden beide Weboberflächen getestet und waren vollständig nutzbar:

**Pi-hole:** Dashboard, Query Log, Adlists, Settings – alle Seiten geladen. Median der Ladezeiten bei etwa 251 ms. Kein Login erforderlich (kein Passwort gesetzt). Die Oberfläche ist übersichtlich und schlank gehalten.

**AdGuard Home:** Dashboard, Query Log, Filterverwaltung, DNS Settings – alle Seiten nach erfolgreichem Login geladen. Median bei etwa 278 ms. Das Interface wirkt moderner und bietet mehr integrierte Einstellungen direkt sichtbar.

*Hinweis: Die Bewertung der Bedienbarkeit ist eine subjektive Einschätzung, kein objektiver Messwert.*

## 8. Out-of-the-Box-Blockabdeckung

Der Browser-Werbeblocktest über adblock.turtlecute.org zeigte:

| System | Blockiert | Quote |
|---|---|---|
| Pi-hole | 94 von 133 | ~70,7 % |
| AdGuard Home | 107 von 133 | ~80,5 % |

**Wichtige Einschränkung:** Die Filtermengen sind nicht direkt vergleichbar. Pi-hole nutzte die StevenBlack-Liste (~78.451 Regeln), AdGuard Home den AdGuard DNS Filter (~157.206 Regeln) – etwa doppelt so viele. Der Blockabdeckungs-Unterschied ist daher nicht auf die Software, sondern maßgeblich auf die unterschiedlichen Filterlisten zurückzuführen.

Zudem ist zu beachten: Cosmetic Filtering (Ausblenden von Werbeplätzen auf Webseiten) ist keine DNS-Funktion und wurde nicht bewertet.

Es lässt sich aus diesen Werten kein allgemeiner Qualitäts- oder Performance-Sieger ableiten.

## 9. Welche Lösung passt zum Futro?

Für den konkreten 4-GB-Futro S7010 spricht einiges für Pi-hole: geringerer Prozessspeicher, schnellere DNS-Verarbeitung, ausreichender Funktionsumfang für einen reinen DNS-Blocker.

AdGuard Home ist die bessere Wahl, wenn die modernere Oberfläche und die integrierte Filterlisten-Verwaltung wichtiger sind als der minimale Speichervorteil.

Technisch sind beide Systeme für den Futro S7010 geeignet.

## 10. 256 oder 512 MB?

Der Test hat gezeigt: Beide Systeme arbeiten mit 256 MB RAM zuverlässig – DNS, WebUI, Filterupdate und Neustart waren in allen Fällen erfolgreich, ohne OOM-Ereignisse.

Für Pi-hole liegt das 256-MB-Profil unter der offiziellen Speicherempfehlung (die 512 MB vorsieht). Es hat im Test dennoch funktioniert.

**Meine Empfehlung:** 256 MB sind ein getestetes Sparprofil, das funktioniert. Für den dauerhaften Betrieb würde ich dennoch 512 MB zuweisen – wegen Updates, potenziell größerer Filterlisten und zukünftiger Versionen, die mehr Speicher benötigen könnten.

## 11. Realistisches Futro-Profil

Ein Futro S7010 im Kaufzustand (4 GB RAM, 64 GB SSD) kann realistisch betreiben:

- Proxmox VE (benötigt ~1,3 GB RAM)
- **einen DNS-LXC** (Pi-hole oder AdGuard, 256–512 MB RAM)
- einen kleinen zusätzlichen Test-LXC (z. B. ein Monitoring-Tool)
- USB-HDD als Backup-Ziel

Was nicht sinnvoll ist: mehrere VMs, KI-/Ollama-Dienste, Medien-Server oder Cloud-Anwendungen. Dafür fehlen schlicht RAM und CPU-Leistung im Kaufzustand.

## 12. Fazit

Pi-hole und AdGuard Home liefen auf dem Futro S7010 im Test selbst mit 256 MB RAM vollständig – einschließlich WebUI, Filterupdate und Neustart. Für einen dauerhaften Betrieb würde ich trotzdem 512 MB zuweisen. Pi-hole war in diesem Aufbau die schlankere Lösung, während AdGuard Home mit modernerer Bedienung und einer größeren Standardfilterliste überzeugte.

**Wichtige Einschränkung:** Die Ergebnisse gelten für die getesteten Versionen, Filterlisten und den verwendeten Futro S7010. Sie sind kein allgemeiner Beweis, dass eine Lösung in jeder Umgebung schneller oder sparsamer ist.
