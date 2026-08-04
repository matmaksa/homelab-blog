+++
title = "USB-Festplatte als Proxmox-Backup-Ziel einrichten und Restore testen"
description = "Eine bereits mit ext4 formatierte USB-Festplatte kontrolliert als Proxmox-Backup-Ziel einbinden, VZDump-Backups prüfen und einen LXC-Restore kontrolliert und konfliktarm testen."
date = 2026-08-02
draft = false
aliases = ["/preview/blog/proxmox-usb-festplatte-backup-ziel/"]
ShowShareButtons = true
ShowPostNavLinks = true
comments = false
tags = ["proxmox", "backup", "usb-hdd", "restore", "lxc", "homelab"]
categories = ["Backup", "Virtualisierung"]

[workflow]
content_state = "published"
editorial_status = "pass"
technical_status = "pass"
visual_status = "pass"
seo_status = "pass"
external_preview_verified = true
user_publish_approval = true
commands_executed_on = "PVE04"
commands_verified_at = "2026-08-03T19:57:14Z"
screenshots_complete = true
desktop_visual_check = true
mobile_visual_check = true
links_verified = true
image_licenses_verified = true
affiliate_review_required = false
affiliate_review_passed = false
canonical_verified = false
sitemap_verified = false
robots_verified = false
deployed_commit = ""
preview_checked_at = "2026-08-04T18:26:51Z"
external_images_used = false
screenshots_required = true
claims_practical_test = true
public_placeholders_present = false
+++

## Kurzantwort

Eine externe USB-Festplatte ist ein gutes erstes, getrenntes Ziel für Proxmox-Gast-Backups. Diese Anleitung zeigt einen kontrollierten Weg für eine **bereits partitionierte und mit ext4 formatierte** USB-HDD: Laufwerk eindeutig erkennen, per UUID einhängen, als reinen VZDump-Storage einrichten, einen unkritischen LXC-Container sichern und in einen neuen Test-Container wiederherstellen.

> **Praxisnachweis aus PVE04, 03.08.2026:** Eine 1-TB-USB-HDD mit dem Label `Backup` war als Directory-Storage `Backup` eingebunden. Der Mountpoint-Schutz `is_mountpoint 1` wurde geprüft. Ein neu angelegter unkritischer Testcontainer mit VMID 103 wurde per VZDump auf die USB-HDD gesichert; die Sicherung wurde nach VMID 102 wiederhergestellt, vor dem ersten Start ohne Netzwerkschnittstelle gesetzt und über eine Testdatei geprüft.

| Merkmal | Wert |
|---|---|
| **Zeit** | etwa 30–45 Minuten für Einrichtung, Test-Backup und ersten Restore |
| **Kosten** | 0 € mit vorhandener externer Festplatte |
| **Schwierigkeit** | ⭐⭐⭐☆☆ |
| **Benötigt** | Proxmox VE, separate USB-HDD, sicherer Konsolenzugriff, kleiner unkritischer LXC-Testcontainer |
| **Beispielpfad** | Mountpoint `/mnt/usb-backup`, Storage-ID `usb-backup` |
| **Ziel** | Separates Backup-Ziel für LXC-Container oder VMs und ein getesteter Wiederherstellungsweg |

{{< figure src="backup-ablauf-pve04.svg" alt="Diagramm: PVE04 speichert ein LXC-Backup auf einer USB-Festplatte; daraus wird ein isolierter Restore-Testcontainer erstellt." caption="Der kontrollierte Ablauf: Gast sichern, Backup auf dem getrennten USB-Ziel prüfen, dann isoliert wiederherstellen." >}}

## Voraussetzungen und Grenzen

Du brauchst:

- einen Proxmox-VE-Host,
- eine separate USB-HDD mit ausreichend freiem Platz,
- eine **bereits mit ext4 formatierte** Partition als Beispiel-Dateisystem,
- physischen oder sicheren Konsolenzugriff für den Fall einer fehlerhaften `/etc/fstab`,
- einen kleinen, unkritischen LXC-Testcontainer ohne wichtige Dienste oder einzigartige Daten,
- eine root-Sitzung in der Proxmox-Webshell oder an der lokalen Konsole.

Die Werte aus dem PVE04-Testlab sind Beispiele, keine universellen Vorgaben. Insbesondere Größe, Label, Hostname und freie VMID können in deinem Homelab abweichen.

