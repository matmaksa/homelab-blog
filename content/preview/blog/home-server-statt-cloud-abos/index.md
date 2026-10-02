+++
title = "Eigener Home-Server statt Cloud-Abos: Kosten, Hardware und Grenzen"
slug = "home-server-statt-cloud-abos"
description = "Lohnt sich ein Home-Server? So kalkulierst du Strom und Gesamtkosten, wählst passende Hardware und planst Backups vor dem Umzug."
draft = true
robotsNoIndex = true
noindex = true
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
stage = "SOL_WRITER_DRAFT_FOR_REVIEW"
research_date = "2026-09-30"

[sitemap]
  exclude = true

[workflow]
  content_state = "draft_generated"
  editorial_status = "pass"
  technical_status = "pass"
  visual_status = "pass"
  seo_status = "pass"
+++

# Eigener Home-Server statt Cloud-Abos: Kosten, Hardware und Grenzen

Ein Mini-PC zu Hause, die Fotos auf der eigenen SSD und weniger monatliche Abos: Das klingt verlockend. Ein eigener Server übernimmt aber nicht nur Daten, sondern auch Arbeit. Du musst Updates einspielen, Fehler erkennen und verlorene Dateien wiederherstellen können.

Die richtige Frage lautet deshalb nicht: „Wie viele Cloud-Dienste kann dieser Mini-PC ersetzen?“ Sondern: „Welche konkrete Aufgabe möchte ich selbst übernehmen – und kann ich sie zuverlässig betreiben und sichern?“

## Kurzantwort: Für wen lohnt sich ein Home-Server?

Ein eigener Home-Server passt zu dir, wenn du mit einem klar begrenzten Dienst starten möchtest und Wartung als Teil des Projekts akzeptierst. Beginne nicht mit dem vollständigen Umzug deines digitalen Alltags.

Anwendungen wie Immich oder Nextcloud können Fotos und Dateien auf eigener Hardware verwalten. Sie brauchen aber ausreichend Ressourcen, regelmäßige Updates und eine Datensicherung, die du auch zurückspielen kannst.[^immich-req] [^immich-backup] [^nextcloud-files] [^nextcloud-backup]

Wenn niemand im Haushalt den Betrieb übernehmen möchte, bleiben wichtige Daten bei einem verwalteten Anbieter oft besser aufgehoben. Eine Mischlösung ist ebenfalls sinnvoll: Dienste und Arbeitsdaten lokal, eine verschlüsselte Sicherung außer Haus. Das ist kein gescheitertes Selfhosting, sondern eine bewusste Aufgabenteilung.

## Was das Video zeigt – und was daraus nicht folgt

Anlass für diesen Artikel ist das Video „Tschüss Cloud! Mein eigener Home-Server (nur 50 € Strom/Jahr)“ von Smart Home Nerd vom 5. September 2026.[^video]

Laut den für diesen Artikel bereitgestellten Videoangaben nutzt der Creator einen HP EliteDesk 800 G4 Mini mit Intel Core i5-8500T, 32 GB RAM, zwei 1-TB-NVMe-SSDs im RAID-1-Verbund und einer 500-GB-SATA-SSD. Genannt werden außerdem 2,5-GbE, Intel AMT und Unraid. Das beschreibt seinen Aufbau – es ist kein MATMAKSA-Hardwaretest.

Vier Punkte solltest du getrennt betrachten:

- Strom: 14 Watt im Mittel ergeben bei 0,40 €/kWh rechnerisch rund 49 Euro im Jahr. Damit stimmt die Rechnung, nicht automatisch der angenommene Verbrauch. Auch die genannten 25 Watt unter Last sind keine garantierte Obergrenze für andere Systeme.
- Netzwerk: Das HP-Datenblatt nennt für dieses Modell integriertes Gigabit-Ethernet. 2,5-GbE gehört daher nicht zur zugesicherten Standardausstattung; wie der Anschluss im Video realisiert wurde, belegt das Datenblatt nicht.[^hp]
- Fernverwaltung: Intel AMT setzt eine geeignete Plattform, passende Firmware und eine korrekte Einrichtung voraus. Der Prozessorname allein ist kein Kompatibilitätsnachweis.[^amt]
- Datensicherheit: Zwei gespiegelte SSDs sind keine unabhängige Sicherung. RAID kann den Ausfall eines Datenträgers abfedern, schützt aber nicht vor versehentlichem Löschen, Schadsoftware oder dem Verlust des gesamten Rechners.

Auch ältere Hardware ist nicht automatisch ein guter Neukauf. Intel nennt für den i5-8500T den 30. Juni 2025 als Ende der Servicing Updates. Das bedeutet nicht, dass ein darauf installiertes Linux keine Updates mehr bekommt. Vor einem Gebrauchtkauf solltest du Firmware- und Plattformpflege trotzdem gesondert prüfen.[^intel-servicing] [^intel-cpu]

