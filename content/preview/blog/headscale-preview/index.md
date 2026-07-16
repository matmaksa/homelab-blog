+++
title = "Headscale im Homelab – Tailscale-Alternative selbst hosten"
description = "Headscale selbst hosten als Tailscale-Alternative: Mesh-VPN auf eigener Infrastruktur mit WireGuard, Grants, ACLs und voller Kontrolle über dein Homelab-Netzwerk."
date = 2026-06-29
robotsNoIndex = true
sitemap = { exclude = true }
image = "featured.jpg"

[cover]
image = "featured.jpg"
alt = "Headscale Mesh-VPN Dashboard – selbst gehosteter Tailscale Control Server im Homelab"
relative = true

[taxonomies]
tags = ["software", "headscale", "tailscale", "mesh-vpn", "wireguard", "proxmox", "lxc", "selfhosting", "netzwerk"]
categories = ["Software"]

[extra]
preview = true
approved_for_publish = false
content_state = "draft"
audit_status = "pending"
user_approval_required = true
instagram_derivatives_required = true
instagram_derivatives_status = "planned"
content_cluster = "headscale"
content_role = "pillar"
risk_level = "medium"
next_action = "manual_review_headscale_basis_commands_for_consistency"
related_articles = ["headscale-clients-acls-homelab"]
notes = [
  "Revised: no fixed version in codeblock, Grants before ACLs, Tailscale plan relativized, no 'unbegrenzt', cloud-outage softened, privacy metadata note added, Headscale marked as advanced, no superlatives.",
  "Align older Headscale CLI/config examples before publishing the follow-up.",
  "Instagram asset headscale-selfhost is planned/review_ready."
]
+++

**Aktualisiert: Juni 2026 | Lesezeit: 7 Minuten**

<!--more-->

## Was ist Headscale? (In zwei Sätzen)

Headscale ist ein **Open-Source-Server** (MIT-Lizenz), der den gleichen Dienst bereitstellt wie die Tailscale-Cloud – nur dass **du** ihn auf deiner eigenen Hardware betreibst. Deine Geräte verbinden sich direkt per WireGuard-Verschlüsselung, ohne dass ein zentraler Cloud-Server die Kontrolle hat.

Wenn du noch keinen Proxmox-Server hast: Im [Mini-PC-Vergleich](/posts/mini-pc-homelab-vergleich/) findest du passende Hardware ab 40 €. Und falls du Proxmox noch nicht kennst: Der Artikel zur [kostenlosen Virtualisierung mit Proxmox](/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) zeigt dir den Einstieg.

> **Hinweis zum Schwierigkeitsgrad:** Headscale richtet sich an Nutzer, die bereits Erfahrung mit Linux, Reverse Proxies und Netzwerk-Grundlagen haben. Wenn du zum ersten Mal einen eigenen Server einrichtest, empfiehlt sich zunächst ein einfacherer Einstieg.

---

## Warum Headscale statt Tailscale-Cloud?

Tailscale ist einfach einzurichten. Aber mit der Entscheidung gibst du die Kontrolle über dein eigenes Netzwerk zum Teil aus der Hand:

**Nachteile der Tailscale-Cloud:**
- Tailscale sieht, welche Geräte du verbindest – auch wenn die Verbindungsinhalte verschlüsselt sind, bleiben Metadaten (wer verbindet sich wann mit wem) für den Anbieter sichtbar
- Tailscale entscheidet über die Infrastruktur – ein Ausfall der Cloud kann die Koordination neuer Verbindungen beeinträchtigen, bestehende Peer-to-Peer-Verbindungen laufen je nach Konfiguration weiter
- Der Personal-Plan von Tailscale erlaubt derzeit bis zu 3 Nutzer und 100 Geräte – diese Konditionen können sich ändern
- Du vertraust einem externen Unternehmen, dass der Dienst in seiner aktuellen Form bestehen bleibt

**Vorteile von Headscale:**
- **Dein Netzwerk, deine Regeln** – Kein externer Dienst sieht deine Verbindungsmetadaten
- **Unabhängig von Drittdiensten** – solange dein Server erreichbar ist, läuft die Koordination über deine eigene Infrastruktur
- **Kein festes Limit** – Gerätezahl und Nutzerzahl werden nicht künstlich begrenzt
- **Open Source** – voller Zugriff auf den Code
- **Eigene Zugriffskontrolle** – du definierst selbst, wer auf wen zugreifen darf

---

## Alternativen im Vergleich

| Lösung | Kosten | Cloud nötig? | Einrichtung | Besonderheit |
|--------|--------|-------------|-------------|--------------|
| **Headscale** | **0 €** | ❌ Nein | Mittel–Fortgeschritten | Du hostest selbst, volle Kontrolle |
| Tailscale-Cloud | 0–6 €/Monat | ✅ Ja | Einfach | Kein eigener Server nötig |
| Netbird | 0–8 €/Monat | Teilweise (kostenloser Plan: Cloud-Management) | Mittel | Open Source, ähnliches Konzept |
| ZeroTier | 0–5 €/Monat | Teilweise (Basis-Koordination via Cloud) | Einfach | Breite Unterstützung |
| Manuelles WireGuard | **0 €** | ❌ Nein | Aufwändig | Volle Kontrolle, aber jede Verbindung manuell |

