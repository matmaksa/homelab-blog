+++
title = "Pi-hole im Proxmox-Homelab: Der echte Weg von der Installation bis zum Backup"
description = "Pi-hole im unprivilegierten Proxmox-LXC: echter TTY-Fehler, minimale Rechtekorrektur, DNS-Tests, Neustart und Snapshot-Backup."
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

[sitemap]
  exclude = true

# Preview Classification
preview_content_type = "article_draft"
publish_eligible = false
user_visual_approval_required = true
fact_check_required = true
link_check_required = true
price_check_required = false
recommended_action = "Eigentümer prüft und genehmigt den final redigierten Pi-hole-Artikel einschließlich der fünf Screenshot-Platzhalter."
content_intent = "deep_dive"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = false
risk_level = "medium"

content_state = "draft_generated"
audit_status = "technical_factcheck_completed"
user_approval_required = true
approved_for_publish = false
next_action = "owner_review_and_approve_final_pihole_article"
+++

> [!IMPORTANT]
> **Preview – noch nicht veröffentlicht.** Dieser redigierte Entwurf ist nur zur visuellen und redaktionellen Prüfung bestimmt.
> - Typ: `article_draft`
> - Publish-Eligible: `false`
> - Technischer Faktencheck: abgeschlossen
> - Nächster Schritt: Eigentümerprüfung einschließlich der fünf Screenshot-Platzhalter.

---

# Pi-hole im Proxmox-Homelab: Der echte Weg von der Installation bis zum Backup

Pi-hole war mein erster Dienst auf PVE04. Ein DNS-Werbeblocker ist dafür ein guter Einstieg: Ich konnte einen eigenen Container planen, Netzwerk und DNS verstehen, die Funktion gezielt testen und anschließend einen Sicherungspunkt anlegen.

PVE04 ist ein eigenständiger, nicht produktiver Proxmox-Testhost. Dieser Artikel ist deshalb kein Bauplan für jedes Heimnetz und auch keine Migration meines produktiven Homelabs. Er zeigt stattdessen den dokumentierten Ablauf dieses Projekts: Was funktionierte, was zunächst scheiterte und was bewusst offen blieb.


## Kurz gesagt

Pi-hole passt als erster Dienst, wenn du bereits einen kleinen Proxmox-Host betreibst und DNS nicht nur einschalten, sondern nachvollziehbar testen möchtest. In diesem Projekt beantwortete der Container DNS-Anfragen über UDP und TCP, löste externe Namen auf, blockierte die getesteten Standard-Werbedomains, startete nach einem Neustart wieder und wurde per Snapshot mit zstd gesichert.

Entscheidend war aber nicht allein die Installation. Der erste Installer-Lauf scheiterte ohne nutzbares Terminal. Zwei Pi-hole-Pfade hatten falsche Eigentümer, und beim Backup fiel ein separates Thin-Pool-Risiko auf. Erst nachdem diese Punkte eingegrenzt, gezielt korrigiert oder als offen festgehalten waren, war der Aufbau nachvollziehbar dokumentiert.

| Voraussetzung | Dokumentierter Wert |
|---|---|
| ⏱ Zeit | Installations-, Test- und Dokumentationsdauer wurden nicht getrennt erfasst. |
| 💰 Kosten | Pi-hole selbst ohne Lizenzkosten; PVE04 wurde für 41 Euro bei pioparts.de gekauft. |
| 📊 Schwierigkeit | Mittel: Proxmox-Grundlagen, feste Netzwerkkonfiguration und kontrollierte DNS-Tests sind nötig. |
| 🖥️ Testhost | Fujitsu Futro S7010, 4 CPU-Kerne, 4 GB RAM, 64-GB-SSD; eigenständiges Content- und Test-Lab ohne Cluster. |
| 🎯 Ziel | Einen Pi-hole-LXC nachvollziehbar aufbauen, testen und sichern. |
| ✅ Getestet mit | Proxmox VE, Debian 13.6, Pi-hole Core v6.4.3, Web v6.6 und FTL v6.7. |

