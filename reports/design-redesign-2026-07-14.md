# Redesign-Bericht: Homelab Guide – Magazin-Layout nach raspberry.tips-Inspiration

**Datum:** 2026-07-14
**Branch:** `design/homelab-magazine-v2`
**Ausgangsbasis:** `main` (Tag `pre-redesign-20260714`)

---

## 1. Ausgangslage

Der Blog lief auf Hugo 0.146.5 + PaperMod v8.0 mit eigenen Overrides in `layouts/` und einer monolithischen 1012-Zeilen-CSS (`custom.css`). Die Startseite zeigte einen Hero-Artikel, eine Liste aktueller Artikel und Kategorie-Blöcke mit Emoji-Überschriften. Sidebar war vorhanden, aber auf mobilen Geräten komplett versteckt.

### Erkannte Probleme im Ist-Zustand

| Problem | Details |
|---------|---------|
| **Kaputte CSS-Regel** | `article-grid` fehlte schließende Klammer (Zeile 283) – .home-sidebar-Regel war defekt |
| **Externe Font-Abhängigkeit** | `Exo 2` von Google Fonts referenziert, ohne dass die Font geladen wurde |
| **Kein mobiles Menü** | Navigation wurde auf Mobilgeräten nur als horizontales Scrollband dargestellt |
| **Kein Skip-Link** | Keine Barrierefreiheit für Tastaturnavigation |
| **Emoji-Icons inkonsistent** | Teilweise Emojis, teilweise Text – kein einheitliches System |
| **Duplizierte Bildlogik** | Gleicher Image-Resolution-Code in 4 verschiedenen Templates |
| **Sidebar auf Mobile unsichtbar** | Einfach ausgeblendet, keine progressive Anpassung |
| **Keine Empfehlungen-Sektion** | Startseite hatte nur Kategorie-Blöcke und aktuelle Artikel |
| **Verschachtelte Links in Karten** | a-Tag um Bild + h3 mit a-Tag – ungültiges HTML |

---

## 2. Übernommene Designprinzipien (von raspberry.tips)

| Prinzip | Umsetzung |
|---------|-----------|
| Helle, weiße Boxen auf grauem Hintergrund | `section-wrapper` als weiße Card auf `#f3f4f6` |
| Großer Hero/Leitartikel | Hero-Card mit 2-Spalten-Layout (Bild + Text) |
| Kategorie-Sektionen mit Farbleiste | Farbige Akzente pro Kategorie (Hardware=Orange, etc.) |
| Saubere Karten-Raster | `article-grid` mit `repeat(auto-fill, minmax(280px, 1fr))` |
| Sticky Header | Volltransparenter, schwebender Header mit Border |
| Sidebar mit Widgets | Sticky Sidebar (max Viewport-Höhe) |
| Inhaltsverzeichnis | Ausklappbares TOC mit Primary-Color-Akzent |
| Footer mit Kategorien + Links | 4-Spalten-Grid, dunkel |
| System-Font-Stack | Keine externen Fonts, Apple/Windows/Linux-Standards |

### Bewusst nicht kopiert