**Fazit zum Vergleich:** Tailscale ist leichter einsteigerfreundlich, Headscale gibt dir mehr Kontrolle auf Kosten von mehr Aufwand. Wenn du bereits einen Proxmox-Server hast, hast du die nötige Hardware schon – die Frage ist, ob du den administrativen Mehraufwand in Kauf nehmen willst.

---

## Headscale installieren (Proxmox LXC)

Du brauchst: Einen Proxmox-Server, einen LXC-Container (Debian/Ubuntu), und eine Domain oder DynDNS-Adresse.

> ⚠️ **Wichtige Hürde:** Headscale muss von deinen Clients erreichbar sein. Das bedeutet: Du brauchst entweder eine öffentliche Domain mit DynDNS, einen Reverse Proxy mit HTTPS-Zertifikat oder zumindest eine VPN-Verbindung zwischen allen Geräten und dem LXC. Für FRITZ!Box-Nutzer ohne DynDNS ist das eine echte Hürde – du kannst entweder eine DDNS-Domain bei einem kostenlosen Anbieter (dyn.com, duckdns.org) einrichten oder zunächst im lokalen Netzwerk testen.

### 1. LXC-Container vorbereiten

Erstelle einen unprivilegierten LXC mit **Debian 12** (oder Ubuntu 24.04), mindestens **1 CPU-Kern**, **1 GB RAM**, **8 GB Speicher**.

Nach dem Erstellen:

```bash
apt update && apt upgrade -y
```

### 2. Headscale installieren