[SCREENSHOT BENÖTIGT: Bereinigte Proxmox-Übersicht von PVE04 mit dem Pi-hole-Container; keine privaten Netzdaten oder Zugangsinformationen.]

## 1. Warum Pi-hole mein erster Dienst auf PVE04 wurde

DNS ist das Telefonbuch des Netzes: Bevor ein Gerät `example.com` öffnen kann, muss es die passende IP-Adresse ermitteln. Pi-hole kann bekannte Werbe- und Tracking-Domains anhand seiner Listen schon an dieser Stelle blockieren.

Genau deshalb eignet sich Pi-hole als erster Dienst. Das Ergebnis lässt sich leicht prüfen, der Aufbau verlangt aber trotzdem saubere Grundlagen: eine feste Netzwerkkonfiguration, klar benannte Upstream-DNS-Server und einen vorbereiteten Rückweg, bevor ein Host auf den neuen Resolver zeigt.

Pi-hole blockiert nicht jede sichtbare Werbung. DNS-Blocking arbeitet mit Domainnamen. Werbung, die über dieselbe Domain wie der eigentliche Inhalt ausgeliefert wird, kann weiterhin erscheinen. Für das Projekt war das kein Nachteil: Ich wollte zuerst nachvollziehen, ob ein schlanker, eigener DNS-Dienst zuverlässig läuft.

Wenn du vor der Installation noch zwischen Pi-hole und AdGuard Home schwankst, passt der vorhandene Praxisvergleich **„Pi-hole oder AdGuard Home auf einem Futro S7010: Was läuft mit 256 MB RAM?“** als Entscheidungshilfe. Dieser Artikel beginnt dort, wo der Vergleich endet: bei einem konkreten Pi-hole-Projekt.

## 2. Ausgangslage und verwendete Hardware

PVE04 ist ein Fujitsu Futro S7010 mit vier CPU-Kernen, 4 GB installiertem RAM und einer 64-GB-SSD. Die Live-Inventur wies davon 3,6 GiB als nutzbaren RAM aus. Der Kaufpreis lag bei 41 Euro bei pioparts.de. Der Host ist kein Cluster und kein produktiver Homelab-Server. Er dient ausschließlich als eigenständiges Content- und Test-Lab.

Diese Abgrenzung ist wichtig. Ein Erfolg auf PVE04 beweist nicht, dass jede Router-, DHCP- oder DNS-Konfiguration in einem anderen Heimnetz identisch funktioniert. PVE04 hatte weder eine lokale `home.lab`-DNS-Zone noch Pi-hole-DHCP, Unbound oder DNS-over-HTTPS. Auch einen gemessenen Stromverbrauch über Home Assistant gab es nicht.

Für Pi-hole entstand der Container mit der VMID 101 und dem Namen `01-pihole`:

| Bereich | Konfiguration |
|---|---|
| Basis | Debian 13.6 als unprivilegierter LXC |
| CPU | 1 vCPU |
| Arbeitsspeicher | 512 MiB RAM und 512 MiB Swap |
| Root-Disk | 8 GiB auf `local-lvm` |
| Netzwerk | Bridge `vmbr0`, VLAN 20 |
| Adresse | `192.168.20.201/24`, Gateway `192.168.20.254` |
| Startverhalten | Autostart aktiviert |
| Upstream-DNS | `1.1.1.1` und `1.0.0.1` |

Ein **LXC** ist ein Linux-Container: Er nutzt den Kernel des Hosts, bleibt aber als eigener, schlanker Gast getrennt. **Unprivilegiert** bedeutet hier zusätzlich, dass der Container auf dem Proxmox-Host nicht automatisch weitreichende Root-Rechte erhält. Für diesen kleinen DNS-Dienst war kein zusätzlicher Sonderzugriff dokumentiert. Deshalb blieb die Konfiguration bei einem Kern, 512 MiB RAM, 8 GiB Disk und ohne optionale Container-Features ohne belegten Bedarf.