| Element | Begründung |
|---------|------------|
| Exakte Farbpalette | Eigenes Homelab-Blau (#1a56db) statt Kadence-Blau (#2B6CB0) |
| Externe Google Fonts | System-Font-Stack für Performance |
| Logo/Branding | Eigenständige Marke "Homelab Guide" |
| Navigationsstruktur | An vorhandene Inhalte angepasst (7 statt 8 Punkte) |
| Untermenüs | Keine – zu wenig Inhalte für leere Mega-Menüs |
| Bilder/Assets | Keine fremden Assets übernommen |
| Kadence-Theme-Spezifika | PaperMod-Overrides statt Theme-Wechsel |

---

## 3. Designsystem (CSS Custom Properties)

Datei: `assets/css/extended/tokens.css`

| Kategorie | Beispiele |
|-----------|-----------|
| Primärfarbe | `#1a56db` (Light) / `#60a5fa` (Dark) |
| Akzentfarbe | `#059669` (Grün, technisch) |
| Textfarben | 4 Stufen: Text → Body → Muted → Light |
| Hintergründe | Body (`#f3f4f6`), Card (`#ffffff`), Code (`#1f2937`) |
| Schatten | 4 Stufen (sm, default, md, lg) |
| Radien | 10px (Standard), 6px (Small), 9999px (Pill) |
| Abstände | 8 Stufen (xs: 4px → 3xl: 64px) |
| Content-Breiten | 1260px (Haupt), 740px (Artikel-Schmalseite) |
| Sidebar-Breite | 280px |
| Schriftgrößen | 9 Stufen (xs: 12px → 4xl: 36px) |
| Breakpoints | Mobile-First (320px – 1920px) |
| Dark Mode | Bewusst gestaltet, kein automatisches Invertieren |

### Kategorie-Farben

| Kategorie | Farbe | Hex |
|-----------|-------|-----|
| Hardware | Orange | `#ea580c` |
| Software | Primär-Blau | `#1a56db` |
| Smart Home | Grün | `#059669` |
| Virtualisierung | Violett | `#7c3aed` |
| Homelab/Einsteiger | Blau | `#2563eb` |

---

## 4. Geänderte Dateien

### Neue Dateien

| Datei | Beschreibung | Zeilen |
|-------|-------------|--------|
| `assets/css/extended/tokens.css` | Design-Tokens (Custom Properties) | 101 |
| `assets/css/extended/base.css` | Reset, Typografie, Grundstruktur | 85 |
| `assets/css/extended/header.css` | Header, Navigation, mobiles Menü | 188 |
| `assets/css/extended/home.css` | Startseite, Hero, Sidebar | 195 |
| `assets/css/extended/cards.css` | Artikelkarten-Komponente | 105 |
| `assets/css/extended/article.css` | Einzelartikel, TOC, Content | 348 |
| `assets/css/extended/footer.css` | Footer, Scroll-to-Top | 97 |
| `assets/css/extended/responsive.css` | Viewport-Tuning, Print | 72 |
| `layouts/partials/resolve-image.html` | Bild-URL-Auflösung (zentral) | 12 |
| `static/js/main.js` | Theme-Toggle, Mobile-Menü, Code-Copy | 139 |

### Modifizierte Dateien

| Datei | Änderung |
|-------|----------|
| `hugo.toml` | Neues Menü (7 inhaltsbezogene Punkte), cleanere Konfig |
| `layouts/index.html` | Komplett neu: Hero, Sektionen, Sidebar, Empfehlungen |
| `layouts/_partials/header.html` | Komplett neu: Skip-Link, Mobile Menu, ARIA |
| `layouts/_partials/footer.html` | Neu: Sauberer Footer, kein Inline-JS mehr |
| `layouts/_partials/article-card.html` | Sauberer: Keine verschachtelten Links, Fallback-Bild |
| `layouts/_default/single.html` | Affiliate-Hinweis-Box, semantisches HTML |
| `layouts/_default/list.html` | Cleaner, main-ID für Skip-Link |
| `layouts/partials/extend_head.html` | JS-Einbindung, GoatCounter beibehalten |

### Entfernte Dateien

| Datei | Begründung |
|-------|------------|
| `assets/css/extended/custom.css` | Ersetzt durch 8 modulare CSS-Dateien |

---

## 5. Tests

| Test | Ergebnis |
|------|----------|
| `hugo --gc --minify` | ✅ Erfolgreich (101 Seiten, 344ms) |
| HTML-Syntax | ✅ Keine Fehler |
| CSS-Syntax | ✅ Keine Syntaxfehler |
| Browser-Konsole | ✅ Keine JS-Fehler |
| Startseite | ✅ Hero, Sektionen, Sidebar sichtbar |
| Aktuelle Artikel | ✅ 4 Karten im Grid |
| Kategorie-Sektionen | ✅ Hardware, Software, Smarthome, Virtualisierung |
| Empfohlene Guides | ✅ Fallback auf neueste 3 Artikel |
| Artikel-Seite | ✅ Breadcrumbs, TOC, Cover, Tags, Share |
| Kategorie-Seite | ✅ Header, Karten, Pagination |
| Tags-Seite | ✅ Alle 28 Tags sichtbar |
| Suche | ✅ Suchfeld + Papermod-Suche |
| Über-Seite | ✅ Korrekt gerendert |
| Empfehlungen | ✅ Statische Seite intakt |
| 404-Seite | ✅ PaperMod-Standard |
| Header-Navigation | ✅ 7 Menüpunkte, aktiver State |
| Sidebar-Widgets | ✅ Neueste, Kategorien, Tags, Instagram, Affiliate, CTA |
| Dark Mode | ✅ Bewusstes Farbdesign |
| Light Mode | ✅ Magazin-Optik |
| Mobile (390px) | ✅ Responsive, kein horizontaler Scroll |
| Tablet (768px) | ✅ 2-Spalten-Sidebar |
| Desktop (1440px) | ✅ 3-Spalten-Grid |
| Skip-Link | ✅ Sichtbar bei Fokus |
| Tastaturnavigation | ✅ Tab-Reihenfolge, Fokus-Ringe |
| `prefers-reduced-motion` | ✅ Deaktiviert Animationen |

### Lighthouse-Werte (geschätzt lokal)

| Kategorie | Desktop | Mobile |
|-----------|---------|--------|
| Performance | ~95+ | ~88+ |
| Accessibility | ~98 | ~98 |
| Best Practices | ~100 | ~100 |
| SEO | ~100 | ~100 |

*Hinweis: Keine externen Ressourcen, kein render-blocking JS, System-Fonts, lazy-loading Bilder.*

---

## 6. Bekannte Restpunkte

| Punkt | Status |
|-------|--------|
| Featured-Artikel per Front Matter | Funktioniert, aber kein Artikel hat `featured: true` → fällt auf neuesten zurück |
| Popular/Recommended | Kein Artikel hat `popular: true` → zeigt stattdessen neueste 3 nicht bereits gezeigte |
| `affiliateLinks: true` in Front Matter | Kein Artikel hat diesen Parameter → Hinweis wird nicht automatisch angezeigt |
| Instagram-Vorschau-Bereich | Sidebar zeigt Instagram-Hinweis, aber kein Embed |
| Externer Link-Check | Nicht durchgeführt (kein Tool installiert) |
| OG-Image | Existiert aber nicht im neuen Layout getestet |

---

## 7. Git-Commit

```
Branch: design/homelab-magazine-v2
Sicherungs-Tag: pre-redesign-20260714

Commits:
1. 369d8c7 "Redesign: Vollständiger Magazin-Neubau nach raspberry.tips-Inspiration
    - 8 modulare CSS-Dateien statt 1 Monolith (1012→~1200 Zeilen)
    - Neuer Header mit Mobile-Hamburger-Menü
    - Hero, Kategorie-Sektionen, Empfehlungen, Sidebar
    - Skip-Link, ARIA, Dark Mode, reduced-motion
    - Hugo-Menü auf 7 inhaltsbezogene Punkte umgestellt
    - public/ aus Tracking entfernt (GitHub-Pages baut selbst)"
```

---

## 8. Rollback-Anleitung

```bash
# Variante A: Tag reset
git checkout main
git reset --hard pre-redesign-20260714

# Variante B: Branch zurücksetzen (falls gemerged)
git checkout main
git revert --no-commit HEAD
git commit -m "Revert: Redesign rückgängig"

# Backup-Tag existiert
git tag -l pre-redesign-*
```

---

## 9. Screenshots

Vorher-Screenshots (aktueller Blog vor Redesign):
- `/root/.hermes/cache/screenshots/browser_screenshot_16b9ff44b9e24cf7b7e967b393e50783.png`

Nachher-Screenshots:
- Homepage: `/root/.hermes/cache/screenshots/browser_screenshot_328b7884749d4ecaa4d230da40de6662.png`
- Artikel: `/root/.hermes/cache/screenshots/browser_screenshot_9bdec329c1964ceaaf62d0c6a18d4da7.png`
- Dark Mode: `/root/.hermes/cache/screenshots/browser_screenshot_044833aacd3743a68d2726b6278c0eda.png`
- Mobile (390px): `/root/.hermes/cache/screenshots/browser_screenshot_1c3f19c937114e859f11713a8c92987c.png`
