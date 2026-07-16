+++
title = "Preview: Lesbarkeitsverbesserungen"
description = "Zentrale Übersicht aller Preview-Inhalte mit Lesbarkeitsverbesserungen"
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
+++

<div class="preview-overview">

## 🖋️ Redaktionelle Überarbeitungen

Diese Preview-Entwürfe enthalten **redaktionelle Verbesserungen** der existierenden Blog-Artikel – erstellt mit `anthropic/claude-sonnet-4-6`. Keine öffentlichen Artikel wurden verändert.

<div class="preview-meta">
  <strong>Modell:</strong> Claude Sonnet 4.6 &nbsp;·&nbsp;
  <strong>Status:</strong> ⚠️ Preview – nicht öffentlich &nbsp;·&nbsp;
  <strong>Nächster Schritt:</strong> Deine visuelle Freigabe
</div>

| Seite | Status | Wichtigste Änderungen |
|-------|--------|----------------------|
| **<a href="/preview/blog/homelab-unter-100-euro/">🖥️ Homelab unter 100€</a>** | ✅ überarbeitet | 'Invest' korrigiert, 4/8GB differenziert, USV entkoppelt |
| **<a href="/preview/blog/home-assistant-preview/">🏠 Home Assistant</a>** | ✅ überarbeitet | Superlative entfernt, Titel sachlich, Zigbee relativiert |
| **<a href="/preview/blog/proxmox-preview/">📦 Proxmox</a>** | ✅ überarbeitet | Subscription erklärt, Snapshot≠Backup, KI-Angaben entfernt |
| **<a href="/preview/blog/headscale-preview/">🔗 Headscale</a>** | ✅ überarbeitet | Keine feste Version, Grants>ACLs, Datenschutz korrigiert |
| **<a href="/preview/blog/futro-s7010-preview/">🖥️ Futro S7010</a>** | ✅ überarbeitet | OPNsense braucht 2. NIC, PVE04-Werte, Preise datiert |
| **<a href="/preview/blog/mini-pc-vergleich-preview/">📊 Mini-PC Vergleich</a>** | ✅ überarbeitet | Prozent entfernt, 'beste Wahl'→'passend wenn', KI reduziert |
| **<a href="/preview/about/">👤 Über mich</a>** | ✅ überarbeitet | Alter entfernt, PVE04 als Test-Lab |
|| **<a href="/preview/home/">🏠 Startseite (Preview)</a>** | ✅ erstellt | Werbung-Text moderiert, RAM-Empfehlung gestaffelt, geplante Guides gruppiert |
|| **<a href="/preview/links/">🔗 Empfehlungen (Preview)</a>** | ✅ erstellt | Im Einsatz/Empfehlung getrennt, Einschränkungen ergänzt, geprüft Juli 2026 |

---

## 📐 Lesbarkeit & Layout

Diese Preview zeigt Verbesserungen der Lesbarkeit des Blogs **matmaksa.de** – isoliert, ohne die öffentliche Website zu verändern.

<div class="preview-meta">
  <strong>Erstellt:</strong> 15. Juli 2026 &nbsp;·&nbsp;
  <strong>Status:</strong> ⚠️ Preview – nicht öffentlich &nbsp;·&nbsp;
  <strong>Benötigt:</strong> Deine visuelle Freigabe
</div>

### Was wurde verbessert?

| Bereich | Änderung |
|---|---|
| **Fließtext** | Textbreite auf ~760 px begrenzt, Schrift 18 px, Zeilenhöhe 1,75, mehr Absatzabstand |
| **Überschriften** | Deutlich mehr Abstand vor H2/H3, klarere Größenhierarchie |
| **Tabellen** | Horizontal scrollbar auf Mobil, mehr Innenabstand, einklappbar bei langen Tabellen |
| **Info-Boxen** | Wiederkehrende Boxen („Zu wissen", „Meine Erfahrung", „Wichtig", „Technische Details") mit farbiger linker Kante |
| **Inhaltsverzeichnis** | Auf Mobil standardmäßig eingeklappt, keine Doppelanzeige |
| **Artikelabsätze** | Auf 3–4 Sätze begrenzt (redaktioneller Hinweis); technische Details in aufklappbaren Bereichen |

### Beispiel-Seiten