Ein **VLAN** trennt Netzbereiche logisch auf derselben Netzwerkinfrastruktur. Hier liegt CT 101 in VLAN 20. Die Adresse und das Gateway bleiben feste Teile seiner Netzwerkkonfiguration.

[SCREENSHOT BENÖTIGT: Bereinigte CT-101-Konfiguration mit CPU, RAM, Disk, VLAN und Autostart; Netzwerkadresse im Bild schwärzen.]

## 3. Planung des neuen Containers

Vor der Installation war die DNS-Reihenfolge der wichtigste Punkt. Ein DNS-Server lässt sich schlecht reparieren, wenn der Host für jede Namensauflösung schon von genau diesem noch nicht funktionierenden Dienst abhängt. Deshalb entstand der neue Container zunächst parallel. Während des Aufbaus nutzte er vorübergehend `192.168.20.13` als Resolver; Pi-hole leitete später an die dokumentierten **Upstream-DNS-Server** `1.1.1.1` und `1.0.0.1` weiter. Upstream-DNS bezeichnet die Server, an die Pi-hole Anfragen weitergibt, die es nicht selbst beantwortet.

Die Planung enthielt außerdem einen Rückweg. Der bestehende DNS-Zustand durfte erst verändert werden, nachdem Pi-hole als eigener Dienst getestet worden war. Die Grundregel lautet auch für Einsteiger: Nicht gleichzeitig Container, DNS-Server, DHCP, Filterlisten und Router-Konfiguration ändern. Sonst ist bei einem Fehler nicht mehr klar, welcher Schritt die Ursache war.

Für eine spätere PVE04-DNS-Umstellung wurde ein kontrollierter Ablauf mit Sicherung und sofortigem Rückfall vorbereitet. Der neue Pi-hole wurde parallel aufgebaut und technisch getestet. Die anschließende Umschaltung des PVE04-Resolvers sowie die Ablösung der alten Testcontainer waren als separates Abschlussarbeitspaket geplant.

Der letzte eindeutig dokumentierte Stand lautet: PVE04 verwendete weiter `192.168.20.12`; CT 100 `docs-pihole` und CT 102 `docs-adguard` liefen weiterhin. Für eine anderslautende Behauptung über Cutover, Löschung oder eine wieder freie VMID 102 liegt in den geprüften Projektakten kein nachvollziehbarer Abschlussnachweis vor.

## 4. Debian-LXC und Pi-hole installieren

Für den Aufbau kam das offizielle Debian-13-Template zum Einsatz. Den Pi-hole-Installer führte ich nicht blind als Pipeline aus dem Internet aus: Die offizielle Installerdatei wurde zuerst gespeichert und geprüft. Erst danach begann die interaktive Installation.

Dort lag auch der erste reale Fehler. Der erste Versuch hatte kein nutzbares TTY. Ein **TTY** ist vereinfacht ein Terminal, über das ein Programm Ein- und Ausgaben in einer interaktiven Sitzung zuverlässig steuert. Der Installer konnte diese Umgebung im ersten Lauf nicht öffnen; die Installation blieb dadurch unvollständig.

Der zweite Versuch lief über ein **Pseudo-TTY**, also eine bereitgestellte Terminalumgebung für interaktiv arbeitende Programme. Damit ließ sich die Installation erfolgreich abschließen.

Beim Installationsvorgang erschien ein generiertes Webpasswort unerwartet in einer Prozessmeldung. Ich behandelte dieses Passwort deshalb als offengelegt und änderte es anschließend manuell. Es wurde weder gespeichert noch dokumentiert.

Die verwendeten Pi-hole-Versionen waren:

| Komponente | Version |
|---|---|
| Pi-hole Core | v6.4.3 |
| Weboberfläche | v6.6 |
| FTL | v6.7 |

