+++
title = 'Proxmox Backup für Einsteiger: Snapshot, Backup und Restore richtig verstehen'
description = 'Proxmox Backup für Einsteiger: Snapshot ist kein Backup. Dieser Guide zeigt, wie du deine VMs und LXCs richtig sicherst und den Restore testest.'
date = 2026-07-13
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
recommended_action = "next_article_candidate_after_fact_check_and_visual_review"
content_intent = "pillar"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = true
risk_level = "medium"

[cover]
image = "featured.jpg"
relative = true
alt = "Proxmox Backup Dashboard auf einem Monitor in einem dunklen Homelab-Rack mit Backup-Laufwerken"
+++

> [!IMPORTANT]
> **Preview-Review-Box**
> TYPE=article_draft
> PUBLISH_ELIGIBLE=no
> USER_VISUAL_APPROVAL_REQUIRED=yes
> FACT_CHECK_REQUIRED=yes (Proxmox-Menünamen, Backup-Ziel)
> LINK_CHECK_REQUIRED=yes
> PRICE_CHECK_REQUIRED=no
> RECOMMENDED_ACTION=next_article_candidate_after_fact_check_and_visual_review
>
> **Preview-Hinweis:** Nicht veröffentlichter Entwurf – noch nicht publish-ready.
> **Cover-Bild:** Wird vor Freigabe generiert.

---

# Proxmox Backup für Einsteiger: Snapshot, Backup und Restore richtig verstehen

## TL;DR: Snapshot ist kein Backup

Ein **Snapshot** ist praktisch, wenn du vor einem Update schnell einen Rücksprungpunkt brauchst. Ein echtes **Backup** liegt getrennt von der VM oder dem LXC und lässt sich auch dann wiederherstellen, wenn dein Dienst kaputt konfiguriert wurde oder du den Container versehentlich gelöscht hast.

Meine Einsteiger-Regel: **Snapshot vor riskanten Änderungen, Backup regelmäßig, Restore mindestens einmal testen.** Erst wenn du eine Wiederherstellung erfolgreich ausprobiert hast, weißt du wirklich, dass dein Homelab nicht nur läuft, sondern auch reparierbar ist.

## Voraussetzungen

| Punkt | Wert |
|---|---|
| ⏱ Zeit | 30–45 Minuten |
| 💰 Kosten | 0 € mit vorhandenem Speicherziel |
| 📊 Schwierigkeit | ⭐⭐☆☆☆ |
| 🖥️ Benötigt | Laufender Proxmox-Host, mindestens eine VM oder ein LXC, ein Backup-Ziel |
| 🎯 Ziel | Erstes Backup erstellen und Wiederherstellung testweise prüfen |
| ✅ Getestet mit | Proxmox VE (aktuelle Version) |

## Die einfache Entscheidung: Snapshot, Backup oder Restore-Test?

Viele Einsteiger klicken in Proxmox zuerst auf „Snapshot" und fühlen sich sicher. Das ist verständlich, aber gefährlich: Ein Snapshot hilft nur in bestimmten Situationen.

| Situation | Nimm das | Warum |
|---|---|---|
| Du installierst ein Update und willst schnell zurück | Snapshot | Schnell erstellt, gut für kurze Tests |
| Du willst eine VM/LXC regelmäßig sichern | Backup | Wiederherstellung unabhängig vom laufenden Zustand |
| Du willst wissen, ob deine Sicherung wirklich funktioniert | Restore-Test | Nur ein getestetes Backup ist ein brauchbares Backup |
| Du speicherst alles auf derselben internen SSD | Nicht ausreichend | Bei SSD-Ausfall sind Original und Sicherung weg |

Die wichtigste Unterscheidung:

* **Snapshot:** Kurzfristiger Rücksprungpunkt auf demselben Speicher – hilft, wenn du ein Update rückgängig machen musst. Ein Snapshot ist **kein externes Backup** und schützt nicht vor defekter Festplatte.
* **Backup:** Sicherung auf einem separaten Ziel – enthält VM-Konfiguration **und** Daten. Schützt vor Konfigurationsfehlern, versehentlichem Löschen und Hardware-Ausfall (nur bei getrenntem Speicher).
* **Restore-Test:** Beweis, dass dein Backup nicht nur existiert, sondern nutzbar ist.

## Schritt für Schritt: Backup-Ziel prüfen und ersten Backup-Job anlegen

Für den ersten Artikel läuft der Ablauf über die Proxmox-Weboberfläche. Das senkt die Hürde für Einsteiger.

### 1. Prüfen, wo dein Backup liegen soll

Ein Backup braucht ein Ziel. Drei realistische Varianten für Einsteiger:

| Backup-Ziel | Geeignet für | Hinweis |
|---|---|---|
| Zweite interne SSD/HDD | Erste Tests | Besser als nichts, aber kein Schutz vor Geräteausfall |
| Externe USB-Festplatte | Einfacher Start | Muss sauber eingebunden und zuverlässig erreichbar sein |
| NAS oder zweiter Mini-PC | Dauerhafter Betrieb | Sauberer, aber mehr Einrichtung nötig |

**Wichtig:** Ein Backup auf derselben internen SSD schützt nicht vor Hardware-Defekt, hilft aber gegen Konfigurationsfehler, versehentliches Löschen und kaputte Updates.

In meinem Homelab sichert Proxmox auf eine angeschlossene **1-TB-USB-Festplatte** (HGST HTS721010A9E630). Die Platte hängt am USB-Port des Proxmox-Hosts und ist als Directory Storage `Backup` eingebunden. Das ist ein einfaches, kostengünstiges externes Backup-Ziel – kein Pflichtkauf, aber ein stabiler Einstieg.

Die Einrichtung zeige ich dir im Artikel **[USB-Festplatte als Proxmox-Backup-Ziel einrichten](/preview/blog/proxmox-usb-festplatte-backup-ziel/)**.

### 2. Backup über die Weboberfläche starten

In Proxmox läuft der Einsteiger-Weg so:

1. VM oder LXC in der Seitenleiste auswählen.
2. Menüpunkt „Backup" öffnen.
3. Backup-Ziel auswählen (Storage).
4. Modus und Kompression bei den Standardwerten lassen.
5. Backup starten.
6. Log prüfen: Der Job muss erfolgreich beendet sein.

> **Tipp:** Ändere beim ersten Backup so wenig wie möglich. Ziel ist nicht Tuning, sondern ein erfolgreiches, wiederherstellbares Backup.

### 3. Einen einfachen Backup-Rhythmus festlegen

Für den Einstieg reicht eine klare Regel besser als eine perfekte Enterprise-Strategie:

- **Test-LXC:** Backup vor größeren Änderungen.
- **Wichtiger Dienst:** Regelmäßiges automatisches Backup einrichten.
- **Vor Updates:** Kurzer Snapshot plus aktuelles Backup.
- **Nach größeren Änderungen:** Restore-Test einplanen.

## Restore testen: Der wichtigste Schritt

Ein Backup ist erst dann beruhigend, wenn du einmal gesehen hast, dass die Wiederherstellung klappt. Viele Einsteiger lassen diesen Schritt aus – das ist nachvollziehbar, aber riskant.

So testest du risikoarm und ohne deine produktiven Dienste zu gefährden:

1. **Test-LXC sichern:** Wähle einen kleinen, nicht kritischen Container aus oder lege einen neuen an. Das ist dein Testobjekt, an dem du den Restore übst.

2. **Mit neuer ID wiederherstellen:** Beim Restore vergibst du eine neue VMID/CTID. So bleibt der originale Container unverändert, und du vermeidest Konflikte im laufenden Betrieb.

3. **Mit deaktiviertem Netzwerk starten:** Starte den wiederhergestellten Container zunächst mit deaktiviertem Netzwerk – entweder über die Weboberfläche (Netzwerk-Interface deaktivieren) oder in einem isolierten Bridge-Port. So vermeidest du IP-Adresskonflikte mit dem laufenden Original, falls der Restore doch zu früh online geht.

4. **Funktion prüfen:** Nach dem Start prüfst du Schritt für Schritt: Lässt sich der Login durchführen? Sind die konfigurierten Dienste erreichbar? Funktioniert das interne Netzwerk? Stimmen die Daten? Erst wenn du alles aktiv getestet hast, kannst du das Netzwerk zuschalten und die volle Erreichbarkeit prüfen.

5. **Test-Container löschen:** Nach erfolgreicher Prüfung entfernst du den Test-Container sauber über „Remove". Der originale LXC bleibt unberührt und läuft weiter.

> **Wichtig:** Übe zuerst mit einem Test-LXC, bevor du den Restore auf einen echten Dienst anwendest. Der erste Restore ist der lehrreichste – da willst du nicht unter Zeitdruck stehen.

## Warum funktioniert das?

Proxmox verwaltet VMs und LXC-Container als eigene Einheiten. Dadurch kann Proxmox nicht nur den laufenden Zustand anzeigen, sondern auch vollständige Sicherungen dieser Einheiten erstellen – inklusive **Konfiguration und Daten**.

Für Einsteiger reicht die praktische Idee:

- Deine VM oder dein LXC ist die Arbeitskopie.
- Das Backup ist die Sicherheitskopie.
- Der Restore baut aus der Sicherheitskopie wieder eine lauffähige Maschine oder einen Container.

Snapshots fühlen sich ähnlich an, sind aber wie ein Lesezeichen im aktuellen Buch. Ein Backup ist dagegen eine Kopie des Buchs, die du aus dem Regal holen kannst, wenn das Original beschädigt wurde.