## Hardware nach Workload auswählen

Schreibe zuerst auf, welche Anwendungen laufen sollen. Ergänze Datenmenge, gleichzeitige Nutzer sowie Anforderungen an virtuelle Maschinen oder Videokonvertierung. Erst danach lohnt sich der Modellvergleich.

Ein gebrauchter Business-Mini-PC ist eine mögliche Bauform, kein Leistungsversprechen. Beim EliteDesk aus dem Video dokumentiert HP zwei RAM-Steckplätze, zwei M.2-Steckplätze für Speicher und einen 2,5-Zoll-Schacht. Die nutzbare Bestückung hängt von der Gerätevariante ab. Beim 35-Watt-Modell mit optionaler separater Grafikkarte kann laut Datenblatt nur eine M.2-SSD eingesetzt werden.[^hp]

Prüfe beim konkreten Angebot deshalb nicht nur CPU und RAM:

| Teil | Vor dem Kauf klären |
| --- | --- |
| CPU | Welche Anwendungen laufen gleichzeitig? Für Medienserver zusätzlich benötigte Codecs und Hardwarebeschleunigung prüfen. |
| RAM | Bedarf aller Dienste plus Betriebssystem und Reserve einplanen. Nicht nur den Startzustand eines leeren Servers betrachten. |
| SSD | Nutzdaten, Datenbanken, Vorschaubilder und Wachstum berücksichtigen. Bei Gebrauchtware Zustandsdaten, Schreibausdauer und Garantiebedingungen prüfen. |
| Netzwerk | Kabelgebundenes Gigabit reicht häufig für den Einstieg. Schnellere Anschlüsse lohnen erst, wenn Gegenstelle, Switch und Datenträger mithalten. |
| Erweiterbarkeit | Freie Steckplätze, belegte Anschlüsse sowie mitgelieferte Halterungen und Kabel kontrollieren. |
| Pflege | Firmware, unterstütztes Betriebssystem und einen verständlichen Wiederherstellungsweg prüfen. |

Für einen gemischten Einstieg sind 16 GB RAM eine brauchbare Planungsgröße, aber keine universelle Mindestanforderung. Ein einzelner kleiner Dienst kann mit weniger auskommen. Immich zeigt, warum pauschale Aussagen wie „Container brauchen kaum RAM“ nicht helfen: Das Projekt nennt mindestens 6 GB und empfiehlt 8 GB RAM sowie vier CPU-Kerne. Für den Host und weitere Dienste brauchst du zusätzliche Reserve.[^immich-req]

Für den amd64-Machine-Learning-Container von Immich gilt seit Version 3 zusätzlich die Anforderung x86-64-v2. Läuft dieser Container in einer VM, muss der konfigurierte CPU-Typ die benötigten Funktionen an den Gast weiterreichen. Prüfe das vor dem Kauf und bei der VM-Konfiguration erneut; für Immich-Komponenten ohne diesen Machine-Learning-Container ist daraus keine allgemeine x86-64-v2-Pflicht abzuleiten.[^immich-req]

Für Jellyfin hängt der Bedarf stark davon ab, ob Endgeräte Medien direkt abspielen oder der Server sie umwandeln muss. Die Jellyfin-Dokumentation beschreibt Intel-Prozessoren der 7. bis 10. Generation weiterhin als nutzbar, führt sie aber nicht mehr als bevorzugten Neukauf. Kaufe einen i5-8500T daher nicht allein mit dem Versprechen, er sei „ideal für jeden Medienserver“.[^jellyfin]

## Stromkosten realistisch berechnen

Für einen Rechner im Dauerbetrieb gilt:

    Jahresverbrauch in kWh = durchschnittliche Leistung in W × 24 × 365 ÷ 1.000
    Jährliche Stromkosten = Jahresverbrauch × Arbeitspreis in €/kWh

Die folgende Tabelle enthält Rechenbeispiele, keine Messwerte und keinen deutschen Durchschnittstarif. Annahmen: 365 Tage Dauerbetrieb und Arbeitspreise von 0,30, 0,40 oder 0,50 €/kWh. Nutze für deine Entscheidung den Arbeitspreis aus deinem eigenen Vertrag. Ein unveränderter Grundpreis wird nicht zusätzlich angesetzt.

