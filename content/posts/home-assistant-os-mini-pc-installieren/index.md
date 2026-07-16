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

**Aktualisiert: Juli 2026 | Lesezeit: 5 Minuten**

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
|-----------------|---------|
| Mini-PC mit **x86-64** (64-Bit Intel/AMD) | Die meisten [Mini-PCs und Thin Clients]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}}) ab 2016 erfüllen diese Voraussetzung |
| **UEFI** (modernes BIOS) | Wird von HAOS zwingend benötigt – die meisten Geräte ab Baujahr 2015 haben UEFI |
| **Interner SSD-Speicher** (mindestens 16 GB) | HAOS wird direkt auf die interne SSD geschrieben |
| USB-Stick (mindestens 2 GB) | Nur zum Zwischenspeichern des Images – **kein USB-Installer** (siehe unten) |
| Monitor und Tastatur | Nur für die Erstinstallation |
| LAN-Kabel | WLAN wird von HAOS nicht unterstützt |

### Zwingend: UEFI

Home Assistant OS benötigt **UEFI** als Boot-Modus. Die meisten Mini-PCs und Business-Clients ab Baujahr 2015 haben UEFI. Im BIOS findest du diesen Modus als **UEFI Boot** (nicht Legacy/CSM).

Sollte dein Gerät nur Legacy-Boot unterstützen, ist HAOS nicht installierbar – hier hilft nur ein neueres Gerät oder die Container-Variante auf einem Linux-System.

---

## Wichtiger Hinweis: HAOS hat keinen normalen USB-Installer

Im Gegensatz zu den meisten Betriebssystemen (Ubuntu, Proxmox, Windows) besitzt Home Assistant OS **keinen interaktiven Installer**, den du von einem USB-Stick starten und dann auf die SSD installieren kannst.

Stattdessen wird das HAOS-Image **direkt auf die interne SSD des Mini-PCs geschrieben** – der USB-Stick dient nur als Zwischenspeicher, von dem du das Image auf die SSD überträgst.

> ⚠️ **Warnung vor Datenverlust:** Beim Schreiben des Images auf die SSD werden **alle vorhandenen Daten auf dem Ziellaufwerk vollständig und unwiderruflich gelöscht**. Stelle sicher, dass du vorher alle wichtigen Daten gesichert hast.

---

## Schritt 1: Image herunterladen

Lade das aktuelle **Home Assistant OS Generic x86-64**-Image von der offiziellen Home-Assistant-Website herunter:

👉 [home-assistant.io/installation/generic-x86-64](https://www.home-assistant.io/installation/generic-x86-64)

Wähle dort den Abschnitt **"Generic x86-64"** und lade das `.img.xz`-File herunter. Das ist ein komprimiertes Image des gesamten HAOS-Betriebssystems.

**Achtung beim Download:** Es gibt mehrere Varianten:
- **Generic x86-64** – ✅ Das richtige für normale Mini-PCs und Thin Clients
- **Raspberry Pi** – ❌ Nur für Raspberry Pi
- **VMware / VirtualBox** – ❌ Nur für virtuelle Maschinen
- **Odroid / ASUS Tinker Board** – ❌ Nur für diese speziellen ARM-Geräte

---

## Schritt 2: Image auf die interne SSD schreiben

Da HAOS keinen USB-Installer besitzt, gibt es zwei Wege, das Image auf die interne SSD zu bringen.

### Weg A: Direktes Schreiben von einem Linux-Live-System (empfohlen)

1. Schreib das heruntergeladene `.img.xz`-Image mit **Balena Etcher** oder **Rufus** auf einen USB-Stick
2. **Fahre den Mini-PC komplett herunter** und schalte ihn aus
3. Entferne alle internen Laufwerke bis auf die Ziel-SSD – oder bereite dich darauf vor, das richtige Laufwerk zu identifizieren
4. **Stecke den USB-Stick ein** und starte den Mini-PC vom USB-Stick (ggf. Boot-Reihenfolge im BIOS anpassen)
5. Der Stick bootet ein Linux-Live-System (je nach Tool)
6. Identifiziere im Terminal die Ziel-SSD mit `lsblk` (sie ist meist `/dev/sda` oder `/dev/nvme0n1`)
7. Übertrage das Image auf die SSD:

```bash
# Beispiel – Passe den Pfad zur SSD an!
xzcat /pfad/zum/image.img.xz | dd of=/dev/sda bs=4M status=progress
```

8. Nach erfolgreichem Schreiben: `sync` ausführen, USB-Stick entfernen, Mini-PC neustarten

### Weg B: Über ein bestehendes Linux

Wenn auf dem Mini-PC bereits ein Linux (Ubuntu, Debian) installiert ist:

1. Lade das HAOS-Image auf dem Mini-PC herunter
2. Identifiziere die Ziel-SSD mit `lsblk`
3. Übertrage das Image:

```bash
xzcat ~/haos_generic-x86-64.img.xz | sudo dd of=/dev/sda bs=4M status=progress
sudo sync
```

4. **Mini-PC ausschalten**, nicht neu starten – damit HAOS booten kann

---

## Schritt 3: HAOS starten und einrichten

Nachdem du das Image auf die SSD geschrieben hast:

1. **Entferne den USB-Stick** (falls noch eingesteckt)
2. Starte den Mini-PC neu
3. HAOS bootet jetzt direkt von der internen SSD
4. Der erste Start dauert etwa 5–15 Minuten – HAOS richtet das System ein
5. Sobald der Bootvorgang abgeschlossen ist, öffnest du im Browser:

```
http://homeassistant.local:8123
```

Falls die `.local`-Adresse nicht funktioniert, findest du die IP-Adresse des Mini-PCs in deinem Router-Interface.

6. Folge dem Einrichtungsassistenten – Benutzer anlegen, Standort wählen, Geräte verbinden.

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
| Mini-PC bootet nicht von der SSD | BIOS-Prüfung: Ist **UEFI-Boot aktiviert** und die Boot-Reihenfolge korrekt? |
| `homeassistant.local` nicht erreichbar | Prüfe die IP des Mini-PCs im Router. Browser → `http://<IP>:8123` |
| SSD wird nicht erkannt | Prüfe im BIOS, ob die SSD sichtbar ist. Bei Futro: **kein NVMe!** Nur M.2 SATA |
| Bootet immer noch vom USB-Stick | USB-Stick entfernen, Boot-Reihenfolge im BIOS prüfen |

---

## Fazit

Die Installation von Home Assistant OS auf einem Mini-PC ist unkompliziert, wenn du den Unterschied zu einem normalen USB-Installer verstanden hast. HAOS wird direkt auf die interne SSD geschrieben – das macht den Vorgang anders als bei den meisten Betriebssystemen, aber dafür läuft das System danach sauber und stabil.

**Wichtige Punkte zum Mitnehmen:**
- HAOS wird **direkt auf die SSD geschrieben** – kein USB-Installer
- **UEFI** ist zwingend erforderlich
- **Alle Daten auf dem Ziellaufwerk werden gelöscht**
- HAOS ≠ HA Container (Container hat keinen Supervisor/Add-ons)
- Nach der Installation: Browser öffnen und `http://homeassistant.local:8123` aufrufen

👉 Zurück zum [Hardware-Artikel: Welcher Mini-PC für Home Assistant?]({{< relref "home-assistant-gebrauchter-mini-pc-2026" >}})
