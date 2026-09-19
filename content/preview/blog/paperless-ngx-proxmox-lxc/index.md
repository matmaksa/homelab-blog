+++
title = "Paperless-ngx im Proxmox-LXC installieren: Dokumente selbst hosten"
description = "Installiere Paperless-ngx im Proxmox LXC mit dem Community-Script. Digitale Dokumentenverwaltung für Einsteiger – mit Screenshots."
date = 2026-09-19
draft = false
robotsNoIndex = true
noindex = true
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
tags = ["paperless-ngx", "proxmox", "lxc", "homelab", "ocr"]
categories = ["Homelab", "Virtualisierung"]

[sitemap]
  exclude = true

# Preview Classification
preview_content_type = "article_draft"
publish_eligible = false
user_visual_approval_required = true
fact_check_required = true
link_check_required = true
price_check_required = false
recommended_action = "Screenshots prüfen und Testdokument importieren vor Publikation."
content_intent = "howto"
monetization_intent = "none"
affiliate_disclosure_required = false
+++

# Paperless-ngx im Proxmox-LXC installieren: Digitale Dokumentenverwaltung für Einsteiger

Hast du auch genug von Papierbergen im Schrank? Rechnungen, Verträge, Quittungen – irgendwann findet niemand mehr das, was er braucht. Paperless-ngx löst dieses Problem. Die Software digitalisiert deine Dokumente automatisch, erkennt den Text per OCR und macht alles durchsuchbar. Du behältst den Überblick, ohne einen einzigen Zettel zu verlieren.

In diesem Artikel zeige ich Schritt für Schritt, wie du Paperless-ngx in einem Proxmox-LXC einrichtest – ganz ohne Docker, ganz easy.

---

## Was ist Paperless-ngx?

Paperless-ngx ist eine kostenlose Open-Source-Software für die digitale Dokumentenverwaltung. Du lädst Fotos oder gescannte PDFs hoch, und das System:

- **Erkennt den Text per OCR** – auch handschriftliche Notizen und gescannte Papiere werden durchsuchbar
- **Ordnet automatisch ein** – mit Tags, Dokumenttypen und Absendern
- **Erstellt Archiv-PDFs** – im hochwertigen PDF/A-Format für die langfristige Aufbewahrung
- **Macht alles suchbar** – finde jeden Satz in Sekunden, nicht nur Dateinamen

Alles läuft lokal auf deinem Server. Keine Cloud, kein Dritter sieht deine Daten.

---

## Voraussetzungen

Bevor wir starten, brauchst du:

- Einen Proxmox VE Host (z.B. deinen Home-Server)
- SSH-Zugang als root
- Einen freien Container auf Proxmox (oder Lust auf einen neuen)
- Mindestens 10 GB Speicher und 2 GB RAM verfügbar

---

## Schritt 1: Container mit dem Community-Script erstellen

Der schnellste Weg führt über das offizielle Community-Script von Proxmox. Es installiert alles automatisch.

### Option A: Automatisches Script (empfohlen)

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/paperless-ngx.sh)"
```

Das Script fragt ein paar Dinge ab (Container-Name, IP etc.) und erledigt den Rest: Debian 13 wird installiert, PostgreSQL, Redis, Paperless-ngx, Tesseract OCR und alle Services konfiguriert.

### Option B: Container manuell erstellen

Wenn du selbst bestimmen willst, was passiert:

```bash
# Container erstellen
pct create 103 local:debian-13-standard_13.11-1_amd64.tar.zst \
  --hostname paperless \
  --cores 2 \
  --memory 2048 \
  --rootfs local-lvm:10 \
  --net0 name=eth0,ip=dhcp,gw=192.168.1.1 \
  --unprivileged 1