| Durchschnittliche Leistung | kWh/Jahr | 0,30 €/kWh | 0,40 €/kWh | 0,50 €/kWh |
| --- | ---: | ---: | ---: | ---: |
| 5 W | 43,80 | 13,14 € | 17,52 € | 21,90 € |
| 10 W | 87,60 | 26,28 € | 35,04 € | 43,80 € |
| 14 W | 122,64 | 36,79 € | 49,06 € | 61,32 € |
| 15 W | 131,40 | 39,42 € | 52,56 € | 65,70 € |
| 25 W | 219,00 | 65,70 € | 87,60 € | 109,50 € |

Die 50-Euro-Aussage aus dem Video ist unter dessen Annahmen plausibel. Sie ist weder eine Gesamtkostenrechnung noch ein Versprechen für deinen Aufbau.

Miss für eine belastbarere eigene Kalkulation den Verbrauch an der Steckdose über mehrere typische Tage. Der Zeitraum sollte Leerlauf, Fotoimport, Backups und Mediennutzung enthalten. Beziehe zusätzliche Laufwerke, mögliche USV-Verluste und neu angeschaffte Netzwerkgeräte ein.

Die TDP des Prozessors ersetzt diese Messung nicht. Intel führt den i5-8500T mit 35 Watt TDP; das ist nicht der durchschnittliche Verbrauch des vollständigen Mini-PCs an der Steckdose.[^intel-cpu]

## Gesamtkosten: Strom ist nur ein Posten

Für den Vergleich mit einem Abo brauchst du mindestens diese Rechnung:

    Gesamtkosten = Anschaffung + Backup-Hardware + Strom
                   + Software/Lizenzen + Offsite-Speicher + Ersatzteile
                   + optional bewertete Arbeitszeit

Das folgende Drei-Jahres-Beispiel ist ausdrücklich fiktiv. Es verwendet keine aktuellen Händlerangebote:

| Position | Annahme | Betrag |
| --- | --- | ---: |
| Rechner einschließlich System-SSD | einmalig | 200,00 € |
| Separater Backup-Datenträger | einmalig | 70,00 € |
| Strom | 15 W, 0,40 €/kWh, drei Jahre | 157,68 € |
| Offsite-Sicherung | frei gewählter Ansatz: 24 €/Jahr | 72,00 € |
| Ersatzteilreserve | frei gewählter Ansatz | 40,00 € |
| Softwarelizenz | kostenlose Route im Beispiel | 0,00 € |
| Summe | ohne bewertete Arbeitszeit | 539,68 € |

Das sind rund 14,99 Euro pro Monat. Hardware, Offsite-Speicher und Ersatzteilreserve sind Planungsannahmen, keine Angebote. Je nach Datenmenge kann insbesondere die externe Sicherung deutlich mehr kosten. Unraid würde zusätzliche Lizenzkosten verursachen.

Vergleiche die Summe nur mit Funktionen, die du tatsächlich ersetzt. Ein DNS-Filter spart kein Cloud-Speicher-Abo. Ein Medienserver für deine eigene Sammlung bietet nicht automatisch den Katalog eines Streamingdienstes. Zähle ersetzte Funktionen, nicht installierte Apps.

## Proxmox, Docker oder Unraid?

Die Begriffe liegen nicht auf derselben Ebene. Proxmox VE ist eine Virtualisierungsplattform für virtuelle Maschinen und LXC-Container. Docker Engine betreibt Anwendungscontainer; Compose beschreibt zusammengehörige Dienste, Netzwerke und Volumes in einer Konfiguration. Unraid kombiniert unter anderem Speicherverwaltung, Container und virtuelle Maschinen.[^proxmox] [^docker-engine] [^docker-compose] [^unraid-buy]

Eine einfache Auswahlhilfe:

- Wenige Containerdienste: Starte mit einem unterstützten Linux wie Debian und Docker Engine mit Compose. Ein zusätzlicher Hypervisor ist nicht nötig, nur weil er verfügbar wäre. Docker Desktop brauchst du für diesen privaten Linux-Server nicht.
- Mehrere getrennte Systeme und Interesse an Virtualisierung: Proxmox VE ist eine passende Option. Die Plattform ist ohne Pflichtabonnement nutzbar; kostenpflichtige Subscriptions betreffen unter anderem Enterprise-Repository und Support.[^proxmox]
- Speicherverwaltung und eine integrierte Oberfläche als Schwerpunkt: Prüfe Unraid und rechne die Lizenzkosten ein.

Wenn du Proxmox nutzt, betreibe einen Docker-Stack besser in einer eigenen Linux-VM statt direkt auf dem Hypervisor. Immich rät zudem von Docker in LXC ab und verweist bei Problemen auf eine unterstützte VM-Installation.[^immich-req]

### Unraid-Preise und Update-Regel