Diese Anleitung sichert primär **Gäste**: VMs und LXC-Container. Sie ersetzt kein vollständiges Backup des Proxmox-Hosts.

> **Wichtiger Sicherungsumfang:** VZDump sichert VMs beziehungsweise LXC-Gäste samt Gastkonfiguration und enthaltenen Daten. Host-Konfiguration, Netzwerk, Repositories und weitere Hostdateien benötigen eine eigene Sicherungsstrategie. Inhalte von LXC-Bind-Mounts und Device-Mounts werden nicht automatisch durch VZDump gesichert. Prüfe bei LXC-Mountpoints vor dem Backup, welche Daten tatsächlich im Container enthalten sind.

## 1. Warum eine getrennte USB-HDD sinnvoll ist

Ein Backup auf derselben SSD wie ein Container oder eine VM hilft bei versehentlich gelöschten Dateien. Fällt diese SSD aus, können Original und Sicherung aber gleichzeitig verloren gehen. Die angeschlossene USB-HDD ist davon getrennt und deshalb ein sinnvoller erster Schritt.

Sie ist trotzdem nicht offline: Fehlbedienung, kompromittierter Root-Zugang und elektrische Schäden können sie weiterhin treffen. Die nächste Ausbaustufe ist eine zweite, getrennte oder rotierende Kopie. Eine vollständige 3-2-1-Strategie braucht zusätzlich eine Kopie außerhalb des Standorts – zum Beispiel ein NAS an einem zweiten Standort, eine verschlüsselte Cloud-Kopie oder eine an einem anderen Standort gelagerte zweite Festplatte.

## 2. USB-HDD nur lesend eindeutig erkennen

Linux-Namen wie `/dev/sdb` können sich nach einem Neustart ändern. Verwende deshalb später die UUID der Partition, nicht den Gerätenamen.

Führe auf deinem Proxmox-Host – im Beispiel PVE04 – als `root` zunächst nur diese Lese-Befehle aus. Sie ändern keine Daten:

```bash
lsblk -o NAME,TRAN,SIZE,MODEL,FSTYPE,LABEL,UUID,MOUNTPOINTS
blkid
```

Vergleiche mindestens Größe, Modell, Dateisystem `ext4` und UUID mit deiner angeschlossenen USB-HDD. Das Label `Backup` gehört nur zum PVE04-Labbeispiel; deine eigene Festplatte kann ein anderes oder gar kein Label besitzen. Für den späteren fstab-Eintrag ist die UUID entscheidend.

> **Stopp-Regel:** Stimmen Größe, Modell und Dateisystem nicht mit deiner USB-HDD überein, führe keinen Schreib-, Mount- oder Formatierungsbefehl aus. Prüfe zusätzlich die UUID und – falls vorhanden – das Label. Ziehe im Zweifel die USB-HDD ab, prüfe die Ausgabe erneut und kläre die Zuordnung zuerst.

{{< figure src="pve04-usb-erkennung.webp" alt="Bereinigter Terminalauszug aus PVE04: USB-HDD mit Transporttyp USB, 931,5 GiB, Modell, ext4, Label Backup, gekürzter UUID und Mountpoint." caption="USB-HDD eindeutig erkennen: Größe und Modell identifizieren, dann ext4, Label, gekürzte UUID und Mountpoint abgleichen." >}}

## 3. Falls die Festplatte noch nicht mit ext4 vorbereitet ist

Die Hauptanleitung setzt eine bereits partitionierte und mit ext4 formatierte USB-HDD voraus. Partitionierung und Formatierung sind nicht Teil dieser Anleitung, weil sie destruktiv sind und vorhandene Daten löschen können. Deshalb enthält dieser Entwurf bewusst **keinen blind kopierbaren `/dev/sdX`-Befehl**.

Wenn die USB-HDD noch nicht ext4-formatiert ist, verwende zuerst eine getrennte, dokumentierte Vorbereitung mit zweiter Sichtprüfung des Ziellaufwerks. Erst danach kehrst du zu Schritt 4 zurück. Eine Festplatte mit vorhandenen Daten wird nicht für diese Anleitung formatiert.

## 4. Mountpoint anlegen und `/etc/fstab` sicher vorbereiten

Lege den Beispiel-Mountpoint an:

```bash
mkdir -p /mnt/usb-backup
```

