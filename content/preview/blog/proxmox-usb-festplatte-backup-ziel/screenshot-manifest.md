# Screenshot-Manifest: Proxmox-USB-Backup-Artikel

Stand der Prüfung: 03.09.2026 (Europe/Berlin)

## Fachliche Einordnung

Die fünf vorhandenen WEBP-Dateien sind bereinigte, einheitlich gestaltete Terminal-Nachweisgrafiken. Sie zeigen plausible Proxmox-/Linux-Befehle und die im Artikel dokumentierten PVE04-Testwerte. Sie sind keine unveränderten Bildschirmfotos: Der sichtbare Titel „Bereinigter Terminalauszug aus dem PVE04-Testlab“ kennzeichnet die redigierte Darstellung. Die Testzeitpunkte stammen aus dem Artikeltext (`03.08.2026`) und nicht aus den Dateisystem-Zeitstempeln der Preview-Dateien.

Eine aktuelle, rein lesende Prüfung auf PVE04 am 03.09.2026 bestätigte:

- Node: `pve04`
- USB-Datenträger: 931,5G, ext4, Label `Backup`, Mountpoint `/mnt/pve/Backup`
- Proxmox-Storage `Backup`: `dir`, `active`, `content backup`, `is_mountpoint 1`
- Aktuelle Auslastung des Storage: 0,46 %
- Keine Backup-, Mount-, Restore- oder Konfigurationsaktion ausgeführt

Daraus wurde die zusätzliche, ausdrücklich als Live-Leseauszug gekennzeichnete Grafik `pve04-usb-storage-live-status.svg` erstellt. Sie ist ein aktueller Statusnachweis für USB-Erkennung und aktives Directory-Storage, aber kein Nachweis eines neuen Backup- oder Restore-Laufs.

## Bildzuordnung

| Datei | Inhalt / fachlicher Nachweis | Aufnahme-/Testbezug | Empfohlene Artikelposition | Alt-Text-Vorschlag |
|---|---|---|---|---|
| `pve04-usb-erkennung.webp` | `lsblk` zeigt USB-Transport, 931,5G, ext4, Label `Backup`, gekürzte UUID und `/mnt/pve/Backup`. | PVE04-Labortest laut Artikel: 03.08.2026. | Nach Abschnitt 2 „USB-HDD nur lesend eindeutig erkennen“. | Bereinigter Terminalauszug aus dem PVE04-Testlab: USB-HDD mit ext4, Label Backup, gekürzter UUID und Mountpoint. |
| `pve04-usb-mount-storage.webp` | `findmnt`, `df -hT` und `mountpoint` bestätigen ext4, freien Speicher und echten Mountpoint. | PVE04-Labortest laut Artikel: 03.08.2026. | Nach Abschnitt 4 „Mountpoint anlegen und fstab sicher vorbereiten“. | Bereinigter Terminalauszug aus PVE04: ext4-Dateisystem, freier Speicher und bestätigter Mountpoint `/mnt/pve/Backup`. |
| `pve04-usb-storage-config.webp` | `/etc/pve/storage.cfg` zeigt Directory-Storage `Backup`, `content backup`, `is_mountpoint 1`; `pvesm status` zeigt aktiv. | PVE04-Labortest laut Artikel: 03.08.2026. | Nach Abschnitt 5 „USB-HDD als Proxmox-Backup-Storage konfigurieren“. | Bereinigter Proxmox-Konfigurationsauszug aus PVE04: Storage Backup mit `content backup` und `is_mountpoint 1`. |
| `pve04-usb-storage-live-status.svg` | Aktuelle, redigierte Leseprüfung: `pve04`, USB-Partition, aktives Storage und aktuelle Auslastung. | Live-READ am 03.09.2026; kein Zustandswechsel. | Optional zusätzlich oder statt `pve04-usb-storage-config.webp` im Abschnitt 5. Nicht als Backup-/Restore-Beleg verwenden. | Aktueller bereinigter Leseauszug aus PVE04: USB-HDD als ext4 und Proxmox-Storage Backup aktiv. |
| `pve04-vzdump-erfolgreich.webp` | VZDump von Testcontainer 103 im Snapshot-Modus mit zstd, Archivname, Größe und erfolgreichem Abschluss. | PVE04-Labortest laut Artikel: 03.08.2026; Archivgröße im Artikel: 160.468.124 Bytes. | Nach Abschnitt 6 „Test-Backup eines unkritischen LXC“. | Bereinigter VZDump-Auszug aus PVE04: Testcontainer 103 wurde im Snapshot-Modus mit zstd erfolgreich auf Storage Backup gesichert. |
| `pve04-restore-isoliert.webp` | Restore 103 → 102, vor Start `net0` entfernt, Restore gestartet und Testdatei vorhanden. | PVE04-Labortest laut Artikel: 03.08.2026; temporärer Restore anschließend bereinigt. | Nach Abschnitt 7 „Restore isoliert testen“. | Bereinigter Restore-Auszug aus PVE04: VMID 102 startete ohne aktive Netzwerkschnittstelle und enthielt die Testdatei. |

## Sicherheitsprüfung

In den geprüften Bildern sind keine Tokens, Passwörter oder UUIDs vollständig sichtbar. Die neue Live-Grafik enthält bewusst weder UUID noch IP-Adresse. Hostname `pve04`, Storage-ID `Backup`, VMIDs und Mountpoint sind für die technische Aussage erforderlich und entsprechen dem dokumentierten nichtproduktiven PVE04-Testlab.

## Grenze der aktuellen Prüfung

Ein neuer VZDump-Lauf oder Restore-Test wurde nicht angestoßen. Das wäre ein Zustandswechsel und ist für diesen READ-Auftrag ausdrücklich ausgeschlossen. Deshalb bleiben `pve04-vzdump-erfolgreich.webp` und `pve04-restore-isoliert.webp` historische, im Artikel dokumentierte Testbelege; die Live-Grafik ergänzt nur den aktuellen USB-/Storage-Status.
