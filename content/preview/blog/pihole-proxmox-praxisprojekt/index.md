+++
title = "Pi-hole im Proxmox-Homelab: Dein erster eigener DNS-Werbeblocker"
description = "Einsteigerfreundlicher Pi-hole-Einstieg im Proxmox-LXC: Container, DNS, Blocking, Neustart und Backup verständlich prüfen."
date = 2026-07-22
draft = false
robotsNoIndex = true
noindex = true
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
tags = ["pihole", "proxmox", "dns", "lxc", "homelab"]
categories = ["Software", "Virtualisierung"]

sitemap = { exclude = true }

# Preview Classification (minimale Felder für die Übersichtskarte)
content_state = "user_review_required"
user_visual_approval_required = true

[cover]
image = "featured.jpg"
alt = "Innenansicht des kompakten Mini-PCs mit Transcend-64-GB-M.2-SSD, Intel-AX200NGW-WLAN-Modul und SK-Hynix-4-GB-DDR4-Speicher"
relative = true

[workflow]
content_state = "user_review_required"
editorial_status = "pass"
technical_status = "pass"
visual_status = "pass"
seo_status = "pass"
external_preview_verified = true
user_publish_approval = false
commands_executed_on = "PVE04 / CT 101"
commands_verified_at = "2026-08-04T19:44:14Z"
screenshots_complete = true
desktop_visual_check = true
mobile_visual_check = true
local_visual_checked_at = "2026-08-23T12:59:25Z"
links_verified = true
image_licenses_verified = true
affiliate_review_required = false
affiliate_review_passed = false
canonical_verified = true
sitemap_verified = true
robots_verified = true
external_images_used = false
screenshots_required = true
claims_practical_test = true
public_placeholders_present = false
+++

Pi-hole war mein erster **sauber neu aufgebauter** Dienst auf PVE04. Das ist ein guter Einstieg ins Homelab: Du baust einen kleinen Container, lernst den DNS-Weg kennen und prüfst anschließend, ob normale DNS-Anfragen und das Blocking funktionieren.

PVE04 ist ein eigener Proxmox-Testhost, nicht mein produktives Homelab. Die verwendeten IP-Adressen, Container-IDs und Ressourcen sind deshalb Labwerte, die du an dein Netz anpassen musst.

## Kurz gesagt

Pi-hole nimmt DNS-Anfragen entgegen. DNS ist das Telefonbuch des Netzes: Wenn du `www.google.de` eingibst, wird daraus die passende Internetadresse. Mit Pi-hole fragt ein Gerät zuerst diesen kleinen Dienst. Pi-hole beantwortet normale Anfragen und kann bekannte Werbe- und Tracking-Domains blockieren.

## Dein einfacher Weg durch das Projekt

1. Container anlegen
2. Netzwerk festlegen und eine freie feste IP notieren
3. Debian starten und Pi-hole installieren
4. DNS und Blocking testen
5. Neustart prüfen

Damit bleibt der Ablauf bewusst klein: erst parallel aufbauen, dann testen und erst später entscheiden, ob weitere Geräte Pi-hole verwenden sollen.

## Das brauchst du

> **Für diesen Einstieg brauchst du:**
> - einen laufenden Proxmox-Host
> - eine freie feste IP-Adresse und die Gateway-IP deines Netzes
> - Grundzugriff auf die Proxmox-Oberfläche
> - für den PVE04-Finalisierungsstand 1 vCPU, 256 MiB RAM, 256 MiB Swap und 8 GiB Speicher; für dein eigenes Setup abhängig von Filterlisten und Reserve passend planen

> **Das brauchst du noch nicht:**
> - VLANs
> - Unbound oder DNS-over-HTTPS
> - Pi-hole als DHCP-Server
> - eine lokale DNS-Zone
> - einen Restore-Test
>
> Diese Themen können später sinnvoll sein. Für den ersten funktionierenden Pi-hole-Container machen sie den Einstieg aber nur unnötig kompliziert.

