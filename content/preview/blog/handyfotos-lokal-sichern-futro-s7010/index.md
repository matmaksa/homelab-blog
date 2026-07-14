+++
title = 'Handyfotos lokal sichern: Reicht ein Futro S7010 mit 4 GB RAM?'
description = 'Handyfotos lokal sichern mit dem Futro S7010: Nextcloud, Syncthing oder Immich? Was mit 4 GB RAM wirklich geht – und wo Schluss ist.'
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
risk_level = "medium"
+++

## Kurze Antwort

**Nein, mit 4 GB RAM und 64 GB SSD nicht als dauerhafte Lösung.** Der Futro S7010 kann als Testplattform dienen, aber für den produktiven Betrieb eines Foto-Backups fehlen Ressourcen.

## Die Ausgangslage

- 4 GB RAM (3,6 GiB nutzbar)
- 64 GB SSD (davon ~18 GB frei)
- Proxmox-Host braucht ~1,3 GB
- Verbleiben ~2,2 GB für Gäste

Eine Foto-Backup-Lösung braucht nicht nur RAM, sondern vor allem **Speicherplatz**. Die 64-GB-SSD reicht für ein paar Handyfotos, aber nicht für dauerhafte Sicherungen.

## Optionen im Vergleich

### Nextcloud – die vielseitige Lösung

- **Offizielle Apps** für Android und iOS mit automatischem Fotoupload
- **Ressourcenbedarf:** Höher (PHP, MariaDB/PostgreSQL, Redis)
- **Auf 4 GB:** Nur eingeschränkter **Testbetrieb** möglich
- **Empfohlen ab:** 8 GB RAM + separates Datenlaufwerk

**Voraussetzungen für späteren Betrieb:**
- Mindestens 8 GB RAM
- Separates primäres Datenlaufwerk (nicht die Backup-HDD)
- HTTPS-Verschlüsselung
- Zwei-Faktor-Authentifizierung
- Backup- und Restore-Konzept

### Syncthing – leicht, aber mit Einschränkung

- **Android:** Offizielle App, zuverlässiger automatischer Sync
- **iOS:** **Kein offizieller Client** – nur Drittanbieter-Apps
- iOS-Hintergrundbeschränkungen verhindern zuverlässigen automatischen Upload
- **Fazit:** Keine gleichwertige iOS-/Android-Empfehlung möglich
- Ressourcentechnisch auf dem Futro machbar

### Immich – nicht empfohlen

- Machine-Learning-Komponenten (Gesichtserkennung, Objekterkennung)
- Offizielle Mindestanforderungen: 4+ Kerne, 8+ GB RAM empfohlen
- **Nicht geeignet** für den Futro S7010 im Kaufzustand
- Auch mit 8 GB RAM auf diesem Prozessor kein optimales System

## Notwendige Infrastruktur

> **Drei Grundregeln für Foto-Backups:**
> 1. **Separates Datenlaufwerk** – die 64-GB-SSD oder die Backup-USB-HDD allein reichen nicht
> 2. **Backup-HDD bleibt Backup** – Originalfotos und einziges Backup niemals auf derselben HDD
> 3. **RAM-Upgrade auf 8 GB** vor produktiver Nextcloud-Inbetriebnahme

## Externer Zugriff (später, nicht in dieser Konfiguration)

**Variante 1 – VPN (empfohlen für Einsteiger):**
- Keine öffentliche Nextcloud-Freigabe nötig
- Geringere Angriffsfläche
- Je nach VPN-Lösung kein DynDNS oder Reverse Proxy erforderlich
- Ideal für den Einstieg

**Variante 2 – Öffentliche Webfreigabe (fortgeschritten):**
- DynDNS (z. B. DuckDNS, IPv64)
- Reverse Proxy (z. B. Nginx Proxy Manager)
- TLS-Zertifikat
- Portweiterleitung
- Regelmäßige Updates, 2FA, Rate Limiting
- Deutlich höherer Betriebs- und Sicherheitsaufwand

## Upgrade-Pfad

1. **Jetzt:** Konzept erstellen, keine Installation
2. **Nächster Schritt:** 8 GB RAM nachrüsten (~15–20 Euro)
3. **Danach:** Separates Datenlaufwerk anschließen
4. **Dann:** Nextcloud-Testinstanz mit Backup-Konzept
5. **Später:** Externen Zugriff via VPN realisieren

## Fazit

Der Futro S7010 mit 4 GB RAM **kann** als Testplattform für Nextcloud dienen, ist aber **kein produktives Foto-Backup-System**. Wer Handyfotos lokal sichern will, sollte mindestens **8 GB RAM** und ein **separates Datenlaufwerk** einplanen. Syncthing ist eine leichte Alternative – aber nur für Android-Nutzer.
+++
