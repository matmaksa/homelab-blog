---
title: "Headscale Clients verbinden und ACLs setzen"
date: 2026-07-02
draft: true
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Headscale Server im Homelab verbindet mehrere Clients per Mesh-VPN mit Zugriffregeln"
  relative: true
tags:
  - software
  - headscale
  - tailscale
  - mesh-vpn
  - wireguard
  - acl
  - proxmox
  - netzwerk
categories:
  - Software

# Production State Flow
content_state: "parked"
audit_status: "minor_fix"
user_approval_required: true
approved_for_publish: false
instagram_derivatives_required: false
instagram_derivatives_status: "not_applicable"
content_cluster: "headscale"
content_role: "deep_dive"
risk_level: "medium"
next_action: "verify_headscale_commands_and_align_basis_article_before_publish"
related_articles:
  - "headscale-homelab"
notes:
  - "Automatically generated draft; parked after audit."
  - "Requires Headscale v0.29.2 command verification before publication."
  - "Basis article should be aligned before this follow-up is published."
---

**Aktualisiert: Juli 2026 | Lesezeit: 8 Minuten**

<!--more-->

## TL;DR: So kommen deine Geräte sauber ins Headscale-Netz

Wenn Headscale läuft, verbindest du deine Geräte mit dem normalen Tailscale-Client und gibst als Login-Server deine Headscale-URL an. Für Linux-Server nimmst du einen kurz gültigen Pre-Auth-Key, für Laptop oder Desktop ist die Web-Freigabe übersichtlicher.

ACLs sind danach Pflicht, wenn nicht jedes Gerät jedes andere Gerät erreichen soll. Starte mit einer einfachen Regel: Admin-Geräte dürfen alles, normale Clients dürfen nur auf Homelab-Server, Server dürfen nicht ungefragt zurück auf deine privaten Geräte.

## Voraussetzungen

| Punkt | Wert |
|---|---|
| ⏱ Zeit | 30–45 Minuten |
| 💰 Kosten | 0 € |
| 📊 Schwierigkeit | ⭐⭐⭐☆☆ |
| 🖥️ Benötigt | Laufender Headscale-Server, erreichbare HTTPS-URL, Tailscale-Client |
| 🎯 Ziel | Clients verbinden und erste Zugriffregeln setzen |
| ✅ Geprüft gegen | Headscale-Dokumentation v0.29.2, Tailscale-Client-Befehle |

> Das ist der Anschlussartikel zu [Headscale im Homelab – Tailscale-Alternative selbst hosten](/posts/headscale-tailscale-alternative-selbst-hosten/). Dort geht es um Installation und Grundidee. Hier geht es um den Alltag danach: Geräte verbinden, prüfen, einschränken.

---

## Für wen lohnt sich dieser Schritt?

Richte Clients und ACLs ein, wenn du mehr als einen Server oder mehrere Geräte im Homelab hast:

- Proxmox-Node, NAS oder LXC sollen von unterwegs erreichbar sein
- Laptop und Handy sollen ins Homelab, aber nicht alles dürfen
- ein Server soll als Subnet-Router dein LAN erreichbar machen
- du willst nicht jedes Gerät per Portfreigabe ins Internet stellen

Nicht einrichten, wenn du nur einen einzelnen Dienst zu Hause nutzt und schon mit WireGuard auf der FRITZ!Box zufrieden bist. Headscale lohnt sich erst, wenn mehrere Geräte und klare Zugriffsregeln ins Spiel kommen.

---

## Die Entscheidung: Web-Login oder Pre-Auth-Key?

Headscale kennt zwei einfache Wege, um neue Geräte aufzunehmen.

| Gerätetyp | Empfehlung | Warum |
|---|---|---|
| Dein Laptop / Desktop | Web-Login | Du siehst bewusst, welches Gerät du freigibst |
| Server / LXC | Pre-Auth-Key | Einmaliger Befehl, gut für SSH und Automatisierung |
| Handy / Tablet | App mit alternativem Server | Kein Terminal nötig |
| Temporäres Testgerät | kurz gültiger Pre-Auth-Key | Danach kann der Key nicht weitergegeben werden |

**Meine Faustregel:** Persönliche Geräte per Web-Login, Server per Pre-Auth-Key. So bleibt die Einrichtung einfach, ohne dass dauerhaft gültige Schlüssel herumliegen.

---

## Schritt 1: Headscale-Server kurz prüfen

Bevor du Clients verbindest, prüfst du zwei Dinge: Ist Headscale erreichbar und gibt es einen Benutzer?

