+++
title = 'USB-Festplatte als Proxmox-Backup-Ziel einrichten'
description = 'Proxmox Backup auf eine USB-Festplatte: Schritt für Schritt eine externe HDD identifizieren, als Proxmox-Storage einrichten und das erste Backup erstellen.'
date = 2026-07-14
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false

# Preview Classification
preview_content_type = "article_draft"
publish_eligible = false
user_visual_approval_required = true
fact_check_required = true
link_check_required = true
price_check_required = false
recommended_action = "review_before_publish"
content_intent = "pillar"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = false
risk_level = "medium"

[cover]
image = "featured.jpg"
relative = true
alt = "Proxmox WebGUI: Storage Backup aktiv mit USB-Festplatte"
+++

⚠️ **Interner Review-Hinweis:** Dieser Artikel ist ein Preview-Entwurf. Screenshots fehlen noch.  
👉 **Nächster Schritt:** Screenshots über die Proxmox-WebGUI ergänzen, dann USER_VISUAL_APPROVAL vor Publish einholen.

---

# USB-Festplatte als Proxmox-Backup-Ziel einrichten

**TL;DR:** Eine USB-Festplatte ist die einfachste Möglichkeit, ein externes Backup-Ziel für Proxmox einzurichten. Du identifizierst die Platte über ihre UUID, mountest sie per fstab dauerhaft und bindest sie als Directory Storage ein. Ein Backup eines Containers und ein Restore-Test bestätigen die Funktion. **Eine einzelne USB-HDD ist besser als kein externes Backup, ersetzt aber keine vollständige 3-2-1-Strategie.**

---

| | |
|---|---|
| **⏱ Zeit** | 15–20 Minuten |
| **💰 Kosten** | ca. 30–50 € (gebrauchte 1-TB-USB-HDD) oder vorhandene Platte |
| **📊 Schwierigkeit** | ⭐⭐☆☆☆ (Einsteiger) |
| **🖥️ Benötigt** | Proxmox-Host, eine USB-Festplatte (min. 500 GB empfohlen) |
| **🎯 Ziel** | Externes Backup-Ziel für Proxmox-VMs und -LXCs |
| **✅ Getestet mit** | Proxmox VE 9.2.4, HGST HTS721010A9E630 (1 TB, ext4) |

---

## 1. Warum eine separate USB-HDD?

Proxmox speichert Backups standardmäßig auf dem lokalen Storage (`local`). Das ist praktisch, aber **kein echtes Backup**:

- **Snapshot ≠ Backup:** Ein Snapshot liegt auf demselben Speicher wie das Original. Wenn die SSD ausfällt, sind Snapshot *und* Original weg.
- **Lokaler Speicher ist begrenzt:** Die System-SSD hat oft nur 64–128 GB – zu wenig für regelmäßige Backups mehrerer VMs/LXCs.
- **USB-HDD als externes Ziel:** Eine separate Platte, die nicht dauerhaft am System hängt, schützt vor gleichzeitigem Ausfall.

Die USB-HDD ist **nicht** die perfekte Backup-Lösung – aber sie ist besser als gar kein externes Backup. Eine vollständige 3-2-1-Strategie (3 Kopien, 2 Medien, 1 extern) sieht anders aus.

---

## 2. Die richtige USB-Festplatte auswählen

Grundsätzlich eignet sich jede externe USB-Festplatte ab etwa 500 GB. Wichtiger als die Marke ist die **Zuverlässigkeit**:

- **Größe:** Für ein Homelab mit 2–3 VMs/LXCs reichen 500 GB. 1 TB gibt Luft für Snapshots und mehrere Backup-Generationen.
- **Anschluss:** USB 3.0 (reicht für Gigabit-Netzwerk-Speed).
- **Empfehlung:** Eine gebrauchte 2,5-Zoll-USB-HDD von einer bekannten Marke (HGST, Western Digital, Seagate). Neuware ist oft überteuert für diesen Zweck.

**Mein Setup:** HGST HTS721010A9E630 (1 TB) als 2,5-Zoll-USB-HDD – leise, stromsparend (ca. 2–3 W) und völlig ausreichend für ein Einsteiger-Homelab.

---

## 3. Die USB-HDD eindeutig identifizieren

Stecke die USB-HDD ein und prüfe mit `lsblk`, ob sie erkannt wird:

```
pve04:~# lsblk -o NAME,SIZE,MODEL,SERIAL,UUID,LABEL,MOUNTPOINT,FSTYPE
NAME     SIZE MODEL                SERIAL         UUID                                   LABEL  MOUNTPOINT      FSTYPE
sda     59.6G TS64GMTS552T-FTS     H476410269                                                                   
└─sda3  58.5G                                                                                                   LVM2_member
sdb    931.5G HGST HTS721010A9E630 JR1020D33XHUKE                                                             
└─sdb1 931.5G                       0fe4e784-...-f4c0bc4041d7 Backup                    /mnt/pve/Backup ext4
```

