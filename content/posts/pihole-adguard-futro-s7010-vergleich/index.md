+++
title = 'Pi-hole oder AdGuard Home auf einem Futro S7010: Was läuft mit 256 MB RAM?'
description = 'Pi-hole und AdGuard Home im Vergleich auf dem Fujitsu Futro S7010 mit 4 GB RAM. Getestet mit 256 und 512 MB – echte Messwerte zu Speicher, DNS-Latenz, WebUI und Blockabdeckung.'
date = 2026-07-14
draft = false
image = "featured.jpg"
cover = { image = "featured.jpg" }
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
+++

## 1. Einleitung

Der Fujitsu Futro S7010 ist ein typisches Einstiegs-System fürs Homelab. Gebraucht häufig günstig erhältlich, mit 4 GB RAM und einer 64-GB-SSD im Kaufzustand – kein High-End-Server, aber eine solide Basis für erste Gehversuche mit Proxmox und kleinen Diensten.

Was ist mit so einem schmalen System realistisch möglich? Welche DNS-Werbeblocker laufen darauf stabil? Und reichen 256 MB Arbeitsspeicher für einen LXC-Container mit Pi-hole oder AdGuard Home, oder muss es mehr sein?

Dieser Artikel vergleicht Pi-hole und AdGuard Home auf einem Futro S7010. Getestet am 14. Juli 2026 mit Pi-hole v6.4.3 und AdGuard Home v0.107.78 – mit 512 MB und mit 256 MB RAM. Ziel ist nicht, einen allgemeingültigen Sieger zu küren, sondern eine datenbasierte Orientierung für Einsteiger mit schmalem Budget zu geben.

> **Dieser Artikel ist ein Praxisvergleich und keine vollständige Installationsanleitung.**

### Kurz erklärt

- **Homelab** – Ein eigenes kleines Rechenzentrum zu Hause zum Experimentieren und Lernen.
- **Proxmox VE** – Eine kostenlose Virtualisierungsplattform, auf der mehrere kleine Server gleichzeitig laufen können.
- **LXC-Container** – Eine besonders schlanke Methode, um einen Dienst (wie Pi-hole) in einer abgeschotteten Umgebung zu betreiben.
- **DNS** (Domain Name System) – Das Telefonbuch des Internets: Es übersetzt eine Adresse wie `example.com` in eine IP-Adresse, die der Computer versteht.
- **DNS-Werbeblocker** – Ein DNS-Server, der bekannte Werbe- und Tracking-Domains von vornherein blockiert.
- **WebUI** – Die Weboberfläche, über die man einen Dienst im Browser verwaltet.
- **Filterliste** – Eine Liste mit Domains, die der Werbeblocker ausfiltert.
- **Upstream-DNS** – Der übergeordnete DNS-Server, an den dein Werbeblocker Anfragen weiterleitet, wenn die Domain nicht auf der Sperrliste steht.
- **DNS-Anfrage, auch Query genannt** – Wenn dein Computer nach der IP-Adresse einer Webseite fragt.
- **OOM** (Out of Memory) – Ein Absturz, weil der Arbeitsspeicher nicht ausreicht.
- **Cosmetic Filtering** – Optisches Ausblenden von Werbeelementen im Browser; ein reiner DNS-Filter kann das nicht leisten.
- **Hosts-basierte Filterliste** – Eine Liste von Domains, die auf eine nicht erreichbare Adresse umgeleitet und dadurch blockiert werden.
- **Cluster** – Zusammenschluss mehrerer Proxmox-Hosts zu einem Verbund; PVE04 lief hier eigenständig ohne Cluster.

## 2. Testaufbau

**Hardware:** Fujitsu Futro S7010 mit 4 GB RAM und einer 64-GB-SSD als eigenständiger Proxmox-Host ohne Cluster. Eine USB-Festplatte dient als separates Backup-Ziel.

Beide DNS-Systeme liefen in eigenen Debian-12-LXC-Containern. Die Container erhielten dieselben CPU-, RAM- und Speicherlimits und wurden mit demselben Testablauf geprüft. Die jeweiligen Standardfilterlisten unterschieden sich jedoch deutlich.

| Parameter | Wert |
|---|---|
| LXC-Basis | Debian 12 Bookworm |
| CPU | Ein virtueller CPU-Kern |
| Disk | 4 GB virtueller Speicherplatz |
| Netzwerk | Eigenes Lab-Netz, isoliert |
| Upstream DNS | Cloudflare (1.1.1.1) + Google (8.8.8.8) |

