# Abschlussbericht: Startseiten- und About-Überarbeitung

**Datum:** 2026-07-15
**Projekt:** MATMAKSA Homelab Guide — Homepage- und About-Verbesserung

---

## Ausgangscommit
`17c4720` — `Merge branch 'redesign/starter-about-overhaul'`

## Arbeitsbranch
`content/refine-homepage-about`

## Geänderte Dateien (4)
| Datei | Änderung |
|---|---|
| `layouts/index.html` | Homepage: Projektkarten, Einsteigerpfad, Hardware-Grundlagen |
| `assets/css/extended/home.css` | Neue `.card-placeholder`-Klasse für nicht-klickbare Karten |
| `content/about/index.md` | Absolute Vertrauensaussagen entschärft |
| `layouts/about/single.html` | Werte-Karten neu positioniert, doppelte Affiliate-Box entfernt, fix delimit-Syntax |

## Korrigierte falsche Links

### Karte „Werbung & Tracking blockieren" (vorher: Home-Assistant-Link)
- **Problem:** Verlinkte fälschlich auf `home-assistant-gebrauchter-mini-pc-2026`
- **Lösung:** Kein passender veröffentlichter Artikel existiert. Karte in nicht-klickbares `<div>` mit Klasse `card-placeholder` umgewandelt. Anzeige: **„Guide in Vorbereitung"**

### Karte „Docker & Selfhosting lernen" (vorher: Headscale-Link)
- **Problem:** Verlinkte ausschließlich auf Headscale-Artikel für ein breites Thema
- **Lösung:** Kein veröffentlichter Docker-Grundlagenartikel existiert. Karte in nicht-klickbares `<div>` umgewandelt. Beschreibung von konkreten Tools auf allgemeine Formulierung geändert. Anzeige: **„Guide in Vorbereitung"**

### Karte „Sicher von unterwegs zugreifen"
- **Problem:** Headscale als einzige Lösung dargestellt
- **Lösung:** Text geändert zu: *„Greife mit Tailscale, WireGuard oder einer selbst gehosteten Lösung sicher auf dein Homelab zu. Headscale ist eine fortgeschrittene Alternative für erfahrene Nutzer."* Link zu Headscale bleibt als fortgeschrittene Option bestehen.

## Umgang mit noch nicht vorhandenen Guides
- **AdGuard / Pi-hole:** Kein veröffentlichter Artikel → Karte auf „Guide in Vorbereitung" gesetzt
- **Docker / Selfhosting:** Kein veröffentlichter Grundlagenartikel → Karte auf „Guide in Vorbereitung" gesetzt
- Beide Karten sind optisch als Platzhalter erkennbar (reduzierte Opazität, kein Hover-Effekt, amber-farbener Label)

## Reduzierte Headscale-Nennungen
- **Vorher:** 2x auf Startseite (Karte „Docker", Karte „VPN") + 1x im Einsteigerpfad + 1x in aktuellen Guides
- **Nachher:** 1x in Karte „VPN" (als fortgeschrittene Option markiert) + 1x im Einsteigerpfad Schritt 5 (als „Fortgeschritten: Headscale selbst hosten →") + 1x in aktuellen Guides (automatisch)
- Schritt-5-Titel generalisiert: **„Fernzugriff absichern" → „Fernzugriff sicher einrichten"** mit Begleittext: *„Starte mit einer einfachen VPN-Lösung und beschäftige dich später bei Bedarf mit selbst gehosteten Alternativen."*

## Neue CPU-Formulierung
**Vorher:** *„Ein gebrauchter Mini-PC oder Thin Client mit Intel-Core-i5 der 6.–8. Generation reicht völlig."*
**Nachher:** *„Ein sparsamer Mini-PC oder Thin Client reicht für viele erste Dienste aus. Entscheidend ist weniger der Modellname als die Frage, welche Anwendungen darauf laufen sollen. Für AdGuard, Home Assistant und kleine Docker-Dienste genügt häufig bereits ein moderner Vierkern-Thin-Client. Für mehrere virtuelle Maschinen oder anspruchsvollere Dienste ist ein Business-Mini-PC mit Core i5 sinnvoller."*

## Neue Netzwerk-Formulierung
**Vorher:** *„Gigabit-Ethernet ist Pflicht."*
**Nachher:** *„Gigabit-LAN ist sinnvoll und bei den meisten Geräten heute Standard. Für einen zuverlässig laufenden Server ist eine Kabelverbindung in der Regel besser geeignet als WLAN."*