Lade das aktuelle `.deb`-Paket direkt von GitHub. Prüfe vor der Installation die [aktuellste Version auf GitHub](https://github.com/juanfont/headscale/releases) und ersetze `VERSIONSNUMMER` durch die tatsächliche aktuelle Versionsnummer:

```bash
# Aktuelle Version auf https://github.com/juanfont/headscale/releases prüfen
# und VERSIONSNUMMER unten ersetzen (z. B. 0.24.0)
wget https://github.com/juanfont/headscale/releases/latest/download/headscale_VERSIONSNUMMER_linux_amd64.deb
dpkg -i headscale_VERSIONSNUMMER_linux_amd64.deb
```

### 3. Konfiguration anpassen

Öffne die Konfiguration:

```bash
nano /etc/headscale/config.yaml
```

Wichtige Einstellungen:

```yaml
server_url: https://headscale.deine-domain.de:443  # Deine Domain
listen_addr: 0.0.0.0:8080
metrics_listen_addr: 127.0.0.1:9090
grpc_listen_addr: 127.0.0.1:50443

# Kannst du anpassen:
dns:
  magic_dns: true
  base_domain: headscale.local
  nameservers:
    - 1.1.1.1
    - 9.9.9.9
```

Für den **öffentlichen Zugriff** richtest du am besten einen Reverse Proxy (Nginx, Caddy) oder einen Cloudflare-Tunnel ein. Für erste Tests im lokalen Netz reicht auch die LAN-IP des LXC – deine Clients müssen den Server dann per LAN-IP erreichen können.

### 4. Headscale starten

```bash
systemctl enable --now headscale
```

Prüfen ob es läuft:

```bash
systemctl status headscale
journalctl -u headscale -f
```

### 5. Ersten Nutzer anlegen

```bash
headscale users create homelab
```

---

## Clients mit Headscale verbinden

### Auf Linux (CLI)

```bash
# Tailscale-Client installieren
curl -fsSL https://tailscale.com/install.sh | sh

# Mit Headscale verbinden
tailscale up --login-server https://headscale.deine-domain.de
```

Ein Link für die Authentifizierung wird ausgegeben. Kopiere ihn, öffne ihn im Browser oder gib ihn auf dem Headscale-Server ein:

```bash
headscale nodes register --key <node-key-aus-browser>
```

### Auf Windows / macOS

Lade den Tailscale-Client von [tailscale.com/download](https://tailscale.com/download) herunter. Bei der Installation wählst du nicht „Login with Google", sondern klickst auf das Tailscale-Icon in der Taskleiste → „Use a different server" → gib deine Headscale-URL ein.

### Verbindung prüfen

```bash
tailscale status
# Ausgabe:
# 100.x.x.x    homelab-server    headscale homelab  linux   active
# 100.x.x.x    desktop           headscale homelab  windows active
```

Deine Geräte sind jetzt per Mesh-VPN verbunden. Du erreichst jedes Gerät über seine Tailscale-IP (100.x.x.x).

---

## Zugriffskontrolle: Grants und ACLs

Ohne Zugriffskontrolle kann jedes deiner Geräte jedes andere erreichen. Headscale unterstützt zwei Ansätze, die du in der Policy-Datei kombinieren kannst.

### Grants (aktueller Ansatz)

Grants sind der in neueren Headscale-Versionen bevorzugte Weg zur Zugriffskontrolle. Sie erlauben eine feingranulare Steuerung darüber, welche Quellen welche Ziele auf welchen Ports erreichen dürfen.

Erstelle `/etc/headscale/acl.hujson`:

```json5
{
  "tagOwners": {
    "tag:server": ["dein-user@domain"],
    "tag:client": ["dein-user@domain"]
  },
  "grants": [
    // Admins dürfen auf alles zugreifen
    {
      "src": ["dein-user@domain"],
      "dst": ["*"],
      "ip":  ["*"]
    },
    // Clients dürfen Server auf bestimmten Ports erreichen
    {
      "src": ["tag:client"],
      "dst": ["tag:server"],
      "ip":  ["tcp:22", "tcp:80", "tcp:443"]
    }
  ]
}
```

### ACLs (älterer Ansatz, weiterhin unterstützt)

ACLs sind das ältere Format und in vielen Anleitungen noch verbreitet. Sie funktionieren weiterhin, sind aber weniger flexibel als Grants:

```json5
{
  "groups": {
    "group:admin": ["dein-user@domain"],
    "group:server": ["homelab-server", "nas"],
    "group:client": ["desktop", "laptop"]
  },
  "acls": [
    // Admins dürfen auf alles
    { "action": "accept", "src": ["group:admin"], "dst": ["*:*"] },
    // Server dürfen sich untereinander erreichen
    { "action": "accept", "src": ["group:server"], "dst": ["group:server:*"] },
    // Clients dürfen nur Server erreichen (nicht andere Clients)
    { "action": "accept", "src": ["group:client"], "dst": ["group:server:*"] }
  ]
}
```

### Policy aktivieren

Trage in `config.yaml` den Pfad zur Policy-Datei ein:

```yaml
acl_policy_path: /etc/headscale/acl.hujson
```

Dann Headscale neu starten:

```bash
systemctl restart headscale
```

---

## Vorteile & Nachteile

| Vorteile | Nachteile |
|----------|-----------|
| Volle Kontrolle über dein VPN | Einrichtung aufwändiger als Tailscale-Cloud |
| Verbindungsmetadaten bleiben bei dir | Du brauchst einen öffentlich erreichbaren Server (LXC, VPS) |
| Kein festes Limit bei Geräten und Nutzern | Kein offizielles Web-GUI (nur CLI + Drittanbieter) |
| Open Source (MIT) | Updates musst du selbst einspielen |
| Funktioniert an jeder FRITZ!Box, kein Port-Forwarding | Reverse Proxy für HTTPS nötig |
| WireGuard-Verschlüsselung (schnell, etabliert) | Erfordert Linux- und Netzwerkkenntnisse |

---

## Für wen geeignet?

- **Du hast bereits einen Proxmox-Server** und suchst nach einer Alternative zur Tailscale-Cloud
- **Du hostest mehrere Dienste** und willst sie per Mesh-VPN verbinden, ohne Ports in der FRITZ!Box freizugeben
- **Du möchtest verstehen, wie dein Mesh-VPN funktioniert** auf TCP/IP-Ebene und nicht nur „es läuft"
- **Du hast Erfahrung mit Linux-Administration** und willst auch die Netzwerk-Infrastruktur selbst betreiben
- Tailscale-Nutzer, die mehr Kontrolle wollen und den Mehraufwand bewusst in Kauf nehmen

---

## Für wen ungeeignet?

- **Du willst einfach nur schnell zwei Geräte verbinden** – dann installier Tailscale, Headscale bedeutet deutlich mehr Aufwand
- **Du hast nur ein Gerät im Homelab** – ein Mesh-VPN lohnt sich erst ab 2–3 Geräten
- **Du möchtest keine Kommandozeile sehen** – Headscale hat kein einfaches Web-GUI
- **Du hast keinen öffentlich erreichbaren Server** (oder willst keinen DynDNS/RP einrichten)
- **Linux-Administration ist Neuland für dich** – der Betrieb erfordert laufende Wartung

---

## Fazit

Headscale ist eine sinnvolle Option, wenn du Tailscale kennst, aber die Cloud-Komponente nicht möchtest. Der Einrichtungsaufwand ist mit Vorwissen überschaubar – rechne aber mit mehr als einem schnellen Setup, besonders wenn Reverse Proxy und DynDNS neu für dich sind. Der Vorteil ist klar: **Dein Netzwerk, deine Regeln, kein externer Dienst sieht deine Metadaten.**

**Kosten:** 0 € (Headscale läuft in einem LXC auf deinem bestehenden Proxmox-Server)

**Einrichten wenn:** Du bereits mehrere Geräte in deinem Homelab hast, Erfahrung mit Linux-Administration mitbringst und nicht nur Dienste, sondern auch die Netzwerk-Infrastruktur selbst betreiben willst.

**Nicht einrichten wenn:** Tailscale-Cloud für dich ausreicht und du keinen Grund siehst, etwas zu ändern. Tailscale ist ein etabliertes Produkt – Headscale ist die Antwort auf die Frage „Was, wenn ich es selbst hosten will und den Aufwand nicht scheue?"