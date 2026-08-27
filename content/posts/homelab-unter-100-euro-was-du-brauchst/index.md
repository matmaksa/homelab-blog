+++
title = "Homelab unter 100€: Was du wirklich brauchst"
description = "Einsteiger-Guide für das erste Homelab unter 100 Euro: verständliche Begriffe, klare Hardware-Basis, Debian als einfacher Start und ein erstes abgeschlossenes Praxisprojekt."
date = 2026-07-06
lastmod = 2026-08-27
draft = false
ShowToc = true
ShowShareButtons = true
ShowPostNavLinks = true
ShowCodeCopyButtons = true
tags = ["homelab", "einsteiger", "thin-client", "debian", "proxmox", "sparen"]
categories = ["Homelab"]

# Public Article Classification
preview_content_type = "public_article"
publish_eligible = true
user_visual_approval_required = false
fact_check_required = false
link_check_required = false
price_check_required = false
ebay_disclosure_expert_review_required = true
ebay_disclosure_expert_review_blocking = false
recommended_action = "finale Owner-Entscheidung über eine öffentliche Aktualisierung einholen."
content_intent = "pillar"
monetization_intent = "soft_affiliate"
affiliate_disclosure_required = true
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = false
risk_level = "medium"
content_state = "published"
audit_status = "passed"
user_approval_required = false
approved_for_publish = true
next_action = "monitor_and_promote"

[cover]
image = "featured.jpg"
alt = "Fujitsu Futro Thin Client auf einem Schreibtisch als Beispiel für einen günstigen Homelab-Einstieg"
relative = true
caption = "Ein kleiner Bürorechner kann für den Einstieg reichen; Preise und konkrete Angebote sind Momentaufnahmen und sollten regelmäßig geprüft werden."
+++

**Überarbeitungsstand: 27. August 2026 | Zielgruppe: Homelab-Einsteiger ohne Linux-Vorerfahrung**

Hinweis: Dieser Artikel enthält Affiliate-Links. Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision. Für dich entstehen dadurch keine Mehrkosten. Als Amazon-Partner verdiene ich an qualifizierten Verkäufen. Dieser Artikel enthält außerdem Werbung: eBay-Partnerlinks (eBay Partner Network). Wenn du über diese Links einkaufst, erhalte ich ggf. eine Provision; für dich entstehen dadurch keine Mehrkosten.

## Kurzantwort

Für dein erstes Homelab brauchst du keinen Serverschrank. Ein kleiner Bürorechner, ein Netzwerkkabel und ein freier Anschluss am Router reichen für den Start. Wenn du Linux noch nicht kennst, installierst du zuerst **Debian direkt auf dem Gerät** und baust einen kleinen Webserver. Proxmox ist der nächste Schritt, sobald du mehrere getrennte Systeme auf derselben Hardware betreiben möchtest.

Die Grenze von 100 Euro kann mit refurbished Hardware erreichbar sein. Ob ein konkretes Angebot wirklich ins Budget passt, hängt aber von RAM, SSD, Netzteil, Kabeln, Zustand und Versand ab. Prüfe deshalb immer den Gesamtumfang des Angebots und aktuelle Preise.

## Für wen ist dieser Artikel?

Dieser Einstieg passt zu dir, wenn du:

- IT-Wissen zu Hause praktisch aufbauen möchtest,
- einen leisen Rechner für kleine lokale Dienste suchst,
- wenig Linux-Erfahrung und ein begrenztes Budget hast,
- refurbished Business-Hardware statt eines neuen Gaming-PCs verwenden möchtest.

Ein paar Begriffe vorab:

- **Docker** startet Anwendungen in voneinander getrennten Software-Umgebungen, sogenannten Containern.
- **Pi-hole** ist ein DNS-Werbeblocker für Geräte in deinem Heimnetz.
- **Home Assistant** ist eine Plattform zur Steuerung und Automatisierung deines Smart Homes.
- **VPN** bezeichnet eine verschlüsselte Verbindung in ein anderes Netzwerk, zum Beispiel für den Zugriff von unterwegs.

