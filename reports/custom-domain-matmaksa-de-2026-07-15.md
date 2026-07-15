# Abschlussbericht: Custom-Domain-Migration matmaksa.de

**Datum:** 15. Juli 2026  
**Projekt:** Domain-Migration von matmaksa.github.io/homelab-blog → matmaksa.de  
**Repository:** github.com/matmaksa/homelab-blog  

---

## 1. Ausgangscommit

`8bfa4204d139707fa65d6d4d61f149b6b11481b5` auf `main`

## 2. Arbeitsbranch

`domain/matmaksa-de`

## 3. Geänderte Dateien

| Datei | Änderung |
|-------|----------|
| `hugo.toml` | `baseURL` → `https://matmaksa.de/`, `images` → `/og-image.png` |
| `static/robots.txt` | Sitemap-URL → `https://matmaksa.de/sitemap.xml` |
| `content/posts/mini-pc-homelab-vergleich/index.md` | 3× Bildpfad `/homelab-blog/images/products/` → `/images/products/` |

## 4. Gefundene alte Domain- und Basispfad-Verweise

### Produktionsrelevante Funde (korrigiert)
| Datei | Alter Wert | Korrigiert |
|-------|-----------|------------|
| `hugo.toml` (baseURL) | `https://matmaksa.github.io/homelab-blog/` | `https://matmaksa.de/` ✅ |
| `hugo.toml` (images) | `/homelab-blog/og-image.png` | `/og-image.png` ✅ |
| `static/robots.txt` | `matmaksa.github.io/homelab-blog/sitemap.xml` | `matmaksa.de/sitemap.xml` ✅ |
| `content/posts/mini-pc-homelab-vergleich/index.md` (line 90) | `/homelab-blog/images/products/fujitsu-s7010.jpg` | `/images/products/fujitsu-s7010.jpg` ✅ |
| `content/posts/mini-pc-homelab-vergleich/index.md` (line 161) | `/homelab-blog/images/products/lenovo-m720q-tiny.jpg` | `/images/products/lenovo-m720q-tiny.jpg` ✅ |
| `content/posts/mini-pc-homelab-vergleich/index.md` (line 182) | `/homelab-blog/images/products/gmktec-g3s.jpg` | `/images/products/gmktec-g3s.jpg` ✅ |

### Historische Funde (nicht korrigiert – nicht veröffentlichte Preview-/Planungsdokumente)
- `instagram-assets/` – Instagram-Planungsdokumente (historisch, nicht veröffentlicht)
- `instagram-derivate/` – Derivate-Planung (historisch)
- `content/preview/` – Preview-Drafts (robotsNoIndex, sitemap.exclude)
- `reports/` – Interne Berichte
- `static/ig-review/` – IG-Review (per robots.txt disallowed)
- `static/robots.txt.test` – Testdatei

## 5. Hugo-Build-Ergebnis

| Metrik | Wert |
|--------|------|
| Hugo-Version | 0.146.5 extended |
| Build-Dauer | 297 ms |
| Pages | 103 |
| Paginator pages | 1 |
| Non-page files | 16 |
| Static files | 114 |
| Processed images | 12 |
| Aliases | 35 |
| Fehler | 0 |

## 6. Link- und Asset-Prüfung (Produktionsbuild)

| Prüfung | Ergebnis |
|---------|----------|
| Canonical URLs | ✅ `https://matmaksa.de/` |
| OG:url | ✅ `https://matmaksa.de/` |
| Sitemap-URLs | ✅ Alle `https://matmaksa.de/` |
| RSS-Links | ✅ Alle `https://matmaksa.de/` |
| Alte `matmaksa.github.io` in HTML/XML/JSON | ✅ Keine in Produktionsdateien |
| Alte `/homelab-blog/`-Pfade in Produktion | ✅ Keine |
| Produktbilder (fujitsu-s7010.jpg u.a.) | ✅ 200 OK live |
| robots.txt | ✅ Sitemap-URL korrigiert |

## 7. GitHub-Pages-Custom-Domain-Status