<div class="preview-card">
  <span class="preview-badge modified">verbessert</span>
  <h3><a href="/preview/blog/pihole-adguard-futro-s7010-vergleich/">🔍 Pi-hole vs. AdGuard Home auf Futro S7010</a></h3>
  <p class="preview-desc">Vollständiger Artikel mit allen Lesbarkeitsverbesserungen: schmalere Textbreite, größere Schrift, optimierte Tabellen, Info-Boxen, einklappbares TOC.</p>
</div>

<div class="preview-card">
  <span class="preview-badge modified">verbessert</span>
  <h3><a href="/preview/blog/home-assistant-gebrauchter-mini-pc/">🏠 Home Assistant auf gebrauchtem Mini-PC</a></h3>
  <p class="preview-desc">Zweiter Beispiel-Artikel mit denselben Layout-Verbesserungen – zeigt Konsistenz über verschiedene Artikel hinweg.</p>
</div>

<div class="preview-card">
  <span class="preview-badge modified">visuell</span>
  <h3>🏠 Startseite (matmaksa.de)</h3>
  <p class="preview-desc">Die Startseite wird durch die Preview-Änderungen nicht beeinflusst – sie hat kein <code>preview = true</code>. Die Lesbarkeitsverbesserungen greifen nur auf Artikelseiten. Die Startseite bleibt im aktuellen Layout sichtbar.</p>
</div>

<div class="preview-card">
  <span class="preview-badge new">neu</span>
  <h3><a href="/preview/home/">🏠 Startseite (Preview)</a></h3>
  <p class="preview-desc">Eigenständige Preview-Version der Startseite: Werbung-Text moderiert, RAM-Empfehlung in 4/8/16 GB gestaffelt, geplante Guides in eigenem Bereich gruppiert.</p>
</div>

<div class="preview-card">
  <span class="preview-badge new">neu</span>
  <h3><a href="/preview/links/">🔗 Empfehlungen (Preview)</a></h3>
  <p class="preview-desc">Preview-Version der Empfehlungsseite: Kategorien getrennt nach „Im Einsatz" und „Empfehlung", Einschränkungen ergänzt, Prüfstand Juli 2026, Affiliate-Hinweis sichtbar.</p>
</div>

### Vorher / Nachher

| Bereich | Vorher | Nachher |
|---|---|---|
| **Textbreite** | Volle Breite (~900 px+) | ~760 px, zentriert |
| **Schriftgröße** | ~16 px (Browser-Standard) | **18 px** |
| **Zeilenhöhe** | ~1,6 | **1,75** |
| **Absatzabstand** | ~1em | **1,6em** |
| **Überschrift H2** | ~1,5em Abstand | **2,4em** Abstand |
| **Tabellen** | Standard-Abstand, Überlauf | **10 px 14 px** Innenabstand, horizontal scrollbar |
| **Info-Boxen** | Keine speziellen Formate | **4 farbige Typen** mit Rand links |
| **TOC mobil** | Immer sichtbar | **Eingeklappt**, auf Klick ausklappbar |

### Technische Details

<details class="tech-detail">
<summary>📋 Wie wurde das umgesetzt?</summary>

- **Keine öffentliche CSS geändert** – Alle Preview-Styles sind in `extend_head.html` innerhalb von `{{- if .Params.preview }}` gekapselt
- **Alle Regeln** sind mit `.preview-mode` als Parent-Selektor geschützt – nur Seiten mit `preview = true` im Frontmatter erhalten die Klasse
- **baseof.html** wurde lokal überschrieben, um `preview-mode` ans `<body>` zu hängen
- **Keine Shortcodes, keine neuen JavaScript-Abhängigkeiten** – reines CSS
- **Preview-Übersicht** unter `/preview/` erreichbar
</details>

<details class="tech-detail">
<summary>🔧 Einschränkungen</summary>

- **Artikelabsatz-Begrenzung** (3–4 Sätze) ist ein redaktioneller Hinweis, kein automatischer Zwang – müsste pro Artikel manuell umgesetzt werden.
- Bei sehr langen Tabellen müssten Autoren manuell `details.table-toggle` um die Tabelle legen.
- Startseiten-/Empfehlungs-Preview sind separate Preview-Seiten – das originale Layout bleibt auf der echten Startseite unverändert.
</details>

</div>