Auf dem Headscale-Server:

```bash
headscale users list
```

Falls noch kein Benutzer existiert:

```bash
headscale users create homelab
```

Prüfe außerdem den Health-Endpunkt im Browser oder per Terminal:

```bash
curl https://headscale.deine-domain.de/health
```

Wenn hier nichts zurückkommt, ist noch nicht der Client dein Problem. Dann stimmt meistens DNS, Reverse Proxy oder HTTPS nicht.

---

## Schritt 2: Linux-Client per Web-Login verbinden

Auf dem Linux-Gerät installierst du den Tailscale-Client und verweist ihn auf deinen Headscale-Server.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --login-server https://headscale.deine-domain.de
```

Der Client zeigt dir danach eine URL oder eine Auth-ID an. Die Freigabe machst du auf dem Headscale-Server:

```bash
headscale auth register --user homelab --auth-id <AUTH_ID>
```

Danach prüfst du auf dem Client:

```bash
tailscale status
```

Und auf dem Server:

```bash
headscale nodes list
```

Wenn das Gerät in beiden Listen auftaucht, ist die Verbindung hergestellt.

> Wichtig: In aktuellen Headscale-Versionen läuft die Freigabe über `headscale auth register --user ... --auth-id ...`. Ältere Anleitungen nennen teilweise andere Befehle. Wenn ein Befehl nicht existiert, prüfe mit `headscale auth --help` und `headscale nodes --help`.

---

## Schritt 3: Server oder LXC per Pre-Auth-Key verbinden

Für Server ist ein Pre-Auth-Key praktischer. Du erzeugst ihn auf dem Headscale-Server:

```bash
headscale preauthkeys create --user homelab
```

Der Befehl gibt einen Schlüssel aus. Nutze ihn direkt auf dem Zielserver:

```bash
sudo tailscale up \
  --login-server https://headscale.deine-domain.de \
  --authkey <PRE_AUTH_KEY>
```

Danach den Schlüssel nicht in Notizen, Skripten oder Chatverläufen speichern. Standardmäßig ist so ein Key nur begrenzt gültig und nicht für dauerhafte Geheimnisverwaltung gedacht.

Für wiederholbare Server-Setups kannst du später mit Ablaufzeiten und wiederverwendbaren Keys arbeiten. Für den Einstieg reicht: Key erzeugen, Gerät verbinden, Key vergessen.

---

## Schritt 4: Windows, macOS, Android und iOS verbinden

Du nutzt weiter die offiziellen Tailscale-Clients. Der Unterschied ist nur der Login-Server.

| System | Vorgehen |
|---|---|
| Windows | Tailscale installieren, PowerShell öffnen, `tailscale login --login-server https://headscale.deine-domain.de` ausführen |
| macOS | Tailscale installieren, im Terminal denselben Login-Befehl nutzen oder im Menü einen Custom Login Server setzen |
| Android | Tailscale-App öffnen → Accounts → Drei-Punkte-Menü → Alternate Server / alternativer Server |
| iOS | Tailscale-App öffnen → Log in → Optionen → Custom Coordination Server |

Danach musst du das Gerät wie bei Linux auf dem Headscale-Server freigeben, sofern du keinen Pre-Auth-Key nutzt.

---

## Schritt 5: Verbindungen testen

Nach zwei verbundenen Geräten sollte ein Ping über die Tailscale-IP funktionieren.

Auf Gerät A:

```bash
tailscale status
```

Suche die 100.x.x.x-Adresse von Gerät B und teste:

```bash
ping 100.x.x.x
```

Falls MagicDNS aktiv ist, kannst du auch den Namen testen:

```bash
ping servername
```

Praktischer Test für dein Homelab:

```bash
ssh root@100.x.x.x
```

Wenn SSH über die Tailscale-IP klappt, brauchst du für diesen Server keine öffentliche Portfreigabe mehr.

---

## Warum ACLs wichtig sind

Ohne Policy-Datei gilt sinngemäß: Geräte im Tailnet dürfen miteinander sprechen. Für ein kleines Testnetz ist das okay. Für dein echtes Homelab ist das zu grob.

Ein Beispiel:

- dein Laptop darf auf Proxmox, NAS und Uptime Kuma
- dein Handy darf vielleicht nur auf Home Assistant
- ein LXC für Monitoring muss nicht auf deinen privaten Laptop zugreifen
- ein Testserver soll nicht automatisch das ganze Netz sehen