![Zwei DNS-Wege: Links fragt ein Rechner über Router und Standard-DNS direkt das Internet. Rechts fragt der Rechner zuerst Pi-hole als DNS-Werbeblocker; Pi-hole filtert bekannte Werbe- und Tracking-Domains und leitet erlaubte Anfragen weiter.](dns-ablauf-mit-pihole.svg?v=20260722)

*Ohne Pi-hole läuft die DNS-Anfrage über den bisherigen Weg. Mit Pi-hole fragt dein Gerät zuerst den kleinen DNS-Dienst; dieser filtert bekannte Werbe- und Tracking-Domains und fragt bei Bedarf weiter.*

> **Wichtig:** Der Rechner nutzt Pi-hole nur dann, wenn Pi-hole ausdrücklich als DNS-Server eingetragen ist – direkt am Gerät oder über die DHCP-Einstellung deines Routers. Router und Switch transportieren die Netzwerkpakete, sie leiten DNS-Anfragen nicht automatisch zu Pi-hole um.

## 1. Container in Proxmox anlegen

**Kurz erklärt:** Eine Bridge wie `vmbr0` verbindet den Container mit deinem normalen Netzwerk. Das Gateway ist die Router-Adresse, über die der Container andere Netze und das Internet erreicht. `local-lvm` ist der lokale Speicherbereich des Proxmox-Hosts. Swap ist ein Notfall-Puffer auf dem Datenträger und deutlich langsamer als Arbeitsspeicher.

PVE04 ist ein Fujitsu Futro S7010 mit vier CPU-Kernen, 4 GB RAM und einer 64-GB-SSD. Der Host dient ausschließlich als Content- und Test-Lab. Für Pi-hole entstand der unprivilegierte LXC-Container CT 101 mit dem Namen `01-pihole`.

**CT 101** ist keine technische Abkürzung, die du auswendig kennen musst: Proxmox führt jeden Container unter einer numerischen ID. Mein Pi-hole erhielt die ID **101** und den Namen **01-pihole**. Für dein eigenes Setup wählst du eine bei dir freie ID.

In der Proxmox-Oberfläche wählst du zuerst deinen Host aus und klickst oben rechts auf **Create CT**.

{{< figure src="proxmox-create-ct.webp" alt="Bereinigte Proxmox-Oberfläche mit markierter Schaltfläche Create CT oben rechts; links ist der PVE04-Testhost ausgewählt." caption="Wähle zuerst deinen Proxmox-Host aus und öffne dann oben rechts den Assistenten über Create CT. Der Screenshot stammt aus dem MATMAKSA-Testlab; der verwendete Hostname ist nur ein Beispiel." >}}

Die folgenden Werte sind die tatsächlich getestete Konfiguration dieses Praxisaufbaus:

| Bereich | Verwendete Konfiguration |
|---|---|
| Vorlage | `debian-13-standard_13.6-1_amd64.tar.zst` als unprivilegierter LXC |
| ID und Name | 101 und `01-pihole` – nur Beispielwerte; bei dir muss die ID frei sein |
| CPU | 1 vCPU |
| Arbeitsspeicher | **Aktueller Finalisierungsstand:** 256 MiB RAM und 256 MiB Swap; die frühere 512-MiB-Angabe gehört zu einem historischen Teststand und wird nicht als aktueller Wert verwendet |
| Root-Disk | 8 GiB auf `local-lvm` |
| Netzwerk | Bridge `vmbr0`, im Test-Lab VLAN 20 |
| Startverhalten | Autostart aktiviert |
| Upstream-DNS | `1.1.1.1` und `1.0.0.1` |

{{< figure src="pve04-ct101-status.webp" alt="Bereinigter Terminalauszug aus dem PVE04-Testlab: CT 101 läuft mit einem CPU-Kern, 256 MiB RAM, 256 MiB Swap, 8 GiB Root-Disk und aktiviertem Autostart." caption="Ressourcennachweis vom 04.08.2026: CT 101 lief als unprivilegierter Container. Die gezeigten Ressourcen sind Labwerte dieses Aufbaus und keine allgemeine Mindestanforderung für Pi-hole." >}}

