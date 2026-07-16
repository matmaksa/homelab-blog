# eBay Partner Network – Integration

**Stand:** Juli 2026  
**Status:** Vorbereitet, aber noch nicht aktiv – benötigt Konfiguration aus dem eBay-Dashboard

## Benötigte Angaben aus dem eBay-Partner-Dashboard

1. **Registrierung** unter [https://www.ebaypartnernetwork.com](https://www.ebaypartnernetwork.com) (ePN, nicht partner.ebay.de)
2. Nach der Anmeldung: **Simple Link Generator** öffnen
3. Einen echten Partnerlink erzeugen, z. B. für `www.ebay.de/sch/i.html?_nkw=...`
4. Die vollständige generierte URL kopieren (enthält **alle** erforderlichen Parameter)
5. Aus dieser URL den `_nkw=`-Parameter entfernen (samt Wert)
6. Die Rest-URL in `hugo.toml` unter `[params.ebay] baseUrl` eintragen

### Erwartete Parameter in der generierten URL

Die offizielle EPN-Linkstruktur enthält mindestens:
- `mkevt=1`
- `mkcid=1`
- `mkrid=707-53477-19255-0` (eBay Deutschland)
- `campid=DEINE_CAMPAIGN_ID`
- `toolid=XXXXX`
- Optional: `customid=...`

**Keine dieser Werte schätzen oder manuell zusammensetzen.** Die Parameterwerte können sich ändern. Verwende ausschließlich den offiziellen Simple Link Generator.

## Konfiguration in `hugo.toml`

```toml
[params.ebay]
  baseUrl = "https://www.ebay.de/sch/i.html?_sop=15&_LH_ItemCondition=3000&mkevt=1&mkcid=1&mkrid=707-53477-19255-0&campid=DEINE_ID&toolid=10001&"
```

Die baseUrl muss mit `&` oder `?` enden, da der Shortcode `_nkw=SUCHBEGRIFF` anhängt.

Statt des `query`-Modus kann auch direkt eine vollständige URL über den `url`-Parameter übergeben werden:
```
{{< ebay-link url="https://www.ebay.de/sch/i.html?_nkw=..." text="Angebote" >}}
```

## Shortcode-Verwendung

### Variante 1: Suchbegriff (empfohlen)

```
{{< ebay-link query="Fujitsu Futro S7010" text="Gebrauchte Fujitsu Futro S7010 bei eBay ansehen" >}}
```

Erzeugt: `baseUrl + _nkw=Fujitsu+Futro+S7010`

### Variante 2: Direkte URL

Für spezifische Suchergebnisseiten oder Filter:

```
{{< ebay-link url="https://www.ebay.de/sch/i.html?_nkw=Fujitsu+Futro+S7010&_sop=15" text="Angebote durchsuchen" >}}
```

### Variante 3: Mit Custom-ID (für Auswertung)

```
{{< ebay-link query="Fujitsu Futro S7010" text="Angebote" customid="futro-s7010-preistabelle" >}}
```

`customid` wird an die URL angehängt, damit im ePN-Dashboard nachvollziehbar ist, aus welchem Artikel und an welcher Position der Klick kam.  
**Empfehlung:** Kurze, stabile IDs ohne personenbezogene Daten, z. B. `futro-preistabelle`, `100e-thin-clients`, `vergleich-futro`.

### Alle Parameter

| Parameter | Pflicht | Beschreibung |
|-----------|---------|-------------|
| `query` | ja (oder `url`) | Suchbegriff für eBay (wird URL-encodiert) |
| `url` | ja (oder `query`) | Vollständige eBay-URL (Affiliate- oder Normal-Link) |
| `text` | nein | Linktext (Standard: "Gebrauchte Angebote bei eBay ansehen") |
| `customid` | nein | Für ePN-Auswertung – Position/Artikel-Identifikator |

## Affiliate-Kennzeichnung

Alle Links enthalten automatisch:
- `rel="sponsored nofollow noopener noreferrer"`
- `target="_blank"`

## Normaler vs. Affiliate-Link

| | Normaler eBay-Link | Affiliate-Link (Shortcode) |
|---|---|---|
| `rel` | keins oder `nofollow` | `sponsored nofollow noopener noreferrer` |
| Ziel | `_blank` (optional) | `_blank` (Pflicht) |
| Kennzeichnung | keine | ⓘ im Link |
| Nutzung | Quellenangaben | Kaufempfehlungen |

## Wo eBay-Links vorbereitet wurden

1. **content/posts/fujitsu-futro-s7010-homelab-einstieg/index.md**
   - Nach der Preistabelle
2. **content/posts/homelab-unter-100-euro-was-du-brauchst/index.md**
   - Nach dem Hinweis auf schwankende Preise
3. **content/posts/mini-pc-homelab-vergleich/index.md**
   - Im Abschnitt "Bis 50 €: Fujitsu Futro S7010"

## Verhalten ohne Konfiguration

Wenn `baseUrl` in `hugo.toml` nicht gesetzt oder leer ist:
- **Im Hugo-Produktionsbuild** (`hugo`): gar kein Link – nur der Text wird als reiner Text ausgegeben
- **Im lokalen Dev-Server** (`hugo server`): erscheint ein HTML-Kommentar als Entwicklerhinweis
- **Keine gelben Warnboxen** im produktiven Build
- **Keine scheinbar getrackten, tatsächlich aber nicht funktionierenden Links**

Nach dem Eintragen der `baseUrl` werden automatisch echte Affiliate-Links generiert.

## Test der Integration

1. `baseUrl` in `hugo.toml` eintragen (vom Simple Link Generator)
2. `hugo server` starten
3. Einen der Artikel mit eBay-Shortcode öffnen
4. Prüfen:
   - Link sichtbar mit ⓘ?
   - `rel="sponsored nofollow noopener noreferrer"` vorhanden?
   - URL enthält `mkevt=1`, `mkcid=1`, `mkrid=707-53477-19255-0`, `campid=...`, `toolid=...`?
   - Custom-ID (falls angegeben) in der URL sichtbar?
5. Klick testen: landest du korrekt auf eBay?
6. **Vergleiche mit dem ursprünglichen Link aus dem Simple Link Generator** – die URL-Struktur sollte identisch sein, nur `_nkw=` wird vom Shortcode hinzugefügt

## Zentrale Deaktivierung

Sollen alle eBay-Links deaktiviert werden:
1. `hugo.toml` öffnen
2. `baseUrl` auskommentieren oder auf `""` setzen
3. Hugo-Build erneut ausführen
4. Alle Shortcodes wechseln automatisch in den inaktiven Modus (kein Link)

Die Shortcodes selbst müssen nicht aus den Artikeln entfernt werden. Bestehende Amazon-Links bleiben unberührt.