Sichere vor jeder Änderung die vorhandene `fstab` mit Zeitstempel:

```bash
cp /etc/fstab /etc/fstab.bak-$(date +%F-%H%M)
```

Öffne danach `/etc/fstab` mit dem auf deinem Host hinterlegten Standardeditor und ergänze **eine** Zeile:

```bash
editor /etc/fstab
```

Ersetze ausschließlich `<DEINE-UUID>` durch die in Schritt 2 geprüfte UUID:

```text
UUID=<DEINE-UUID> /mnt/usb-backup ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2
```

Kurz erklärt:

- **UUID:** stabiler als ein wechselnder Name wie `/dev/sdb`.
- **ext4:** muss dem tatsächlich vorhandenen Dateisystem entsprechen.
- **nofail:** der fehlende USB-Datenträger verhindert keinen erfolgreichen Host-Start.
- **x-systemd.device-timeout=10s:** begrenzt die Wartezeit auf ein beim Start fehlendes USB-Gerät.
- **0 2:** übliche Prüfwerte für ein ext4-Datenlaufwerk.

Vor einem Neustart prüfst du die Konfiguration und aktivierst nur den gewünschten Mount. `systemctl daemon-reload` liest die von systemd aus der fstab erzeugten Mount-Units neu ein:

```bash
findmnt --verify --verbose
systemctl daemon-reload
mount /mnt/usb-backup
```

Dann kontrollierst du Mount, Dateisystem, freien Speicher und Schreibzugriff:

```bash
findmnt /mnt/usb-backup
df -hT /mnt/usb-backup
mountpoint /mnt/usb-backup
touch /mnt/usb-backup/.write-test
rm /mnt/usb-backup/.write-test
```

Der Schreibtest darf nur erfolgreich sein, wenn `findmnt` und `mountpoint` vorher den echten USB-Mount bestätigen. So schreibst du nicht versehentlich in ein leeres Verzeichnis auf der Root-Partition.

{{< figure src="pve04-usb-mount-storage.webp" alt="Bereinigter Terminalauszug aus PVE04: ext4-Dateisystem am Mountpoint /mnt/pve/Backup, freier Speicher und bestätigter Mountpoint." caption="USB-Mount auf PVE04 verifizieren: ext4, freier Speicherplatz und echter Mountpoint." >}}

## 5. USB-HDD als Proxmox-Backup-Storage konfigurieren

Öffne die Proxmox-Weboberfläche:

1. **Datacenter → Storage → Add → Directory** öffnen.
2. **ID:** `usb-backup` eintragen.
3. **Directory:** `/mnt/usb-backup` eintragen.
4. Bei **Content** ausschließlich **VZDump backup file** aktivieren.
5. **Shared** nicht aktivieren.
6. **Enabled** aktiv lassen.
7. Den Storage bei Bedarf auf den Node **PVE04** begrenzen.

Sehr wichtig ist `is_mountpoint=1`. Diese Schutzoption sorgt dafür, dass Proxmox das Storage nur verwendet, wenn an diesem Pfad wirklich ein Dateisystem eingehängt ist. Falls die verwendete Proxmox-GUI diese Option nicht anbietet, setze sie nach dem Anlegen als `root`:

```bash
pvesm set usb-backup --is_mountpoint 1
grep -A8 '^dir: usb-backup$' /etc/pve/storage.cfg
pvesm status
```

Im PVE04-Test heißt das reale Storage `Backup` und der Mountpoint `/mnt/pve/Backup`. Die Beispielwerte `usb-backup` und `/mnt/usb-backup` oben sind frei wählbar und müssen auf anderen Hosts angepasst werden. Die PVE04-Konfiguration enthält `content backup` und `is_mountpoint 1`; `pvesm status` zeigte das Storage nach dem Mount als aktiv.

{{< figure src="pve04-usb-storage-config.webp" alt="Bereinigter Terminalauszug aus PVE04: Storage Backup mit Pfad /mnt/pve/Backup, content backup und is_mountpoint 1." caption="Das reale PVE04-Storage heißt `Backup`. Die allgemeine Anleitung verwendet `usb-backup` als frei wählbare Beispiel-ID." >}}

### Schutztest für einen fehlenden Datenträger

Führe diesen Test nur aus, wenn kein Backup-Job läuft oder unmittelbar starten wird und der Storage nicht in Benutzung ist:

1. Im Proxmox Task Viewer und bei den Backup-Jobs prüfen, dass kein Job läuft oder unmittelbar starten wird.
2. Schreibvorgänge beenden und den Puffer leeren:

   ```bash
   sync
   ```

3. USB-Dateisystem sauber aushängen:

   ```bash
   umount /mnt/usb-backup
   mountpoint /mnt/usb-backup
   pvesm status
   ```

4. `mountpoint` muss melden, dass der Pfad kein Mountpoint mehr ist; `pvesm status` muss `usb-backup` als inaktiv zeigen.
5. **Kein absichtliches Backup auf den inaktiven Storage starten.**
6. USB-Dateisystem wieder einhängen und Mount sowie Storage erneut prüfen:

   ```bash
   mount /mnt/usb-backup
   findmnt /mnt/usb-backup
   pvesm status
   ```

Dieser Schutztest prüft, ob `is_mountpoint=1` den Storage bei ausgehängtem USB-Dateisystem inaktiv hält. Er ersetzt keine allgemeine Prüfung vor jedem wichtigen Backup.

## 6. Test-Backup eines unkritischen LXC erstellen

Erst jetzt sicherst du einen kleinen Test-Container. Das Original darf keine wichtigen Dienste oder einzigartigen Daten enthalten.

1. In Proxmox den Test-Container öffnen und **Backup** wählen.
2. Als Storage `usb-backup` auswählen.
3. Job starten und im **Task Viewer** auf ein erfolgreiches Ende prüfen.
4. Danach **Datacenter → Storage → usb-backup → Content** öffnen. Die neue VZDump-Datei muss dort erscheinen.
5. Freien Speicher auf der USB-HDD prüfen.

Eine plausible Backup-Größe bedeutet: nicht 0 Byte und grob passend zur belegten Datenmenge. Kompression kann die Datei deutlich kleiner machen. Ohne Aufbewahrungsregel füllt sich eine USB-HDD irgendwann; Zeitplanung und Retention bleiben bewusst Thema eines Folgeartikels.

Im PVE04-Test wurde dafür ein neuer unkritischer Debian-LXC mit VMID 103 und deaktivierter Netzwerkschnittstelle erzeugt. Das VZDump-Backup lief im Snapshot-Modus mit zstd auf Storage `Backup` erfolgreich durch. Die erzeugte Datei hatte 160.468.124 Bytes; nach dem Test waren noch etwa 866 GiB auf der USB-HDD frei.

{{< figure src="pve04-vzdump-erfolgreich.webp" alt="Bereinigter Terminalauszug aus PVE04: erfolgreicher VZDump eines LXC mit VMID 103 auf Storage Backup, Dateiname und Archivgröße." caption="Realer PVE04-Test: VZDump von Testcontainer 103 wurde erfolgreich auf der USB-HDD im Storage `Backup` abgelegt." >}}

## 7. Restore isoliert testen

Ein Backup ist erst belastbar, wenn eine Wiederherstellung funktioniert. Überschreibe nie den Original-Container.

1. Verwende eine freie neue VMID.
2. Wähle die Backup-Datei unter **Datacenter → Storage → usb-backup → Content** und starte **Restore**.
3. Wähle bewusst das Ziel-Storage für das wiederhergestellte Root-Dateisystem.
4. Deaktiviere die Netzwerkschnittstelle oder entferne sie vor dem ersten Start.
5. Prüfe vor dem Start Hostname, gespeicherte IP-Adresse, MAC-Adresse und mögliche laufende Dienste auf Konflikte.
6. Starte den Restore-Test erst ohne Netzwerk.
7. Prüfe eine vorher definierte Testdatei und zusätzlich eine kleine Funktion des Dienstes.
8. Dokumentiere das Ergebnis.
9. Lösche den temporären Restore erst nach erfolgreicher Prüfung.

Ohne Netzwerk kann der Restore weder eine vorhandene IP-Adresse noch einen gleichnamigen Dienst im Heimnetz stören.

> **PVE04-Labbeispiel:** Im PVE04-Test wurde für den isolierten Restore die freie VMID 102 verwendet. VMID 100 blieb bewusst frei. Diese Werte sind keine Vorgabe für dein Homelab.

