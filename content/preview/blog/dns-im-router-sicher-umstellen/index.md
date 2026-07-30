+++
title = "DNS im Router sicher umstellen: Pi-hole oder AdGuard Home ohne Netzausfall nutzen"
description = "So stellst du einen DNS-Werbeblocker im Heimnetz sicher bereit: erst mit einem einzelnen Gerät testen, Ausfallrisiken verstehen und erst dann die Router-Einstellung ändern."
date = 2026-07-30
draft = false
robotsNoIndex = true
noindex = true
preview = true
draft_banner = true
hideMeta = true
ShowShareButtons = false
ShowPostNavLinks = false
comments = false
tags = ["dns", "router", "pihole", "adguard-home", "homelab", "einsteiger"]
categories = ["Netzwerk", "Software"]

[sitemap]
  exclude = true

# Preview Classification
preview_content_type = "article_draft"
publish_eligible = false
user_visual_approval_required = true
fact_check_required = true
link_check_required = true
price_check_required = false
recommended_action = "Router-spezifische Menüwege und Fallback-DNS vor einer Veröffentlichung prüfen; anschließend visuelle Eigentümerfreigabe einholen."
content_intent = "follow_up"
monetization_intent = "none"
affiliate_disclosure_required = false
price_research_required = false
product_recommendation_allowed = false
instagram_derivatives_required = false
risk_level = "medium"
content_state = "draft_generated"
audit_status = "not_started"
user_approval_required = true
approved_for_publish = false
next_action = "technical_factcheck_and_owner_review_before_publish"
+++

> **Preview – noch nicht veröffentlicht.** Dieser Entwurf erklärt das sichere Vorgehen allgemein. Router-Menünamen und das konkrete Heimnetz werden vor einer Veröffentlichung separat geprüft.

# DNS im Router sicher umstellen: Pi-hole oder AdGuard Home ohne Netzausfall nutzen

## Kurzantwort

Stelle Pi-hole oder AdGuard Home **nicht als Erstes im ganzen Router ein**. Teste den DNS-Server zunächst an genau einem Rechner oder Smartphone. Erst wenn Webseiten, Apps und die Verwaltung zuverlässig funktionieren, trägst du ihn im Router ein.

Der Grund: Wenn der einzige DNS-Server ausfällt, können Geräte Namen wie `example.com` nicht mehr auflösen. Das fühlt sich für viele Geräte wie ein Internetausfall an, obwohl die Internetverbindung selbst noch vorhanden sein kann.

| | |
|---|---|
| **⏱ Zeit** | 20–30 Minuten inklusive Test |
| **💰 Kosten** | 0 € bei bereits vorhandenem DNS-Server |
| **📊 Schwierigkeit** | ⭐⭐☆☆☆ |
| **🖥️ Benötigt** | Router, ein laufendes Pi-hole oder AdGuard Home, ein Testgerät |
| **🎯 Ziel** | DNS-Werbeblocker sicher für das Heimnetz aktivieren |
| **✅ Grundlage** | Testablauf mit isoliertem DNS-Lab; keine produktive Routerumstellung im zugrunde liegenden Test |

## 1. Was ändert sich im Router überhaupt?

**DNS** ist das Telefonbuch deines Netzwerks. Wenn du eine Webadresse eingibst, fragt dein Gerät einen DNS-Server nach der passenden Internetadresse. Normalerweise übernimmt diese Aufgabe dein Router oder ein öffentlicher Anbieter.

Mit Pi-hole oder AdGuard Home verwendest du stattdessen einen eigenen DNS-Server im Heimnetz. Er beantwortet normale Anfragen und kann bekannte Werbe- oder Tracking-Domains blockieren.

Wichtig: Die Einstellung im Router verteilt den neuen DNS-Server oft an **alle Geräte** im Heimnetz. Deshalb ist sie kein sinnvoller erster Testschritt.

## 2. Die Begriffe, die du kennen musst