Getestet wurde mit zwei RAM-Profilen: 512 MB und 256 MB. Für DNS wurden zwei getrennte Läufe dokumentiert: ein gedrosselter Latenzlauf mit 1.000 Anfragen bei maximal 10 Anfragen pro Sekunde sowie ein separater Cold-Cache-Lauf mit je 500 eindeutigen Anfragen ohne festes QPS-Limit. Die Werte beider Methoden werden nicht miteinander vermischt. Die Weboberflächen wurden mit einem automatisierten Browser-Test geprüft.

Es fand keine produktive Routerumstellung statt – die Container blieben im isolierten Lab-Netz.

## 3. Pi-hole und AdGuard Home kurz erklärt

Beide Systeme sind DNS-Werbeblocker: Sie filtern unerwünschte Domains auf DNS-Ebene heraus, bevor Werbung oder Tracker den Browser erreichen.

**Gemeinsamkeiten:** Beide laufen als lokaler DNS-Server, blockieren Domains anhand von Filterlisten und bieten eine Weboberfläche zur Verwaltung.

**Unterschiede:** Pi-hole bietet eine übersichtliche, minimalistische Oberfläche und schlanke Kernfunktionen. AdGuard Home wirkt moderner, bietet mehr integrierte Einstellungen direkt sichtbar und bringt eine größere Standard-Filterliste mit.

## 4. Speicherverbrauch

| System | Zugewiesener RAM | Höchster gemessener Verbrauch | Ergebnis |
|---|---|---|---|
| Pi-hole | 256 MB | ca. 114 MB | stabil |
| Pi-hole | 512 MB | ca. 113 MB | stabil |
| AdGuard Home | 256 MB | ca. 120 MB | stabil |
| AdGuard Home | 512 MB | ca. 118 MB | stabil |

Mehr zugewiesener RAM machte die Dienste im Test nicht automatisch schneller. Er bietet aber zusätzliche Reserve für Updates, größere Filterlisten und zukünftige Versionen.

### Technischer Hintergrund zur Speichermessung

Der Speicherverbrauch wurde vom Host-System pro Container erfasst. Der gemessene Wert umfasst den gesamten zugewiesenen Speicher – also Prozesse, Datei-Zwischenspeicher und System-Overhead. Der Datei-Zwischenspeicher kann bei Bedarf vom Hauptsystem freigegeben werden. Die tatsächliche Belastung des Hosts war bei beiden Systemen ähnlich: Pi-hole verbrauchte weniger reinen Prozessspeicher, baute aber mehr Datei-Zwischenspeicher auf, sodass der Gesamtwert nah beieinander lag. Das ist normal und kein Fehler.

Dass Pi-hole bei 256 MB (ca. 114 MB) und bei 512 MB (ca. 113 MB) fast gleich viel verbrauchte, zeigt: Der Dienst nutzt nur den tatsächlich benötigten Speicher. Mehr zugewiesener RAM schafft hauptsächlich zusätzliche Reserve.

## 5. DNS-Antwortzeiten

Die DNS-Latenzen stammen aus zwei getrennten Testmethoden. Sie beantworten unterschiedliche Fragen und sind deshalb nicht direkt gegeneinander vergleichbar.

### Gedrosselter Latenzlauf: 1.000 Anfragen bei maximal 10 QPS

Dieser Cold-Cache-Lauf bildet eine bewusst begrenzte Last ab. Die 1.000 DNS-Anfragen wurden mit maximal zehn Anfragen pro Sekunde gesendet; alle vier Konfigurationen beendeten den Lauf ohne Fehler oder Timeouts.

| System | Zugewiesener RAM | Durchschnittliche Antwortzeit | Fehler |
|---|---|---|---|
| Pi-hole | 512 MB | 1,53 ms | 0 |
| Pi-hole | 256 MB | 1,54 ms | 0 |
| AdGuard Home | 512 MB | 3,03 ms | 0 |
| AdGuard Home | 256 MB | 3,15 ms | 0 |

Die Werte gelten für diesen gedrosselten Lauf mit seinen getesteten Versionen, Filterlisten und Upstream-DNS-Servern. Sie sind kein allgemeiner Geschwindigkeitsvergleich.

### Separater Cold-Cache-Lauf: 500 eindeutige Anfragen ohne QPS-Limit

