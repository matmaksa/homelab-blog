# PVE04-Testnachweis: USB-Backup und isolierter Restore

- **Datum:** 2026-08-03
- **Host:** PVE04
- **Artikelstand vor Artikel-Commit:** `d810170`
- **USB-Storage:** `Backup` (`/mnt/pve/Backup`, ext4)
- **Ergebnis:** PASS mit dokumentierter Abweichung und Wiederholung des Restore-Schritts

## Vorbedingungen

| Prüfung | Tatsächliches Ergebnis |
|---|---|
| VMID 100 | frei |
| VMID 102 | frei |
| VMID 103 | frei |
| konfigurierte Backup-Jobs | keine |
| laufende VZDump-/Backup-Prozesse | keine |
| USB-HDD | USB, 931,5 GiB, Modell HGST HTS721010A9E630, ext4, Label `Backup` |
| Mount | `/mnt/pve/Backup` ist ein Mountpoint |
| freier Speicher vor Test | ca. 867 GiB |

## Gesicherte Konfiguration und Korrektur

Vor Änderungen wurde auf PVE04 gesichert:

`/root/blog-usb-backup-test-20260803T195504Z/`

Darin liegen `/etc/fstab`, `/etc/pve/storage.cfg` und `SHA256SUMS.before`.

Danach wurden ausschließlich ergänzt:

- fstab: `x-systemd.device-timeout=10s` zusätzlich zu `nofail`
- Storage `Backup`: `is_mountpoint 1`

Die anschließende Kontrolle zeigte `content backup`, `is_mountpoint 1` und Storage-Status `active`.

## Befehle und Ergebnisse

| Schritt | Ausgeführter Vorgang | Tatsächliches Ergebnis |
|---|---|---|
| Erkennung | `lsblk`, `findmnt`, `df -hT`, `mountpoint`, `findmnt --verify --verbose` | USB-HDD, ext4, Label, Mount und fstab-Syntax bestätigt |
| Schutztest | `sync`, `umount /mnt/pve/Backup`, Storage-Status prüfen, wieder mounten | Mountpoint `NO`, Storage `inactive`; danach Mountpoint `YES`, Storage `active` |
| Testcontainer | neuer Debian-12-LXC VMID 103, 2 GiB RootFS, 1 Core, 128 MiB RAM, Netzwerk für Test deaktiviert | erstellt, gestartet und mit Testdatei versehen |
| Backup | `vzdump 103 --storage Backup --mode snapshot --compress zstd` | erfolgreich, Archiv `vzdump-lxc-103-2026_08_03-21_57_03.tar.zst`, 160.468.124 Bytes |
| Restore | Backup nach VMID 102, RootFS `local-lvm` | erfolgreich |
| Isolation | bei der finalen Wiederholung vor erstem Start `pct set 102 --delete net0` | 0 Netzwerkschnittstellen vor erstem Start |
| Prüfdaten | `cat /root/backup-restore-proof.txt` im Restore | `PVE04 USB backup restore proof` vorhanden |
| Bereinigung | Restore 102 gestoppt/zerstört; Testcontainer 103 zerstört | PASS |

## Abweichung und Behandlung

Der erste Restore-Lauf nach VMID 102 wurde nach dem Start zwar erfolgreich wieder entfernt, aber die gewünschte Abwesenheit einer Netzwerkschnittstelle war vor dem Start nicht explizit nachgewiesen. Dieser Lauf wird **nicht** als Isolationsnachweis verwendet.

Der Restore wurde deshalb mit derselben Backup-Datei wiederholt. Vor dem ersten Start wurde `net0` explizit entfernt und die Konfiguration zeigte danach null Netzwerkschnittstellen. Nur dieser zweite Lauf ist der gültige isolierte Restore-Nachweis.

## Ergebnis

**PASS.** Die aktuelle Befehlsfolge wurde auf PVE04 praktisch geprüft. Der Mountpoint-Schutz reagierte beim Aushängen wie erwartet; VZDump schrieb die Test-Sicherung auf die USB-HDD; der wiederholte Restore nach VMID 102 startete ohne Netzwerkschnittstelle und enthielt die Testdatei.
