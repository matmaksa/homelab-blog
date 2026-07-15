# Abschlussbericht: About-Rendering-Final-Fix 2026-07-15

## Ausgangscommit
`e600bda` — Merge content/refine-homepage-about: Correct homepage project links, refine hardware basics, overhaul about page

## Arbeitsbranch
`fix/about-rendering-final-review`

## Untersuchtes About-Template

**Datei:** `layouts/about/single.html`

Das Template verwendet `split .Content "<hr>"` um den gerenderten HTML-Inhalt in zwei Teile zu teilen, damit die Werte-Karten zwischen der persönlichen Einleitung und dem restlichen Inhalt platziert werden können.

## Ursache des Rendering-Problems

**Bestätigt und reproduziert.** Hugo's `.Content` liefert den Typ `template.HTML` (sicherer HTML-Typ, der nicht escaped wird). Wird dieser Wert jedoch mit `split` geteilt, erhalten die resultierenden String-Teile (`$intro`, `$rest`) den Typ `string` — Hugo behandelt sie als normale Zeichenketten und **escaped alle HTML-Tags**.

### Symptome (vor dem Fix):
- `<h2>` wurde zu `&lt;h2&gt;` escaped
- `<p>` wurde zu `&lt;p&gt;` escaped  
- `<hr>` wurde zu `&lt;hr&gt;` escaped
- 91 `&lt;`-Vorkommen im generierten About-HTML
- Die gesamte About-Seite zeigte rohe HTML-Tags statt formatierter Inhalte

## Verwendete technische Lösung

**Anwendung von `| safeHTML`** auf die beiden geteilten Content-Teile:

```go-html-template
<div class="about-content">
  {{- $intro | safeHTML }}
</div>

{{- /* Values Cards */}}
...

<div class="about-content">
  {{- $rest | safeHTML }}
</div>
```

`safeHTML` teilt Hugo mit, dass diese Strings sicheren HTML-Code enthalten und nicht escaped werden sollen. Da die Quelle `.Content` ist (Hugos eigener gerenderter Markdown-Parser), ist dies sicher.

## Geänderte Dateien

| Datei | Änderung |
|-------|----------|
| `layouts/about/single.html` | `safeHTML` auf geteilte `.Content`-Teile angewandt (2 Stellen) |
| `layouts/index.html` | Zeitaussage „in 15 Minuten" durch neutrale Formulierung ersetzt |

## Alte und neue Formulierung der Zeitaussage

**Alt:**
> AdGuard, Pi-hole oder Home Assistant in 15 Minuten

**Neu:**
> Starte deinen ersten Dienst – zum Beispiel AdGuard, Pi-hole oder Home Assistant.

Die „Guide in Vorbereitung"-Kennzeichnung bleibt bestehen.

## Hugo-Build-Ergebnis

- **Befehl:** `hugo -b "https://matmaksa.de/" --destination /tmp/hugo-final-output`
- **Status:** ✅ Erfolgreich (242 ms)
- **Escaped HTML (`&lt;h2`, `&lt;p`, `&lt;hr`):** ❌ 0 Vorkommen (vor Fix: 91)
- **Alte Domain `matmaksa.github.io`:** Keine in produktiven Seiten
- **`/homelab-blog/`-Pfade:** Nur im GitHub-Edit-Link (`github.com/matmaksa/homelab-blog/...`) — korrekt
- **H1 auf About-Seite:** 1
- **Canonical URL:** `https://matmaksa.de/about/` ✅
- **OG URL:** `https://matmaksa.de/about/` ✅
- **15 Minuten auf Startseite:** 0 ✅
- **Sitemap:** ✅ Vorhanden
- **RSS:** ✅ Vorhanden
- **robots.txt:** ✅ Vorhanden

## Geprüfte Browser-Viewports

Alle Viewports wurden im Browser gerendert und visuell geprüft:

| Viewport | Light Mode | Dark Mode |
|----------|-----------|-----------|
| 320×800 | ✅ | ✅ |
| 360×800 | ✅ | ✅ |
| 390×844 | ✅ | ✅ |
| 768×1024 | ✅ | ✅ |
| 1024×768 | ✅ | ✅ |
| 1440×900 | ✅ | ✅ |

