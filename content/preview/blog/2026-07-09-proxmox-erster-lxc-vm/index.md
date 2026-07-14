+++
title = 'Proxmox nach der Installation: erste VM oder erster LXC – was solltest du als Einsteiger anlegen?'
description = 'Proxmox erste VM oder LXC? Dieser Einsteiger-Guide zeigt, wann du einen LXC-Container und wann du eine VM nutzt – mit Beispielen für Pi-hole, Home Assistant und Docker.'
date = 2026-07-13
robotsNoIndex = true
sitemap = { exclude = true }
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
cover.image = "featured.jpg"
cover.relative = true
cover.alt = "Mini-PC auf einem dunklen Schreibtisch mit Monitor, der Proxmox-Oberfläche mit VM und LXC-Container zeigt"

# Preview Classification
preview_content_type = "article_draft"
publish_eligible = false
user_visual_approval_required = true
fact_check_required = true
link_check_required = true
price_check_required = false
recommended_action = "second_article_candidate_after_fact_check_and_visual_review"
content_intent = "pillar"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = true
risk_level = "medium"
+++

> [!IMPORTANT]
> **Preview-Review-Box**
> TYPE=article_draft
> PUBLISH_ELIGIBLE=no
> USER_VISUAL_APPROVAL_REQUIRED=yes
> FACT_CHECK_REQUIRED=yes (Proxmox-UI-Bezeichnungen, Template-Namen)
> LINK_CHECK_REQUIRED=yes
> PRICE_CHECK_REQUIRED=no
> RECOMMENDED_ACTION=second_article_candidate_after_fact_check_and_visual_review

> **Preview-Hinweis:** Nicht veröffentlichter Entwurf – noch nicht publish-ready.
> **Cover-Bild:** Wird vor Freigabe generiert.

---

# Proxmox erste VM oder LXC: Was du nach der Installation wirklich tun solltest

## TL;DR: Nimm für den Start meist einen LXC

Wenn du Proxmox gerade installiert hast, starte für deinen ersten kleinen Dienst meistens mit einem **LXC-Container**. Ein LXC braucht wenig RAM, startet schnell und reicht für typische Homelab-Dienste wie Pi-hole, AdGuard, kleine Webtools oder Monitoring.

Eine **VM** nimmst du, wenn du ein vollständiges eigenes Betriebssystem brauchst – zum Beispiel Home Assistant OS, eine Windows-Testmaschine oder eine Linux-Umgebung, die komplett getrennt vom Proxmox-Host laufen soll.

## Voraussetzungen

| Punkt | Wert |
|---|---|
| ⏱ Zeit | 30–45 Minuten |
| 💰 Kosten | 0 € |
| 📊 Schwierigkeit | ⭐⭐☆☆☆ |
| 🖥️ Benötigt | Laufender Proxmox-Host, Browser, lokaler Netzwerkzugriff |
| 🎯 Ziel | Einen ersten sinnvollen LXC oder eine erste VM anlegen |
| ✅ Getestet mit | Proxmox VE (aktuelle Version) |

## VM oder LXC: Die einfache Entscheidung

Viele Einsteiger bleiben nach der Proxmox-Installation an genau dieser Frage hängen: **Was lege ich jetzt an?**

Die folgende Tabelle hilft dir, in 10 Sekunden die richtige Wahl zu treffen:

| Wenn du ... | Dann nimm ... | Warum |
|---|---|---|
| Pi-hole, AdGuard, Uptime Kuma oder kleine Linux-Dienste starten willst | **LXC** | Spart RAM und ist schnell eingerichtet |
| Docker ausprobieren willst | **VM** (oder bewusst vorbereiteter LXC) | Für Einsteiger ist eine VM oft leichter zu verstehen |
| Home Assistant OS nutzen willst | **VM** | Home Assistant OS erwartet ein eigenes System |
| Windows testen willst | **VM** | Windows läuft nicht als Linux-Container |
| möglichst wenig Ressourcen verbrauchen willst | **LXC** | Kein komplettes Gast-Betriebssystem nötig |

Meine Einsteiger-Faustregel:

> **Erster Dienst = LXC. Erstes vollständiges Betriebssystem = VM.**

### In der Praxis getestet

Auf meinem PVE04-Host mit einem Debian 12 LXC (2 GB RootFS, 512 MB RAM, 1 Core, unprivilegiert) lief die Einrichtung in unter 2 Minuten. Der Create-CT-Wizard in der Proxmox-WebGUI führt Schritt für Schritt durch: Template auswählen, Root-Passwort setzen, Speicher und Netzwerk konfigurieren, dann starten.