⚠️ **Wichtig:** Niemals allein anhand von `/dev/sdX` auswählen. Der Device-Name kann sich nach einem Neustart ändern (z. B. von `/dev/sdb` zu `/dev/sdc`). Verwende stattdessen **Modell, Seriennummer und UUID** gemeinsam zur Identifikation.

### Identifikations-Checkliste:

- [ ] Das Gerät hat eine Größe von ~1 TB (oder deiner erwarteten Größe)
- [ ] Es ist eine USB-HDD (Transporttyp USB, erkennbar an Modellbezeichnung oder `lsblk -t`)
- [ ] Es ist **nicht** das Systemlaufwerk (das ist `/dev/sda` – eine 64-GB-SSD im Beispiel)
- [ ] Die UUID ist eindeutig – notiere sie dir für den späteren Mount

---

## 4. Partitionieren und formatieren (nur bei neuer/roher Platte nötig)

Falls die USB-HDD noch kein passendes Dateisystem hat, erstellst du eine Partition und formatierst sie als ext4 mit dem Label `Backup`.

**Gefahr!** Die folgenden Befehle löschen ALLE Daten auf der identifizierten Platte. Prüfe vorher dreimal, ob du das richtige Gerät erwischt hast.

```
# Alle alten Partitionen und Signaturen entfernen
wipefs -af /dev/sdX

# Neue GPT-Partitionstabelle
parted /dev/sdX mklabel gpt

# Eine primäre Partition
parted /dev/sdX mkpart primary ext4 0% 100%

# ext4-Dateisystem mit Label Backup
mkfs.ext4 -L Backup /dev/sdX1
```

Nach der Formatierung sollte die Partition in `lsblk` mit dem Label `Backup` erscheinen.

---

## 5. UUID-basiert mounten (fstab)

Ein Mount über `/dev/sdX1` ist unsicher, weil sich der Device-Name ändern kann. Daher verwendest du die UUID:

```
# UUID auslesen
blkid /dev/sdX1 -s UUID -o value

# Ausgabe: 0fe4e784-f034-41ae-b47f-f4c0bc4041d7
```

Dann trägst du den Mount in `/etc/fstab` ein. **Wichtig:** Der Eintrag `nofail` sorgt dafür, dass der Server auch bootet, wenn die USB-HDD nicht angeschlossen ist:

```
UUID=0fe4e784-f034-41ae-b47f-f4c0bc4041d7 /mnt/pve/Backup ext4 defaults,nofail,noatime 0 2
```

Mount ausführen und prüfen:

```
mkdir -p /mnt/pve/Backup
mount UUID=0fe4e784-f034-41ae-b47f-f4c0bc4041d7 /mnt/pve/Backup
df -h /mnt/pve/Backup
```

Erwartete Ausgabe:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1       916G  2.1M  870G   1% /mnt/pve/Backup
```

---

## 6. Proxmox Directory Storage einrichten

Jetzt wird die USB-HDD als offizieller Proxmox-Storage eingerichtet:

```
pvesh create /storage --type dir --storage Backup --path /mnt/pve/Backup --content backup
```

Mit `pvesm status` prüfst du, ob der Storage aktiv ist:

```
root@pve04:~# pvesm status
Name             Type     Status     Total (KiB)      Used (KiB) Available (KiB)        %
Backup            dir     active       960302096           159300       911288372    0.02%
local             dir     active        25429000          5616260        18495672   22.09%
local-lvm     lvmthin     active        18018304           648658        17369645    3.60%
```

Der Storage `Backup` ist jetzt sichtbar und aktiv. Der Inhaltstyp ist auf `VZDump backup files` beschränkt, sodass keine ISO-Dateien oder Container-Rootfs auf der USB-HDD landen.

---

## 7. Backup eines Containers testen

Erstelle ein Backup auf den neuen Storage:

```
vzdump 101 --storage Backup --compress zstd --mode stop
```

Auszug aus dem Backup-Log:

```
INFO: Starting Backup of VM 101 (lxc)
INFO: status = stopped
INFO: backup mode: stop
INFO: CT Name: docs-lxc01
INFO: creating vzdump archive '/mnt/pve/Backup/dump/vzdump-lxc-101-2026_07_14-08_39_49.tar.zst'
INFO: Total bytes written: 554536960 (529MiB, 58MiB/s)
INFO: archive file size: 153MB
INFO: Backup finished at 2026-07-14 08:39:59 (00:00:10)
```

Prüfe die Backup-Datei:

```
pve04:~# ls -la /mnt/pve/Backup/dump/
total 157220
-rw-r--r-- 1 root root       612 vzdump-lxc-101-2026_07_14-08_39_49.log
-rw-r--r-- 1 root root 160977318 vzdump-lxc-101-2026_07_14-08_39_49.tar.zst
```

---

## 8. Restore-Test (Pflicht!)

Ein Backup ist erst dann ein Backup, wenn du den Restore getestet hast. Proxmox kann ein Backup mit einer neuen CTID wiederherstellen:

```
# Backup als neuen Container mit CTID 102 wiederherstellen
pct restore 102 /mnt/pve/Backup/dump/vzdump-lxc-101-2026_07_14-08_39_49.tar.zst \
  --storage local-lvm --hostname docs-restore01