ACLs verhindern nicht jeden Fehler. Aber sie reduzieren den Schaden, wenn ein Gerät falsch konfiguriert ist oder ein Testdienst zu viel darf.

---

## Schritt 6: Einfache Policy-Datei anlegen

Headscale nutzt das gleiche huJSON-Format wie Tailscale. In aktuellen Headscale-Versionen verweist du in der Konfiguration über `policy.path` auf diese Datei.

Für Zugriffsregeln sind **Tags** praktischer als Gerätenamen. Ein Server bekommt zum Beispiel `tag:server`, dein NAS bekommt `tag:nas`. Dann bleibt die Regel stabil, auch wenn sich die Tailscale-IP ändert.

Lege auf dem Headscale-Server eine Policy-Datei an:

```bash
nano /etc/headscale/policy.hujson
```

Ein einfacher Startpunkt:

```json5
{
  "tagOwners": {
    "tag:server": ["homelab"],
    "tag:nas": ["homelab"],
    "tag:homeassistant": ["homelab"]
  },

  "acls": [
    {
      // Persönliche Geräte des Benutzers homelab dürfen auf SSH/Webdienste
      "action": "accept",
      "src": ["homelab"],
      "dst": ["tag:server:22", "tag:nas:443", "tag:homeassistant:8123"]
    },
    {
      // Server dürfen nur gezielt zum NAS-Webdienst
      "action": "accept",
      "src": ["tag:server"],
      "dst": ["tag:nas:443"]
    }
  ]
}
```

Das Beispiel ist bewusst klein. Es zeigt drei Dinge:

1. Der Benutzer `homelab` darf Geräte mit diesen Tags registrieren.
2. Persönliche Geräte dürfen nur auf konkrete Homelab-Dienste.
3. Server bekommen keine pauschale Freigabe auf alle anderen Geräte.

Wenn du einen Server mit Tag verbinden willst, nutzt du beim Login zusätzlich `--advertise-tags`:

```bash
sudo tailscale up \
  --login-server https://headscale.deine-domain.de \
  --authkey <PRE_AUTH_KEY> \
  --advertise-tags=tag:server
```

---

## Schritt 7: Policy in Headscale aktivieren

Öffne die Headscale-Konfiguration:

```bash
nano /etc/headscale/config.yaml
```

Suche den Policy-Bereich und setze den Pfad:

```yaml
policy:
  path: /etc/headscale/policy.hujson
```

Danach Headscale neu laden:

```bash
systemctl reload headscale
```

Falls Reload nicht funktioniert:

```bash
systemctl restart headscale
journalctl -u headscale -n 80 --no-pager
```

Headscale schreibt beim Laden ins Log, ob die Policy verarbeitet werden konnte. Genau dort findest du Tippfehler in JSON, falsche Gruppen oder ungültige Ziele.

---

## Schritt 8: ACLs wirklich testen

Teste nicht nur den erlaubten Fall. Teste auch, was blockiert sein soll.

Vom Laptop:

```bash
ssh root@proxmox
curl -k https://nas
curl http://homeassistant:8123
```

Danach ein absichtlich nicht erlaubtes Ziel testen:

```bash
ssh root@homeassistant
```

Wenn alles erreichbar ist, obwohl du es nicht erlaubt hast, greift deine Policy nicht oder die Regel ist zu breit.

Typische Ursachen:

- `policy.path` zeigt auf die falsche Datei
- Headscale wurde nach Änderung nicht neu geladen
- deine Gruppe enthält mehr Nutzer/Geräte als gedacht
- `*: *` beziehungsweise `*:*` wurde zu früh als Bequemlichkeitsregel genutzt

---

## Optional: Subnet-Router fürs LAN

Ein Subnet-Router ist ein Gerät im Headscale-Netz, das zusätzlich dein normales LAN erreichbar macht. Das ist nützlich, wenn du Geräte erreichen willst, auf denen kein Tailscale läuft: Drucker, Switch, IP-Kamera oder ältere Weboberflächen.

Auf dem Router-Gerät:

```bash
sudo tailscale up \
  --login-server https://headscale.deine-domain.de \
  --advertise-routes=192.168.30.0/24
```

Auf dem Headscale-Server anzeigen:

```bash
headscale nodes list-routes
```

Route freigeben:

```bash
headscale nodes approve-routes --identifier <NODE_ID> --routes 192.168.30.0/24
```

Auf dem Client, der die Route nutzen soll:

```bash
sudo tailscale set --accept-routes
```

