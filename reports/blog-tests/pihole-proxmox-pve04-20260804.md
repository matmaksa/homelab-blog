# Pi-hole-Praxisguide: PVE04-/CT-101-Finalisierungstest

- **Zeitfenster:** 2026-08-04T19:17:07Z bis 2026-08-04T19:44:14Z
- **Host:** PVE04, Proxmox VE 9.2.4
- **Container:** CT 101 / `01-pihole`
- **Artikel-Ausgangsstand:** `839c915`
- **Testkontext:** PVE04 als getrennte Test-Shell gegen die feste CT-101-Labadresse. Keine Router-, DHCP-, Firewall-, VLAN- oder Heimnetz-DNS-Änderung.

## Gelesener Ist-Zustand

| Bereich | Tatsächlicher Wert |
|---|---|
| CT-Status | `running` |
| Typ | unprivilegierter Debian-LXC |
| Betriebssystem | Debian GNU/Linux 13 (trixie) |
| CPU | 1 vCPU |
| RAM / Swap | 256 MiB / 256 MiB |
| Root-Disk | 8 GiB auf `local-lvm` |
| Netzwerk | `vmbr0`, VLAN 20, fester Labadressbereich |
| Autostart | aktiviert |
| FTL | aktiv und aktiviert |
| FTL-Version | v6.7 |
| Paketmetadaten | `pihole-meta` 0.7 |
| DNS-Upstreams | 1.1.1.1 und 1.0.0.1 |
| Blocking-Modus | `NULL` |
| Query Logging / Privacy-Level | aktiv / 0 |
| Rechtepfade | `/var/log/pihole/FTL.log` und `/etc/pihole/config_backups` aktuell `pihole:pihole`; kein aktueller Rechteeingriff nötig |

Die historische Artikelnennung „Pi-hole Core v6.4.3, Web v6.6 und FTL v6.7“ wird nicht als neuer Versionsnachweis verwendet: Der aktuelle `pihole`-CLI-Befehl war im CT nicht im Pfad verfügbar. Neu bestätigt wurde FTL v6.7 sowie der laufende Dienst.

## Funktionsprüfung vor Neustart

| Test von PVE04 gegen CT 101 | Erwartung | Tatsächliches Ergebnis |
|---|---|---|
| DNS UDP: `deb.debian.org A` | kein Timeout, erfolgreiche Antwort | `NOERROR` |
| DNS TCP: `deb.debian.org A` | kein Timeout, erfolgreiche Antwort | `NOERROR` |
| Blocking: `ad.doubleclick.net A` | NULL-Blocking-Ausgabe | `0.0.0.0` |
| Weboberfläche | lokaler Admin-Endpunkt antwortet | HTTP 302 auf den Anmeldefluss; keine Anmeldung oder Sitzung verwendet |

## Kontrollierter Neustart

- CT 101 war vor dem Neustart `running`.
- PVE04 selbst verwendet einen anderen Nameserver als CT 101; es wurde keine Heimnetz-DNS-Konfiguration verändert.
- Neustart gestartet und bis zum Zustand `running` gemessen: **11 Sekunden**.
- Proxmox meldete dabei eine nicht blockierende Systemd-257-/Nesting-Warnung.
- Nach dem Neustart: FTL `active`; UDP `NOERROR`; TCP `NOERROR`; Blocking `0.0.0.0`; Webendpunkt HTTP 302.

## VZDump-Backup

| Feld | Tatsächlicher Wert |
|---|---|
| VMID | 101 |
| Name | `01-pihole` |
| Storage | `Backup` (aktiv) |
| Modus | Snapshot |
| Kompression | zstd |
| Start | 2026-08-04 21:43:57 lokale PVE-Zeit |
| Ende | 2026-08-04 21:44:13 lokale PVE-Zeit |
| Dauer | 18 Sekunden (VZDump meldete 16 Sekunden) |
| Archiv | `/mnt/pve/Backup/dump/vzdump-lxc-101-2026_08_04-21_43_57.tar.zst` |
| Dateigröße | 304.619.079 Bytes (VZDump-Ausgabe: 290 MB) |
| Ergebnis | erfolgreich; Datei anschließend im Storage vorhanden |

Nach dem Backup war Storage `Backup` weiterhin aktiv und hatte 907.738.444 KiB freien Speicher.

## Abweichungen und Grenzen

1. Der aktuelle CT-101-Ressourcenstand ist 256 MiB RAM und 256 MiB Swap, nicht die historische 512-MiB-Nennung im Entwurf.
2. Der lokale Admin-Endpunkt bestätigte den Anmeldefluss via HTTP 302. Es wurde kein Admin-Passwort gelesen, keine Sitzung verwendet und daher kein authentifiziertes Dashboard-Screenshot erzeugt.
3. Dieses Backup ist ein echter Sicherungsnachweis, aber **kein Restore-Test**.

## Gesamtstatus

**PASS** für aktuelle CT-/FTL-, UDP-, TCP-, Blocking-, Neustart-, lokalen Webendpunkt- und VZDump-Nachweise. Kein produktives Heimnetz wurde umgestellt.