Wenn du den Assistenten zum ersten Mal siehst, arbeite ihn einfach von oben nach unten durch. Die Screenshots zeigen den Assistenten aus dem MATMAKSA-Testlab (PVE04, Proxmox VE 9.2.11, Erfassung 2026-08-23).

**Schritt 1 – General:** Freie CT-ID wählen, einen kurzen Namen wie `01-pihole` vergeben und ein eigenes starkes Root-Passwort setzen. Die ID `101` ist nur das Beispiel dieses Labs; der Screenshot zeigt die freie Beispiel-ID `103`, weil `101` im Testlab bereits real belegt ist.

{{< figure src="01-general.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt General: Node pve04 ausgewählt, CT-ID 100 als Standardwert, Hostname-Feld noch leer." caption="Schritt General im Assistenten: Node pve04 ist ausgewählt. Die CT-ID 100 ist nur der Proxmox-Standardwert; du trägst hier eine bei dir freie ID ein. Screenshot aus dem MATMAKSA-Testlab (PVE04, 2026-08-23)." >}}

{{< figure src="02-general-filled.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt General ausgefüllt: CT-ID 103, Hostname 01-pihole, Root-Passwort maskiert." caption="Schritt General ausgefüllt: Die CT-ID 103 ist eine freie Beispiel-ID, weil 101 im Testlab bereits real belegt ist. Das Root-Passwort ist im Bild maskiert." >}}

**Schritt 2 – Template:** Das Debian-Template auswählen. Liegt noch kein Template auf dem Host, lädst du es vorher in der Proxmox-Oberfläche herunter: **Datacenter → Storage → local → CT Templates → Templates**, dort das Debian-13-Standard-Template markieren und über die Download-Schaltfläche laden. Im Test war das `debian-13-standard_13.6-1_amd64.tar.zst`.

{{< figure src="10-template-download.webp" alt="Proxmox-Download-Ansicht unter Datacenter → Storage → local → CT Templates: Download-Liste mit dem Debian-13-Standard-Template." caption="Template-Download: In der Proxmox-Oberfläche unter Datacenter → Storage → local → CT Templates das Debian-13-Standard-Template markieren und herunterladen." >}}

{{< figure src="03-template.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt Template: Storage local mit dem ausgewählten Template debian-13-standard_13.6-1_amd64.tar.zst." caption="Schritt Template: Das Debian-13-Standard-Template ist ausgewählt. Der Template-Name ist ein Labwert; die Template-Liste kann auf deinem Host anders aussehen." >}}

**Schritt 3 – Disk, CPU und Memory:** `local-lvm`, 8 GiB und 1 Kern eintragen. Der am 04.08.2026 ausgelesene CT-101-Stand nutzt 256 MiB RAM und 256 MiB Swap; plane für dein eigenes Setup eine passende Reserve statt blind diesen Labwert zu übernehmen.

{{< figure src="04-disks.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt Disks: Storage local-lvm und Disk-Größe 8 GiB." caption="Schritt Disks: 8 GiB auf local-lvm — Labwert dieses Aufbaus, kein allgemeines Minimum." >}}

{{< figure src="05-cpu.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt CPU: 1 Core eingestellt." caption="Schritt CPU: 1 vCPU — Labwert des PVE04-Testlabs." >}}

{{< figure src="06-memory.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt Memory: 256 MiB RAM und 256 MiB Swap." caption="Schritt Memory: 256 MiB RAM und 256 MiB Swap — Labwerte aus dem CT-101-Finalisierungsstand vom 04.08.2026." >}}

**Schritt 4 – Network:** `vmbr0` auswählen. Im Test-Lab waren die feste IPv4 `192.168.20.201/24` und das Gateway `192.168.20.254`; übernimm diese Werte **nicht**, sondern verwende eine freie Adresse und das Gateway deines eigenen Netzes. Ohne VLAN bleibt der VLAN-Tag leer.