Setze Subnet-Router nicht als ersten Schritt ein. Verbinde erst zwei normale Clients, teste Ping und SSH, dann kommt Routing.

---

## Troubleshooting

### 1. Client zeigt Login-Link, aber nichts passiert

Prüfe auf dem Headscale-Server:

```bash
journalctl -u headscale -f
```

Starte den Login auf dem Client neu und achte auf die Auth-ID. Danach:

```bash
headscale auth register --user homelab --auth-id <AUTH_ID>
```

### 2. `tailscale status` zeigt Geräte, aber Ping geht nicht

Prüfe lokale Firewalls. Auf Linux blocken `ufw`, `firewalld` oder Container-Firewalls gerne ICMP oder SSH.

Zum Testen:

```bash
sudo tailscale ping <zielname-oder-ip>
```

Das testet die Tailscale-Verbindung direkter als ein normaler Ping.

### 3. Policy-Datei lädt nicht

Prüfe die letzten Logs:

```bash
journalctl -u headscale -n 100 --no-pager
```

Häufige Fehler: fehlendes Komma, falsche Anführungszeichen, falscher Pfad in `config.yaml`.

### 4. Nach ACL-Aktivierung geht plötzlich nichts mehr

Dann hast du wahrscheinlich zu streng gestartet. Setze kurzfristig eine Admin-Regel für dein Hauptgerät und teste danach schrittweise enger.

```json5
{
  "action": "accept",
  "src": ["group:admins"],
  "dst": ["*:*"]
}
```

Diese Regel ist als Rettungsleine okay. Sie sollte nicht deine einzige Policy bleiben.

### 5. Android oder iOS verbindet sich nicht

Prüfe zuerst, ob die Headscale-URL im mobilen Browser erreichbar ist. Wenn schon die `/health`-URL nicht lädt, liegt es nicht an der App, sondern an DNS, HTTPS oder Erreichbarkeit.

---

## FAQ

### Brauche ich ACLs sofort?

Für einen Test mit zwei Geräten nicht zwingend. Für ein echtes Homelab: ja. Ohne Regeln ist das Netz zu offen.

### Soll ich ACLs oder Grants verwenden?

Headscale unterstützt beides. Die Headscale-Dokumentation empfiehlt Grants, weil Tailscale ACLs als älteres Modell behandelt. Für Einsteiger sind klassische ACLs aber leichter zu verstehen und reichen für den Start.

### Kann ich Headscale ohne öffentliche Domain nutzen?

Lokal ja, unterwegs nur eingeschränkt. Deine Clients müssen den Headscale-Server erreichen können. Für Handy und Laptop außerhalb deines LANs brauchst du eine erreichbare HTTPS-Adresse oder einen anderen sicheren Weg ins Heimnetz.

### Kann ich meine normalen Tailscale-Clients weiterverwenden?

Ja. Du nutzt die offiziellen Tailscale-Clients, stellst aber einen eigenen Login-Server ein. Genau das macht Headscale für Homelabs attraktiv.

---

## Nächster Schritt

Wenn Clients und ACLs laufen, lohnt sich als nächstes ein sauberer Subnet-Router-Artikel: ein Gerät im Headscale-Netz macht ein ganzes VLAN erreichbar, ohne dass du Tailscale auf jedem einzelnen Gerät installieren musst.

Bis dahin reicht diese Reihenfolge:

1. zwei Clients verbinden
2. Ping und SSH testen
3. einfache Policy aktivieren
4. blockierte Zugriffe bewusst testen
5. erst danach Subnet-Router oder Exit-Node einrichten

---

## ✅ Das solltest du jetzt können

- [ ] Headscale-Benutzer prüfen oder anlegen
- [ ] Linux-Client per Web-Login verbinden
- [ ] Server oder LXC per Pre-Auth-Key verbinden
- [ ] Windows, macOS, Android oder iOS mit eigenem Login-Server einordnen
- [ ] Geräte mit `tailscale status` und `headscale nodes list` prüfen
- [ ] einfache Policy-Datei anlegen
- [ ] `policy.path` in Headscale setzen
- [ ] erlaubte und blockierte Zugriffe testen

**Einrichten wenn:** du mehrere Homelab-Geräte sicher verbinden willst und bereit bist, die Zugriffsregeln selbst zu pflegen.  
**Nicht einrichten wenn:** du nur einen einzelnen Dienst erreichen willst und eine einfache WireGuard-Verbindung bereits zuverlässig läuft.