FTL ist der Pi-hole-Dienst, der DNS-Anfragen verarbeitet und die Daten für die Weboberfläche bereitstellt. Nach der Installation waren die Upstreams `1.1.1.1` und `1.0.0.1` gesetzt. Pi-hole-DHCP, Unbound und DNS-over-HTTPS gehörten nicht zu diesem Projekt.

[SCREENSHOT BENÖTIGT: Pi-hole-Weboberfläche nach erfolgreicher Anmeldung; Query-Log, Clientnamen, Domains und Zugangsdaten vorher bereinigen.]

## 5. Was nicht auf Anhieb funktioniert hat

Ein Praxisprojekt wird nicht dadurch glaubwürdig, dass kein Fehler auftritt. Entscheidend ist, den Fehler einzugrenzen und nur das zu ändern, was tatsächlich betroffen ist.

### Der Installer ohne nutzbares Terminal

Der erste Pi-hole-Installer-Versuch scheiterte, weil kein nutzbares TTY verfügbar war. Das sprach nicht gegen Pi-hole im Container, sondern gegen den Ausführungskontext: Der Installer erwartete eine interaktive Terminalsitzung. Deshalb wurden weder beliebige Optionen erzwungen noch eine andere Installationsquelle verwendet. Der offizielle, zuvor geprüfte Installer wurde stattdessen in einer passenden Pseudo-TTY-Umgebung erneut gestartet.

### Falsche Eigentümer bei Log und Konfigurationssicherung

Nach der erfolgreichen Installation zeigten zwei konkrete Pfade falsche Eigentümer: `FTL.log` und `config_backups` gehörten zunächst `root:root`. Pi-hole nutzt diese Bereiche für Protokollierung beziehungsweise Konfigurationssicherungen. Wenn der Dienstbenutzer dort nicht schreiben kann, bleiben Fehler oft zunächst unsichtbar oder tauchen erst beim nächsten Vorgang auf.

Korrigiert wurden ausschließlich die Eigentümer dieser beiden betroffenen Pfade auf `pihole:pihole`. Die bestehenden Modi blieben unverändert: `FTL.log` bei `0644`, `config_backups` bei `0750`. Es gab ausdrücklich keine rekursive Rechteänderung.

Das ist ein wichtiger Unterschied. Ein pauschales `chown -R` kann in einem Container viele Dateien verändern, die gar nicht Teil des Problems sind. Das erschwert spätere Fehlersuche und kann neue Nebenwirkungen erzeugen. Die kleinste passende Reparatur war hier die bessere Reparatur.

### Mount- und Berechtigungswarnungen richtig einordnen

Im unprivilegierten LXC tauchten die systemd-Mount-Warnungen `dev-mqueue.mount`, `run-lock.mount` und `tmp.mount` auf. Sie waren kein Pi-hole-Funktionsfehler: LXC stellt diese Mounts bereits bereit, sodass systemd sie nicht noch einmal einhängen kann. Deshalb wurde nichts maskiert, deaktiviert oder „repariert“.

Auch die Meldung zu `CAP_SYS_NICE` war nicht funktionskritisch. Sie betrifft eine fehlende Fähigkeit zur Priorisierung, blockierte aber weder DNS noch FTL oder die Weboberfläche. Die Lehre daraus: Nicht jede rote Journalzeile verlangt eine Änderung. Erst prüfen, ob die betroffene Funktion wirklich ausfällt.

## 6. DNS, Blocking und Neustart richtig testen

Eine erfolgreiche Installation genügt bei einem DNS-Dienst nicht. Deshalb wurde Pi-hole an mehreren unabhängigen Punkten geprüft:

| Test | Ergebnis |
|---|---|
| Pi-hole FTL | aktiv und aktiviert |
| Weboberfläche | Anmeldung erfolgreich; Admin-Seite erreichbar |
| DNS über UDP/53 | erfolgreich |
| DNS über TCP/53 | erfolgreich |
| Externe Namensauflösung | erfolgreich |
| Normale Domain | `example.com` erfolgreich aufgelöst |
| Default-Blocking | getestete Werbedomains lieferten `0.0.0.0` |
| Kontrollierter Neustart | CT 101 nach 2 Sekunden wieder `running` |
| Autostart | aktiviert; Pi-hole nach Neustart aktiv |