# Starten
pct start 103
```

Danach loggst du dich in den Container ein und folgst dem [offiziellen Installationsguide](https://docs.paperless-ngx.com/setup/).

---

## Schritt 2: Umgebungskonfiguration anpassen

Paperless-ngx liest seine Einstellungen aus einer Konfigurationsdatei. Öffne sie:

```bash
nano /opt/paperless/paperless.conf
```

Trage mindestens diese Werte ein:

```ini
PAPERLESS_URL=http://deine-ip:8000
PAPERLESS_TIMEZONE=Europe/Berlin
PAPERLESS_LANGUAGE=de
PAPERLESS_OCR_LANGUAGE=deu
PAPERLESS_SECRET_KEY=deine_geheime_zufällige_key
```

**Wichtig:** Erzeuge einen echten Secret Key:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Schritt 3: Administrator-Benutzer anlegen

Jetzt erstellst du deinen ersten Login:

```bash
cd /opt/paperless/src
uv run python3 manage.py createsuperuser
```

Wähle einen Benutzernamen und ein starkes Passwort. Schreib sie auf – du wirst sie brauchen!

---

## Schritt 4: Services starten

Starte alle Paperless-Services und aktiviere sie für den Auto-Start:

```bash
systemctl enable --now paperless-webserver paperless-worker paperless-scheduler
```

Verifiziere, ob alles läuft:

```bash
systemctl status paperless-webserver paperless-worker paperless-scheduler
```

Alle drei sollten `active (running)` anzeigen.

![Paperless-ngx Services laufen im Container](services.webp)

*Die drei Hauptdienste sind aktiv – der Webserver, der Aufgaben-Worker und der Planer.*

---

## Schritt 5: Web-Oberfläche öffnen

Öffne in deinem Browser:

```
http://DEINE-IP:8000
```

Logge dich mit den Daten aus Schritt 3 ein.

![Login-Seite von Paperless-ngx](login.png)

*Die Anmeldeseite – hier gibst du deinen Benutzernamen und dein Passwort ein.*

Nach dem Login siehst du das Dashboard:

![Dashboard von Paperless-ngx](dashboard.webp)

*Das Dashboard zeigt dir auf einen Blick, wie viele Dokumente du bereits gespeichert hast. Rechts kannst du neue Dokumente hochladen.*

---

## Schritt 6: Dokumente hochladen und verwalten

### Manuelles Upload

Klicke im Dashboard auf **"Upload"** oder ziehe Dateien in den dafür vorgesehenen Bereich. Akzeptiert werden:

- PDFs (digital oder gescannt)
- Bilder (JPG, PNG, TIFF)
- Textdateien

### Was passiert beim Upload?

Sobald du eine Datei hochlädst, macht Paperless-ngx folgendes:

1. **OCR laufen lassen** – der Text wird erkannt
2. **Metadaten extrahieren** – Datum, Absender, Art des Dokuments
3. **PDF/A erstellen** – archiv-taugliches Format
4. **Volltext indizieren** – alles ist sofort durchsuchbar

Das dauert je nach Dateigröße 5–30 Sekunden.

### Organisation

Nach dem Import kannst du:

- **Tags** hinzufügen (z.B. "Rechnung", "Versicherung")
- Den **Dokumenttyp** wählen (Rechnung, Vertrag, etc.)
- Den **Absender** definieren (Energieversorger, Arbeitgeber, etc.)
- **Notizen** hinzufügen

---

## Schritt 7: Dokumente suchen

Das ist der eigentliche Clou: Du kannst **jedes Wort** suchen, das im Text vorkommt. Nicht nur Dateinamen, sondern auch Inhalt.

Tippe z.B. "Rechnung Dezember 2025" ein – Paperless findet es sofort, auch wenn die Datei "scan_001.pdf" heißt.

---

## Schritt 8: Backup und Restore

**Wichtig:** Backups sind überlebenswichtig! Du willst nicht Jahre organisierter Dokumente verlieren.

### Was muss backupt werden?

- **Dokumente:** `/opt/paperless/data/media/documents/`
- **Medien:** `/opt/paperless/data/media/`
- **Datenbank:** PostgreSQL
- **Einstellungen:** `/opt/paperless/paperless.conf`

### Methode 1: Integrierter Exporter

```bash
cd /opt/paperless/src
uv run python3 manage.py document_exporter /opt/paperless/export
```

Das erzeugt ein ZIP-Paket mit allen Dokumenten und Metadaten.

![Backup-Interface von Paperless-ngx](backup.webp)

*Einrichtung automatischer Backups für maximale Sicherheit.*

### Methode 2: PostgreSQL Dump

```bash
pg_dump -U paperless paperless > backup_$(date +%Y%m%d).sql
```

### Methode 3: Proxmox Backup

Erstelle ein vollständiges Backup des Containers über Proxmox. Einfach, aber ersetze nicht den Tests des Restore.

---

## Schritt 9: Externer Zugriff (optional)

Um von außen darauf zuzugreifen, konfiguriere einen Reverse-Proxy mit TLS. Optionen:

- **Nginx** mit Certbot (Let's Encrypt)
- **Caddy** (einfacher, auto-TLS)
- **Traefik** (falls bereits im Homelab im Einsatz)

Beispiel mit Nginx:

```nginx
server {
    listen 443 ssl;
    server_name paperless.deinedomain.com;

    ssl_certificate /etc/letsencrypt/live/deinedomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/deinedomain.com/privkey.pem;

    location / {
        proxy_pass http://IP-CONTAINER:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Troubleshooting

### OCR funktioniert nicht

Prüfe, ob Tesseract installiert ist und die Sprachen:

```bash
apt list --installed | grep tesseract
# Sollte zeigen: tesseract-ocr-eng, tesseract-ocr-deu (und andere)
```

### Dokumente erscheinen nicht in der Suche

Der Index kann veraltet sein. Erzwing einen Rebuild:

```bash
uv run python3 manage.py rebuild_index
```

### Oberfläche lädt nicht

Prüfe, ob der Service läuft:

```bash
systemctl status paperless-webserver
journalctl -u paperless-webserver -n 50
```

---

## Fazit

Paperless-ngx ist die definitive Lösung für alle, die den Papierkrieg zu Hause beenden wollen. Mit weniger als 2 GB RAM und 10 GB Speicher hast du ein professionelles Dokumentenverwaltungssystem auf deinem Proxmox laufen.

**Abschluss-Checkliste:**

- [ ] Container erstellt und Services laufen
- [ ] Administrator-Benutzer angelegt und Passwörter sicher gespeichert
- [ ] Erstes Dokument hochgeladen und OCR funktioniert
- [ ] Suche mit echten Keywords getestet
- [ ] Backup eingerichtet und getestet (Export + Dump)
- [ ] Reverse Proxy konfiguriert (falls externer Zugriff benötigt)
- [ ] Backup-Routine geplant (cron oder Proxmox Scheduler)

---

*Artigo baseado em teste prático em ambiente doméstico com Proxmox VE e Debian 13. Alguns detalhes podem variar conforme versão do sistema e configurações específicas.*

**Fontes:**
- [Documentação oficial Paperless-ngx](https://docs.paperless-ngx.com/)
- [Script comunidade Proxmox VE](https://github.com/community-scripts/ProxmoxVE)