# Container starten und prüfen
pct start 102
pct exec 102 -- cat /home/pve04_lab_testfile.txt
```

Wenn die Testdatei aus dem Original-Container vorhanden ist, war der Restore erfolgreich.

**Wichtig:** Beim ersten Start nach dem Restore sollte der Container kein Netzwerk haben, um IP-Kollisionen mit dem Original zu vermeiden. Entweder du startest ohne Netzwerk oder entfernst die Netzwerkkonfiguration vor dem Start.

Nach erfolgreichem Test kannst du den wiederhergestellten Container löschen:

```
pct stop 102
pct destroy 102
```

---

## 9. Verhalten bei nicht angeschlossener Platte

Dank der Option `nofail` in `/etc/fstab` bootet Proxmox auch ohne die USB-HDD problemlos – der Mount wird dann übersprungen:

- **Ohne USB-HDD:** Proxmox startet normal, der Storage `Backup` wird in der WebGUI als inaktiv/fehlend angezeigt.
- **Mit USB-HDD:** Wird automatisch gemountet, wenn die Platte beim Booten angeschlossen ist.
- **Hotplug:** Die USB-HDD kann während des Betriebs eingesteckt werden (`mount -a` nach Einstecken).

---

## 10. Grenzen einer einzelnen USB-HDD

Eine USB-HDD ist besser als kein externes Backup, aber kein Ersatz für eine professionelle Backup-Strategie:

| Aspekt | USB-HDD | Empfohlen (3-2-1) |
|--------|---------|-------------------|
| Redundanz | ❌ Single Point of Failure | ✅ Mindestens 2 Kopien |
| Off-Site | ❌ Steckt meist am Server | ✅ Eine Kopie extern |
| Geschwindigkeit | ⚠️ USB 3.0 (ca. 100–150 MB/s) | ✅ NAS über Gigabit-LAN (ca. 110 MB/s) |
| Haltbarkeit | ⚠️ Mechanische HDD | ✅ Je nach Strategie |

---

## ✅ Das solltest du jetzt können

- [ ] Eine USB-HDD eindeutig über Modell, Seriennummer und UUID identifizieren
- [ ] Die HDD per fstab UUID-basiert mounten
- [ ] Einen Proxmox Directory Storage anlegen
- [ ] Ein Backup auf die USB-HDD erstellen
- [ ] Einen Restore-Test mit neuer CTID durchführen
- [ ] Die Grenzen einer einzelnen USB-HDD einordnen

---

## FAQ

**F: Kann ich die USB-HDD auch für ISO-Dateien oder Container-Templates nutzen?**  
A: Technisch ja, aber empfohlen wird, sie ausschließlich für VZDump-Backups zu nutzen. Der Inhaltstyp wird bei der Storage-Konfiguration auf `backup` beschränkt.

**F: Was passiert, wenn die USB-HDD ausfällt?**  
A: Dann ist das Backup weg. Daher: Eine USB-HDD ist nur ein Baustein. Für wichtige Daten zusätzlich ein zweites Backup auf einem anderen Medium (z. B. NAS) einplanen.

**F: Kann ich die USB-HDD auch per SATA anschließen?**  
A: Ja, wenn dein Server einen freien SATA-Port hat. Der Vorteil: kein USB-Adapter als zusätzliche Fehlerquelle. Der Nachteil: Die Platte ist dann fest eingebaut und nicht mehr mobil.

**F: Wie viele Backup-Generationen sollte ich behalten?**  
A: Für ein Homelab reichen 2–3 Generationen. Bei `vzdump` kannst du das mit `--maxfiles 3` begrenzen.

---

## Nächster Schritt

Nachdem das Backup-Ziel steht, geht es an die **automatische Backup-Planung** in Proxmox oder die **Einrichtung eines zweiten Backup-Ziels** für die 3-2-1-Strategie.