| Eigenschaft | Status |
|-------------|--------|
| Custom Domain | ✅ `matmaksa.de` |
| Build Type | `workflow` (GitHub Actions) |
| Pages-Quelle | `gh-pages` branch (Artefakt-Deployment) |
| CNAME-Datei | Nicht benötigt (Actions-basierter Build) |
| Status | ✅ `built` |

**Hinweis:** Die Custom Domain `matmaksa.de` war bereits in den GitHub-Pages-Einstellungen konfiguriert. Dadurch entfiel der manuelle Schritt.

## 8. HTTPS-Zertifikatsstatus

| Eigenschaft | Status |
|-------------|--------|
| Zertifikatsstatus | ✅ `approved` |
| Gültig bis | Oktober 2026 |
| Abgedeckte Domains | `matmaksa.de`, `www.matmaksa.de` |

## 9. Enforce-HTTPS-Status

| Status | Vorher | Nachher |
|--------|--------|---------|
| HTTPS enforced | ❌ `false` | ✅ `true` |

## 10. Deployment-Commit

`3967a0051d5972e14563621864119cc44630e244` auf `main`

GitHub Actions Run #109: **success**

## 11. Getestete Live-URLs

| URL | Status | Ergebnis |
|-----|--------|----------|
| `https://matmaksa.de/` | 200 ✅ | Blog-Homepage |
| `https://www.matmaksa.de/` | 301 → matmaksa.de ✅ | Redirect |
| `https://matmaksa.de/posts/` | 200 ✅ | Artikelübersicht |
| `https://matmaksa.de/categories/` | 200 ✅ | Kategorien |
| `https://matmaksa.de/search/` | 200 ✅ | Suche |
| `https://matmaksa.de/index.xml` | 200 ✅ | RSS mit neuen URLs |
| `https://matmaksa.de/sitemap.xml` | 200 ✅ | Sitemap mit neuen URLs |
| `https://matmaksa.de/posts/homelab-unter-100-euro-was-du-brauchst/` | 200 ✅ | Bestehender Artikel |
| `https://matmaksa.de/posts/fujitsu-futro-s7010-homelab-einstieg/` | 200 ✅ | Bestehender Artikel |
| `https://matmaksa.de/posts/mini-pc-homelab-vergleich/` | 200 ✅ | Artikel mit korrigierten Bildern |
| `https://matmaksa.de/images/products/fujitsu-s7010.jpg` | 200 ✅ | Produktbild lädt |
| `https://matmaksa.github.io/homelab-blog/` | 301 → matmaksa.de ✅ | Alte Domain leitet weiter |

## 12. Manueller Schritt (nicht erforderlich)

✅ **Kein manueller Schritt notwendig.** Die GitHub-Pages-Custom-Domain `matmaksa.de` war bereits konfiguriert. HTTPS Enforcement wurde automatisch aktiviert.

## 13. Rollback-Anweisung

Falls ein Rollback erforderlich ist:

```bash
# On branch main:
git checkout design/redesign-v1 -- .
git checkout 8bfa420 -- hugo.toml static/robots.txt content/posts/mini-pc-homelab-vergleich/index.md
git commit -m "Rollback: restore pre-migration state (custom domain)"
git push origin main
```

Mit dem Rollback-Branch `design/redesign-v1` steht der komplette Redesign-Stand vor der Migration zur Verfügung.

## 14. Akzeptanzkriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Hugo-baseURL auf `https://matmaksa.de/` | ✅ |
| 2 | GitHub Pages Custom Domain `matmaksa.de` | ✅ |
| 3 | Produktionsbuild fehlerfrei | ✅ |
| 4 | Keine `/homelab-blog/`-Abhängigkeit in Produktion | ✅ |
| 5 | Canonical, OG, RSS, Sitemap = neue Domain | ✅ |
| 6 | Redesign unverändert funktionsfähig | ✅ |
| 7 | Assets unter neuer Domain ladbar | ✅ |
| 8 | GitHub Actions erfolgreich | ✅ |
| 9 | matmaksa.de liefert Blog aus | ✅ |
| 10 | Rollback möglich | ✅ |

---

**Migration erfolgreich abgeschlossen.**  
Der MATMAKSA Homelab Guide ist jetzt unter https://matmaksa.de/ erreichbar.
