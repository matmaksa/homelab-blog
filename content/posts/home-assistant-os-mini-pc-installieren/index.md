+++
title = "Home Assistant OS auf dem Mini-PC installieren"
description = "Schritt-für-Schritt: Home Assistant OS auf einem x86-64-Mini-PC installieren – Image schreiben, UEFI-Boot, Unterschied zu HA Container und wichtige Warnungen."
date = 2026-07-16
draft = false
ShowToc = true
ShowShareButtons = true
ShowBreadCrumbs = true
ShowPostNavLinks = true
ShowCodeCopyButtons = true

tags = ["home-assistant", "smart-home", "installation", "mini-pc", "anleitung"]
categories = ["Smarthome"]

content_state = "published"
audit_status = "passed"
user_approval_required = false
approved_for_publish = true
instagram_derivatives_required = false
content_cluster = "home-assistant"
content_role = "guide"
risk_level = "medium"

[cover]
  image = "featured.jpg"
  alt = "Home Assistant OS Installation auf einem Mini-PC"
  relative = true
+++

**Aktualisiert: Juli 2026 | Lesezeit: 7 Minuten**

Dieser Artikel zeigt dir, wie du **Home Assistant OS (HAOS)** auf einem gebrauchten x86-64-Mini-PC installierst. Die Anleitung folgt der [aktuellen offiziellen Home-Assistant-Dokumentation](https://www.home-assistant.io/installation/generic-x86-64).

> **Vor dem Start:** Lies zuerst den Artikel zur [Hardware-Auswahl für Home Assistant]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}}). Dort erfährst du, welcher Mini-PC zu dir passt und was du außer dem PC noch brauchst.

<!--more-->

---

## Home Assistant OS vs. Home Assistant Container – der wichtige Unterschied

Bevor du startest, musst du die beiden Varianten unterscheiden:

| Merkmal | Home Assistant OS | Home Assistant Container |
|---------|------------------|------------------------|
| **Installation** | Komplettes Betriebssystem – wird auf die interne SSD geschrieben | Läuft als Docker-Container auf einem bestehenden Linux |
| **Supervisor** | ✅ Ja – ermöglicht Add-ons und einfache Verwaltung | ❌ Nein – kein Supervisor, keine Add-ons |
| **Add-ons** | ✅ Ja – über den Supervisor einfach installierbar | ❌ Nein – alles manuell per Docker |
| **Zielgruppe** | Einsteiger und die meisten Nutzer | Fortgeschrittene mit Linux-Kenntnissen |
| **Wartung** | Automatische Updates (optional) | Manuelle Container-Updates |

**Dieser Artikel beschreibt die Installation von Home Assistant OS.** Die Container-Variante ist nur etwas für erfahrene Nutzer, die bereits Docker betreiben und auf den Supervisor verzichten können.

---

## Voraussetzungen

| Was du brauchst | Hinweis |
|----------------|---------|
| Mini-PC mit **x86-64** (64-Bit Intel/AMD) | Die meisten [Mini-PCs und Thin Clients]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}}) ab 2016 erfüllen diese Voraussetzung |
| **UEFI** (modernes BIOS) | Wird von HAOS zwingend benötigt – die meisten Geräte ab Baujahr 2015 haben UEFI |
| **Interner SSD-Speicher** (mindestens 16 GB) | HAOS wird direkt auf die interne SSD geschrieben |
| USB-Stick (mindestens 8 GB) | Für Methode A: **separater Ubuntu-Live-USB-Stick** |
| Zweiter PC mit Internetzugang | Zum Herunterladen des HAOS-Images und Erstellen des USB-Sticks |
| Monitor und Tastatur | Nur für die Erstinstallation |
| LAN-Kabel | Für die Installation und den ersten Start wird eine kabelgebundene Ethernet-Verbindung empfohlen. WLAN kann abhängig von Hardware und Treiber funktionieren, ist für die Ersteinrichtung aber nicht der bevorzugte Weg. Internet wird für den ersten Start empfohlen, da HAOS Updates und Integrationen lädt. |