Ein zweiter dnsperf-Lauf nutzte 500 eindeutige Domains je protokolliertem Durchlauf und kein festes QPS-Limit. Er wurde mit dem 512-MB-Profil dokumentiert. Hier änderten sich sowohl Datensatz als auch Lastmodell gegenüber dem 1.000er-Latenzlauf.

| System | Profil | Ø Latenz | QPS | Min. | Max. | Fehler |
|---|---|---|---|---|---|---|
| Pi-hole | 512 MB, Cold Cache | 10,62 ms | 91,09 | 0,43 ms | 322 ms | 0 |
| AdGuard Home | 512 MB, Cold Cache | 22,98 ms | 43,47 | 0,16 ms | 2.064 ms | 0 |

Auch aus diesem separaten Lauf lässt sich kein belastbarer allgemeiner Geschwindigkeitsvorteil ableiten. Er zeigt nur die Ergebnisse unter genau dieser Cold-Cache-Methode.

## 6. Funktionieren 256 MB wirklich?

Kurze Antwort: Ja. Beide Dienste liefen in diesem konkreten Test vollständig mit 256 MB RAM – einschließlich DNS, WebUI, Filterupdate und Neustart. Für einen dauerhaften Betrieb bleiben 512 MB die vernünftigere Empfehlung.

| Kriterium | Pi-hole 256 MB | AdGuard 256 MB |
|---|---|---|
| DNS-Test (1.000 Anfragen) | ✅ bestanden | ✅ bestanden |
| WebUI | ✅ bestanden | ✅ bestanden |
| Filterupdate | ✅ bestanden | ✅ bestanden |
| Neustart | ✅ bestanden | ✅ bestanden |
| OOM-Abstürze | 0 | 0 |

Für den reinen DNS-Betrieb mit den getesteten Filterlisten waren 256 MB in beiden Fällen ausreichend. Das getestete 256-MB-Profil liegt für Pi-hole unter der offiziellen Speicherempfehlung und ist deshalb als erprobtes Sparprofil zu verstehen.

## 7. WebUI und Bedienung

Mit 256 MB RAM wurden beide Weboberflächen getestet und waren vollständig nutzbar:

**Pi-hole:** Dashboard, Abfragenprotokoll, Filterlisten, Einstellungen – alle Seiten geladen und reagierten zügig. Die Oberfläche ist übersichtlich und schlank gehalten.

**AdGuard Home:** Dashboard, Abfragenprotokoll, Filterverwaltung, DNS-Einstellungen – alle Seiten nach erfolgreichem Login geladen. Das Interface wirkt moderner und bietet mehr integrierte Einstellungen direkt sichtbar.

> **Sicherheitshinweis:** Im isolierten Testnetz war die Pi-hole-Weboberfläche zeitweise ohne Passwort erreichbar. Für den dauerhaften Einsatz sollte die Verwaltungsoberfläche mit einem Passwort geschützt und nur aus dem lokalen Netz erreichbar sein.

*Hinweis: Die Bewertung der Bedienbarkeit ist eine subjektive Einschätzung, kein objektiver Messwert.*

## 8. Blockabdeckung im Auslieferungszustand

Der Browser-Werbeblocktest über den standardisierten Test auf adblock.turtlecute.org zeigte:

| System | Blockierte Test-Domains | Quote |
|---|---|---|
| Pi-hole | 94 von 133 | ca. 70,7 % |
| AdGuard Home | 107 von 133 | ca. 80,5 % |

**Wichtige Einschränkung:** Die Filterlisten sind nicht direkt vergleichbar. Pi-hole nutzte eine hosts-basierte Liste (~78.000 Regeln), AdGuard Home einen vollwertigen DNS-Filter (~157.000 Regeln) – etwa doppelt so viele. Die Prozentwerte sind deshalb ein Out-of-the-box-Praxistest, kein normierter Qualitätsvergleich. Der Unterschied in der Blockabdeckung ist daher nicht auf die Software, sondern maßgeblich auf die unterschiedlichen Filterlisten zurückzuführen.

Zudem ist zu beachten: Das Ausblenden von Werbeplätzen auf Webseiten (Cosmetic Filtering) ist keine DNS-Funktion und wurde nicht bewertet.

Es lässt sich aus diesen Werten kein allgemeiner Qualitäts- oder Performance-Sieger ableiten.

## 9. Welche Lösung passt zum Futro?

**Pi-hole:**
- Schlanker im konkreten Test
- Übersichtliche Kernfunktionen
- Passende Empfehlung für den kleinen 4-GB-Futro