DNS nutzt UDP und TCP als Transportwege. Viele Abfragen laufen über UDP; TCP bleibt für bestimmte Antworten und Fehlersituationen relevant. Deshalb wurden beide Varianten getrennt getestet.

```bash
# DNS-Abfrage über UDP an den Pi-hole-Container
dig @192.168.20.201 deb.debian.org A +time=2 +tries=1

# Dieselbe Art Abfrage über TCP
dig +tcp @192.168.20.201 deb.debian.org A +time=2 +tries=1
```

`dig` fragt einen DNS-Server gezielt ab. `@192.168.20.201` legt fest, dass die Anfrage direkt an den Pi-hole-Container geht. Die kurzen Zeitlimits begrenzen den Testlauf, damit ein Fehler nicht unbemerkt lange hängt.

Beim Blocking wurden `ad.doubleclick.net`, `googleads.g.doubleclick.net` und `ads.youtube.com` getestet. Sie lieferten `0.0.0.0`. Das belegt die Default-Blockierung für diese konkret getesteten Domains; es ist kein Versprechen, jede Werbung oder jeden Tracker zu blockieren.

[SCREENSHOT BENÖTIGT: Je ein bereinigter DNS-Test für UDP und TCP sowie ein unkritischer Blocking-Nachweis.]

## 7. Backup und reale Ressourcenwerte

Nach Aufbau und Funktionstests wurde CT 101 als Proxmox-Snapshot mit zstd gesichert. Die bestätigte Backupdatei war 304.195.522 Bytes groß, also ungefähr 290 MiB. Der Lauf dauerte 18 Sekunden und endete erfolgreich.

Ein **Snapshot-Backup** ist hier ein Sicherungspunkt des Containerzustands. Es ersetzt keinen nachgewiesenen Restore-Test. Für dieses Projekt ist kein Wiederherstellungstest dokumentiert; einen dauerhaft eingerichteten täglichen Backupjob gab es ebenfalls nicht. Beides bleibt bewusst offen.

Kurz nach Aufbau und Test lagen die dokumentierten Ressourcenwerte bei 20 MiB RAM-Nutzung, ohne verwendeten Swap. Auf der Root-Disk waren ungefähr 874 MiB belegt, rund 12 Prozent. Diese Werte sind eine Momentaufnahme nach Aufbau und Test. Sie sind keine Langzeitmessung, kein Lasttest und kein allgemeiner Mindestwert für jedes Pi-hole-Setup.

| Messpunkt | Dokumentierter Wert | Aussagegrenze |
|---|---|---|
| RAM nach Aufbau und Test | 20 MiB | Momentaufnahme, kein Langzeitwert |
| Swap | 0 MiB genutzt | Momentaufnahme |
| Root-Disk | ungefähr 874 MiB, rund 12 % | Momentaufnahme auf 8-GiB-Root-Disk |
| Snapshot-Backup | 304.195.522 Bytes, ungefähr 290 MiB | Erfolgreicher Sicherungspunkt, kein Restore-Nachweis |
| Backupdauer | 18 Sekunden | Ergebnis dieses einzelnen Laufs |
| Stromverbrauch | nicht gemessen | Kein eindeutig zugeordneter Home-Assistant-Sensor |

Beim Backup wurde außerdem ein Thin-Pool-Kapazitätsrisiko sichtbar. Das Backup selbst war erfolgreich. Die Warnung war aber ein separates Storage-Thema: kein Grund, die Kapazität zu ignorieren, aber auch kein Leistungswert für den Artikel. An LVM-, Storage- oder Auto-Extend-Einstellungen wurde in diesem Projekt nichts geändert.

