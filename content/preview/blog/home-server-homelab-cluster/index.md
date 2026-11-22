+++
title = "Vom Home-Server zum Homelab-Cluster: Wann sich mehrere Nodes lohnen"
description = "Zweiter Host oder gleich K3s? So unterscheidest du Redundanz, Backup und Hochverfügbarkeit und planst den Ausbau ohne unnötige Komplexität."
slug = "home-server-homelab-cluster"
draft = true
robotsNoIndex = true
noindex = true
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
stage = "REVIEWER_PASS_PREVIEW_VALIDATION"
preview_content_type = "article_draft"
publish_eligible = false
approved_for_publish = false
content_state = "test_only_draft"

[sitemap]
  exclude = true

[workflow]
  content_state = "draft_generated"
  editorial_status = "pass"
  technical_status = "pass"
  visual_status = "pass"
  seo_status = "pass"
+++

# Vom Home-Server zum Homelab-Cluster: Wann sich mehrere Nodes lohnen

Dein Home-Server läuft, die ersten Dienste sind eingerichtet. Beim nächsten Update fällt dir jedoch auf: Ist dieses Gerät aus, sind auch alle Dienste darauf aus. Ein zweiter Rechner wirkt wie der logische nächste Schritt. Ob daraus gleich ein Cluster werden sollte, ist eine andere Entscheidung.

Kaufe den nächsten Node erst, wenn du benennen kannst, welches Problem er lösen soll. Mehr Platz für Experimente, ein Ersatzgerät für die Wiederherstellung und automatischer Weiterbetrieb nach einem Ausfall sind drei verschiedene Ziele. Dieser Artikel hilft dir bei der Entscheidung. Er ist keine Installationsanleitung und kein nachgebauter Hardwaretest.