Du musst diese Programme nicht sofort installieren. Dein erstes Ziel ist kleiner: Gerät anschließen, Linux starten und eine Testseite im eigenen Heimnetz öffnen.

## Das Herz: ein Thin Client oder Mini-PC

Ein **Thin Client** ist ein kleiner Bürorechner, der ursprünglich für einfache Arbeitsplätze gebaut wurde. Er ist meist kompakt, sparsam und leise. Für ein Homelab bekommt er ein normales Linux-System und übernimmt kleine Serveraufgaben.

Ein **Mini-PC** ist ebenfalls ein kleiner Rechner, hat aber häufig eine stärkere CPU und mehr Aufrüstmöglichkeiten. Dafür kostet er meist mehr. Für den sehr günstigen Einstieg ist ein Thin Client deshalb oft realistischer.

Modelle wie Fujitsu Futro S740 oder S7010, HP t730 und Dell Wyse 5070 werden refurbished angeboten. Eine brauchbare Basis liegt nach Marktprüfung vom 27. August 2026 meist bei **30–50 Euro**. Einzelne Minimalkonfigurationen können bei rund 20 Euro beginnen, enthalten dann aber häufig wenig RAM oder SSD und zuzüglich Versand. Achte beim einzelnen Angebot vor allem auf diese Punkte:

- Ist ein passendes Netzteil enthalten?
- Sind RAM und SSD bereits eingebaut?
- Welchen Monitoranschluss hat das Gerät? Viele Thin Clients verwenden DisplayPort statt HDMI.
- Ist die SSD mit genau diesem Modell kompatibel?
- Gibt es Rückgaberecht oder Gewährleistung beim Händler?

### Fujitsu Futro S740 und S7010 kurz eingeordnet

| Frage | Futro S740 | Futro S7010 |
|---|---|---|
| Wofür reicht er? | Pi-hole, ein kleiner Webserver, erste Linux-Tests | Pi-hole, ein kleiner Webserver, erste Linux- und Proxmox-Tests |
| Arbeitsspeicher | Angebot und Datenblatt prüfen | Angebot und Datenblatt prüfen |
| Monitoranschluss | 2 × DisplayPort | 2 × DisplayPort |
| Einordnung | sehr günstiger Einstieg | etwas mehr Reserve, wenn passend verfügbar |

Der Futro S7010 bleibt ein leiser, sparsamer Low-Budget-Einstieg. Er ist keine Empfehlung für lokale KI-Modelle oder Ollama.

Leistungsfähigere Business-Mini-PCs wie Lenovo ThinkCentre M710q/M720q, HP ProDesk 400 G5 oder Dell OptiPlex 3070 Micro können mehr Reserven bieten. Die bisher genannten Preisbereiche wurden für diese Revision nicht aktualisiert und sind **keine aktuelle Kaufgrundlage**.

{{< ebay-link query="Thin Client Homelab" text="Aktuelle Angebote für refurbished Thin Clients bei eBay prüfen" customid="homelab-100-thin-clients" >}}

## Speicher: Was bedeuten SSD und RAM?

- Die **SSD** ist der dauerhafte Speicher. Dort liegen Betriebssystem, Programme und Daten.
- **RAM** ist der schnelle Arbeitsspeicher, den laufende Programme verwenden.

Für den Einstieg ist ein vollständiges Gerät mit eingebautem RAM und passender SSD einfacher als ein leeres Gehäuse. Eine kleine SSD kann für Linux und erste Übungen reichen; entscheidend ist die Kompatibilität mit dem konkreten Modell. Beim Futro darfst du eine M.2-SATA-SSD nicht mit einer ähnlich aussehenden NVMe-SSD verwechseln.

Mehrere Dienste benötigen mehr RAM. Kaufe aber nicht auf Verdacht: Prüfe zuerst das Datenblatt des exakten Modells und die bereits eingebaute Ausstattung.

## Netzwerk: Router zuerst, Switch nur bei Bedarf

Verbinde den Homelab-Rechner möglichst per **LAN-Kabel** mit deinem Router. LAN ist die kabelgebundene Netzwerkverbindung und für den Einstieg einfacher vorhersehbar als WLAN.