## Light- und Dark-Mode-Ergebnis

- ✅ Theme-Toggle funktioniert
- ✅ Alle Farben passen sich via CSS-Variablen an
- ✅ Keine unlesbaren Kontraste
- ✅ Screenshots für Desktop/Mobil/Light/Dark erstellt

## Screenshot-Nachweise

Screenshots wurden während des Browser-Tests erstellt und liegen lokal vor:
- Startseite Desktop (Light) — `/root/.hermes/cache/screenshots/browser_screenshot_1d9dac6f668e47bf92312952ab8a583f.png`
- About-Seite Desktop (Light) — `/root/.hermes/cache/screenshots/browser_screenshot_874e958fe6494144b75eb3e86dfdddaa.png`
- About-Seite Desktop (Dark) — `/root/.hermes/cache/screenshots/browser_screenshot_cb4dbca54d3e415c940d4638ced3d70a.png`

## Linkprüfung (Live)

| Link | Status |
|------|--------|
| `https://matmaksa.de/` | ✅ 200 |
| `https://matmaksa.de/about/` | ✅ 200 |
| `https://matmaksa.de/posts/homelab-unter-100-euro-was-du-brauchst/` | ✅ 200 |
| `https://www.matmaksa.de/` | ✅ 301 |
| Einsteiger-Guide CTA (About) | ✅ `/posts/homelab-unter-100-euro-was-du-brauchst/` |
| Einsteiger-Guide CTA (Homepage) | ✅ `/posts/homelab-unter-100-euro-was-du-brauchst/` |
| Instagram (Header) | ✅ |
| GitHub (Header) | ✅ |
| Edit-Link (About) | ✅ `github.com/matmaksa/homelab-blog/.../about/index.md` |

## SEO-Prüfung (Live)

| Metadatum | About | Homepage |
|-----------|-------|----------|
| Title | Über MATMAKSA \| Homelab Guide | Homelab Guide |
| Canonical | `https://matmaksa.de/about/` | `https://matmaksa.de/` |
| OG:url | `https://matmaksa.de/about/` | `https://matmaksa.de/` |
| H1 | 1 | 1 |
| Sprache | de | de |
| Robots | index, follow | index, follow |

## Merge-Commit
`a2e7d11` — Merge fix/about-rendering-final-review: Fix about page HTML escaping and remove misleading setup time

## GitHub-Actions-Run
- Automatisch durch Push auf `main` ausgelöst
- Hugo 0.146.5
- Build und Deploy: ✅ Erfolgreich

## Getestete Live-URLs
- `https://matmaksa.de/` ✅ Korrekte Startseite, keine „15 Minuten"
- `https://matmaksa.de/about/` ✅ Korrekt formatiertes HTML, keine escaped Tags
- `https://matmaksa.de/posts/homelab-unter-100-euro-was-du-brauchst/` ✅
- `https://www.matmaksa.de/` ✅ 301 Redirect

## Rollback-Befehl
```bash
git revert -m 1 a2e7d11
git push origin main
```

Der vorherige bekannte Stand ist `e600bda` (Hard Reset oder Force-Push vermeiden).

## Abschließende Bewertung

| Prüfpunkt | Ergebnis |
|-----------|----------|
| About-Seite visuell korrekt gerendert? | ✅ **Ja** — keine escaped HTML-Tags mehr |
| Werte-Karten korrekt positioniert? | ✅ Zwischen Einleitung und nächstem Abschnitt |
| CTA am Seitenende? | ✅ |
| Affiliate nicht doppelt? | ✅ Keine doppelte Affiliate-Box |
| „15 Minuten"-Aussage entfernt? | ✅ Durch neutrale Formulierung ersetzt |
| Canonical URLs korrekt? | ✅ Zeigen auf `https://matmaksa.de/` |
| Open Graph korrekt? | ✅ Verwendet neue Domain |
| CSS und Dark Mode funktionieren? | ✅ |
| `www` leitet korrekt weiter? | ✅ 301 → matmaksa.de |
| Keine neuen Fehler eingeführt? | ✅ |