[SCREENSHOT BENÖTIGT: Erfolgreicher Backup-Task mit Größe und Dauer; interne Pfade, Task-IDs und sensible Details bereinigen.]

## 8. Fazit und nächster Schritt

Pi-hole war für PVE04 ein sinnvoller erster Dienst. Das Projekt bestand nicht nur aus der Installation: Container planen, Upstreams festlegen, die interaktive Installation sauber ausführen, kleine Fehler gezielt korrigieren, DNS über UDP und TCP prüfen, Neustart testen und einen Sicherungspunkt anlegen gehörten zusammen.

**Pi-hole einrichten, wenn** du einen kleinen Proxmox-Host hast, eine feste Containerkonfiguration nachvollziehen kannst und Tests vor einer größeren DNS-Umstellung einplanst. **Noch nicht einrichten, wenn** dir ein dokumentierter Rückweg für DNS-Änderungen fehlt oder der Dienst sofort ungeprüft das gesamte produktive Heimnetz versorgen soll.

Die zentrale Erkenntnis dieses Projekts: Mit dem Ende des Installers ist ein Dienst nicht fertig. Erst Tests, Neustart, ein gesicherter Zustand und eine ehrliche Liste offener Punkte machen den Aufbau nachvollziehbar.

Als nächster Dienst auf PVE04 ist **Uptime Kuma** geplant. Das wäre ein passendes zweites Projekt, um die Erreichbarkeit eigener Dienste und einfache Statusüberwachung kennenzulernen.

## FAQ

### Reichen 512 MiB RAM für Pi-hole im LXC?

Im dokumentierten CT 101 liefen Pi-hole, Weboberfläche, DNS-Tests und der Neustart mit 512 MiB RAM. Das ist keine allgemeine Garantie: Andere Filterlisten, Versionen oder Umgebungen können andere Anforderungen haben.

### Warum wurde ein unprivilegierter LXC verwendet?

Der Dienst brauchte im Projekt keine dokumentierten Sonderrechte. Ein unprivilegierter Container reduziert die Berechtigungen auf dem Host und passte deshalb zum schlanken DNS-Dienst.

### Ist das Snapshot-Backup ein getesteter Wiederherstellungsnachweis?

Nein. Der Sicherungslauf war erfolgreich, aber ein Restore-Test ist für dieses Projekt nicht dokumentiert.

### Warum wurden die Mount-Warnungen nicht repariert?

Weil sie im unprivilegierten LXC keine Pi-hole-Funktion blockierten. DNS, Weboberfläche, Blocking und Neustart waren erfolgreich. Eine Änderung ohne nachgewiesenen Funktionsfehler hätte nur zusätzliche Risiken geschaffen.

## ✅ Das solltest du jetzt können

- [ ] Du weißt, warum Pi-hole als erster Proxmox-Dienst sinnvoll sein kann.
- [ ] Du kannst einen kleinen DNS-LXC anhand klarer Ressourcen- und Netzwerkwerte einordnen.
- [ ] Du verstehst, warum ein interaktiver Installer ein nutzbares Terminal braucht.
- [ ] Du weißt, weshalb eine gezielte Rechtekorrektur besser ist als eine rekursive Änderung.
- [ ] Du kannst DNS über UDP und TCP getrennt testen.
- [ ] Du verwechselst ein erfolgreiches Snapshot-Backup nicht mit einem getesteten Restore.
- [ ] Du weißt, dass Stromverbrauch und Langzeitbetrieb hier nicht gemessen wurden.

## Offizielle Dokumentation

- [Pi-hole: Installation](https://docs.pi-hole.net/main/basic-install/) – Der offizielle Installer kann heruntergeladen und vor der Ausführung geprüft werden.
- [Proxmox VE Administration Guide: Container Toolkit](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#chapter_pct) – Grundlagen zu LXC-Containern, Einstellungen und Sicherungen.
- [Debian „trixie“ Release Information](https://www.debian.org/releases/trixie/) – Einordnung von Debian 13.6 als `trixie`.