### BIOS einstellen: UEFI aktivieren, Secure Boot deaktivieren

Home Assistant OS benötigt **UEFI** als Boot-Modus. Die meisten Mini-PCs und Business-Clients ab Baujahr 2015 haben UEFI.

1. **Ins BIOS gelangen:** Beim Einschalten wiederholt **F2**, **F10**, **Entf** oder **F1** drücken (je nach Hersteller).
2. **UEFI-Boot aktivieren:** Suche nach *Boot Mode* oder *Boot Configuration* und stelle auf **UEFI** (nicht Legacy/CSM).
3. **Secure Boot deaktivieren:** Suche nach *Secure Boot* → **Disabled**.
4. **Einstellungen speichern und BIOS verlassen.**

Sollte dein Gerät nur Legacy-Boot unterstützen, ist HAOS nicht installierbar – hier hilft nur ein neueres Gerät oder die Container-Variante auf einem Linux-System.

> ⚠️ **Secure Boot** muss deaktiviert sein. HAOS bootet nicht zuverlässig mit aktiviertem Secure Boot.

---

## Wichtiger Hinweis: HAOS hat keinen normalen USB-Installer

Home Assistant OS enthält **keinen interaktiven Installer**, den du starten und mit ein paar Klicks ausführen kannst. Stattdessen wird das HAOS-Image **direkt auf das spätere Bootlaufwerk geschrieben** – also auf die interne SSD deines Mini-PCs.

Du brauchst daher ein Hilfssystem (Ubuntu-Live-USB), um das Image auf das Ziellaufwerk zu übertragen.

> ⚠️ **Warnung vor Datenverlust:** Beim Schreiben des Images werden **alle vorhandenen Daten auf dem Ziellaufwerk vollständig und unwiderruflich gelöscht**. Stelle sicher, dass du vorher alle wichtigen Daten gesichert hast. Kontrolliere vor dem Schreiben **immer** die Laufwerksgröße und den Gerätenamen.

---

## Methode A: Installation über Ubuntu-Live-USB (empfohlen – grafische Oberfläche)

Diese Methode verwendet einen **separaten Ubuntu-Live-USB-Stick**, von dem du den Mini-PC startest. Aus der grafischen Live-Umgebung heraus lädst du das HAOS-Image herunter und schreibst es mit der vorinstallierten **Laufwerke**-Anwendung (Disks) auf die interne SSD.

> **Wichtig:** Der Ubuntu-Live-USB-Stick und das spätere HAOS-System sind zwei verschiedene Dinge. Du bootest Ubuntu als Hilfssystem, nicht HAOS. Das HAOS-Image wird auf die **interne SSD** geschrieben.

### Schritt 1: Ubuntu-Live-USB-Stick erstellen

Lade das aktuelle **Ubuntu Desktop**-Image von [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) herunter und erstelle einen bootfähigen USB-Stick:

- **Windows:** [Balena Etcher](https://www.balena.io/etcher/) oder [Rufus](https://rufus.ie/) (Modus: *DD-Image*)
- **Linux/macOS:** `dd` oder Balena Etcher

Der USB-Stick sollte mindestens **8 GB** groß sein. Dieser Stick enthält das **Ubuntu-Live-System** – nicht das HAOS-Image.

### Schritt 2: Mini-PC vom Ubuntu-Stick starten

1. Stecke den Ubuntu-Live-USB-Stick in den Mini-PC.
2. Schalte den Mini-PC ein und rufe das **Boot-Menü** auf (meist **F12**, **F10** oder **ESC** – je nach Hersteller).
3. Wähle den USB-Stick als Boot-Medium.
4. Wähle im Ubuntu-Boot-Menü **"Ubuntu ausprobieren"** (Try Ubuntu).

Das System startet nun in die Ubuntu-Live-Umgebung – eine voll funktionsfähige, aber **nicht installierte** Desktop-Oberfläche. Ubuntu läuft dabei ausschließlich vom USB-Stick, nicht von der internen SSD.

### Schritt 3: Netzwerk verbinden und HAOS-Image herunterladen

Stelle eine Internetverbindung her (LAN-Kabel einstecken – das wird automatisch erkannt). Öffne dann den Firefox-Browser und lade das aktuelle **Home Assistant OS Generic x86-64**-Image herunter:

👉 [home-assistant.io/installation/generic-x86-64](https://www.home-assistant.io/installation/generic-x86-64)

Wähle dort den Abschnitt **"Generic x86-64"** und lade das `.img.xz`-File herunter. Speichere es im Ordner **"Downloads"** (Standard-Download-Pfad). Die genaue Versionsnummer im Dateinamen kann variieren – das ist normal.

**Achtung beim Download:** Es gibt mehrere Varianten – wähle immer **Generic x86-64**:
- **Generic x86-64** – ✅ Das richtige für normale Mini-PCs und Thin Clients
- **Raspberry Pi** – ❌ Nur für Raspberry Pi
- **VMware / VirtualBox** – ❌ Nur für virtuelle Maschinen
- **Odroid / ASUS Tinker Board** – ❌ Nur für diese speziellen ARM-Geräte

### Schritt 4: Ziel-SSD in der Laufwerke-Anwendung identifizieren

Öffne die Anwendung **"Laufwerke"** (Disks). Du findest sie über die Ubuntu-Suche (❖-Taste → "Laufwerke" tippen).

Die Anwendung zeigt alle angeschlossenen Laufwerke in einer Seitenleiste. Klicke jedes Laufwerk an und prüfe:

1. **Modellbezeichnung** – z. B. "Samsung SSD 860 EVO" oder "SanDisk SD8SNAT"
2. **Größe** – z. B. 120 GB oder 240 GB
3. **Gerätename** – z. B. `/dev/sda` (SATA) oder `/dev/nvme0n1` (NVMe)

Das Ubuntu-Live-System erkennst du an der Größe des USB-Sticks (z. B. 8 GB oder 16 GB). **Das interne Laufwerk ist dein Ziel.** Der USB-Stick ist nicht das Ziel.

> ⚠️ **Warnung:** Verwechsle das Ziel-Laufwerk nicht mit dem Ubuntu-USB-Stick. Kontrolliere **immer** Modell, Größe und Gerätenamen. Ein Fehler hier zerstört alle Daten auf dem falschen Laufwerk.

### Schritt 5: HAOS-Image auf die interne SSD schreiben

1. Wähle in der Seitenleiste das **interne Ziellaufwerk** aus.
2. Klicke auf das **☰ (Drei-Punkte-Menü)** rechts oben in der Laufwerks-Ansicht.
3. Wähle **"Datenträgerabbild wiederherstellen"** (Restore Disk Image).
4. Wähle die heruntergeladene `.img.xz`-Datei aus dem Download-Ordner aus.
   > **Hinweis zur .img.xz-Datei:** Die Laufwerke-Anwendung entpackt das komprimierte Image automatisch. Du musst die Datei **nicht** manuell entpacken.
5. Bestätige die Warnung – ja, du willst alle Daten auf dem Ziellaufwerk löschen.
6. Der Schreibvorgang startet. Die Anwendung zeigt den Fortschritt an. Der Vorgang dauert je nach Laufwerk **2–5 Minuten**.

**Erwartetes Ergebnis:** Nach Abschluss zeigt die Laufwerke-Anwendung eine Erfolgsmeldung an. Die Partitionstabelle des Ziellaufwerks hat sich verändert.

### Schritt 6: Abschluss

1. Klicke in Ubuntu auf das obere rechte Symbol → **Ausschalten** → **Herunterfahren**.
2. Sobald der Mini-PC aus ist: **Entferne den Ubuntu-USB-Stick**.
3. Schalte den Mini-PC wieder ein – er bootet jetzt direkt von der internen SSD.

> **Hinweis:** Sollte der Mini-PC nach dem Einschalten nicht von der SSD booten, prüfe im BIOS: Ist UEFi-Boot aktiv? Ist die Boot-Reihenfolge korrekt (interne SSD vor USB)?

---

## Alternative für erfahrene Linux-Nutzer: Image mit `dd` schreiben

Wenn du mit dem Terminal vertraut bist und die grafische Oberfläche nicht nutzen möchtest (oder kein Ubuntu-Desktop zur Verfügung steht), kannst du das Image auch per Kommandozeile schreiben.

### Vorbereitung

1. Führe Schritt 1–3 wie bei Methode A aus (Ubuntu-Live-USB erstellen, booten, Image herunterladen).

### Ziel-SSD identifizieren

Öffne ein Terminal (Strg + Alt + T) und führe aus:

```bash
lsblk
```

Die Ausgabe zeigt alle Laufwerke. Die interne SSD ist meist `/dev/sda` (SATA) oder `/dev/nvme0n1` (NVMe). Der USB-Stick ist meist `/dev/sdb`. Kontrolliere anhand der Größe, welches Laufwerk dein Ziel ist.

> ⚠️ **GEFAHR – Datenverlust:** Ein falscher Gerätename in `dd` zerstört **sofort und unwiderruflich** sämtliche Daten auf dem gewählten Laufwerk. Kontrolliere den Gerätenamen **vor** dem Befehl **mehrfach** mit `lsblk`. Schreibe ihn auf, bevor du fortfährst.

### Image schreiben

Wechsle in das Download-Verzeichnis und führe den Befehl aus – **ersetze `/dev/sda` durch dein tatsächliches Ziellaufwerk**:

```bash
cd ~/Downloads
xzcat haos_generic-x86-64-*.img.xz | sudo dd of=/dev/sda bs=4M status=progress
```

- `xzcat` entpackt das komprimierte Image
- `sudo dd` schreibt es Block für Block auf das Ziel
- `status=progress` zeigt den Fortschritt an
- Ersetze `/dev/sda`, falls dein Ziellaufwerk anders heißt

Der Vorgang dauert **2–5 Minuten**. Nach Abschluss:

```bash
sudo sync
```

### Abschluss

Wie bei Methode A: System herunterfahren (`sudo shutdown -h now`), USB-Stick entfernen, Mini-PC einschalten.

---

## Methode B: Direktes Flashen des Images (Laufwerk ausbauen)

Diese Methode eignet sich, wenn du das interne Laufwerk ausbaust und an einem zweiten Rechner flashen möchtest.

### Schritt 1: Laufwerk ausbauen und anschließen

1. Baue die interne SSD aus dem Mini-PC aus (bei Thin Clients meist über eine Klappe auf der Unterseite zugänglich).
2. Schließe das Laufwerk per **USB-Adapter** oder externem Gehäuse an einen zweiten PC an.

### Schritt 2: Image auf das Laufwerk schreiben

**Mit Balena Etcher (Windows/Linux/macOS):**
1. Balena Etcher öffnen
2. Heruntergeladene `.img.xz`-Datei auswählen (Etcher entpackt automatisch)
3. Das externe Laufwerk als Ziel auswählen
4. "Flash!" klicken

> ⚠️ **Achtung:** Wähle in Etcher genau das ausgebaute Laufwerk aus – nicht dein System-Laufwerk. Die Größe des Laufwerks ist dein Anhaltspunkt.

**Mit `dd` (Linux):**
```bash
xzcat ~/Downloads/haos_generic-x86-64-*.img.xz | sudo dd of=/dev/sdX bs=4M status=progress
sudo sync
```
Ersetze `/dev/sdX` durch das externe Laufwerk.

### Schritt 3: Laufwerk einbauen und starten

1. Baue die SSD wieder in den Mini-PC ein.
2. Schließe alle Kabel an und schalte den Mini-PC ein.

---

## Nach dem ersten Start – HAOS einrichten

Unabhängig von der gewählten Methode:

1. Der **erste Start kann 5–15 Minuten dauern** – HAOS richtet das System ein, erstellt die Datenpartition und startet alle Dienste. Sei geduldig, das ist normal.
2. Öffne anschließend einen Browser auf einem Gerät im selben Netzwerk.
3. Rufe folgende Adresse auf:

   ```
   http://homeassistant.local:8123
   ```

   **Falls `homeassistant.local` nicht funktioniert** (mDNS wird nicht von allen Routern unterstützt), findest du die IP-Adresse des Mini-PCs im Router-Interface unter "DHCP-Leases" oder "Verbundene Geräte". Rufe dann diese Adresse auf:

   ```
   http://<IP-ADRESSE>:8123
   ```

4. Folge dem Einrichtungsassistenten – Benutzer anlegen, Standort wählen, Geräte verbinden.

---

## Nach der Installation

Deine Home-Assistant-Installation läuft jetzt auf dem Mini-PC. Was jetzt?

- **Geräte verbinden:** Zigbee-Stick einstecken, WLAN-Geräte suchen lassen
- **Erste Automation:** Licht schalten, Temperatur messen
- **Add-ons:** Über den Supervisor-Bereich lassen sich zusätzliche Dienste wie Zigbee2MQTT oder Node-RED installieren

Wenn du später Frigate (Kameras mit KI-Objekterkennung), Immich (Fotoverwaltung) oder lokale KI-Sprachassistenten betreiben möchtest, sind das mögliche Ausbauoptionen für die Zukunft – für den Start nicht nötig.

---

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| Mini-PC bootet nicht von der SSD | BIOS-Prüfung: Ist **UEFI-Boot aktiviert**? Ist **Secure Boot deaktiviert**? Boot-Reihenfolge korrekt (SSD vor USB)? |
| Bootet immer noch vom USB-Stick | USB-Stick entfernen, Boot-Reihenfolge im BIOS prüfen |
| `homeassistant.local` nicht erreichbar | Prüfe die IP des Mini-PCs im Router. Browser → `http://<IP>:8123` |
| Ubuntu-Live-System startet nicht | Boot-Menü (F12/F10/ESC) beim Einschalten drücken. Secure Boot ggf. deaktivieren |
| SSD wird nicht erkannt | Prüfe im BIOS, ob die SSD sichtbar ist. Bei Futro: **kein NVMe!** Nur M.2 SATA |
|| HAOS startet, aber Web-UI nicht erreichbar | Prüfe, ob der Mini-PC per LAN-Kabel angeschlossen ist – für Installation und ersten Start wird eine kabelgebundene Ethernet-Verbindung empfohlen. WLAN kann abhängig von Hardware und Treiber funktionieren, ist für die Ersteinrichtung aber nicht der bevorzugte Weg. |
| Image-Schreiben bricht ab | Reicht die SSD-Größe aus? HAOS benötigt mindestens 16 GB |
|| Nach BIOS-Änderung bootet nichts mehr | BIOS-Standardwerte über **Load Setup Defaults** wiederherstellen. Falls das Gerät nicht mehr startet, den vom Hersteller dokumentierten BIOS-Reset verwenden. |

---

## Fazit

HAOS wird **direkt auf die interne SSD geschrieben** – es gibt keinen interaktiven Installer. Das ist der wichtigste Unterschied zu anderen Betriebssystemen.

**Wichtige Punkte zum Mitnehmen:**
- **Methode A (empfohlen):** Ubuntu-Live-USB mit der grafischen Laufwerke-Anwendung (Disks) – kein Terminal nötig
- **dd-Alternative:** Eine klar getrennte Methode für erfahrene Nutzer, die das Terminal bevorzugen
- **Methode B:** Laufwerk ausbauen und extern flashen – gut als Alternative, wenn der Mini-PC keinen einfachen Zugang zu Ubuntu erlaubt
- **UEFI ist zwingend erforderlich**, Secure Boot muss deaktiviert sein
- **Alle Daten auf dem Ziellaufwerk werden gelöscht** – vor dem Schreiben immer Modell, Größe und Gerätenamen kontrollieren
- HAOS ≠ HA Container (Container hat keinen Supervisor/Add-ons)
- Nach der Installation: Browser öffnen und `http://homeassistant.local:8123` oder die IP-Adresse aufrufen

👉 Zurück zum [Hardware-Artikel: Welcher Mini-PC für Home Assistant?]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}})