Im PVE04-Test wurde die Sicherung von VMID 103 nach der freien VMID 102 wiederhergestellt. Vor dem ersten Start wurde `net0` entfernt; die anschließende Konfigurationsprüfung ergab null Netzwerkschnittstellen. Die zuvor definierte Testdatei war im gestarteten Restore vorhanden. Der temporäre Restore wurde danach kontrolliert gelöscht.

{{< figure src="pve04-restore-isoliert.webp" alt="Bereinigter Terminalauszug aus PVE04: Restore nach VMID 102, vor dem Start entfernte Netzwerkschnittstelle, vorhandene Testdatei und erfolgreicher Lauf." caption="Realer isolierter Restore: VMID 102 startete ohne aktive Netzwerkschnittstelle; die Testdatei aus dem Backup war vorhanden." >}}

## Häufige Fehler

| Problem | Sicherer nächster Schritt |
|---|---|
| `usb-backup` ist inaktiv | USB-Mount mit `findmnt` prüfen; nicht formatieren. |
| Backup landet lokal | Backup-Job auf Storage `usb-backup` korrigieren und Test wiederholen. |
| Mount schlägt fehl | `findmnt --verify --verbose` ausführen und die fstab-Sicherung bereithalten. |
| Restore kollidiert mit dem Original | Restore stoppen, Netzwerk entfernen und VMID/Hostname/IP/MAC erneut prüfen. |

## FAQ

**Reicht die USB-HDD als vollständiges Backup?**

Nein. Sie ist ein getrenntes erstes Ziel, aber dauerhaft angeschlossen. Für wichtige Daten folgt eine zweite, getrennte oder Offsite-Kopie – zum Beispiel eine an einem anderen Standort gelagerte zweite Festplatte.

**Kann die Platte auch ISOs enthalten?**

Technisch ja. Für den Einstieg bleibt ein ausschließliches VZDump-Backup-Ziel übersichtlicher und reduziert Fehlbedienungen.

**Wie oft muss ich den Restore testen?**

Direkt nach der Einrichtung und danach nach größeren Änderungen oder in einem festen Wartungsrhythmus.

## Testergebnis aus PVE04

Am 03.08.2026 wurde die aktuelle Befehlsfolge auf PVE04 praktisch geprüft. Die USB-HDD (`Backup`, ext4) war unter `/mnt/pve/Backup` eingehängt; die fstab-Zeile enthält `nofail` und `x-systemd.device-timeout=10s`. Storage `Backup` ist auf `content backup` begrenzt und enthält `is_mountpoint 1`.

Der Schutztest bestätigte: Nach sauberem Aushängen war der Pfad kein Mountpoint mehr und Proxmox meldete Storage `Backup` als inaktiv. Nach erneutem Einhängen war der Mountpoint wieder vorhanden und das Storage aktiv.

Ein neuer unkritischer Testcontainer (VMID 103) wurde erfolgreich per VZDump im Snapshot-Modus mit zstd auf die USB-HDD gesichert. Die Backup-Datei wurde anschließend nach VMID 102 wiederhergestellt. Vor dem ersten Start wurde die Netzwerkschnittstelle entfernt; die Testdatei war im Restore vorhanden. Der temporäre Restore wurde danach gelöscht. Das bestätigt diesen Wiederherstellungsweg im PVE04-Testlab; es ersetzt keine zweite getrennte oder externe Kopie.

## ✅ Das solltest du jetzt können

- [ ] Die richtige USB-HDD ohne Schreibzugriff eindeutig identifizieren.
- [ ] Einen UUID-Mount mit fstab-Backup und anschließender Prüfung vorbereiten.
- [ ] `usb-backup` als reines VZDump-Storage mit Mountpoint-Schutz einrichten.
- [ ] Einen unkritischen Container sichern und Task Viewer sowie Storage Content prüfen.
- [ ] Einen Restore mit neuer ID und ohne Netzwerk planen.
- [ ] Erklären, warum eine zweite getrennte Kopie der nächste Schritt ist.

## Nächster Schritt

Als Ergänzung folgt ein Artikel über einen planbaren Backup-Rhythmus, Aufbewahrungsregeln und eine zweite, getrennte Kopie.

## Technische Referenzen

- [Proxmox VE Administration Guide: Storage](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#chapter_storage) – Directory-Storage und Storage-Konfiguration.
- [Proxmox VE Administration Guide: Backup and Restore](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#chapter_vzdump) – VZDump, Sicherungsmodi und Wiederherstellung.