Zum Recherchezeitpunkt am 30. September 2026 nennt Unraid regulär 49 US-Dollar für Starter, 109 US-Dollar für Unleashed und 249 US-Dollar für Lifetime. Das sind Dollarpreise des Anbieters, keine zugesicherten deutschen Euro-Endpreise. Steuern, Wechselkurs und Checkout-Bedingungen wurden nicht geprüft.[^unraid-buy]

Starter erlaubt bis zu sechs angeschlossene Speichergeräte. Dabei zählen nicht nur Datenplatten im Array. Laut FAQ sind ein eMMC-Gerät und ein USB-Gerät von der Zählung ausgenommen.[^unraid-faq]

Starter und Unleashed enthalten ein Jahr Updates. Die optionale Verlängerung kostet laut FAQ 36 US-Dollar für ein weiteres Jahr. Ohne Verlängerung bleibt die vorhandene Lizenz gültig. Patches innerhalb der eigenen Minor-Version bleiben verfügbar, solange diese Version unterstützt wird. Nach ihrem Supportende gibt es dafür keine weiteren Sicherheitspatches. Preise und Bedingungen können sich ändern: Prüfe sie vor dem Kauf erneut.[^unraid-faq]

## Welche Dienste eignen sich für den Einstieg?

| Dienst | Nutzen | Grenze und Startempfehlung |
| --- | --- | --- |
| Pi-hole | DNS-basierte Filterung im Heimnetz | Filtert Domains, nicht beliebige Inhalte. Als erstes Lernprojekt geeignet. Notiere vorher, wie du die DNS-Einstellung zurücksetzt.[^pihole] |
| Jellyfin | Eigene Medien bereitstellen | Codec, Abspielgerät und Transcoding bestimmen den Bedarf. Teste mit eigenen Beispieldateien statt mit pauschalen Stream-Zahlen.[^jellyfin] |
| Immich | Eigene Foto- und Videosammlung verwalten | Ressourcenbedarf sowie Sicherung von Mediendateien und Datenbank beachten. Originale zunächst zusätzlich behalten.[^immich-req] [^immich-backup] |
| Nextcloud | Dateien synchronisieren und teilen | Daten, Konfiguration und Datenbank sichern. Synchronisation allein ist kein Wiederherstellungsplan.[^nextcloud-files] [^nextcloud-backup] |
| Home Assistant | Smart-Home-Zentrale auf eigener Hardware | Für die meisten Nutzer empfiehlt das Projekt Home Assistant OS. Die Container-Installation bietet keine integrierten Apps, die früher Add-ons hießen.[^ha-install] |
| Passwortmanager | Besonders sensible Zugangsdaten selbst verwalten | Nicht als erstes Projekt. Updates, MFA, externe Sicherung und Notfallzugang müssen vorher funktionieren. |

Für einen reinen Home-Assistant-Rechner ist Home Assistant OS die naheliegende Route. Soll dasselbe Gerät mehrere getrennte Systeme tragen, kann HA OS in einer VM laufen. Ein eigener Server macht angebundene Herstellerintegrationen aber nicht automatisch cloudfrei. Prüfe vor einer Kündigung die Geräte und Funktionen, die du tatsächlich nutzt.[^ha-install]

## Zugriff und Sicherheit: LAN zuerst

Unterscheide drei Betriebsarten:

1. Lokal: Die Anwendung ist nur im Heimnetz erreichbar.
2. Über VPN: Dein Endgerät verbindet sich zunächst mit einem abgesicherten Zugang zum Heimnetz. Home Assistant beschreibt diese Möglichkeit ausdrücklich.[^ha-remote]
3. Öffentlich: Die Anwendung ist ohne privaten VPN-Zugang aus dem Internet erreichbar. Damit übernimmst du zusätzliche Verantwortung für die exponierte Anwendung.

Für Einsteiger ist „LAN zuerst, VPN bei Bedarf“ meist die risikoärmere Reihenfolge. Das bedeutet nicht, dass jedes VPN ohne erreichbaren Endpunkt auskommt. Je nach Lösung braucht der VPN-Dienst selbst eine Freigabe oder arbeitet über ausgehende Verbindungen. Auch VPN-Software benötigt Updates.

Bevor persönliche Daten auf den Server kommen:

- Betriebssystem, Anwendungen und verfügbare Firmware aktuell halten.
- Für jeden Dienst eigene starke Kennwörter verwenden und MFA aktivieren, wo sie angeboten wird.
- Wiederherstellungscodes und Schlüssel getrennt vom Server aufbewahren.
- Normale Nutzung und Administration trennen.
- Unnötige Dienste und Freigaben abschalten.
- Proxmox-, Unraid- und AMT-Verwaltung nicht öffentlich freigeben.
- Neben IPv4-Portweiterleitungen auch IPv6-Firewallregeln und automatische Freigaben prüfen.
- Update- und Backup-Fehler regelmäßig kontrollieren.

