+++
title = "Preview – Entwürfe"
description = "Nicht veröffentlichte Vorschau-Artikel und Instagram-Beiträge"
robotsNoIndex = true
sitemap = { exclude = true }

[cascade]
  robotsNoIndex = true
  
  [cascade.sitemap]
    exclude = true
  
  preview = true
  draft_banner = true
  hideMeta = true
  ShowShareButtons = false
  ShowPostNavLinks = false
  comments = false
  editPost = []
+++

# Preview – was als Nächstes kommt

Diese Seite bündelt nicht veröffentlichte Vorschauen zur Prüfung.  
Sie sind nicht für die Veröffentlichung freigegeben und werden von Suchmaschinen ausgeschlossen.

## Bereiche

- [Blog-Entwürfe und Review-Drafts](/homelab-blog/preview/blog/)
- [Instagram-Preview-Beiträge](/homelab-blog/preview/insta/)

## Direkte Struktur

- `/preview/blog/<artikel>/` – lesbare Blog-Entwürfe mit Text, Format und ggf. Bildern
- `/preview/insta/<beitrag>/` – Instagram-Carousels/Reels als visuelle Vorschau