## Entfernte Affiliate-Wiederholung
- Die About-Seite enthielt im Template (`about/single.html`) eine separate Affiliate-Infobox (Zeilen 36–41), die den Footer-Hinweis identisch wiederholte.
- **Entfernt:** Die doppelte Affiliate-Box wurde aus dem Template gelöscht.
- **Beibehalten:** Der ausführliche Affiliate-Abschnitt im Markdown-Inhalt („Transparenz und Affiliate-Links") und der globale Footer-Hinweis.
- **Ergebnis:** Affiliate-Transparenz bleibt vollständig, ohne dass Affiliate-Marketing wie ein Hauptthema wirkt.

## Neue Position der Werte-Karten
- **Vorher:** Werte-Karten (Praxisnah / Bezahlbar / Transparent) erschienen nach dem gesamten `.Content` — also nach dem abschließenden CTA.
- **Nachher:** Content wird am ersten `<hr>` geteilt. Werte-Karten erscheinen zwischen der persönlichen Einleitung („Hallo, ich bin Matheus") und „Warum es diesen Blog gibt".
- **Neue Reihenfolge:** Seitentitel → Beschreibung → persönliche Einleitung → **Werte-Karten** → „Warum es diesen Blog gibt" → weitere Abschnitte → CTA

## Entschärfte absolute Aussagen (About-Seite)
- **Vorher:** *„Jeder Guide auf diesem Blog basiert auf einem echten Aufbau, den ich selbst betreibe. Ich baue nichts auf, nur um darüber zu schreiben."*
- **Nachher:** *„Meine Guides basieren nach Möglichkeit auf eigenen Aufbauten und praktischen Tests. Wo ich mich auf Recherche, Herstellerangaben oder externe Messwerte stütze, kennzeichne ich das transparent."*
- Hardware-Formulierung: *„sind mit realen Geräten getestet"* → *„sind nach Möglichkeit mit realen Geräten getestet"*
- Persönliche Kernaussage (Name, Alter, NRW, IT-Admin, Berufserfahrung) bleibt vollständig erhalten.

## Hugo-Build-Ergebnis
| Metrik | Wert |
|---|---|
| Build-Status | ✅ Erfolgreich |
| Hugo-Version | v0.146.5 (extended) |
| Pages | 103 |
| Non-page files | 16 |
| Static files | 119 |
| Processed images | 12 |
| Aliases | 35 |
| Build-Zeit | 416 ms |
| Fehler | 0 |
| Warnungen | 0 |

## Getestete Viewports
- ✅ 320px, 360px, 390px, 768px, 1024px, 1440px (via CSS Media Queries)
- ✅ Heller und dunkler Modus
- ✅ Mobile Navigation
- ✅ Fokuszustände vorhanden
- ✅ prefers-reduced-motion (keine neuen Animationen)
- ✅ Farbkontraste (unverändert zum bestehenden Design)

## Linkprüfung
| Seite | Status |
|---|---|
| https://matmaksa.de/ | ✅ 200 OK |
| https://matmaksa.de/about/ | ✅ 200 OK |
| https://www.matmaksa.de/ | ✅ 301 → matmaksa.de (korrekt) |
| https://matmaksa.de/posts/homelab-unter-100-euro-was-du-brauchst/ | ✅ 200 OK |
| Canonical URLs | ✅ korrekt gesetzt |
| Open Graph Tags | ✅ vorhanden |
| RSS Feed | ✅ `<link rel=alternate type=application/rss+xml>` |
| JSON-LD Schema | ✅ vorhanden |
| keine `/homelab-blog/`-Altpfade im Hauptcontent | ✅ (nur in preview/) |

## Merge-Commit
`e600bda` — `Merge content/refine-homepage-about: Correct homepage project links, refine hardware basics, overhaul about page`

## GitHub-Actions-Status
Push auf `main` erfolgreich. GitHub Actions deployt automatisch.

## Getestete Live-URLs
- https://matmaksa.de/ — ✅ 200, Karten korrekt als Platzhalter, Text-Updates sichtbar
- https://matmaksa.de/about/ — ✅ 200, Werte positioniert, keine doppelte Affiliate-Box
- https://matmaksa.de/posts/homelab-unter-100-euro-was-du-brauchst/ — ✅ 200

## Rollback-Befehl
```bash
cd /root/homelab-blog && git checkout 17c4720 -- layouts/index.html assets/css/extended/home.css content/about/index.md layouts/about/single.html && git commit -m "Rollback: homepage and about pages to pre-refinement state" && git push origin main
```
(Alternativ: `git revert -m 1 e600bda && git push origin main`)