{{< figure src="07-network.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt Network: Bridge vmbr0, VLAN 20, IPv4 192.168.20.201/24 und Gateway 192.168.20.254 (Labwerte)." caption="Schritt Network: Bridge vmbr0 mit VLAN 20 sowie die feste Lab-IPv4 192.168.20.201/24 und Gateway 192.168.20.254. Nutze in deinem Netz eine eigene freie IP, dein eigenes Gateway und bei Bedarf keinen VLAN-Tag." >}}

{{< figure src="08-dns.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt DNS: DNS-Server 1.1.1.1 und 1.0.0.1." caption="Schritt DNS: Upstream-DNS 1.1.1.1 und 1.0.0.1 — öffentliche Resolver ohne Geheimnischarakter." >}}

**Schritt 5 – Confirm:** Prüfe die Zusammenfassung, klicke auf **Finish** und starte den neuen Container anschließend links in der Proxmox-Übersicht.

{{< figure src="09-confirm.webp" alt="Create-LXC-Wizard von Proxmox VE 9.2, Schritt Confirm: Zusammenfassung mit CT-ID 103, Hostname 01-pihole, Template, 8 GiB, 1 Core, 256 MiB RAM/Swap, vmbr0 und DNS." caption="Schritt Confirm: Zusammenfassung vor dem Erstellen. Prüfe die Werte und klicke erst dann auf Finish." >}}

Die festen Werte sind kein allgemeines Rezept: Eine doppelt vergebene IP oder die Gateway-Adresse aus einem fremden Netz verhindert den Zugriff auf den Container.

Ein **LXC** ist ein schlanker Linux-Container. Er nutzt den Kernel des Proxmox-Hosts, bleibt aber ein eigener Gast. **Unprivilegiert** bedeutet: Der Container bekommt auf dem Host nicht automatisch weitreichende Root-Rechte.

Im Test-Lab lag CT 101 in VLAN 20. Ein **VLAN** trennt Netzbereiche logisch. Wenn du keine VLANs verwendest, ist das kein Problem: Hänge den Container einfach an deine normale Proxmox-Bridge **ohne** VLAN-Tag. Die feste IP-Adresse und das Gateway müssen dann zu deinem normalen Netz passen.

> **Kontrollpunkt vor dem Erstellen:** Notiere dir die freie feste IP-Adresse, das Gateway und die gewählte Container-ID. Erst wenn diese Werte zu deinem eigenen Netz passen, erstellst du den Container und startest ihn über die Proxmox-Oberfläche.

{{< figure src="pve04-ct101-konfiguration.webp" alt="Bereinigter Terminalauszug aus dem PVE04-Testlab: CT 101 nutzt eth0 über die Bridge vmbr0, im Lab VLAN 20, eine ausgeblendete feste Lab-IP, Debian und die aktivierte Firewall." caption="Netzwerknachweis vom 04.08.2026: Bridge vmbr0 und VLAN 20 gehören zum MATMAKSA-Testlab. Nutze in deinem Netz eine eigene freie IP und lasse den VLAN-Tag leer, wenn du keine VLANs verwendest." >}}

## 2. Erst parallel aufbauen, dann in Ruhe testen

Für den Aufbau nutzte der neue Container zunächst einen vorhandenen Resolver. Pi-hole leitete später unbekannte Anfragen an die dokumentierten Upstream-DNS-Server `1.1.1.1` und `1.0.0.1` weiter.

Der wichtige Punkt für Einsteiger: Ändere nicht gleichzeitig Container, DNS-Server, DHCP, Filterlisten und Router. Baue Pi-hole zuerst parallel auf und prüfe ihn direkt. So weißt du bei einem Fehler, an welcher Stelle du suchen musst.

