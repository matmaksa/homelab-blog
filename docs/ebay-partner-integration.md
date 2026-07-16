# eBay Partner Network – Integration

**Stand:** Juli 2026  
**Status:** Vorbereitet, aber noch nicht aktiv

## Benötigte eBay-Kennung

Nach der Registrierung im [eBay Partner Network](https://partner.ebay.de/) (ePN) musst du im Dashboard deine **Campaign ID** (Custom-ID) finden/erstellen. Diese ID trägst du an genau einer Stelle ein:

### Konfiguration in `hugo.toml`

```toml
[params.ebay]
  campaignId = "DEINE_CAMPAIGN_ID"
```

Öffne `hugo.toml` im Repository-Stammverzeichnis. Dort findest du bereits den vorbereiteten Abschnitt `[params.ebay]` mit einer auskommentierten Beispiel-ID. Ersetze den Platzhalter durch deine tatsächliche Campaign-ID.

**Solange keine Campaign-ID gesetzt ist,** arbeiten die Shortcodes im Preview-Modus: Es wird eine gelbe Warnung angezeigt, aber kein Link generiert. So können keine kaputten oder scheinbar getrackten Links veröffentlicht werden.

## Shortcode-Verwendung

Es gibt einen wiederverwendbaren Shortcode `{{< ebay-link >}}`.

### Variante 1: Suchbegriff (empfohlen)

Verlinkt auf eine langlebige eBay-Suche mit dem Suchbegriff:

```
{{< ebay-link query="Fujitsu Futro S7010" text="Gebrauchte Fujitsu Futro S7010 bei eBay ansehen" >}}
```

Der Shortcode erzeugt automatisch eine eBay-Suche mit:
- Filter auf "Gebraucht" (LH_ItemCondition=3000)
- Sortierung nach "Neu eingestellt zuerst" (_sop=15)

### Variante 2: Direkte URL

Nur verwenden, wenn du eine spezifische Suchergebnisseite verlinken möchtest:

```
{{< ebay-link url="https://www.ebay.de/sch/i.html?_nkw=Fujitsu+Futro+S7010&_sop=15" text="Angebote durchsuchen" >}}
```

### Parameter

| Parameter | Pflicht | Beschreibung |
|-----------|---------|-------------|
| `query` | ja (oder `url`) | Suchbegriff für eBay |
| `url` | ja (oder `query`) | Direkte eBay-URL |
| `text` | nein | Linktext (Standard: "Gebrauchte Angebote bei eBay ansehen") |

## Affiliate-Kennzeichnung

Alle eBay-Links enthalten automatisch:
- `rel="sponsored nofollow"` – für Suchmaschinen und als Affiliate-Kennzeichnung
- `target="_blank"` – Link öffnet in neuem Tab
- `customid`-Parameter mit der Campaign-ID – für die ePN-Nachverfolgung

Die Links sind unterscheidbar von normalen eBay-Links durch den `customid`-Parameter in der URL.

## Normaler vs. Affiliate-Link

| | Normaler eBay-Link | Affiliate-Link (Shortcode) |
|---|---|---|
| rel | keins oder `nofollow` | `sponsored nofollow` |
| URL | https://www.ebay.de/... | https://www.ebay.de/...?customid=DEINE_ID&mkrid=... |
| Nutzung | In Fußnoten, Quellenangaben | In Affiliate-Kontext (Kaufempfehlungen) |

## Wo eBay-Links vorbereitet wurden

In folgenden Artikeln sind bereits eBay-Shortcodes eingefügt:

1. **content/posts/fujitsu-futro-s7010-homelab-einstieg/index.md**
   - Nach der Preistabelle (S7010-Angebote)
2. **content/posts/homelab-unter-100-euro-was-du-brauchst/index.md**
   - Nach dem Hinweis auf schwankende Preise (gebrauchte Thin Clients)
3. **content/posts/mini-pc-homelab-vergleich/index.md**
   - Im Abschnitt "Bis 50 €: Fujitsu Futro S7010"

## Test der Integration

1. Campaign-ID in `hugo.toml` eintragen
2. `hugo server` starten
3. Einen der Artikel mit eBay-Shortcode öffnen
4. Prüfen: Link sichtbar? `rel="sponsored nofollow"` vorhanden? URL enthält `customid`?
5. Klick testen: Wirst du zur eBay-Suche weitergeleitet?

## Zentrale Deaktivierung

Sollen alle eBay-Links deaktiviert werden:
1. `hugo.toml` öffnen
2. `campaignId` auskommentieren oder leeren
3. Hugo-Build erneut ausführen
4. Alle Shortcodes wechseln automatisch in den Preview-Modus (Warnung statt Link)

Die Shortcodes selbst müssen nicht aus den Artikeln entfernt werden.