Das ist eine konservative Startkonfiguration, keine Sicherheitszertifizierung. CISA empfiehlt unter anderem zeitnahe Patches, begrenzte Exposition, starke Zugriffskontrollen und getestete Sicherungen.[^cisa-ransomware] [^cisa-mfa]

## Backup: RAID ist nicht die zweite Kopie

Eine Spiegelung kann beim Ausfall einer einzelnen SSD helfen. Sie schützt nicht davor, dass du Dateien löschst, ein kompromittierter Dienst sie verändert oder der gesamte Rechner verloren geht. Redundanz im Server und ein Backup außerhalb seines Ausfallbereichs lösen unterschiedliche Probleme.

Nutze die 3-2-1-Regel als Planungsbasis: drei Kopien insgesamt, auf zwei unterschiedlichen Medientypen, davon eine außer Haus. Ergänze eine offline oder anderweitig vor Änderungen geschützte Kopie und teste die Wiederherstellung.[^cisa-backup] [^cisa-ransomware]

Ein möglicher Aufbau:

- Arbeitskopie auf der Server-SSD
- versionierte Sicherung auf einer externen HDD
- verschlüsselte Offsite-Kopie

Bewahre den Entschlüsselungsschlüssel unabhängig vom Server auf. Eine dauerhaft angeschlossene USB-Platte erfüllt das Offsite-Ziel nicht. Eine zweite Partition derselben SSD ist ebenfalls keine unabhängige Kopie.

Sichere nicht nur die sichtbaren Dateien:

- Immich: Fotos und Videos plus Datenbank. Automatische Datenbanksicherungen enthalten die Medien nicht.[^immich-backup]
- Nextcloud: Daten, Datenbank, Konfiguration sowie eigene Apps und Themes.[^nextcloud-backup]
- Proxmox: Prüfe den Umfang jedes Backup-Jobs. Inhalte von LXC-Bind- und Device-Mounts sind nicht im normalen Containerbackup enthalten.[^proxmox-backup]

### Ein kleiner Restore-Test

1. Lege eine harmlose Testdatei an und starte die reguläre Sicherung.
2. Stelle sie in einem getrennten Testziel wieder her, ohne Originale zu überschreiben.
3. Prüfe Inhalt und Lesbarkeit. Bei Anwendungen testest du zusätzlich Anmeldung, Datenbank und Zuordnung der Dateien.
4. Notiere Schritte, benötigte Schlüssel und Dauer. Wiederhole den Test nach größeren Änderungen.