- **Primärer DNS-Server:** Die erste Adresse, die Geräte für DNS-Anfragen verwenden.
- **Sekundärer DNS-Server:** Eine zusätzliche Adresse für den Fall, dass der erste Server nicht erreichbar ist. Manche Geräte verwenden ihn aber auch parallel; dadurch kann Blocking teilweise umgangen werden.
- **DHCP:** Die Router-Funktion, die Geräten automatisch Netzwerkeinstellungen zuweist.
- **Fallback-DNS:** Ein bewusst vorbereiteter Rückweg für den Fall, dass der eigene DNS-Dienst nicht funktioniert.

> **Wichtig:** Ein zweiter öffentlicher DNS-Server ist kein neutraler Notfallknopf. Je nach Gerät kann er dazu führen, dass Anfragen am Werbeblocker vorbeigehen. Plane deshalb bewusst, wie du einen Ausfall behebst, statt unüberlegt eine beliebige zweite Adresse einzutragen.

## 3. Vor dem Test: Rückweg vorbereiten

Bevor du etwas im Router änderst, notiere die aktuellen DNS-Einstellungen. Ein Foto der Router-Seite oder eine kurze Notiz genügt. So kannst du sie bei Problemen wiederherstellen.

Prüfe außerdem:

- [ ] Der DNS-Container oder -Server startet nach einem Neustart zuverlässig.
- [ ] Die Verwaltungsoberfläche ist nur im lokalen Netz erreichbar und geschützt.
- [ ] Du weißt, wie du den DNS-Server lokal wieder auf die bisherige Einstellung zurückstellst.
- [ ] Du testest nicht während einer Videokonferenz, eines Updates oder anderer wichtiger Nutzung.
- [ ] Du hast ein Gerät, das während des Tests weiterhin die bisherigen Router-Einstellungen nutzt.

## 4. Zuerst nur ein Gerät testen

Nimm einen Rechner oder ein Smartphone als Testgerät. Trage dort **vorübergehend** die lokale Adresse deines Pi-hole- oder AdGuard-Home-Servers als DNS-Server ein. Die genaue Stelle heißt je nach Betriebssystem zum Beispiel „DNS-Server“, „DNS konfigurieren“ oder „Manuell“.

Lass alle anderen Geräte unverändert. So bleibt dein Heimnetz nutzbar, falls der Test nicht klappt.

Danach prüfst du auf dem Testgerät:

1. Öffne mehrere normale Webseiten.
2. Teste eine App, die du regelmäßig nutzt.
3. Prüfe in Pi-hole oder AdGuard Home, ob Anfragen ankommen.
4. Öffne eine Seite mit Werbung und kontrolliere, ob die Blockliste erwartungsgemäß greift.
5. Starte den DNS-Dienst nur dann neu, wenn du weißt, wie du bei Problemen zurückwechselst; danach erneut testen.

Ein einzelner erfolgreicher Seitenaufruf reicht nicht. Ziel ist, dass normale Nutzung, Namensauflösung und Verwaltung zusammen funktionieren.

## 5. Was du bei Problemen zuerst prüfst

| Symptom | Wahrscheinliche Ursache | Sicherer erster Schritt |
|---|---|---|
| Keine Webseiten öffnen | DNS-Server nicht erreichbar oder falsche Adresse | Am Testgerät wieder die bisherigen DNS-Einstellungen aktivieren |
| Manche Webseiten gehen, andere nicht | Filterliste blockiert zu viel | Betroffene Domain im Query Log prüfen; keine ganze Filterliste blind deaktivieren |
| Verwaltung nicht erreichbar | Falsche lokale Adresse, Dienst nicht gestartet oder Browser-Problem | Erst lokale Erreichbarkeit prüfen; Router nicht ändern |
| Werbung ist weiter sichtbar | DNS-Blocking entfernt keine Werbung, die direkt von der gleichen Domain wie der Inhalt kommt | Nicht als Fehler werten; Cosmetic Filtering ist eine Browser-Funktion, keine DNS-Funktion |

## 6. Erst jetzt im Router eintragen

Wenn der Test mit einem einzelnen Gerät stabil war, kannst du die DNS-Einstellung im Router ändern. Die Bezeichnungen unterscheiden sich je nach Hersteller, etwa „Lokaler DNS-Server“, „DHCP-DNS“, „DNSv4-Server“ oder „Netzwerkeinstellungen“.