**AdGuard Home:**
- Modernere Weboberfläche
- Mehr integrierte Einstellungen
- Höhere Blockabdeckung im Auslieferungszustand im konkreten Test (allerdings mit umfangreicherer Standard-Filterliste)

Technisch sind beide Systeme für den Futro S7010 geeignet.

## 10. 256 oder 512 MB?

Der Test hat gezeigt: Beide Systeme arbeiten mit 256 MB RAM zuverlässig – DNS, WebUI, Filterupdate und Neustart waren in allen Fällen erfolgreich, ohne Abstürze.

Für Pi-hole liegt das 256-MB-Profil unter der offiziellen Speicherempfehlung (die 512 MB vorsieht). Es hat im Test dennoch funktioniert.

**Meine Empfehlung:** 256 MB sind ein erprobtes Sparprofil. Für den dauerhaften Betrieb würde ich dennoch 512 MB zuweisen – wegen Updates, potenziell größerer Filterlisten und zukünftiger Versionen, die mehr Speicher benötigen könnten.

## 11. Realistisches Futro-Profil

Ein Futro S7010 im Kaufzustand (4 GB RAM, 64 GB SSD) kann realistisch betreiben:

- Proxmox VE (belegte auf diesem Futro im Leerlauf rund 1,3 GB RAM)
- **Einen DNS-Container** (Pi-hole oder AdGuard, 512 MB empfohlen)
- Einen zusätzlichen kleinen Test-Container, der nur zeitweise läuft – beispielsweise mit 256 bis 512 MB (z. B. ein Monitoring-Werkzeug)
- USB-Festplatte als Backup-Ziel

Was nicht sinnvoll ist: mehrere Dienste gleichzeitig, mehrere virtuelle Maschinen, KI-Dienste, Medien-Server oder Cloud-Anwendungen. Dafür fehlen schlicht Arbeitsspeicher und Rechenleistung im Kaufzustand.

## 12. Bevor du den DNS-Server im Router einträgst

Bevor du die DNS-Einstellungen in deinem Router änderst, solltest du einige Vorsichtsmaßnahmen treffen:

- **Teste zuerst mit einem einzelnen Gerät.** Stelle auf einem Rechner oder Smartphone manuell die IP-Adresse des neuen DNS-Servers ein und prüfe, ob das Internet wie gewohnt funktioniert.
- **Erst nach erfolgreichem Test die Router-Einstellung ändern.** Trage den neuen DNS-Server erst im Router ein, wenn du sicher bist, dass der Dienst stabil läuft.
- **Notiere die bisherigen DNS-Einstellungen.** So kannst du jederzeit zur alten Konfiguration zurückwechseln.
- **Halte einen Rückweg bereit.** Wenn der einzige DNS-Container gestoppt ist (zum Beispiel nach einem Neustart oder Update), können viele Geräte im Netzwerk keine Webseiten mehr öffnen – es wirkt, als sei das Internet ausgefallen.
- **Stoppe den DNS-Container nicht versehentlich.** Ein solcher Ausfall betrifft das gesamte Heimnetz und ist für Einsteiger schwer zu diagnostizieren.

## 13. Fazit

Für meinen Futro im Kaufzustand würde ich Pi-hole wählen, weil es im Test schlank war und alle benötigten Funktionen bot. AdGuard Home ist ebenso geeignet und besonders interessant, wenn eine modernere Oberfläche und mehr integrierte Einstellungen wichtiger sind.

Die Ergebnisse gelten für die getesteten Versionen, Filterlisten und diesen Futro S7010. Sie sind kein allgemeiner Beweis dafür, dass eine Lösung in jeder Umgebung schneller oder sparsamer ist.

## 14. Wie geht es jetzt weiter?

- **Pi-hole in einem Proxmox-LXC installieren** – Eine Schritt-für-Schritt-Anleitung ist geplant.
- **AdGuard Home in einem Proxmox-LXC installieren** – Eine Schritt-für-Schritt-Anleitung ist geplant.
- **DNS im Router sicher umstellen** – Eine Schritt-für-Schritt-Anleitung ist geplant.
- **Den DNS-Container sichern und wiederherstellen** – Eine Schritt-für-Schritt-Anleitung ist geplant.
- **USB-Festplatte als Proxmox-Backup-Ziel verwenden** – Eine Schritt-für-Schritt-Anleitung ist geplant.