Das ist ein empfohlener Ablauf. Für diesen Artikel wurde kein Restore durchgeführt. Ein konkretes Proxmox-Beispiel findest du im [MATMAKSA-Guide zur USB-Festplatte als Backup-Ziel](https://matmaksa.de/posts/proxmox-usb-festplatte-backup-ziel/).

## Wann die Cloud die bessere Wahl bleibt

Ein verwalteter Dienst ist oft sinnvoller, wenn Dateien ohne eigenes Eingreifen verfügbar sein müssen, niemand Updates übernehmen kann oder Freigaben für andere Menschen möglichst unkompliziert bleiben sollen. Prüfe beim Anbieter trotzdem Export, Sicherung und Wiederherstellung: „Cloud“ ist kein automatisches Backup-Gütesiegel.

Ein einzelner Server zu Hause hängt an der Stromversorgung und meist auch am Internetanschluss deines Haushalts. Fällt eines davon aus, ist der Fernzugriff unterbrochen. Ein VPN schafft keinen zweiten Server. Eine Sicherung stellt nicht automatisch einen laufenden Ersatz bereit.

Teste den geplanten Ersatz deshalb parallel zum bisherigen Dienst. Prüfe auf deinen tatsächlichen Endgeräten Upload, Download, Freigaben und Wiederherstellung. Kündige erst, wenn die benötigten Funktionen funktionieren und die Betriebsverantwortung geklärt ist.

## Startkonfigurationen für 50, 150 und 300 Euro

Die folgenden Beträge sind selbst gesetzte Budgetobergrenzen vom 30. September 2026. Sie sind keine recherchierten Marktpreise, Händlerangebote oder Zusagen zur Verfügbarkeit. Strom und laufende Offsite-Kosten kommen hinzu. Wenn kein passendes Angebot verfügbar ist, reduzierst du den Umfang oder wartest – nicht die Datensicherung.

### Bis 50 Euro: Lernprojekt statt Cloud-Ersatz

Ziel: vorhandener Rechner oder günstiger gebrauchter Thin Client, 4 GB RAM, kleine vorhandene SSD und kabelgebundenes Netzwerk. Starte nur einen DNS-Filter oder einen ähnlich begrenzten Dienst.

Mögliche Budgetaufteilung:

- höchstens 40 Euro für das vollständige Gerät
- 10 Euro Zubehörreserve

Das setzt ein passendes Angebot oder vorhandene Teile voraus. Eine neue große Datensammlung und ein vollständig neu gekauftes 3-2-1-System passen nicht in dieses Budget. Sichere zumindest die Konfiguration auf ein unabhängiges vorhandenes Ziel. Wenn das nicht möglich ist, nutze nur ersetzbare Testdaten. Immich ist für diese Stufe nicht die Zielanwendung.

### Bis 150 Euro: Wenige Dienste mit separater Sicherung

Ziel: gebrauchter Business-Mini-PC mit 8 GB RAM, 256-GB-SSD und Gigabit-LAN, darauf Linux und ein kleiner Compose-Stack.

Mögliche Budgetaufteilung:

- höchstens 100 Euro für das vollständige Gerät
- 40 Euro für ein unabhängiges Backup-Ziel
- 10 Euro Reserve

Auch das ist ein Suchbudget, kein Nachweis eines verfügbaren Angebots. Für persönliche Daten brauchst du zusätzlich eine Offsite-Kopie. Eine große Fotobibliothek oder mehrere gleichzeitige Medienumwandlungen sind nicht das Ziel dieser Stufe.

### Bis 300 Euro: Mehr Reserve, weiterhin ein einzelner Server

Ziel: Mini-PC mit 16 GB RAM, 500-GB-SSD und einem für deine Anwendungen geeigneten Prozessor.

Mögliche Budgetaufteilung:

- höchstens 200 Euro für das vollständige Gerät
- 70 Euro für Backup-Speicher
- 30 Euro Reserve

Nutze entweder Linux mit Compose oder Proxmox mit zunächst einer Linux-VM. Lerne nicht mehrere Plattformen gleichzeitig. Bei Immich musst du den Ressourcenbedarf in der VM plus Reserve für den Host einplanen. Bei Jellyfin prüfst du vor dem Kauf Grafik- und Codec-Unterstützung. Wenn deine vorhandenen Daten den geplanten Speicher bereits ausfüllen, passt die Konfiguration unabhängig vom Preis nicht. Offsite-Speicher und eine mögliche Unraid-Lizenz sind in diesem Budget nicht enthalten.

## Checkliste vor dem Kauf

- Welche konkrete Funktion möchte ich ersetzen, und welches Abo kann danach wirklich entfallen?
- Wie viele Daten habe ich heute, und wie schnell wächst die Sammlung?
- Sind RAM, Anschlüsse, Firmwarepflege und Medienfunktionen beim konkreten Gerät geprüft?
- Ist der Stromverbrauch gemessen oder nur angenommen?
- Sind Backup-Ziel, Offsite-Kopie und benötigte Schlüssel eingeplant?
- Kann ich einen Ausfall erkennen und Daten in ein getrenntes Ziel zurückholen?
- Bleibt der Start lokal, und gibt es einen begründeten Bedarf für Fernzugriff?
- Wer kümmert sich während Urlaub oder Krankheit um den Betrieb?

## Fazit: Erst Workload und Backup, dann Hardware

Ein eigener Home-Server ist kein pauschales „Tschüss Cloud“. Beginne mit einer Aufgabe, die du selbst betreiben und wiederherstellen kannst. Die rund 50 Euro Strom aus dem Video sind eine nachvollziehbare Beispielrechnung. Ob sich der Server lohnt, entscheidet sich aber erst mit Anschaffung, Sicherung, Pflege und den Funktionen, die du wirklich ersetzt.

Für die nächsten Schritte:

- [Mini-PCs fürs Homelab nach Budget vergleichen](https://matmaksa.de/posts/mini-pc-homelab-vergleich/)
- [Homelab unter 100 Euro planen](https://matmaksa.de/posts/homelab-unter-100-euro-was-du-brauchst/)
- [Proxmox-Backup auf USB-Festplatte einschließlich Restore vorbereiten](https://matmaksa.de/posts/proxmox-usb-festplatte-backup-ziel/)
- [Grundlagen zu Proxmox als kostenloser Virtualisierungsplattform lesen](https://matmaksa.de/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/)

Erst Workload und Backup klären, dann Hardware auswählen. Ein niedriger Leerlaufwert allein ist kein Kaufgrund.

Transparenz: Dieser Artikel ist eine recherchierte Entscheidungshilfe, kein eigener Test des im Video gezeigten Geräts. Wir haben für diesen Artikel weder den Stromverbrauch eines Geräts gemessen noch eine Installation oder einen Restore durchgeführt. Die Budgetaufteilungen sind Planungsbeispiele und keine Marktpreisvergleiche. Der Entwurf enthält keine Affiliate- oder Händlerlinks. Ein Kauf ist nicht erforderlich; vorhandene geeignete Hardware kann der bessere Einstieg sein.

## Quellen

[^video]: Smart Home Nerd: [„Tschüss Cloud! Mein eigener Home-Server (nur 50 € Strom/Jahr)“](https://www.youtube.com/watch?v=39rKFTFuURM), veröffentlicht am 5. September 2026. Hardware- und Verbrauchsangaben sind Creator-Aussagen aus dem verifizierten Projektbrief, keine MATMAKSA-Messwerte.
[^hp]: HP: [EliteDesk 800 35W G4 Desktop Mini PC – Datenblatt (PDF)](https://www.bhphotovideo.com/lit_files/447151.pdf), Herstellerdokument über Händler-Mirror.
[^intel-servicing]: Intel: [Support and Servicing Updates for Intel Processors](https://www.intel.com/content/www/us/en/support/topics/support-and-servicing-for-processors.html).
[^intel-cpu]: Intel: [Core i5-8500T – Spezifikationen](https://www.intel.com/content/www/us/en/products/sku/129941/intel-core-i58500t-processor-9m-cache-up-to-3-50-ghz/specifications.html).
[^amt]: Intel: [Intel Active Management Technology – Plattform- und Einrichtungsanforderungen](https://www.intel.com/content/www/us/en/support/articles/000102462/technologies.html).
[^unraid-buy]: Unraid: [Lizenzstufen und Preise](https://account.unraid.net/buy), geprüft am 30. September 2026.
[^unraid-faq]: Unraid: [Licensing FAQ](https://docs.unraid.net/unraid-os/troubleshooting/licensing-faq/), geprüft am 30. September 2026.
[^proxmox]: Proxmox: [Proxmox Virtual Environment – Get Started](https://www.proxmox.com/en/products/proxmox-virtual-environment/get-started).
[^docker-engine]: Docker: [Docker Engine Documentation](https://docs.docker.com/engine/).
[^docker-compose]: Docker: [Docker Compose Documentation](https://docs.docker.com/compose/).
[^pihole]: Pi-hole: [Dokumentation](https://docs.pi-hole.net/) und [Regex-Filter](https://docs.pi-hole.net/regex/).
[^immich-req]: Immich: [System Requirements](https://docs.immich.app/install/requirements/).
[^immich-backup]: Immich: [Backup and Restore](https://docs.immich.app/administration/backup-and-restore/).
[^nextcloud-files]: Nextcloud: [Nextcloud Files](https://nextcloud.com/files/).
[^nextcloud-backup]: Nextcloud: [Backup – Administration Manual](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/backup.html).
[^jellyfin]: Jellyfin: [Hardware Selection](https://jellyfin.org/docs/general/administration/hardware-selection/).
[^ha-install]: Home Assistant: [Installation](https://www.home-assistant.io/installation/).
[^ha-remote]: Home Assistant: [Remote Access](https://www.home-assistant.io/docs/configuration/remote/).
[^cisa-ransomware]: CISA: [StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide).
[^cisa-backup]: CISA/US-CERT: [Data Backup Options (PDF)](https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf). Grundlagenquelle von 2012; verwendet wird die 3-2-1-Regel.
[^cisa-mfa]: CISA: [Require Multifactor Authentication](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-multifactor-authentication).
[^proxmox-backup]: Proxmox: [vzdump-Dokumentation im offiziellen Repository](https://raw.githubusercontent.com/proxmox/pve-docs/master/vzdump.adoc).

---

## Redaktioneller Evidenzanhang – nicht für die öffentliche Artikelseite

### Evidenzklassen

- DOKUMENTIERT: Eine Primärdokumentation stützt den konkreten Claim.
- CREATOR: Aussage des Video-Creators; kein eigener Mess- oder Gerätenachweis.
- RECHNUNG: Reproduzierbare Rechnung mit ausdrücklich hypothetischen Eingaben.
- EMPFEHLUNG: Konservative redaktionelle Planungsentscheidung; kein Benchmark oder Hersteller-Mindestwert.
- ABLEITUNG: Schluss aus Architektur und Quellen; im Artikel als Einordnung erkennbar.
- OFFEN: Kein verifizierter Nachweis; deshalb kein entsprechendes Versprechen.

### Claim-to-source-Matrix

| Claim-Gruppe | Klasse | Quelle/Grundlage | Erhaltene Grenze |
| --- | --- | --- | --- |
| Videoausstattung, 14 W, 25 W und 0,40 €/kWh | CREATOR | Video/Projektbrief | Keine eigene Messung oder erneute Transkriptanalyse |
| Rund 50 €/Jahr | RECHNUNG | 14 W × 8.760 h × 0,40 €/kWh | Stromkosten, kein TCO und keine Verbrauchsgarantie |
| HP serienmäßig mit GbE statt zugesichertem 2,5-GbE | DOKUMENTIERT | HP-Datenblatt | Individueller Umbau im Video unbekannt |
| Steckplätze und dGPU-Ausnahme | DOKUMENTIERT | HP-Datenblatt | Konkrete Gerätevariante und Lieferumfang prüfen |
| Intel-Servicing und 35-W-TDP | DOKUMENTIERT/ABLEITUNG | Intel | Weder Linux-EOL noch Steckdosenverbrauch daraus ableiten |
| 16-GB-Planungsziel und Hardwareauswahl | EMPFEHLUNG | Redaktionsmethodik, konkrete Grenzen aus Immich/Jellyfin | Keine universelle Mindestkonfiguration |
| Stromtabelle | RECHNUNG | 8.760 h/Jahr; 5/10/14/15/25 W; 0,30/0,40/0,50 €/kWh | Keine Messwerte und kein Marktmittel |
| TCO 539,68 € bzw. 14,99 €/Monat | RECHNUNG/EMPFEHLUNG | Fiktive Drei-Jahres-Annahmen | Keine Angebote; Arbeitszeit nicht bewertet |
| Proxmox, Compose und Unraid | DOKUMENTIERT/EMPFEHLUNG | Hersteller-/Projektdokumentationen | Unterschiedliche Ebenen; Docker-VM ist Empfehlung |
| Unraid 49/109/249 USD, 36 USD Verlängerung und Patchregel | DOKUMENTIERT | Unraid-Kaufseite und FAQ, Stand 30.09.2026 | Keine deutschen Checkout-Endpreise; vor Kauf neu prüfen |
| Immich RAM und CPU; x86-64-v2 seit v3 für den amd64-Machine-Learning-Container; VM statt Docker-in-LXC | DOKUMENTIERT | Immich-Anforderungen | Keine allgemeine x86-64-v2-Pflicht für Immich ohne diesen ML-Container; kein Installationstest und kein 4-GB-Fullstack-Versprechen |
| Jellyfin und Transcoding | DOKUMENTIERT | Jellyfin-Dokumentation | Keine erfundenen Stream-Zahlen; ältere Intel-CPUs nicht pauschal unbrauchbar |
| Pi-hole, Immich, Nextcloud und Home Assistant | DOKUMENTIERT/EMPFEHLUNG | jeweilige Projektdokumentation | Kein automatischer Ersatz aller Cloud-Funktionen |
| LAN, VPN und öffentliche Exposition | DOKUMENTIERT/ABLEITUNG | Home Assistant und CISA | Kein Versprechen, dass VPN grundsätzlich ohne erreichbaren Endpunkt auskommt |
| RAID ist kein Backup; 3-2-1 und Restore | DOKUMENTIERT/ABLEITUNG/EMPFEHLUNG | CISA, Spiegelungsprinzip | Kein Restore für diesen Artikel ausgeführt |
| Proxmox Bind-/Device-Mounts | DOKUMENTIERT | offizielle vzdump-Dokumentation | Externe Daten separat sichern |
| Budgetstufen 50/150/300 € | EMPFEHLUNG/RECHNUNG | selbst gesetzte Obergrenzen | Keine Marktpreise oder verfügbaren Komplettangebote; Strom/Offsite extra |
| Vier interne CTA-Ziele | DOKUMENTIERT/redaktionell | geprüfte MATMAKSA-URLs | Historische Preise der Zielartikel nicht übernommen |

### Rechenannahmen und offengelegte Grenzen

- Strom: 8.760 Betriebsstunden pro Jahr; angenommene mittlere Leistungen 5, 10, 14, 15 und 25 Watt.
- Tarife: 0,30, 0,40 und 0,50 €/kWh als Szenarien, nicht als Marktmittel.
- TCO: 200 € Rechner, 70 € Backup-Datenträger, 15 W bei 0,40 €/kWh über drei Jahre, 24 €/Jahr Offsite, 40 € Ersatzteilreserve, 0 € Softwarelizenz; Arbeitszeit nicht bewertet.
- Kein eigener Hardware-, Leistungs- oder Stromtest.
- Keine Installation, kein Restore und kein Marktpreisvergleich.
- Keine Affiliate-Links im Writer-Draft.
- Keine Zusage, dass ein einzelner Home-Server alle Cloud-Abos ersetzt.
