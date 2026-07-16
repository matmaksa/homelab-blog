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

**Aktualisiert: Juli 2026 | Lesezeit: 6 Minuten**

Dieser Artikel zeigt dir, wie du **Home Assistant OS (HAOS)** auf einem gebrauchten x86-64-Mini-PC installierst. Die Anleitung folgt der aktuellen offiziellen Home-Assistant-Dokumentation.

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
| USB-Stick (mindestens 4 GB) | Für Methode A: **separater Ubuntu-Live-USB-Stick** |
| Zweiter PC mit Internetzugang | Zum Herunterladen des HAOS-Images und Erstellen des USB-Sticks |
| Monitor und Tastatur | Nur für die Erstinstallation |
| LAN-Kabel | WLAN wird von HAOS nicht unterstützt |

### Zwingend: UEFI

Home Assistant OS benötigt **UEFI** als Boot-Modus. Die meisten Mini-PCs und Business-Clients ab Baujahr 2015 haben UEFI. Im BIOS findest du diesen Modus als **UEFI Boot** (nicht Legacy/CSM).

Sollte dein Gerät nur Legacy-Boot unterstützen, ist HAOS nicht installierbar – hier hilft nur ein neueres Gerät oder die Container-Variante auf einem Linux-System.

> ⚠️ **Secure Boot** muss unter Umständen deaktiviert werden. HAOS bootet nicht zuverlässig mit aktiviertem Secure Boot. Die Einstellung findest du im BIOS unter *Secure Boot* → *Disabled*.

---

## Wichtiger Hinweis: HAOS hat keinen normalen USB-Installer

Im Gegensatz zu den meisten Betriebssystemen (Ubuntu, Proxmox, Windows) besitzt Home Assistant OS **keinen interaktiven Installer**, den du von einem USB-Stick starten und dann auf die SSD installieren kannst.

Stattdessen wird das HAOS-Image **direkt auf die interne SSD des Mini-PCs geschrieben**. Du brauchst daher ein Hilfsmittel, um das Image auf das Ziellaufwerk zu übertragen.

> ⚠️ **Warnung vor Datenverlust:** Beim Schreiben des Images auf die SSD werden **alle vorhandenen Daten auf dem Ziellaufwerk vollständig und unwiderruflich gelöscht**. Stelle sicher, dass du vorher alle wichtigen Daten gesichert hast.

---

## Methode A: Installation über Ubuntu-Live-USB (empfohlen)

Diese Methode verwendet einen **separaten Ubuntu-Live-USB-Stick**, von dem du den Mini-PC startest. Aus der Live-Umgebung heraus lädst du das HAOS-Image herunter und schreibst es auf die interne SSD.

> **Wichtig:** Der Ubuntu-Live-USB-Stick und das spätere HAOS-System sind zwei verschiedene Dinge. Du bootest Ubuntu zum Zwischenschritt, nicht HAOS.

### Schritt 1: Ubuntu-Live-USB-Stick erstellen

Lade das aktuelle **Ubuntu Desktop**-Image (24.04 LTS oder neuer) von [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) herunter und erstelle einen bootfähigen USB-Stick:

- **Windows:** [Balena Etcher](https://www.balena.io/etcher/) oder [Rufus](https://rufus.ie/) (Modus: *DD-Image*)
- **Linux/macOS:** `dd` oder Balena Etcher

> Der USB-Stick sollte mindestens 4 GB groß sein. Dieser Stick dient **ausschließlich als Ubuntu-Live-System** – er wird nicht das HAOS-Image enthalten.

### Schritt 2: Mini-PC vom Ubuntu-Stick starten

1. Stecke den Ubuntu-Live-USB-Stick in den Mini-PC
2. Schalte den Mini-PC ein und rufe das Boot-Menü auf (meist **F12**, **F10** oder **ESC** – je nach Hersteller)
3. Wähle den USB-Stick als Boot-Medium
4. Wähle im Ubuntu-Boot-Menü **"Ubuntu ausprobieren"** (Try Ubuntu)

Das System startet nun in die Ubuntu-Live-Umgebung – eine voll funktionsfähige, aber nicht installierte Desktop-Oberfläche. Du kannst hier Programme ausführen und auf das Internet zugreifen.

### Schritt 3: HAOS-Image herunterladen

Öffne den Firefox-Browser in der Live-Umgebung und lade das aktuelle **Home Assistant OS Generic x86-64**-Image herunter:

👉 [home-assistant.io/installation/generic-x86-64](https://www.home-assistant.io/installation/generic-x86-64)

Wähle dort den Abschnitt **"Generic x86-64"** und lade die Datei `haos_generic-x86-64-xx.x.img.xz` herunter. Speichere sie im Ordner **"Downloads"** (Standard-Download-Pfad).

**Achtung beim Download:** Es gibt mehrere Varianten:
- **Generic x86-64** – ✅ Das richtige für normale Mini-PCs und Thin Clients
- **Raspberry Pi** – ❌ Nur für Raspberry Pi
- **VMware / VirtualBox** – ❌ Nur für virtuelle Maschinen
- **Odroid / ASUS Tinker Board** – ❌ Nur für diese speziellen ARM-Geräte

### Schritt 4: Ziel-SSD identifizieren

Öffne ein Terminal (Strg + Alt + T) und führe folgenden Befehl aus:

```bash
lsblk
```

Die Ausgabe zeigt alle angeschlossenen Laufwerke. Suche die **interne SSD** des Mini-PCs anhand der Größe:

- `/dev/sda` – bei SATA-SSD (häufig bei Thin Clients)
- `/dev/nvme0n1` – bei NVMe-SSD (bei neueren Mini-PCs)

> ⚠️ **Achtung:** Verwechsle das Ziel-Laufwerk nicht mit dem Ubuntu-USB-Stick (meist `/dev/sdb` oder `/dev/sdc`). Kontrolliere vor dem Schreiben immer die Laufwerksgröße und den Gerätenamen mit `lsblk`.

### Schritt 5: Image auf die interne SSD schreiben

Wechsle im Terminal in das Download-Verzeichnis und schreibe das Image:

```bash
cd ~/Downloads
xzcat haos_generic-x86-64-*.img.xz | sudo dd of=/dev/sda bs=4M status=progress
```

> **Erklärung:** `xzcat` entpackt das komprimierte Image und übergibt es an `dd`, das es Block für Block auf das Ziel-Laufwerk (`/dev/sda`) schreibt. `status=progress` zeigt den Fortschritt an.

Ersetze `/dev/sda` durch das in Schritt 4 ermittelte Ziel-Laufwerk.

Der Vorgang kann **2–5 Minuten** dauern, abhängig von der SSD-Geschwindigkeit.

**Erwartetes Ergebnis:** Nach dem Schreiben erscheint eine Meldung wie `XXX+0 Datensätze ein/aus`. Führe dann aus:

```bash
sudo sync
```

### Schritt 6: Abschluss

1. **Fahre das System herunter** (nicht neu starten):
   ```bash
   sudo shutdown -h now
   ```
2. **Entferne den Ubuntu-USB-Stick**
3. **Entferne ggf. andere USB-Geräte**
4. Schalte den Mini-PC wieder ein – er bootet jetzt direkt von der internen SSD

---

## Methode B: Direktes Flashen des Images (Fortgeschrittene)

Diese Methode ist nützlich, wenn du das HAOS-Image ohne Umwege auf das interne Laufwerk schreiben möchtest, z. B. mit einem zweiten Rechner.

### Schritt 1: Laufwerk ausbauen oder anschließen

1. **Baue die interne SSD / das interne Laufwerk aus dem Mini-PC aus** (bei den meisten Thin Clients über eine Klappe auf der Unterseite zugänglich)
2. **Schließe das Laufwerk per USB-Adapter an einen zweiten PC an**

Oder alternativ: Schließe das Laufwerk über einen externen USB-Enclosure an.

### Schritt 2: Image direkt auf das Laufwerk schreiben

Auf dem zweiten PC:

1. Lade das aktuelle HAOS-Image herunter: [home-assistant.io/installation/generic-x86-64](https://www.home-assistant.io/installation/generic-x86-64)
2. Identifiziere das externe Laufwerk mit `lsblk`
3. Schreibe das Image:

**Linux:**
```bash
xzcat ~/Downloads/haos_generic-x86-64-*.img.xz | sudo dd of=/dev/sdX bs=4M status=progress
sudo sync
```

**Windows mit Balena Etcher:**
1. Balena Etcher öffnen
2. Image-Datei auswählen
3. Ziel-Laufwerk auswählen
4. "Flash!" klicken

> ⚠️ **Achtung:** Wähle in Etcher genau das aus- oder umgebaute Laufwerk aus, nicht dein System-Laufwerk.

### Schritt 3: Laufwerk wieder einbauen und starten

1. Baue die SSD wieder in den Mini-PC ein
2. Schließe ggf. den Deckel und schließe alle Kabel an
3. Schalte den Mini-PC ein

---

## Nach dem ersten Start – HAOS einrichten

Unabhängig von der gewählten Methode:

1. Der **erste Start kann 5–15 Minuten dauern** – HAOS richtet das System ein, erstellt die Datenpartition und startet alle Dienste. Sei geduldig, das ist normal.
2. Öffne anschließend einen Browser auf einem Gerät im selben Netzwerk.
3. Rufe eine der folgenden Adressen auf:

   ```
   http://homeassistant.local:8123
   ```

   oder – falls die `.local`-Adresse nicht funktioniert – die vom Router vergebene IP-Adresse:

   ```
   http://<IP-DES-MINI-PCS>:8123
   ```

   > **Hinweis:** Ob `homeassistant.local` (mDNS) funktioniert, hängt von deinem Netzwerk ab. Nicht alle Router unterstützen mDNS-Weiterleitung. Die IP-Adresse findest du im Router-Interface unter "DHCP-Leases" oder "Verbundene Geräte".

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
| Mini-PC bootet nicht von der SSD | BIOS-Prüfung: Ist **UEFI-Boot aktiviert** und die **Boot-Reihenfolge** korrekt? |
| Bootet immer noch vom USB-Stick | USB-Stick entfernen, Boot-Reihenfolge im BIOS prüfen |
| `homeassistant.local` nicht erreichbar | Prüfe die IP des Mini-PCs im Router. Browser → `http://<IP>:8123` |
| Ubuntu-Live-System startet nicht | Boot-Menü (F12/F10/ESC) beim Einschalten drücken. Secure Boot ggf. deaktivieren |
| SSD wird nicht erkannt | Prüfe im BIOS, ob die SSD sichtbar ist. Bei Futro: **kein NVMe!** Nur M.2 SATA |
| `lsblk` zeigt keine Laufwerke | Prüfe, ob die SSD korrekt angeschlossen ist. Bei Methode B: Adapter prüfen |
| HAOS startet, aber Web-UI nicht erreichbar | Prüfe, ob der Mini-PC per LAN-Kabel angeschlossen ist (WLAN wird nicht unterstützt) |
| `dd`-Befehl bricht mit "Kein Speicherplatz" ab | Reicht die SSD-Größe aus? HAOS benötigt mindestens 16 GB |

---

## Fazit

Die Installation von Home Assistant OS auf einem Mini-PC ist unkompliziert, wenn du den grundlegenden Unterschied verstanden hast: HAOS wird **direkt auf die interne SSD geschrieben** – es gibt keinen interaktiven Installer.

**Wichtige Punkte zum Mitnehmen:**
- **Methode A (empfohlen):** Separaten Ubuntu-Live-USB-Stick erstellen, von dort das HAOS-Image auf die interne SSD schreiben
- **Methode B (alternativ):** Laufwerk ausbauen und direkt von einem anderen PC flashen
- **UEFI ist zwingend erforderlich**, Secure Boot ggf. deaktivieren
- **Alle Daten auf dem Ziellaufwerk werden gelöscht**
- Vor dem Schreiben: Laufwerksgröße und Gerätenamen mit `lsblk` kontrollieren
- HAOS ≠ HA Container (Container hat keinen Supervisor/Add-ons)
- Nach der Installation: Browser öffnen und `http://homeassistant.local:8123` oder die IP-Adresse aufrufen

👉 Zurück zum [Hardware-Artikel: Welcher Mini-PC für Home Assistant?]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}})