## Typische Fehler und Lösungen

### Fehler 1: „Ich habe Snapshots, also brauche ich kein Backup"

Doch. Snapshots helfen bei kurzfristigen Änderungen, ersetzen aber keine separate Sicherung. Nutze Snapshots vor Updates und Backups für echte Wiederherstellung.

### Fehler 2: „Mein Backup liegt auf derselben internen SSD wie die VM"

Das ist besser als gar kein Backup gegen Konfigurationsfehler, aber kein Schutz gegen Hardware-Defekt. Für wichtige Dienste sollte das Backup auf ein anderes Laufwerk, NAS oder einen zweiten Host.

### Fehler 3: „Der Backup-Job läuft, aber ich habe nie restore getestet"

Dann weißt du nicht, ob dein Backup im Ernstfall reicht. Teste die Wiederherstellung zuerst mit einem kleinen LXC.

### Fehler 4: „Ich sichere zu selten"

Frage dich: Wie viel Arbeit darf ich verlieren? Wenn du eine Woche Konfiguration nicht erneut machen willst, ist ein monatliches Backup zu wenig.

### Fehler 5: „Ich sichere alles, aber dokumentiere nichts"

Notiere mindestens: Was wird gesichert, wohin, wie oft und wann der letzte Restore-Test erfolgreich war. Das reicht für den Anfang.

## FAQ

### Reicht ein Snapshot vor jedem Update?

Für kleine Updates ist ein Snapshot hilfreich. Für wichtige Dienste sollte zusätzlich ein aktuelles Backup vorhanden sein.

### Brauche ich sofort Proxmox Backup Server?

Nicht zwingend für den ersten Lernschritt. Proxmox Backup Server ist ein guter nächster Schritt, wenn mehrere VMs und LXCs regelmäßig gesichert werden sollen. Für den Einstieg zählt zuerst: Backup verstehen, erstellen, wiederherstellen.

### Kann ich auf eine USB-Festplatte sichern?

Als Einstieg ja: Ich verwende eine 1-TB-USB-Festplatte als Backup-Ziel (siehe **[USB-Festplatte als Proxmox-Backup-Ziel einrichten](/preview/blog/proxmox-usb-festplatte-backup-ziel/)**). Die Platte ist per UUID im fstab eingetragen und als Proxmox-Storage eingerichtet. Nicht ideal (Single Point of Failure), aber deutlich besser als nur Snapshots oder Backups auf der System-SSD. Ein NAS oder Proxmox Backup Server ist der nächste sinnvolle Schritt.

### Muss ich jede VM und jeden LXC sichern?

Nein. Sichere zuerst die Dienste, deren Neuaufbau nervig oder zeitkritisch wäre: DNS/Werbeblocker, Home Assistant, Passwortmanager, wichtige Docker-Hosts, zentrale Dashboards.

## Nächster Schritt

Nach diesem Artikel bieten sich zwei Praxisartikel an:

- **„[USB-Festplatte als Proxmox-Backup-Ziel einrichten](/preview/blog/proxmox-usb-festplatte-backup-ziel/)"** – sollte direkt nach dem Grundlagenartikel als Nächstes gelesen werden.
- **„Proxmox Backup Server im Homelab: Lohnt sich ein zweiter Mini-PC?"** – wenn mehrere LXCs regelmäßig gesichert werden sollen.
- Oder als Direkteinstieg: **„Pi-hole oder AdGuard im Proxmox-LXC einrichten"** – mit dem Wissen, vor dem Produktivbetrieb ein Backup zu erstellen.

Im bestehenden Blog findest du passende Einstiegspunkte:

- [Virtualisierung kostenlos: Proxmox als VMware-Alternative](/homelab-blog/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/)
- [Homelab unter 100 Euro: Was du wirklich brauchst](/homelab-blog/posts/homelab-unter-100-euro-was-du-brauchst/)

## ✅ Das solltest du jetzt können

Nach dem Artikel solltest du:

- ✅ den Unterschied zwischen Snapshot und Backup erklären können
- ✅ wissen, warum ein Snapshot kein vollständiges Backup ersetzt
- ✅ ein erstes Proxmox-Backup über die Weboberfläche starten können
- ✅ ein einfaches Backup-Ziel bewusst auswählen können
- ✅ einen Restore-Test mit einem Test-LXC planen können
- ✅ einschätzen können, wann Proxmox Backup Server als nächster Schritt sinnvoll wird

---

**Einrichten wenn:** du erste Dienste im Proxmox-Homelab betreibst und sicherstellen willst, dass sie nach einem Fehler wiederherstellbar sind.  
**Nicht einrichten wenn:** du nur testest und keine Daten zu verlieren hast – aber dann reichen auch Snapshots.