Wenn du noch den ersten Server planst, beginne mit unserem [Home-Server-Einstieg zu Kosten, Hardware und Grenzen – derzeit als Preview](https://matmaksa.de/preview/blog/home-server-statt-cloud-abos/). Hier geht es um den nächsten Schritt: mehrere Geräte, ihre Abhängigkeiten und die Grenze zwischen nützlicher Redundanz und zusätzlicher Arbeit.[6]

## Was wir aus der Homelab-Tour übernehmen – und was nicht

Anlass ist „My 2026 Homelab Tour: Company-Grade Infrastructure at Home“ von **I'll host it myself**. Der Creator nennt zu Beginn sechs Computer, 40 CPU-Threads, 116 GB RAM und rund 200 laufende Pods. Er beziffert seinen Aufbau auf ungefähr 3.000 Euro über etwa vier Jahre und spricht dabei von rund 60 Euro pro Monat.[1]

Das sind **Creator-Angaben aus dem Transcript**, keine MATMAKSA-Messwerte. Besonders die Monatszahl braucht Kontext: Am Ende des Videos zählt er Anschaffungen auf, erwähnt bereits vorhandene Geräte und Geschenke und nimmt den 3D-Drucker ausdrücklich aus den Laborkosten heraus. Die Angabe ist damit keine belegte Rechnung für Strom, Wartung und sämtliche laufenden Kosten.[1]

Auch die Pod-Zahl ist kein Maß dafür, wie viele nützliche Anwendungen ein Haushalt braucht. Ein Pod umfasst einen oder mehrere zusammengehörige Container; eine Anwendung kann wiederum aus mehreren Pods bestehen.[10]
Im Transcript stehen am Anfang 200, später 204 Pods. Wir verwenden deshalb nur „rund 200“ und behandeln die Zahl als Momentaufnahme des Creators.[1]

Die für den Einstieg brauchbarste Aussage steht früh im Video: Der Aufbau ist über Jahre gewachsen und soll ausdrücklich kein Startpunkt sein. Später beschreibt der Creator K3s als Grundlage seines Clusters.[1]
Unsere redaktionelle Folgerung lautet deshalb: Übernimm den schrittweisen Ausbau, nicht die Einkaufsliste.

## Einzelserver, mehrere Hosts und Cluster sind nicht dasselbe

Für die Entscheidung unterscheiden wir drei Betriebsformen:

| Betriebsform | Was damit gemeint ist | Was du nicht voraussetzen darfst |
|---|---|---|
| Einzelserver | Ein Gerät trägt deine Dienste, direkt oder in getrennten Laufzeitumgebungen. | Weitere Container auf demselben Gerät schaffen keinen zweiten physischen Ausfallbereich. |
| Mehrere unabhängige Hosts | Du verteilst Aufgaben auf getrennte Geräte oder hältst ein Ersatzgerät bereit. | Dienste wechseln nicht allein deshalb automatisch den Rechner. |
| Cluster | Eine gemeinsame Steuerung koordiniert die beteiligten Nodes und bestimmte Aufgaben. | Gemeinsame Verwaltung bedeutet noch keine hochverfügbare Anwendung. |

Die ersten beiden Begriffe sind hier eine praktische Einteilung. Bei Kubernetes besteht ein Cluster aus einer Control Plane und mindestens einem Worker-Node. Die Control Plane verwaltet den Zustand, der Scheduler ordnet noch nicht zugewiesene Pods geeigneten Nodes zu.[3]
Proxmox VE gruppiert physische Hosts unter anderem für gemeinsame Verwaltung und Migration; der HA-Manager ist eine zusätzliche Funktion für dafür konfigurierte Ressourcen.[8][5]

Für dich heißt das: Ein zweiter Host kann Experimente vom Alltagsdienst trennen oder als Ziel für eine manuelle Wiederherstellung dienen. Beides ist ein sinnvoller Ausbaupfad, auch ohne automatisches Failover. Diese Einordnung ist unsere Empfehlung, kein HA-Versprechen.

### Warum zwei Rechner nicht automatisch hochverfügbar sind

K3s dokumentiert für eine hochverfügbare Control Plane **mit eingebettetem etcd** mindestens drei Server-Nodes. Diese Variante benötigt eine Mehrheit der etcd-Mitglieder, das Quorum.[2]
Ein Server plus ein Agent erfüllt diese Anforderung nicht; zusätzliche Worker ersetzen keine etcd-Mehrheit.[2]

Das ist keine allgemeine Mindestzahl für jedes Homelab. Auch Proxmox beschreibt mindestens drei Nodes für verlässliches Quorum und dokumentiert für kleinere Zwei-Node-Cluster ein externes QDevice als zusätzliche Stimme.[8]
Eine zusätzliche Stimme stellt aber weder Rechenleistung noch die Daten eines ausgefallenen Hosts bereit. Für HA müssen die Ressourcen auf dem Zielhost tatsächlich ausführbar sein, einschließlich Storage, Netzwerk und weiterer Abhängigkeiten.[5]

Unsere Empfehlung für den Einstieg: Baue kein Zwei-Node-HA-Konstrukt, bevor du Quorum, Datenzugriff und Wiederanlauf getrennt erklären kannst. Zwei unabhängige Hosts mit dokumentierter Wiederherstellung sind oft die übersichtlichere Zwischenstufe.

## Redundanz ist nicht Backup

Hochverfügbarkeit soll einen Dienst trotz bestimmter Ausfälle weiter bereitstellen oder wieder starten. Der Proxmox-HA-Manager kann beispielsweise konfigurierte VMs und Container nach einem Hostfehler auf einem anderen geeigneten Node starten.[5]
Das ist nicht gleichbedeutend mit einem unterbrechungsfreien Dienst.

Ein Backup verfolgt ein anderes Ziel: einen gesicherten Zustand wiederherstellen. Proxmox dokumentiert dafür eigene Backup- und Restore-Verfahren mit unterschiedlichen Konsistenz- und Auszeit-Eigenschaften.[7]
Gegen Schadsoftware empfiehlt CISA ausdrücklich offline gehaltene, verschlüsselte Sicherungen und regelmäßige Wiederherstellungstests.[13]

**Gedankenexperiment:** Du löschst versehentlich eine wichtige Datei. Wenn die Anwendung diese Änderung ordnungsgemäß in alle aktuellen Kopien übernimmt, bleiben die Kopien konsistent und die Datei bleibt gelöscht. Mehr laufende Kopien liefern dir nicht von selbst einen älteren, wiederherstellbaren Stand. Plane Redundanz und Sicherung deshalb als getrennte Aufgaben.

Ein begrenzter Scratch-Test mit einer synthetischen SQLite-Datenbank zeigt zusätzlich, warum eine erfolgreiche Integritätsprüfung noch keinen vollständigen Dateibackup beweist. Im Test waren 100 Datensätze bestätigt, lagen aber noch im Write-Ahead Log (WAL). Eine naive Kopie nur der Hauptdatei enthielt 0 dieser 100 Datensätze, obwohl `integrity_check=ok` meldete. Eine Kopie über die SQLite Backup API enthielt alle 100. SQLite dokumentiert sowohl die separate WAL-Datei als auch die Backup API für Snapshot-Kopien.[14][15][16]

Diese Beobachtung gilt nur für das synthetische SQLite-Beispiel. Sie beweist weder einen Fehler in Proxmox-Backups noch eine allgemeine Unsicherheit von VM-, Anwendungs- oder Cluster-Sicherungen. Für ein wichtiges System brauchst du das passende anwendungsspezifische Backup-Verfahren und einen echten Restore-Test.

### Welche Ausfälle willst du abfangen?

Die folgende Tabelle ist eine redaktionelle Prüfhilfe aus den dokumentierten HA-, Storage- und Backup-Grenzen, keine Zusage für ein konkretes Lab.[5][9][13]

| Angenommener Ausfall | Wobei mehrere Hosts helfen können | Was du zusätzlich prüfen musst |
|---|---|---|
| Ein Rechner fällt aus | Ein anderer kann geeignete Workloads übernehmen. | Sind Kapazität, Steuerung, Daten und Netzwerk dort verfügbar? |
| Die lokale Datenträgerkopie fehlt | Ein anderer Datenbestand könnte nutzbar sein. | Ist er unabhängig, aktuell genug und für die Anwendung konsistent? |
| Das gemeinsame NAS fällt aus | Weitere Compute-Nodes allein lösen das nicht. | Hängen alle Instanzen am selben NAS? Wo liegt die Sicherung? |
| Der gemeinsame Switch oder Router fällt aus | Zusätzliche Server ersetzen den ausgefallenen Netzwerkpfad nicht. | Welche Verbindungen und Verwaltungszugänge bleiben erreichbar? |
| Der gemeinsame Strompfad fällt aus | Geräte am selben ausgefallenen Strompfad helfen einander nicht. | Welche Ausfalldauer willst du überbrücken, und wie wird sauber beendet? |
| Der Internetanschluss fällt aus | Ein lokaler Dienst kann lokal nutzbar bleiben. | Benötigt er externe Anmeldung, DNS, Tunnel oder andere Cloud-Dienste? |
| Eine falsche Konfiguration oder Schadsoftware trifft alle Instanzen | Gleiche Kopien können gemeinsam betroffen sein. | Gibt es getrennt geschützte Backups und einen unabhängigen Wiederherstellungsweg? |

Ein *Single Point of Failure* ist in dieser Betrachtung eine einzelne Abhängigkeit, deren Ausfall den betrachteten Dienst stoppt. Zeichne deshalb als Übung den Weg vom Endgerät zur Anwendung und weiter zu deren Daten. Markiere jede Stelle, die alle Instanzen gemeinsam benötigen. Beginne bei dem Ausfall, der dich tatsächlich stört, statt vorsorglich alles doppelt zu kaufen.

## K3s, Compose oder zunächst eine VM?

Docker Compose beschreibt zusammengehörige Dienste, Netzwerke und Volumes in einer YAML-Konfiguration. Docker dokumentiert auch den Betrieb auf einem einzelnen Server.[4][12]
Kubernetes ergänzt die clusterweite Steuerung: Controller können für verwaltete Workloads Ersatz-Pods erzeugen; der Scheduler platziert sie auf geeigneten Nodes.[3][10]
Ein bestehender Pod wird dabei nicht mitsamt seinem laufenden Speicherzustand auf einen anderen Rechner getragen.

Schwieriger als die reine Pod-Platzierung sind häufig die Daten. K3s bringt den Local Path Provisioner mit, der Speicher auf dem jeweiligen Node bereitstellt. Dass ein Volume einen Pod-Neustart übersteht, bedeutet deshalb nicht, dass es nach Verlust dieses Nodes auf einem anderen verfügbar ist.[9]
Eine hochverfügbare Control Plane löst dieses Storage-Problem nicht automatisch.[2][9]

Unsere Auswahlhilfe:

- **Bleibe zunächst bei Compose**, wenn du wenige Containerdienste betreibst und eine geplante Auszeit oder manuelle Wiederherstellung akzeptieren kannst.
- **Nutze zunächst getrennte VMs auf deiner vorhandenen Plattform**, wenn du vor allem unterschiedliche Systeme verwalten und später auf einen anderen Host wiederherstellen möchtest. Daraus folgt noch keine Hochverfügbarkeit.
- **Prüfe K3s**, wenn du Kubernetes gezielt lernen willst oder eine konkrete Anwendung die zusätzliche Orchestrierung rechtfertigt. Kläre vor wichtigen Daten deren Storage- und Backup-Pfad.

Das sind redaktionelle Empfehlungen, keine Rangliste. Ein Lerncluster darf sich durch seinen Lernwert rechtfertigen. Für einen wichtigen Alltagsdienst sollte dagegen klar sein, welche Auszeit du verkürzen willst und wie du den Erfolg überprüfst.

### Was du im laufenden Betrieb beherrschen solltest

Unsere Mindest-Checkliste: Linux-Dienste und Logs lesen, IP-Adressen und DNS verstehen, Containerkonfigurationen nachvollziehen, persistente Daten finden und eine Sicherung zurückspielen können. Vor einem Cluster kommen Kenntnisse über Quorum, Platzierung und Abhängigkeiten hinzu.

Plane als wiederkehrende Arbeit Updates, Kapazitätskontrolle, Backup-Prüfung, Wiederherstellungsübungen und die Pflege deiner Betriebsnotizen ein. K3s verlangt beim Datastore-Backup zusätzlich den passenden Server-Token für die Wiederherstellung.[11]
Behandle ihn als Geheimnis; er gehört nicht in ein öffentliches Konfigurationsrepository. Ein Datastore-Backup ist außerdem nicht mit einer Sicherung aller Anwendungsdaten gleichzusetzen: Diese liegen je nach Anwendung in gesonderten persistenten Volumes.[3][9][11]

Bei Proxmox-Containern musst du die eingeschlossenen Daten ebenfalls prüfen: Zusätzliche Mountpoints sind standardmäßig nicht alle im Backup enthalten; Device- und Bind-Mount-Inhalte werden durch diesen Backup-Pfad nicht mitgesichert.[7]

## Der MATMAKSA-Ausbaupfad: erst Wiederherstellung, dann Cluster

Die folgenden Schritte sind unsere redaktionelle Empfehlung. Sie setzen kein bestimmtes Budget und keine feste Zahl von Geräten voraus.

1. **Betreibe einen klar begrenzten Dienst auf einem Gerät.** Notiere, wer ihn nutzt, wo seine Daten liegen und welche Auszeit akzeptabel wäre. Wähle für erste Experimente keine unersetzlichen Originaldaten.
2. **Richte eine getrennte Sicherung ein und prüfe den Restore.** Stelle eine Kopie isoliert wieder her. Prüfe nicht nur, ob der Prozess startet, sondern ob du dich anmelden und die erwarteten Daten öffnen kannst. Notiere die benötigte Zeit und den Stand der Daten. Hier wurde kein Restore für dich durchgeführt.
3. **Gib einem zweiten Host eine konkrete Aufgabe.** Er kann Testsystem oder Wiederherstellungsziel sein. Prüfe vor dem Kauf, ob vorhandene Hardware diese Aufgabe erfüllt. Übernahme per Hand ist ausdrücklich zulässig, wenn sie zu deiner akzeptierten Auszeit passt.
4. **Trenne Rollen und dokumentiere Abhängigkeiten.** Halte fest, wo Alltagsdienste, Experimente und Backups liegen. Prüfe auch, ob du bei Ausfall der Anwendung noch an Verwaltung, Zugangsdaten und Anleitung kommst.
5. **Erprobe erst dann einen Cluster.** Beginne mit einem entbehrlichen Dienst. Definiere vorab einen kontrollierten Ausfallversuch im isolierten Testaufbau, den erwarteten Wiederanlauf und einen Abbruchweg. Miss die Unterbrechung am Client, nicht nur die Zahl grüner Nodes.

Stoppe den Ausbau, wenn du keinen zusätzlichen Nutzen benennen kannst oder die Wiederherstellung noch nicht beherrschst. Wenn die Wartung mehr Zeit beansprucht, als du dafür einplanen möchtest, ist die vorherige Stufe ein zulässiger Endzustand.

## Kosten planen: Was kostet der zusätzliche Host wirklich?

Übernimm die rund 60 Euro aus der Tour nicht als monatlichen Betriebspreis. Die Aussage steht dort im Zusammenhang mit den über Jahre angesammelten Anschaffungen.[1]
Für deine Ausbauentscheidung empfehlen wir eine eigene Differenzrechnung: Welche Kosten kommen gegenüber dem bestehenden Server hinzu?

| Kostenposten | Was du für deinen Ausbau eintragen solltest |
|---|---|
| Anschaffung | Zusätzlicher Host, Speicher, Netzteile und tatsächlich benötigte Netzwerkgeräte |
| Strom | Gemessener zusätzlicher Verbrauch über typische Nutzung einschließlich Backups |
| Ersatz und Reserve | Laufwerke, Netzteile oder andere Teile, für die du Ersatz vorhalten willst |
| Datensicherung | Zusätzliches Sicherungsziel und gegebenenfalls externer Speicher |
| Betrieb | Falls zutreffend Lizenzen, Domain und weitere Dienstkosten |
| Zeit | Einrichtung, Updates, Fehlersuche und Wiederherstellungsübungen |

Für die Stromrechnung gilt als Einheitenrechnung: **mittlere zusätzliche Leistung in Watt × Betriebsstunden ÷ 1.000 × eigener Arbeitspreis in Euro pro kWh**. Nutze gemessene Werte und deinen Vertrag; dieser Artikel nennt weder aktuelle Marktpreise noch gemessene Verbrauchswerte.

Unsere Empfehlung: Reserviere Budget für Sicherung und Ersatz, bevor du einen weiteren Rechenknoten kaufst. Vergleiche nicht nur die Hardwarepreise, sondern auch die von dir akzeptierte Wartungszeit. Ein günstiger zusätzlicher Rechner ist kein Beleg für günstigen Clusterbetrieb.

## Checkliste: Ist jetzt der richtige Zeitpunkt?

Nutze diese redaktionelle Entscheidungshilfe vor dem Ausbau:

- Ich kann den Dienst und den Ausfall nennen, für den ich Redundanz brauche.
- Ich habe akzeptable Auszeit und akzeptablen Verlust neuer Daten getrennt notiert.
- Ich habe eine Sicherung tatsächlich wiederhergestellt und das Ergebnis geprüft.
- Ich weiß, welche Daten auf welchem Host liegen und welche gemeinsam genutzten Komponenten bleiben.
- Ich kann nach Ausfall des Hauptsystems noch auf meine Verwaltungs- und Wiederherstellungsanleitung zugreifen.
- Ich habe Zeit und Budget für laufende Pflege eingeplant.
- Ich kann erklären, warum ein Cluster mehr hilft als ein zweiter unabhängiger Host.

Sind die letzten Punkte offen, bleibe zunächst beim kleineren Aufbau. Wenn du Kubernetes lernen möchtest, kannst du daneben einen entbehrlichen Lerncluster betreiben, ohne ihm schon wichtige Alltagsdienste anzuvertrauen.

## Häufige Fragen

### Brauche ich drei Geräte für ein Homelab?

Nein. Die genannte Dreier-Anforderung bezieht sich hier auf K3s-HA mit eingebettetem etcd, nicht auf jeden privaten Serveraufbau.[2]
Unsere Empfehlung bleibt ein einzelner, nachvollziehbar betreibbarer Dienst als Einstieg.

### Macht ein Cluster meine Daten automatisch sicher?

Nein. Die K3s-Dokumentation trennt Cluster-Datastore, dessen Backup und persistenten Anwendungsspeicher.[9][11]
Plane deshalb gesondert, welche Daten du sichern und wie du sie wiederherstellen musst.

### Ist Proxmox-HA dasselbe wie Kubernetes?

Nein. Proxmox-HA verwaltet konfigurierte VMs und Linux-Container als HA-Ressourcen; Kubernetes verwaltet unter anderem Pods über Workload-Controller.[5][10]
Die Auswahl hängt von der Ebene ab, auf der du deine Dienste betreiben möchtest.

### Kann ein zweiter Host ohne Cluster sinnvoll sein?

Ja, als unsere empfohlene Zwischenstufe für getrennte Experimente oder einen vorbereiteten manuellen Wiederanlauf. Bewerte ihn daran, ob dein Ablauf verständlicher wird und deine gewünschte Wiederherstellungszeit erreichbar ist, nicht am Etikett „HA“.

## Fazit: Baue den nächsten Schritt, nicht die ganze Tour nach

Die Tour liefert ein Beispiel für einen gewachsenen Aufbau, aber keinen Nachweis dafür, dass dein Haushalt dieselbe Größe oder Architektur benötigt.[1]
Unsere Empfehlung: Definiere einen Dienst und einen Wiederherstellungsweg, bevor du weitere Nodes kaufst.

Beginne bei Bedarf mit dem [MATMAKSA-Home-Server-Einstieg – derzeit als Preview](https://matmaksa.de/preview/blog/home-server-statt-cloud-abos/). Wenn dein einzelner Server und dessen Sicherung beherrschbar sind, entscheide zwischen einem zweiten unabhängigen Host und einem Cluster. Ein Rack und eine hohe Pod-Zahl sind dabei keine Erfolgskriterien.

*Transparenz: Dieser Beitrag ordnet das Transcript der verlinkten Tour und offizielle Dokumentation ein. Zusätzlich haben wir den beschriebenen SQLite-WAL-Vergleich ausschließlich mit synthetischen Daten im Scratch ausgeführt. Wir haben keine visuelle Prüfung des Videos und keinen Hardware-, Proxmox-, Cluster-, Failover-, Verbrauchs- oder produktiven Restore-Test durchgeführt. Empfehlungen sind redaktionelle Einordnungen. Der Entwurf enthält keine Affiliate-Links.*

## Sources

[1] https://www.youtube.com/watch?v=OijVsKfiD80
[2] https://docs.k3s.io/datastore/ha-embedded
[3] https://kubernetes.io/docs/concepts/overview/components
[4] https://docs.docker.com/compose
[5] https://pve.proxmox.com/pve-docs/chapter-ha-manager.html
[6] https://matmaksa.de/preview/blog/home-server-statt-cloud-abos
[7] https://pve.proxmox.com/pve-docs/chapter-vzdump.html
[8] https://pve.proxmox.com/pve-docs/chapter-pvecm.html
[9] https://docs.k3s.io/storage
[10] https://kubernetes.io/docs/concepts/workloads/pods
[11] https://docs.k3s.io/datastore/backup-restore
[12] https://docs.docker.com/compose/how-tos/production
[13] https://www.cisa.gov/stopransomware/ransomware-guide
[14] https://sqlite.org/backup.html
[15] https://www.sqlite.org/wal.html
[16] https://sqlite.org/c3ref/backup_finish.html