Arbeite dabei langsam:

1. Notiere die vorhandenen Einstellungen erneut.
2. Trage nur die lokale Adresse deines getesteten DNS-Servers ein.
3. Speichere die Änderung.
4. Warte, bis ein Testgerät eine neue Netzwerkverbindung aufgebaut hat.
5. Prüfe wieder normale Webseiten, Apps und die DNS-Verwaltung.
6. Kontrolliere erst danach weitere Geräte.

> **Kein Router-Menüweg in diesem Entwurf:** Die Oberfläche ist je nach Router und Firmware unterschiedlich. Vor Veröffentlichung braucht dieser Abschnitt einen Faktencheck für die unterstützten Router-Modelle, statt allgemeine Menünamen als verbindliche Anleitung auszugeben.

## 7. Was passiert bei einem DNS-Ausfall?

Fällt der einzige DNS-Server aus, verlieren viele Geräte die Übersetzung von Webadressen. Die WLAN-Verbindung kann dabei weiterhin „verbunden“ anzeigen, während Webseiten nicht laden.

Für den Ernstfall brauchst du einen einfachen Ablauf:

1. Prüfe, ob Pi-hole oder AdGuard Home läuft.
2. Stelle am Router oder am betroffenen Gerät die vorherigen DNS-Einstellungen wieder her.
3. Prüfe, ob normale Webseiten wieder laden.
4. Suche erst danach in Ruhe nach der Ursache des DNS-Ausfalls.

Das ist kein Grund, auf einen DNS-Werbeblocker zu verzichten. Es ist ein Grund, den Rückweg vorab zu kennen.

## 8. Sicherheit der Weboberfläche

Die DNS-Verwaltung zeigt unter Umständen an, welche Domains Geräte im Netz angefragt haben. Sie gehört deshalb nicht ins öffentliche Internet.

- Verwende ein starkes eigenes Passwort für die Verwaltungsoberfläche.
- Erlaube den Zugriff nur aus deinem lokalen Netz oder über einen bewusst eingerichteten sicheren Fernzugang.
- Teile keine Screenshots mit lokalen Adressen, Gerätenamen oder Query-Logs ungeprüft.
- Aktualisiere Pi-hole oder AdGuard Home kontrolliert und teste nach Updates die Namensauflösung.

## FAQ

**Soll ich einen öffentlichen zweiten DNS-Server als Fallback eintragen?**

Nur, wenn du die Folgen verstehst. Manche Geräte fragen ihn parallel und umgehen dann den Werbeblocker. Für Einsteiger ist ein dokumentierter Rückweg zur alten Router-Einstellung oft klarer.

**Muss ich jedes Gerät einzeln konfigurieren?**

Nein. Nach einem erfolgreichen Einzelgerät-Test kann der Router die DNS-Einstellung meist per DHCP an Geräte verteilen.

**Blockt DNS jede Werbung?**

Nein. DNS kann bekannte Werbe- und Tracking-Domains blockieren. Das optische Entfernen von Werbeflächen im Browser erledigen Browser-Erweiterungen oder Inhaltsfilter, nicht ein reiner DNS-Server.

## ✅ Das solltest du jetzt können

- [ ] Erklären, warum ein DNS-Test zuerst nur auf einem Gerät stattfindet.
- [ ] Die bisherigen Router-DNS-Einstellungen sichern.
- [ ] Pi-hole oder AdGuard Home auf einem Testgerät prüfen.
- [ ] Einen DNS-Ausfall von einem kompletten Internet-Ausfall unterscheiden.
- [ ] Die Router-Änderung erst nach einem erfolgreichen Einzelgerät-Test durchführen.

## Nächster Schritt

Nach der DNS-Umstellung ist ein getestetes Backup wichtig. Der geplante Folgeartikel erklärt, wie eine USB-Festplatte als separates Proxmox-Backup-Ziel eingerichtet und ein Restore-Test durchgeführt wird.
