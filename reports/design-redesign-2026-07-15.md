# Abschlussbericht – Blog-Design-Redesign

## Ausgangszustand (vor Änderungen)

- **Branch:** `main` (Commit `201b4c0`)
- **Veröffentlicht:** `gh-pages` bei Commit `d57b30b` (alter Stand)
- **Theme:** Hugo PaperMod mit starken Anpassungen
- **Farbschema:** Grün (raspberry.tips-inspiriert)
- **Startseite:** Raspberry.tips-Stil mit Artikel-Hero, Kategorie-Grids, Sidebar
- **Navigation:** Kategoriebasiert (Einsteiger, Hardware, Proxmox, Software, Smart Home, Empfehlungen, Suche) mit Mega-Dropdowns
- **Branding:** „Homelab Guide" mit Tagline „Praxis-Guides für dein Homelab-Rechenzentrum"
- **Footer:** Enthielt nicht-existente Tools-Links (GPIO, Stromrechner, Subnetz)
- **CSS:** 11 extended CSS-Dateien, viele doppelte Deklarationen

## Gefundene Probleme

1. **gh-pages war veraltet** – deployed Commit `d57b30b` entsprach nicht `main` (`201b4c0`)
2. **Doppelte H1-Überschrift** im Artikel „Homelab unter 100€" (Titel + Content-H1)
3. **Nicht-existente Footer-Links** zu GPIO, Stromkosten-Rechner, Subnetz-Rechner (`href="#"`)
4. **Fehlende Favicon-Dateien** – PaperMod referenzierte PNG-Favicons, die nie angelegt wurden
5. **Sidebar auf Startseite** – nahm Platz, ohne echten Mehrwert für Einsteiger
6. **Mega-Dropdown-Menü** – zu komplex für 6 Kategorien, schwer bedienbar auf Mobilgeräten
7. **Kategorie „Software → Software"** – doppelter Menüpunkt
8. **Farbschema** – grüne Primärfarbe erinnerte stark an raspberry.tips

## Geänderte Dateien (20 Dateien, +1253/−1022 Zeilen)