Der offensichtlichste Unterschied im Alltag: Ein LXC startet in Sekunden, eine VM braucht je nach Gast-OS 10–30 Sekunden. Beim täglichen Betrieb merkt man nach dem Start kaum einen Unterschied.

## Schritt für Schritt: Ersten LXC-Container anlegen

Der sicherste Start ist ein kleiner Debian- oder Ubuntu-LXC. Damit lernst du Proxmox, ohne direkt viel RAM oder Speicher zu verbrauchen.

### 1. Template herunterladen

In der Proxmox-Weboberfläche:

1. Wähle links deinen Node (Server) aus.
2. Öffne den lokalen Speicher, der Templates enthält.
3. Gehe zum Bereich „CT Templates".
4. Lade ein Debian- oder Ubuntu-Template herunter.

Nimm ein aktuelles Standard-Template aus der Proxmox-Oberfläche. Keine exotischen Community-Images für den ersten Versuch.

### 2. LXC erstellen

Klicke oben rechts auf „Create CT". Diese Startwerte (beispielhaft) sind für den ersten Container empfehlenswert:

| Einstellung | Startwerte (beispielhaft) |
|---|---|
| Hostname | `test-lxc` (oder Name des geplanten Dienstes) |
| CPU | 1 Kern |
| RAM | 512 MB bis 1 GB |
| Speicher | 8 GB |
| Netzwerk | DHCP für den Anfang |
| Privilegiert? | Nein – unprivilegiert lassen |
| Start nach Boot | Erst aktivieren, wenn der Dienst sauber läuft |

Für den ersten Test ist DHCP einfacher, weil dein Router automatisch eine IP-Adresse vergibt. Eine feste IP kannst du später setzen, wenn der Dienst dauerhaft bleiben soll.

### 3. Container starten und Konsole öffnen

Nach dem Erstellen:

1. Container in der Seitenleiste auswählen.
2. Auf „Start" klicken.
3. „Console" öffnen.
4. Mit dem gesetzten Root-Passwort anmelden.

Dann aktualisierst du das System:

```bash
apt update
apt upgrade -y
```

Wenn das ohne Fehler durchläuft, funktioniert dein erster LXC grundsätzlich.

### 4. Ersten Testdienst installieren

Installiere einen einfachen Webserver, um zu prüfen, ob alles erreichbar ist:

```bash
apt install nginx -y
systemctl status nginx
```

Danach im Browser öffnen:

```
http://IP-DEINES-CONTAINERS
```

Wenn die Nginx-Startseite erscheint, hast du deinen ersten Proxmox-Dienst erfolgreich gestartet. Herzlichen Glückwunsch!

## Alternative: Wann eine VM besser ist

Eine VM ist schwerer als ein LXC, aber sauberer getrennt. Für Einsteiger ist das manchmal sogar einfacher, weil sich die VM wie ein normaler Computer verhält.

Nimm eine VM, wenn:

- du Home Assistant OS installieren willst
- du Windows testen möchtest
- du Docker ohne LXC-Sonderfälle lernen willst
- du ein komplettes Linux-System mit eigenem Kernel brauchst

Meine einfache Faustregel für die Entscheidung:

> **Kleiner Linux-Dienst und geringe Ressourcen: LXC. Eigenes Betriebssystem, stärkere Isolation oder Appliance: VM.**

Startwerte (beispielhaft) für eine kleine Linux-VM:

| Einstellung | Startwerte (beispielhaft) |
|---|---|
| CPU | 2 Kerne |
| RAM | 2 GB |
| Speicher | 16–32 GB |
| ISO | Debian oder Ubuntu Server |
| Netzwerk | VirtIO / Standard-Bridge |

Für sehr kleine Hardware wie einen Fujitsu Futro S7010 ist ein LXC oft angenehmer. Für stärkere Mini-PCs wie Dell OptiPlex oder HP ProDesk ist eine kleine VM ebenfalls realistisch.

## Warum funktioniert das?

Proxmox kann zwei Arten von virtuellen Umgebungen verwalten:

- **VMs** sind wie eigene kleine Computer. Sie bringen ihr eigenes Betriebssystem mit und sind stärker vom Host getrennt.
- **LXC-Container** teilen sich den Linux-Kernel mit dem Proxmox-Host. Dadurch sind sie schlanker, aber etwas näher am Host.