Ein **Switch** ist vereinfacht eine Mehrfachsteckdose für Netzwerkkabel: Aus einem Netzwerkanschluss werden mehrere. Hat dein Router noch einen freien LAN-Port, brauchst du zunächst keinen zusätzlichen Switch. Erst wenn alle Ports belegt sind, reicht ein einfacher, nicht verwalteter Gigabit-Switch mit fünf Ports.

- **Gigabit** bedeutet hier bis zu 1 Gigabit pro Sekunde im lokalen Netz.
- **Unmanaged** bedeutet, dass du den Switch nur anschließt und nichts konfigurieren musst.
- **Cat-6-Patchkabel** sind kurze Netzwerkkabel, die für Gigabit-Verbindungen geeignet sind.

Wifi 7, ein 10-Gigabit-Switch oder ein Enterprise-Switch helfen dir beim ersten Projekt nicht.

## Dein erster Abend nach dem Kauf

Lege diese Dinge bereit:

- Thin Client oder Mini-PC samt passendem Netzteil,
- ein LAN-Kabel,
- Monitor und passendes Bildkabel,
- USB-Tastatur,
- USB-Stick für die Linux-Installation,
- einen zweiten Rechner zum Herunterladen und Schreiben des Installationsabbilds.

Dann gehst du so vor:

1. **Gehäuse und Lieferumfang prüfen:** Stimmen Gerät, Netzteil, RAM und SSD mit dem Angebot überein?
2. **Direkt anschließen:** Verbinde Monitor und Tastatur mit dem Homelab-Rechner. Stecke das LAN-Kabel direkt in einen freien Router-Port; ein Switch ist noch nicht nötig.
3. **Einmal normal starten:** Prüfe, ob das Gerät ein Bild zeigt und RAM sowie SSD erkennt. Ändere im BIOS oder UEFI noch nichts, was du nicht verstehst.
4. **Installations-USB vorbereiten:** Lade das Debian-Installationsabbild nur von der offiziellen Debian-Seite und schreibe es auf den USB-Stick.
5. **Vorhandene Daten schützen:** Die Linux-Installation kann den gewählten Datenträger löschen. Sichere vorhandene Daten und prüfe im Installer genau, welche SSD ausgewählt ist.
6. **Debian installieren:** Wähle für den ersten Versuch die grafische Installation. Nach dem Neustart ziehst du den USB-Stick ab.
7. **Verbindung prüfen:** Melde dich zunächst noch mit Monitor und Tastatur an. Erst wenn Debian läuft und eine Netzwerkadresse anzeigt, kann das Gerät später ohne Monitor betrieben werden.

