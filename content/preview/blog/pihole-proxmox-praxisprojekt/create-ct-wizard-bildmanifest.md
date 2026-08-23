# Bildmanifest: Create-CT-Wizard-Screenshots (pihole-proxmox-praxisprojekt)

Erstellt: 2026-08-23 (Homelab-Admin, Kanban t_db5c6b43)
Quelle: PVE04-Testhost (192.168.20.4), Proxmox VE 9.2.11, Create-LXC-Wizard
Capture-Werkzeug: vm-hermes-browser (192.168.30.1) via SSH-Tunnel, Playwright/Chromium headless
Login: temporärer User screenshot@pve (Administrator auf / und /nodes/pve04, danach gelöscht)
Ablage (Roh): /tmp/pihole-proxmox-praxisprojekt/*.png
Ablage (Content): /root/homelab-blog/content/preview/blog/pihole-proxmox-praxisprojekt/*.webp

## Secrets-Status

- Alle Screenshots zeigen ausschließlich die im Artikel dokumentierten Labwerte:
  CT-ID 103 (freie Beispiel-ID; 101 ist im Testlab real belegt -> 01-pihole),
  Hostname 01-pihole, Template debian-13-standard_13.6-1_amd64.tar.zst,
  local-lvm, 8 GiB, 1 vCPU, 256 MiB RAM/Swap, Bridge vmbr0, VLAN-Tag 20,
  IPv4 192.168.20.201/24, Gateway 192.168.20.254, DNS 1.1.1.1/1.0.0.1.
- KEINE echten Passwörter im Bild: Root-Passwort-Feld wurde mit Fake-Wert
  "LabPasswort-2026" gefüllt und ist maskiert (•••••••••); kein Finish-Klick.
- Kein Login-User sichtbar (Window-Screenshots, Header nicht enthalten).
- Screenshot-User screenshot@pve wurde nach Abschluss gelöscht, Passwort-Dateien
  überschrieben, SSH-Tunnel beendet. Kein neuer Container erstellt (pct list:
  nur CT 101/102, keine neue /etc/pve/lxc/*.conf).

## Bilder

| Datei | Schritt | Inhalt (Labwerte) | Secrets-Status |
|---|---|---|---|
| 01-general.webp | General (leer) | CT ID 100 (Default), Node pve04, Hostname leer | ok |
| 02-general-filled.webp | General (gefüllt) | CT ID 103, Hostname 01-pihole, PW maskiert | ok |
| 03-template.webp | Template | Storage local, debian-13-standard_13.6-1_amd64.tar.zst | ok |
| 04-disks.webp | Disks | Storage local-lvm, Disk size 8 GiB | ok |
| 05-cpu.webp | CPU | 1 Core | ok |
| 06-memory.webp | Memory | 256 MiB RAM, 256 MiB Swap | ok |
| 07-network.webp | Network | eth0, vmbr0, VLAN 20, 192.168.20.201/24, GW 192.168.20.254 | ok |
| 08-dns.webp | DNS | DNS servers 1.1.1.1,1.0.0.1 | ok |
| 09-confirm.webp | Confirm | Zusammenfassung mit allen Labwerten | ok |
| 10-template-download.webp | Template-Download-Ansicht | Storage local, CT Templates, Download-Liste (debian-13 sichtbar) | ok |

## Technische Hinweise für die Einbindung

- 01-09: Wizard-Fenster 760x570 (WebP q82, ca. 6-19 KB)
- 10: Download-Dialog 900x600 (WebP q82, ca. 54 KB)
- Fenster-Screenshots zeigen den Create-LXC-Wizard von PVE 9.2. Die Wizard-Schritte
  heißen in PVE 9.2 General/Template/Disks/CPU/Memory/Network/DNS/Confirm (getrennt);
  die Artikel-Nomenklatur "Disk/CPU/Memory" kann als gemeinsamer Schritt gelesen werden.
- Beispiel-ID 103 wurde gewählt, weil 101 im Testlab real existiert; der Artikeltext
  sagt bereits "wähle eine bei dir freie ID" - Caption entsprechend ergänzen.

## Einbindung (2026-08-23, blog-creator)

- Alle 10 Screenshots sind in `index.md` (Preview-Artikel) im Abschnitt
  "1. Container in Proxmox anlegen" als `{{< figure >}}` eingebunden:
  Schritt 1 General (01 + 02), Schritt 2 Template inkl. Download-Ansicht
  (10 + 03), Schritt 3 Disks/CPU/Memory (04 + 05 + 06), Schritt 4 Network/DNS
  (07 + 08), Schritt 5 Confirm (09).
- Alt-Texte und Captions verwenden ausschließlich die Labwerte aus der Tabelle
  oben; CT-ID 103 als freie Beispiel-ID, 101 real belegt; Root-Passwort maskiert.
- Secrets-Status je Bild: ok (nur Artikel-Labwerte, keine echten Passwörter,
  kein Login-User sichtbar).
- Quelle und Capture-Datum je Bild: PVE04-Testhost (192.168.20.4),
  Proxmox VE 9.2.11, Erfassung 2026-08-23.