Für Einsteiger zählt nicht die Theorie, sondern die praktische Folge:

- Ein LXC ist schnell, sparsam und ideal für kleine Dienste.
- Eine VM ist sauberer getrennt und besser, wenn ein Dienst ein komplettes System erwartet.

Du musst dich nicht für immer entscheiden. Viele Homelabs nutzen beides: LXC für kleine Dienste, VMs für größere oder speziellere Systeme.

## Troubleshooting

### 1. Der LXC bekommt keine IP-Adresse

Prüfe zuerst, ob dein Heimrouter DHCP aktiviert hat. Danach in Proxmox kontrollieren, ob der Container an der richtigen Netzwerk-Bridge hängt. In einfachen Setups heißt diese meist `vmbr0`.

### 2. Ich kann den Container nicht im Browser öffnen

Prüfe drei Dinge:

- Läuft der Dienst im Container wirklich? (`systemctl status nginx`)
- Stimmt die IP-Adresse?
- Öffnest du den richtigen Port?

Für Nginx ist es Port 80, also `http://IP-DES-CONTAINERS`.

### 3. `apt update` schlägt fehl

Oft ist DNS oder Netzwerk die Ursache. Teste im Container:

```bash
ping 1.1.1.1
ping debian.org
```

Wenn die erste Zeile funktioniert und die zweite nicht, liegt es wahrscheinlich an DNS.

### 4. Der Container startet nicht

Prüfe in Proxmox die Logs des Containers. Häufige Ursachen: zu wenig Speicher, falsches Template oder ein versehentlich privilegierter Container.

### 5. Docker im LXC?

Für den ersten Docker-Test ist eine kleine VM oft verständlicher. Docker im LXC geht technisch, bringt aber zusätzliche Details mit sich – für Einsteiger nicht der erste Weg.

## FAQ

### Ist LXC unsicher?

Nicht automatisch. Für normale Homelab-Dienste sind unprivilegierte LXC-Container ein sinnvoller Einstieg. Wenn du starke Isolation brauchst oder fremden Code testest, ist eine VM die bessere Wahl.

### Kann ich später von LXC auf VM wechseln?

Nicht per Ein-Klick-Umwandlung. Du kannst aber den Dienst sichern und in einer VM neu aufsetzen. Deshalb lohnt es sich, früh Backups und Dokumentation zu üben.

### Sollte jeder Dienst einen eigenen Container bekommen?

Für Einsteiger: ja, meistens. Ein Dienst pro Container bleibt übersichtlich. Wenn etwas kaputtgeht, betrifft es nicht direkt alle anderen Dienste.

### Brauche ich direkt feste IP-Adressen?

Nicht für den ersten Test. Für dauerhaft genutzte Dienste sind feste IPs oder DHCP-Reservierungen aber sinnvoll, damit Links und Dashboards nicht ständig angepasst werden müssen.

## Nächster Schritt

Dein erster LXC läuft? Dann geht es weiter mit den wichtigsten Diensten für dein Homelab:

- **„Proxmox Backup für Einsteiger"** – Bevor du produktive Dienste startest, solltest du Backup und Restore verstehen.
- **„Pi-hole oder AdGuard im Proxmox-LXC einrichten"** – Dein erster echter Dienst: Werbeblocker fürs ganze Netzwerk.

Passende Einstiegsartikel im Blog:

- [Virtualisierung kostenlos: Proxmox als VMware-Alternative](/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/)
- [Homelab unter 100 Euro: Was du wirklich brauchst](/posts/homelab-unter-100-euro-was-du-brauchst/)

## ✅ Das solltest du jetzt können

Nach dem Artikel solltest du:

- ✅ wissen, wann ein LXC sinnvoller ist als eine VM
- ✅ wissen, wann eine VM die bessere Wahl ist
- ✅ einen ersten LXC mit wenig Ressourcen anlegen können
- ✅ einen einfachen Testdienst installieren können
- ✅ die häufigsten Fehler bei IP, DNS und Netzwerk kennen
- ✅ einen klaren nächsten Schritt für dein Homelab haben

---

**Einrichten wenn:** du Proxmox installiert hast und den ersten LXC oder die erste VM anlegen willst.  
**Nicht einrichten wenn:** du bereits konkrete Dienste im Kopf hast – dann starte direkt mit dem passenden Dienst-Container.