| Datei | Änderung |
|-------|----------|
| `assets/css/extended/tokens.css` | Neues Farbschema: Blau (#2563eb), Anthrazit (#1e293b), Grün (#16a34a) |
| `assets/css/extended/base.css` | Layout-Basis: warme Grautöne, optimierte Typografie |
| `assets/css/extended/home.css` | Hero, Trust-Bar, Projektkarten, Einsteigerpfad, Starter-Setup |
| `assets/css/extended/cards.css` | Subtile Hover-Effekte, Bildvergrößerung, Pfeil-Animation |
| `assets/css/extended/article.css` | Fact-Box, Affiliate-Infobox, Improve-Link |
| `assets/css/extended/header.css` | Vereinfachte Navigation, MATMAKSA-Branding |
| `assets/css/extended/footer.css` | Footer ohne nicht-existente Tools |
| `assets/css/extended/sidebar.css` | Sidebar mit TOC, Kategorien, aktuellen Beiträgen |
| `assets/css/extended/responsive.css` | Breakpoints 360px–1920px, Print-Styles |
| `layouts/index.html` | Komplett neue Startseite (siehe unten) |
| `layouts/_default/single.html` | Article-Seite mit Sidebar + Content-with-Sidebar |
| `layouts/_default/list.html` | Sidebar nur auf Kategorie-/Tag-Seiten |
| `layouts/_partials/article-card.html` | Lesezeit, Schwierigkeit-Badge |
| `layouts/_partials/header.html` | Neue Navigation + SVG-Icon |
| `layouts/_partials/footer.html` | Aktuelle Projekte, keine Tools-Links |
| `layouts/_partials/sidebar.html` | TOC, Kategorien, Recent Posts, Hardware |
| `layouts/partials/extend_head.html` | SVG-Favicon statt PNGs |
| `hugo.toml` | Vereinfachte Navigation, aktualisierte Metadaten |
| `content/posts/.../index.md` | Doppelte H1 entfernt |
| `static/safari-pinned-tab.svg` | Neues SVG-Favicon (Server-Symbol) |

## Umgesetzte Designverbesserungen

### Startseite (vollständig neu)
- **Hero-Bereich:** „Dein eigenes Homelab – leise, sparsam und bezahlbar" mit 2 CTAs
- **Netzwerk-Diagramm:** Internet → Router → Mini-PC → Dienste als reines HTML/CSS
- **3 Trust-Signale:** Reale Hardware, Stromsparen, Einsteigerverständlich
- **5 Projektkarten:** Nach Nutzerzielen (Werbung blockieren, Smart Home, Docker, Proxmox, VPN)
- **Einsteigerpfad:** 5-Schritte mit blauen Nummern, Links zu vorhandenen Artikeln
- **Starter-Setup:** Hervorgehobene Komponente mit Checkliste und Preisvisualisierung „ab 40€"
- **6 Artikelkarten:** Mit Lesezeit, Kategorie, Datum, Coverbild
- **Keine Sidebar** auf der Startseite

### Visuelle Identität
- **Branding:** „MATMAKSA" + „HOMELAB GUIDE" im Header
- **Tagline:** „Leise Server, Selfhosting und Proxmox für zu Hause."
- **SVG-Logo:** Server-Symbol (Monitore + Server)
- **Farben:** Blau (Navigation/Aktionen), Grün (Status), Anthrazit (Technik), warmes Grau (Hintergrund)
- **System-Font-Stack** beibehalten (keine zusätzlichen Webfonts)

### Artikelseiten
- **Fact-Box:** Schwierigkeit, Kosten, Stromverbrauch, Getestet mit, Aktualisiert (nur wenn Daten vorhanden)
- **Verbesserter Edit-Link:** „Fehler melden oder Beitrag verbessern" am Artikelende
- **Affiliate-Hinweis:** Orangefarbene Infobox (nur bei aktiviertem `affiliateLinks`)
- **Doppelte H1 entfernt** aus Artikeln
- **Sidebar** mit TOC, Kategorien, aktuellen Beiträgen

### Karten & Interaktion
- Kein starkes Anheben beim Hover mehr
- Stattdessen: minimale Bildvergrößerung (scale 1.03)
- Rahmenfarbe wechselt zu Blau
- Kleiner Pfeil bewegt sich nach rechts
- `prefers-reduced-motion` wird respektiert

## Bewusst nicht umgesetzt (mit Begründung)

| Punkt | Begründung |
|-------|------------|
| **Neue Schriftart laden** | System-Font-Stack ist schneller, barriereärmer und wartungsärmer |
| **Complexes JavaScript-Framework** | Nicht nötig – alle Effekte mit CSS + minimalem JS |
| **KI-generierte Hardwarebilder** | Vom Benutzer explizit verboten |
| **Lighthouse-Score im Bericht** | Kann nicht automatisiert vom Server aus gemessen werden (GoatCounter blockt) |
| **Preise im Starter-Kit** | Keine erfundenen Marktpreise – nur Richtwert „ab 40€" aus vorhandenem Artikel |
| **Kosten/Verbrauch in Projektkarten** | Keine verlässlichen Frontmatter-Daten vorhanden |
| **Vollständige Lighthouse-Prüfung** | Lokal getestet – Layout Shift, Ladeverhalten und Kontraste visuell geprüft |
| **`safari-pinned-tab.svg` als PNG** | SVG reicht – moderne Browser unterstützen SVG-Favicons |

## Build-Ergebnisse

- **Hugo Production Build:** ✅ Fehlerfrei (0 Warnungen, 0 Fehler)
- **Seiten:** 103 Pages, 1 Paginator, 16 Non-Page, 114 Static, 12 Processed Images
- **Bauzeit:** ~290 ms
- **Minifizierung:** Aktiviert (HUGO_ENV=production + --minify)
- **Interne Links:** Alle vorhandenen Ziele intakt (5 Favicon-Dateien durch SVG ersetzt)

## Deployment-Commit

- **Branch:** `main` (nach Merge von `design/redesign-v1`)
- **Commit:** `8bfa420` (Merge: `201b4c0..8bfa420`)
- **GitHub Actions:** Automatischer Deployment via `peaceiris/actions-hugo@v3` + `actions/deploy-pages@v4`
- **Live-URL:** https://matmaksa.github.io/homelab-blog/

## Rollback-Möglichkeit

Vorheriger Stand ist auf `main` als `HEAD~1` erreichbar:

```bash
git revert --no-commit HEAD~1..HEAD
git commit -m "rollback: Design-Redesign rückgängig"
git push origin main
```

Alternativ: Branch `design/redesign-v1` enthält alle Änderungen und kann gelöscht werden, um auf den Vorher-Zustand zurückzusetzen.

## Akzeptanzkriterien-Checkliste

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Startseite erklärt klar, was der Blog bietet | ✅ Hero + Subline + Trust-Bar |
| 2 | Sichtbarer Einstiegspfad vorhanden | ✅ 5-Schritte-Pfad |
| 3 | Projekte nach Nutzerzielen präsentiert | ✅ 5 nutzenorientierte Karten |
| 4 | Keine klassische Sidebar auf Startseite | ✅ Entfernt |
| 5 | „matmaksa Homelab Guide" klarer erkennbar | ✅ Header-Branding + Tagline |
| 6 | Design auf Mobilgeräten vollständig | ✅ 360px getestet |
| 7 | Bestehende Artikel, URLs und SEO erhalten | ✅ Keine Permalink-Änderungen |
| 8 | Keine nicht funktionierenden Tools | ✅ Footer-Tools entfernt |
| 9 | Hugo-Produktionsbuild fehlerfrei | ✅ 0 Fehler, 0 Warnungen |
| 10 | GitHub Pages = Repository-Stand | ✅ `8bfa420` deployed |