Die offizielle Debian-Anleitung beschreibt Vorbereitung, USB-Start und Installation ausführlich: [Debian GNU/Linux Installation Guide](https://www.debian.org/releases/stable/amd64/).

## Debian oder Proxmox? Die klare Einsteigerentscheidung

**Starte mit Debian direkt auf dem Gerät**, wenn dies dein erster Linux-Server ist. Du lernst Anmeldung, Updates, Netzwerk und Programme, ohne gleichzeitig eine Virtualisierungsschicht verstehen zu müssen.

Nimm **Proxmox VE** stattdessen erst dann, wenn du bereits weißt, dass du mehrere getrennte virtuelle Maschinen oder Linux-Container auf demselben Rechner betreiben möchtest. Eine virtuelle Maschine ist ein vollständiger Rechner in Software; ein LXC-Container ist eine leichtere, getrennte Linux-Umgebung.

| Dein Ziel | Entscheidung |
|---|---|
| Ein Gerät, ein erstes Projekt, möglichst wenig neue Begriffe | Debian direkt installieren |
| Mehrere getrennte Testsysteme auf einem Gerät | Proxmox VE installieren |
| Du bist noch unsicher | Mit Debian beginnen und Proxmox als Folgeprojekt planen |

Proxmox löscht bei der Installation ebenfalls den ausgewählten Datenträger. Die offizielle Installationsdokumentation findest du bei [Proxmox VE](https://pve.proxmox.com/pve-docs/chapter-pve-installation.html). Eine deutschsprachige Einordnung bietet außerdem unser Artikel [Proxmox VE als VMware-Alternative im Homelab]({{< relref "virtualisierung-kostenlos-2026-proxmox-vmware-alternative" >}}).

## Erstes abgeschlossenes Projekt: eine lokale Webseite

Mit diesem kleinen Projekt prüfst du drei Dinge: Debian kann Pakete installieren, der Webserver läuft und ein zweites Gerät erreicht dein Homelab im lokalen Netz. Die Testseite bleibt zu Hause; richte **keine Portweiterleitung im Router** ein.

### Voraussetzung

Debian läuft, das LAN-Kabel steckt und du bist mit einem normalen Benutzer angemeldet, der `sudo` verwenden darf.

### 1. Netzwerkadresse anzeigen

```bash
hostname -I
```

Notiere die lokale IPv4-Adresse, zum Beispiel `192.168.178.50`. Deine Adresse wird anders aussehen. Wenn mehrere Werte erscheinen, nimm nicht blind irgendeinen: Prüfe im Router, welche Adresse zum Homelab-Rechner gehört.

### 2. Paketliste aktualisieren und Nginx installieren

**Nginx** ist ein Webserver. Er liefert Webseiten an einen Browser aus.

```bash
sudo apt update
sudo apt install nginx
```

Bestätige die Installation nur, wenn `apt` das Paket `nginx` aus den eingerichteten Debian-Paketquellen anzeigt. Füge für dieses Einstiegsprojekt keine fremde Paketquelle hinzu.

### 3. Dienst prüfen

```bash
systemctl is-active nginx
```

Die erwartete Ausgabe lautet `active`. Das bestätigt nur, dass der Dienst auf diesem Rechner läuft. Ob die Seite im Netz erreichbar ist, prüfst du im nächsten Schritt.

### 4. Testseite von einem zweiten Gerät öffnen

Öffne auf einem Laptop oder Smartphone im selben Heimnetz:

```text
http://DEINE-IP-ADRESSE
```

Ersetze `DEINE-IP-ADRESSE` durch den Wert aus Schritt 1. Erscheint die Nginx-Startseite, ist dein erstes Homelab-Projekt abgeschlossen.

### Wenn die Seite nicht erscheint

1. Prüfe, ob beide Geräte im selben Heimnetz sind.
2. Führe `hostname -I` erneut aus und vergleiche die Adresse mit der Geräteliste im Router.
3. Prüfe mit `systemctl is-active nginx`, ob der Dienst noch `active` meldet.
4. Kontrolliere LAN-Kabel und Router-Port.
5. Richte zur Fehlersuche keine Portweiterleitung und keine Freigabe ins Internet ein.

Die Paketbeschreibung von Debian bestätigt Nginx als Webserver; die Nginx-Dokumentation erklärt Start, Stop und Konfiguration: [Debian-Paket nginx](https://packages.debian.org/stable/nginx) und [Nginx Beginner’s Guide](https://nginx.org/en/docs/beginners_guide.html).

## Was du am Anfang nicht brauchst

- **USV:** Eine unterbrechungsfreie Stromversorgung kann später sinnvoll sein, ist aber für diesen Test kein Pflichtkauf.
- **Rack:** Das ist ein Metallgestell für Servergeräte. Ein Thin Client kann einfach neben dem Router stehen.
- **Enterprise-Switch:** Das ist ein aufwendig verwaltbarer Netzwerkverteiler für größere Umgebungen. Für den Start reicht der Router-Port oder ein einfacher unmanaged Switch.
- **NAS:** Das ist ein eigener Netzwerkspeicher. Für die erste Testseite brauchst du ihn nicht. Wenn später wichtige Daten entstehen, planst du ein separates Backup-Ziel und testest die Wiederherstellung.
- **Fernzugriff:** Tailscale, Headscale, DynDNS und eigene Domains sind Folgeprojekte. Öffne den Test-Webserver nicht ins Internet.

## Beispiel-Budget: Marktstand vom 27. August 2026

Die folgende Tabelle ist eine Orientierung aus aktuellen Gebrauchtangeboten. Zustand, Ausstattung, Händler und Versand können das Ergebnis verändern; prüfe vor einem Kauf immer das konkrete Angebot.

| Komponente | Bisherige Orientierung |
|---|---|
| Thin Client mit RAM, kleiner SSD und Netzteil | 30–50 € als brauchbare Basis; etwa 20 € nur bei Minimalkonfiguration zuzüglich Versand |
| 5-Port-Gigabit-Switch | nur nötig, wenn am Router kein Port frei ist |
| LAN-Kabel | vorhandenes Kabel zuerst weiterverwenden |
| **Gesamt** | **Basis-Konfiguration inklusive Versand meist etwa 41–58 €; unter 100 € ist realistisch, Nachrüstungen können das Budget überschreiten** |

Ein vermeintlich günstiges Gerät wird schnell teurer, wenn Netzteil, RAM, SSD oder Bildadapter fehlen. Vergleiche deshalb immer den vollständigen Lieferumfang statt nur den Gerätepreis.

## FAQ

### Muss der Homelab-Rechner rund um die Uhr laufen?

Nein. Für Lernprojekte kannst du ihn nur einschalten, wenn du daran arbeitest. Ein Dauerbetrieb wird erst nötig, wenn andere Geräte einen Dienst ständig verwenden sollen.

### Brauche ich sofort einen Switch?

Nein. Ein freier LAN-Port am Router reicht. Einen Switch brauchst du erst, wenn dir Netzwerkanschlüsse fehlen.

### Kann ich mit Debian später noch Proxmox ausprobieren?

Ja, aber die Proxmox-Installation verwendet das Gerät anschließend neu und kann die SSD löschen. Sichere deshalb vorher alle Daten. Für Experimente kannst du später auch ein zweites Laufwerk oder ein separates Testgerät nutzen.

### Ist die Nginx-Testseite aus dem Internet erreichbar?

Nicht allein durch die Installation. Lass sie im lokalen Netz und richte keine Router-Portweiterleitung ein. Ein sicherer Fernzugriff ist ein eigenes Folgeprojekt.

## Fazit

Für den ersten Homelab-Abend reicht ein vollständiger Thin Client oder Mini-PC, ein LAN-Kabel, ein Monitor und eine Tastatur. Schließe das Gerät zuerst direkt am Router an, installiere Debian und bringe eine lokale Testseite zum Laufen. Damit hast du ein überprüfbares Ergebnis, bevor Docker, Pi-hole, Proxmox oder Fernzugriff zusätzliche Komplexität bringen.

Der nächste sinnvolle Schritt ist die Entscheidung für einen dauerhaften Dienst. Wenn du mehrere getrennte Systeme betreiben möchtest, lies die [Proxmox-Einordnung]({{< relref "virtualisierung-kostenlos-2026-proxmox-vmware-alternative" >}}). Wenn du bei einem einzigen Debian-System bleibst, dokumentiere zuerst Updates, Benutzerzugang und Backup-Rückweg.

## Das solltest du jetzt können

- [ ] Thin Client, Mini-PC und Switch in eigenen Worten unterscheiden
- [ ] Gerät mit Netzteil, Monitor, Tastatur und LAN anschließen
- [ ] Debian als einfachen Start und Proxmox als Virtualisierungsoption einordnen
- [ ] die lokale IP-Adresse des Servers finden
- [ ] Nginx installieren und den Dienstzustand prüfen
- [ ] die Testseite von einem zweiten Gerät im Heimnetz öffnen
- [ ] erklären, warum keine Portweiterleitung nötig ist

## Quellen

- [Debian GNU/Linux Installation Guide](https://www.debian.org/releases/stable/amd64/)
- [Debian-Paket nginx](https://packages.debian.org/stable/nginx)
- [Nginx Beginner’s Guide](https://nginx.org/en/docs/beginners_guide.html)
- [Proxmox VE: Installing Proxmox VE](https://pve.proxmox.com/pve-docs/chapter-pve-installation.html)
