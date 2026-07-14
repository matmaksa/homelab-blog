---
title: "Headscale im Homelab – Tailscale-Alternative selbst hosten"
date: 2026-06-29
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Headscale Mesh-VPN Dashboard – selbst gehosteter Tailscale Control Server im Homelab"
  relative: true
tags:
  - software
  - headscale
  - tailscale
  - mesh-vpn
  - wireguard
  - proxmox
  - lxc
  - selfhosting
  - netzwerk
categories:
  - Software

# Production State Flow
content_state: "published"
audit_status: "passed"
user_approval_required: false
approved_for_publish: true
instagram_derivatives_required: true
instagram_derivatives_status: "planned"
content_cluster: "headscale"
content_role: "pillar"
risk_level: "medium"
next_action: "manual_review_headscale_basis_commands_for_consistency"
related_articles:
  - "headscale-clients-acls-homelab"
notes:
  - "Published Headscale basis article."
  - "Align older Headscale CLI/config examples before publishing the follow-up."
  - "Instagram asset headscale-selfhost is planned/review_ready."
---

**Aktualisiert: Juni 2026 | Lesezeit: 7 Minuten**

<!--more-->

## Was ist Headscale? (In zwei Sätzen)

Headscale ist ein **Open-Source-Server** (MIT-Lizenz), der den gleichen Dienst bereitstellt wie die Tailscale-Cloud – nur dass **du** ihn auf deiner eigenen Hardware betreibst. Deine Geräte verbinden sich direkt per Wireguard-Verschlüsselung, ohne dass ein zentraler Cloud-Server die Kontrolle hat.

Wenn du noch keinen Proxmox-Server hast: Im [Mini-PC-Vergleich](/posts/mini-pc-homelab-vergleich/) findest du passende Hardware ab 40 €. Und falls du Proxmox noch nicht kennst: Der Artikel zur [kostenlosen Virtualisierung mit Proxmox](/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) zeigt dir den Einstieg.

---

## Warum Headscale statt Tailscale-Cloud?

Tailscale ist extrem einfach einzurichten. Aber mit der Entscheidung gibst du die Kontrolle über dein eigenes Netzwerk aus der Hand:

**Nachteile der Tailscale-Cloud:**
- Tailscale sieht, welche Geräte du verbindest (auch wenn sie die Daten nicht sehen können, wissen sie wer wer ist)
- Tailscale entscheidet über die Infrastruktur – Ausfall der Cloud = kein Mesh-VPN
- Tailscale schränkt die Anzahl der Nutzer ein (Personal-Plan: 3 Nutzer / 100 Geräte)
- Du musst einem US-Unternehmen vertrauen, dass der Dienst nicht eingestellt oder kostenpflichtig wird

**Vorteile von Headscale:**
- **Dein Netzwerk, deine Regeln** – Kein externer Dienst weiss, welche Geräte du verbindest
- **Unabhängig von Internet-Ausfällen** – solange deine Geräte im selben Netzwerk sind oder dich via DynDNS/Domain erreichen, läuft es
- **Kein Limit** – Unbegrenzte Geräte und Nutzer
- **Open Source** – voller Zugriff auf den Code, keine bösen Überraschungen
- **Eigene ACLs** – du definierst genau, wer auf wen zugreifen darf (nicht Tailscale)

---

## Alternativen im Vergleich

| Lösung | Kosten | Cloud nötig? | Einrichtung | Besonderheit |
|--------|--------|-------------|-------------|--------------|
| **Headscale** (Empfohlen)) | **0 €** | ❌ Nein | Mittel | Du hostest selbst, volle Kontrolle |
| Tailscale-Cloud | 0–6 €/Monat | ✅ Ja | Sehr einfach | Kein eigener Server nötig |
| Netbird | 0–8 €/Monat | Teilweise (kostenloser Plan: Cloud-Management) | Mittel | Open Source, ähnliches Konzept |
| ZeroTier | 0–5 €/Monat | Teilweise (Basis-Koordination via Cloud) | Einfach | Älter, breite Unterstützung |
| Manuelles Wireguard | **0 €** | ❌ Nein | Aufwändig | Volle Kontrolle, aber jede Verbindung manuell |

**Fazit zum Vergleich:** Tailscale ist am einfachsten, Headscale bietet die meiste Kontrolle. Wenn du bereits einen Proxmox-Server hast (wie die meisten Leser hier), ist Headscale der logische nächste Schritt – du hast die Hardware ja schon.

---

## Headscale installieren (Proxmox LXC)

Du brauchst: Einen Proxmox-Server, ein LXC-Container (Debian/Ubuntu), und eine Domain oder DynDNS-Adresse.

> ⚠️ **Wichtige Hürde:** Headscale muss von deinen Clients erreichbar sein. Das bedeutet: Du brauchst entweder eine öffentliche Domain mit DynDNS, einen Reverse Proxy mit HTTPS-Zertifikat oder zumindest eine VPN-Verbindung zwischen allen Geräten und dem LXC. Für FRITZ!Box-Nutzer ohne DynDNS ist das eine echte Hürde – du kannst entweder eine DDNS-Domain bei einem kostenlosen Anbieter (dyn.com, duckdns.org) einrichten oder zunächst im lokalen Netzwerk testen.

### 1. LXC-Container vorbereiten

