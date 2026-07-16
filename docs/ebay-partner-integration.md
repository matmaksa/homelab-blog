# eBay Partner Network – Integration

**Stand:** Juli 2026  
**Status:** ✅ Aktiv

## Konfiguration in `hugo.toml`

Die eBay-Partner-Integration wird zentral in `hugo.toml` unter `[params.ebay]` konfiguriert:

```toml
[params.ebay]
  active = true
  marketplaceUrl = "https://www.ebay.de"
  campaignId = "5339166386"
  toolId = "10001"
  rotationId = "707-53477-19255-0"
  channelId = "1"
  eventType = "1"
  siteId = "77"
```

- **`active`** – `true` schaltet Affiliate-Links ein; `false` deaktiviert alle Links (nur Text)
- **`campaignId`** – Die vom eBay Partner Network zugewiesene Campaign-ID
- **`toolId`** – Tool-ID aus dem EPN-Dashboard
- **`rotationId`** – eBay-Regions-ID (707-53477-19255-0 für eBay Deutschland)
- **`channelId`** / **`eventType`** / **`siteId`** – EPN-Parameter aus dem Dashboard

## Shortcode-Verwendung

### Syntax

```
{{< ebay-link query="SUCHBEGRIFF" text="LINKTEXT" >}}
{{< ebay-link query="SUCHBEGRIFF" text="LINKTEXT" customid="CUSTOM-ID" >}}
```

### Aktive Positionen

| Artikel | Suchbegriff | Custom-ID |
|---|---|---|
| Fujitsu Futro S7010 | Fujitsu Futro S7010 | `futro-s7010-preistabelle` |
| Homelab unter 100€ | Thin Client Homelab | `homelab-100-thin-clients` |
| Mini-PC-Vergleich | Fujitsu Futro S7010 | `mini-pc-vergleich-futro` |

### Custom-IDs

Custom-IDs ermöglichen im EPN-Dashboard die Zuordnung von Klicks zu einzelnen Linkpositionen. Sie:
- bestehen aus Kleinbuchstaben, Zahlen und Bindestrichen
- enthalten keine personenbezogenen Daten
- sind stabil (keine Jahreszahlen, keine Artikel-URLs)

### Alle Parameter

| Parameter | Pflicht | Beschreibung |
|---|---|---|
| `query` | ja | Suchbegriff (wird URL-encodiert) |
| `text` | nein | Linktext (Standard: "Gebrauchte Angebote bei eBay ansehen") |
| `customid` | nein | Für EPN-Dashboard-Auswertung |

## Generierte URL-Struktur (Beispiel)

```
https://www.ebay.de/sch/i.html?_nkw=Fujitsu+Futro+S7010&mkevt=1&mkcid=1&mkrid=707-53477-19255-0&campid=5339166386&toolid=10001&customid=futro-s7010-preistabelle&siteid=77
```

## Affiliate-Kennzeichnung

Alle Links enthalten automatisch:
- `rel="sponsored nofollow noopener noreferrer"`
- `target="_blank"`
- Sichtbare Kennzeichnung im Linktext

## Verhalten ohne oder mit unvollständiger Konfiguration

- **`active = false`** oder fehlende Campaign-ID: Shortcode gibt nur unverlinkten Text als `<span>` aus – keine Affiliate-Links
- Keine gelben Warnboxen im Produktionsbuild
- Keine scheinbar getrackten, nicht funktionierenden Links

## Zentrale Deaktivierung

Sollen alle eBay-Links deaktiviert werden:
1. `hugo.toml` öffnen
2. `active` auf `false` setzen
3. Hugo-Build erneut ausführen
4. Alle Shortcodes wechseln automatisch in den inaktiven Modus

Die Shortcodes selbst müssen nicht aus den Artikeln entfernt werden. Amazon-Links bleiben unberührt.

## Test der Integration

1. `hugo server` starten
2. Artikel mit eBay-Shortcode öffnen
3. Prüfen:
   - Link sichtbar?
   - `rel="sponsored nofollow noopener noreferrer"` vorhanden?
   - URL enthält: `mkevt`, `mkcid`, `mkrid`, `campid`, `toolid`, `_nkw`, `siteid`?
   - Custom-ID in der URL sichtbar?
   - Keine kurzlebigen Parameter (`itmmeta`, `itmprp`, `amdata`, `tkp`)?
   - Keine einzelne Artikelnummer als Standardziel?
4. Klick testen: Suchergebnisseite auf eBay.de erscheint?