Der neue Pi-hole wurde zuerst parallel aufgebaut und technisch getestet. Im Test-Lab wurde der Resolver des PVE04-Hosts erst später in einem separat gesicherten und geprüften Schritt auf Pi-hole umgestellt. Ob und wann dein gesamtes Heimnetz Pi-hole verwendet, ist ein eigener abgesicherter Schritt: Erst wenn du einen Rückweg für DNS-Änderungen dokumentiert hast, richtest du weitere Geräte auf Pi-hole als DNS-Server aus.

## 3. Pi-hole im gestarteten Container installieren

Öffne nach dem Start von CT 101 dessen **Console** in Proxmox. Das ist wichtig: Der Pi-hole-Installer stellt Rückfragen und braucht deshalb ein echtes interaktives Terminal.

Für diesen Aufbau kam das offizielle Debian-13-Template zum Einsatz. Die Installerdatei wurde von der offiziellen Adresse heruntergeladen und vor der Ausführung mit `less` gelesen. Das ist eine Sichtprüfung des Inhalts, keine kryptografische Echtheits- oder Integritätsprüfung.

Für die aktuelle Download- und Prüfanleitung verwende immer die [offizielle Pi-hole-Installationsdokumentation](https://docs.pi-hole.net/main/basic-install/). Die dort angebotene Installerdatei kann sich ändern. Wichtig ist der Ablauf: **offizielle Quelle öffnen → Datei lokal speichern → Inhalt prüfen → in der CT-Konsole interaktiv starten**.

Melde dich dafür in der Proxmox-**Console** des laufenden Containers als `root` an. Der folgende Ablauf entspricht dem hier dokumentierten, nicht gepipelten Vorgehen; lies die Datei vor dem Start und vergleiche sie bei Abweichungen mit der offiziellen Dokumentation:

```bash
curl -fsSL https://install.pi-hole.net -o pihole-install.sh
less pihole-install.sh
bash pihole-install.sh
```

Im Installer blieben DHCP, Unbound, DNS-over-HTTPS und eine lokale DNS-Zone deaktiviert. Als Upstreams sind aktuell `1.1.1.1` und `1.0.0.1` konfiguriert; Query Logging ist aktiv, der Blocking-Modus ist `NULL`. Das Weboberflächen-Passwort ist ein eigenes Geheimnis: nicht in Artikel, Screenshots oder Shell-Historie schreiben.

**In der CT-Konsole als `root`:** Prüfe nach der Installation Dienst und Versionen. `pihole version` und `pihole status` sind die üblichen Pi-hole-Prüfungen; falls der Wrapper wie im Finalisierungstest nicht im Pfad liegt, prüfst du den FTL-Dienst direkt.

```bash
pihole version
pihole status
systemctl is-active pihole-FTL
systemctl is-enabled pihole-FTL
```

`pihole version` zeigt die installierten Komponenten; `pihole status` fasst den Dienstzustand zusammen. Die beiden `systemctl`-Abfragen erwarten jeweils `active` beziehungsweise `enabled`. Weicht ein Ergebnis ab, ändere nicht vorsorglich Rechte oder LXC-Privilegien, sondern lies zuerst die zugehörigen Dienstprotokolle und die offizielle Pi-hole-Dokumentation. Im Finalisierungstest vom 04.08.2026 war FTL `active` und `enabled`; `pihole-FTL --version` meldete v6.7.

**Auf einem Testclient:** Öffne `http://<DEINE-PIHOLE-IP>/admin/` im Browser. Erscheint die Pi-hole-Anmeldeseite, ist die Weboberfläche erreichbar. Im PVE04-Test war der lokale Einstiegspunkt erreichbar und leitete zur Anmeldung weiter. Stelle die Weboberfläche nur im lokalen oder kontrollierten Verwaltungsnetz bereit – niemals ungeschützt im Internet.

{{< figure src="pihole-dashboard-overview.webp" alt="Bereinigtes Pi-hole-Dashboard mit Dienststatus, Gesamtzahl der DNS-Anfragen, blockierten Anfragen und Verlaufsgrafiken ohne Clientnamen oder einzelne Domains." caption="So sieht die Pi-hole-Übersicht nach einer erfolgreichen Anmeldung aus. Der bereinigte Screenshot stammt aus einer separaten MATMAKSA-Testumgebung; die angezeigten Zähler sind keine Messwerte von CT 101." >}}

## 4. DNS, Blocking und Neustart testen

Jetzt kommt der Teil, der aus einer Installation einen nutzbaren Dienst macht. Pi-hole wurde nicht nur einmal angepingt, sondern an mehreren Stellen geprüft.

| Test | Erwartetes Ergebnis | Dokumentiertes Ergebnis |
|---|---|---|
| Pi-hole FTL | Dienst läuft und startet automatisch | am 04.08.2026 `active` und `enabled` |
| Weboberfläche | lokale Verwaltungsadresse ist erreichbar | Einstiegspunkt leitete zum Anmeldefluss weiter |
| DNS über UDP und TCP | normale Domain liefert eine Antwort | vor und nach Neustart jeweils `NOERROR` |
| Blocking | eine getestete Domain liefert das konfigurierte NULL-Ergebnis | `ad.doubleclick.net` lieferte `0.0.0.0` |
| Neustart | Container und Pi-hole kommen wieder hoch | CT 101 nach 11 Sekunden wieder `running`; FTL aktiv |

DNS kann UDP und TCP verwenden. Viele Anfragen laufen über UDP; TCP bleibt für bestimmte Antworten wichtig. Deshalb wurden beide Wege getrennt geprüft.

**Auf einem Testclient oder in einer getrennten Test-Shell außerhalb des Pi-hole-Containers:** Setze zuerst deine eigene Adresse; die PVE04-Labadresse ist kein Kopierwert.

```bash
PIHOLE_IP="<DEINE-PIHOLE-IP>"

dig @"$PIHOLE_IP" deb.debian.org A +time=2 +tries=1
dig +tcp @"$PIHOLE_IP" deb.debian.org A +time=2 +tries=1
dig @"$PIHOLE_IP" ad.doubleclick.net A +short +time=2 +tries=1
```

Ersetze `<DEINE-PIHOLE-IP>`. Im PVE04-Finalisierungstest antworteten die normale Domain über UDP und TCP jeweils mit `NOERROR`, ohne Timeout. Der aktuelle Blocking-Modus ist `NULL`; deshalb lieferte `ad.doubleclick.net` dort `0.0.0.0`. Andere Pi-hole-Konfigurationen können ein anderes Blocking-Ergebnis zurückgeben.

> **Erwartetes Ergebnis nach dem Neustart:**
> Der Container steht wieder auf `running`, Pi-hole antwortet erneut auf DNS-Anfragen und die Weboberfläche ist erreichbar.

Kurz nach Aufbau und Test lagen die dokumentierten Werte bei 20 MiB RAM-Nutzung, 0 MiB verwendetem Swap und ungefähr 874 MiB auf der Root-Disk. Das sind Momentaufnahmen, keine Langzeitmessung oder allgemeine Mindestwerte.

## 5. Typische Fehler – kurz und gezielt lösen

### Der Installer wartet auf Eingaben oder bricht ab

Starte den Installer direkt in der interaktiven **Console** des Containers. Eine nicht interaktive Shell kann Rückfragen des Installers nicht zuverlässig anzeigen oder beantworten.

### Die Weboberfläche ist nicht erreichbar

Prüfe zuerst, ob du die richtige Container-IP verwendest und ob `systemctl is-active pihole-FTL` den Zustand `active` meldet. Ändere nicht gleichzeitig Firewall, Netzwerk und Pi-hole-Konfiguration – sonst lässt sich die Ursache kaum eingrenzen.

### Im Protokoll stehen Warnungen, DNS funktioniert aber

Warnungen allein sind kein Grund, den Container privilegiert zu betreiben oder Rechte pauschal zu ändern. Beim ursprünglichen PVE04-Aufbau waren zwei einzelne Pi-hole-Pfade betroffen; im Finalisierungstest war keine Rechteänderung mehr erforderlich. Prüfe deshalb immer zuerst die konkret ausgefallene Funktion und den genannten Pfad.

## 6. Fazit: Pi-hole passt gut, wenn du klein anfängst

Pi-hole passt gut als erster Dienst, wenn du einen kleinen Proxmox-Host hast und zunächst nur einen einzelnen Testclient umstellst. Der **kontrollierte Weg** ist: Container klein halten, Netzwerk festlegen, installieren, DNS und Blocking prüfen und den Neustart testen. Backup und Restore sind im separaten Backup-Beitrag ausführlicher erklärt.

Warte mit der Umstellung deines gesamten Heimnetzes, solange noch kein klarer Rückfallweg für DNS-Änderungen existiert. So bleibt ein Fehler auf einen Testcontainer oder Testclient begrenzt.

## Nächste sinnvolle Schritte

- [Pi-hole und AdGuard Home auf dem Futro S7010 vergleichen]({{< relref "/posts/pihole-adguard-futro-s7010-vergleich" >}}): Der Vergleich nutzt getrennte Debian-12-Testcontainer und eigene RAM-/DNS-Messreihen. Übertrage diese Messwerte nicht ungeprüft auf den hier dokumentierten Debian-13-CT 101.
- [Proxmox-Backup und Restore mit USB-Festplatte testen]({{< relref "/posts/proxmox-usb-festplatte-backup-ziel" >}}): Das hier geprüfte Backup ist kein Restore-Nachweis; der separate Guide beschreibt einen isolierten Restore-Test.

## FAQ

### Reichen 256 MiB RAM für Pi-hole im LXC?

Im Finalisierungstest vom 04.08.2026 liefen im dokumentierten CT 101 FTL, DNS über UDP und TCP, Blocking, der Neustart und das Snapshot-Backup mit 256 MiB RAM und 256 MiB Swap. Andere Filterlisten, Versionen oder Umgebungen können mehr Reserve benötigen.

### Brauche ich für Pi-hole ein VLAN?

Nein. Im Test-Lab kam VLAN 20 zum Einsatz. Ohne VLAN verwendest du einfach deine normale Proxmox-Bridge ohne VLAN-Tag.

### Ist ein erfolgreiches Snapshot-Backup ein getesteter Restore?

Nein. Der Sicherungslauf war erfolgreich, ein Restore-Test ist für dieses Projekt aber nicht dokumentiert.

### Warum wurden die LXC-Warnungen nicht repariert?

Weil sie keine Pi-hole-Funktion blockierten. DNS, Weboberfläche, Blocking und Neustart waren erfolgreich. Eine Änderung ohne nachgewiesenen Fehler hätte nur zusätzliche Risiken geschaffen.

## ✅ Das solltest du jetzt können

- [ ] Du weißt, was Pi-hole beim DNS-Weg macht.
- [ ] Du kannst die minimale Containergröße einordnen.
- [ ] Du weißt, dass ein VLAN für den Einstieg nicht zwingend ist.
- [ ] Du kannst eine normale DNS-Antwort von einem Blocking-Ergebnis unterscheiden.
- [ ] Du weißt, warum ein Neustarttest zum Aufbau dazugehört.
- [ ] Du weißt, dass Backup und Restore in einem separaten Beitrag behandelt werden.

## Offizielle Dokumentation

- [Pi-hole: Installation](https://docs.pi-hole.net/main/basic-install/) – Der offizielle Installer kann heruntergeladen und vor der Ausführung geprüft werden.
- [Proxmox VE Administration Guide: Container Toolkit](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#chapter_pct) – Grundlagen zu LXC-Containern, Einstellungen und Sicherungen.
- [Debian „trixie“ Release Information](https://www.debian.org/releases/trixie/) – Einordnung von Debian 13.6 als `trixie`.