Erstelle einen unprivilegierten LXC mit **Debian 12** (oder Ubuntu 24.04), mindestens **1 CPU-Kern**, **1 GB RAM**, **8 GB Speicher**.

Nach dem Erstellen:

```bash
apt update && apt upgrade -y
```

### 2. Headscale installieren

Lade das aktuelle .deb-Paket direkt von GitHub:

```bash
# Beispiel für Version 0.23.0 – aktuelle Version auf
# https://github.com/juanfont/headscale/releases prüfen!
wget https://github.com/juanfont/headscale/releases/latest/download/headscale_0.23.0_linux_amd64.deb
dpkg -i headscale_0.23.0_linux_amd64.deb
```

> **Wichtig:** Prüf vor der Installation die [aktuellste Version auf GitHub](https://github.com/juanfont/headscale/releases) und ersetze `0.23.0` durch die tatsächliche Versionsnummer.

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

# Magst du ändern:
dns:
  magic_dns: true
  base_domain: headscale.local
  nameservers:
    - 1.1.1.1
    - 9.9.9.9
```

Für den **öffentlichen Zugriff** richtest du am besten einen Reverse Proxy (Nginx, Caddy) oder eine Cloudflare-Tunnel ein. Der Einfachheit halber reicht erstmal ein lokaler Zugriff – deine Clients müssen den Server dann per LAN-IP erreichen können.

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

Lade den Tailscale-Client von [tailscale.com/download](https://tailscale.com/download) herunter. Bei der Installation wählst du nicht "Login with Google", sondern klickst auf das Tailscale-Icon in der Taskleiste → "Use a different server" → gib deine Headscale-URL ein.

### Verbindung prüfen

```bash
tailscale status
# Ausgabe:
# 100.x.x.x    homelab-server    headscale homelab  linux   active
# 100.x.x.x    desktop           headscale homelab  windows active
```

Deine Geräte sind jetzt per Mesh-VPN verbunden. Du erreichst jedes Gerät über seine Tailscale-IP (100.x.x.x).

---

## Grundlegende ACLs (Access Control Lists)

Ohne ACLs kann jedes deiner Geräte jedes andere erreichen – das kannst du mit einer kleinen Regel einschränken.

Erstelle `/etc/headscale/acl.hujson`:

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
    // Server dürfen sich untereinander sprechen
    { "action": "accept", "src": ["group:server"], "dst": ["group:server:*"] },
    // Clients dürfen nur Server erreichen (nicht andere Clients)
    { "action": "accept", "src": ["group:client"], "dst": ["group:server:*"] }
  ]
}
```

Aktiviere die ACLs in `config.yaml`:

```yaml
acl_policy_path: /etc/headscale/acl.hujson
```

Dann Headscale neustarten:

```bash
systemctl restart headscale
```

---

## Vorteile & Nachteile

| Vorteile | Nachteile |
|----------|-----------|
| Volle Kontrolle über dein VPN | Einrichtung aufwändiger als Tailscale-Cloud |
| Kein externer Dienst im Spiel | Du brauchst einen öffentlich erreichbaren Server (LXC, VPS) |
| Unbegrenzte Geräte + Nutzer | Kein offizielles Web-GUI (nur CLI + Drittanbieter) |
| Open Source (MIT) | Updates musst du selbst einspielen |
| Funktioniert an jeder FRITZ!Box, kein Port-Forwarding | Reverse Proxy für HTTPS nötig |
| Wireguard-Verschlüsselung (schnell, sicher) | |

---

## Für wen geeignet?

- **Du hast bereits einen Proxmox-Server** und suchst nach einer echten Alternative zur Tailscale-Cloud
- **Du hostest mehrere Dienste** und willst sie per Mesh-VPN verbinden, ohne Ports in der FRITZ!Box freizugeben
- **Du möchtest verstehen, wie dein Mesh-VPN funktioniert** auf TCP/IP-Ebene und nicht nur "es läuft"
- Tailscale-Nutzer, die mehr Kontrolle wollen

---

## Für wen ungeeignet?

- **Du willst einfach nur schnell zwei Geräte verbinden** – dann installier Tailscale, Headscale ist overkill
- **Du hast nur ein Gerät im Homelab** – ein Mesh-VPN lohnt sich erst ab 2-3 Geräten
- **Du möchtest keine Kommandozeile sehen** – Headscale hat kein einfaches Web-GUI
- **Du hast keinen öffentlich erreichbaren Server** (oder willst keinen DynDNS/RP einrichten)

---

## Fazit

Headscale ist die richtige Lösung wenn du Tailscale kennst aber die Cloud-Komponente nicht magst. Der Aufwand für die Einrichtung ist überschaubar (~30 Minuten) und die Vorteile sind klar: **Dein Netzwerk, deine Regeln, kein externer Dienst**.

**Kosten:** 0 € (Headscale läuft in einem LXC auf deinem bestehenden Proxmox-Server)

**Einrichten wenn:** Du bereits mehrere Geräte in deinem Homelab hast und den nächsten Schritt in Richtung Selfhosting machen willst – nicht nur Dienste, sondern auch die Netzwerk-Infrastruktur selbst betreiben willst.

**Nicht einrichten wenn:** Tailscale-Cloud für dich völlig ausreicht und du keinen Grund siehst, etwas zu ändern. Tailscale ist ein gutes Produkt – Headscale ist nur die Antwort auf die Frage "Was, wenn ich es selbst hosten will?"
