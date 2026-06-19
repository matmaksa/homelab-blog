#!/usr/bin/env python3
"""
Interlinking-Script: Fügt automatisch interne Links zwischen Artikeln ein.
Liest alle vorhandenen Artikel, findet relevante Verknüpfungen
und fügt einen "Weiterführende Artikel"-Block vor dem Fazit ein.

Usage: python3 interlink.py                                        # alle Artikel aktualisieren
       python3 interlink.py /pfad/zu/neuem/artikel/index.md         # nur neuen Artikel verlinken
"""
import os, re, sys, json

BLOG_DIR = "/root/homelab-blog"
CONTENT_DIR = os.path.join(BLOG_DIR, "content", "posts")

def find_all_articles():
    """Find all article index.md files and extract metadata."""
    articles = []
    if not os.path.exists(CONTENT_DIR):
        return articles
    for root, dirs, files in os.walk(CONTENT_DIR):
        if "index.md" in files:
            path = os.path.join(root, "index.md")
            try:
                with open(path) as f:
                    content = f.read()
            except Exception:
                continue

            # Extract YAML frontmatter
            title_match = re.search(r"^title:\s*\"(.+?)\"", content, re.MULTILINE)
            title = title_match.group(1) if title_match else os.path.basename(root)

            # Extract tags
            tags = []
            in_tags = False
            for line in content.split("\n"):
                if line.strip() == "tags:":
                    in_tags = True
                    continue
                if in_tags:
                    m = re.match(r"\s*-\s*(.+)", line)
                    if m:
                        tags.append(m.group(1).strip().strip('"'))
                    else:
                        in_tags = False

            # Get slug from directory name
            slug = os.path.basename(root)

            # Convert slug to URL
            url = f"/posts/{slug}/"

            articles.append({
                "path": path,
                "title": title,
                "slug": slug,
                "url": url,
                "tags": tags,
                "content": content,
                "dir": root,
            })
    return articles

def build_keyword_map(articles):
    """Build a map of keywords -> relevant articles for matching."""
    # Key technical terms that indicate relevance
    keyword_map = {}
    for article in articles:
        title_lower = article["title"].lower()
        slug_lower = article["slug"].lower()
        tags_lower = [t.lower() for t in article["tags"]]

        # Extract main keywords from title and tags
        keywords = set()
        keywords.update(tags_lower)

        # Add device/model names
        device_models = re.findall(
            r"(hp prodesk|dell optiplex|lenovo (thinkcentre|tiny)|fujitsu (futro|s740|s7010)"
            r"|minisforum|gmktec|proxmox|virtualisierung|docker|pi-hole|home assistant"
            r"|nuc|mini.?pc|1l.?pc|thin client|gebraucht|neugerät|kaufberatung|vergleich)",
            title_lower + " " + slug_lower
        )
        for dm in device_models:
            if isinstance(dm, tuple):
                keywords.update(d for d in dm if d)
            else:
                keywords.add(dm)

        keyword_map[article["slug"]] = keywords
    return keyword_map

def find_relevant_links(article, all_articles, keyword_map, max_links=5):
    """Find other articles that are relevant to this article."""
    title_lower = article["title"].lower()
    content_lower = article["content"].lower()[:2000]  # Check first 2000 chars
    article_keywords = keyword_map.get(article["slug"], set())

    scored = []
    for other in all_articles:
        if other["slug"] == article["slug"]:
            continue  # Skip self

        score = 0
        other_title_lower = other["title"].lower()
        other_content_lower = other["content"].lower()[:2000]

        # 1. Shared tags
        article_tags = set(t.lower() for t in article["tags"])
        other_tags = set(t.lower() for t in other["tags"])
        shared_tags = article_tags & other_tags
        score += len(shared_tags) * 10

        # 2. Title contains other article's device name
        for kw in keyword_map.get(other["slug"], set()):
            if kw in content_lower:
                score += 5
            if kw in title_lower:
                score += 8

        # 3. Cross-reference: other article mentions this article's device
        for kw in article_keywords:
            if kw in other_title_lower:
                score += 6

        # 4. "Vergleich" / "vs" in both titles
        if "vergleich" in title_lower and "vergleich" in other_title_lower:
            score += 3
        if "kaufberatung" in title_lower and "kaufberatung" in other_title_lower:
            score += 3

        # 5. Tutorial -> Hardware (or vice versa)
        tutorial_keywords = {"installation", "einrichten", "setup", "howto", "anleitung", "tutorial"}
        hardware_keywords = {"kaufberatung", "vergleich", "review", "besten", "empfehlung", "mini-pc"}
        is_tutorial = bool(tutorial_keywords & article_tags)
        is_hardware = bool(hardware_keywords & article_tags)
        other_is_tutorial = bool(tutorial_keywords & other_tags)
        other_is_hardware = bool(hardware_keywords & other_tags)
        if (is_tutorial and other_is_hardware) or (is_hardware and other_is_tutorial):
            score += 4

        if score > 0:
            scored.append((score, other))

    scored.sort(reverse=True)
    return [s[1] for s in scored[:max_links]]

def has_interlinks(content):
    """Check if article already has a 'Weiterführende Artikel' section."""
    return "Weiterführende Artikel" in content or "Weiterlesen" in content or "Empfohlene Artikel" in content

def find_fazit_position(content):
    """Find the position of the Fazit section to insert links before it."""
    # Check for various section markers
    patterns = [
        r"^## Fazit",
        r"^## Zusammenfassung",
        r"^\*Als Amazon-Partner",
        r"^---\s*$",
    ]
    # Find the last relevant position - want to insert before the affiliate disclaimer
    affiliate_pattern = r"\*Als Amazon-Partner"
    m = re.search(affiliate_pattern, content, re.MULTILINE)
    if m:
        return m.start()

    # Otherwise find last ## section (Fazit)
    for pattern in patterns:
        m = re.search(pattern, content, re.MULTILINE)
        if m:
            return m.start()
    return len(content)

def insert_interlinks(content, links, base_url="/homelab-blog"):
    """Insert 'Weiterführende Artikel' section before the Fazit."""
    if not links:
        return content

    link_section = "\n\n---\n\n## Weiterführende Artikel\n\n"
    for link in links:
        full_url = f"{base_url}{link['url']}" if base_url else link['url']
        tag_match = ",".join(link.get("tags", [])[:2])
        if tag_match:
            link_section += f"- 🔗 [{link['title']}]({full_url}) — *(Thema: {tag_match})*\n"
        else:
            link_section += f"- 🔗 [{link['title']}]({full_url})\n"
    link_section += "\n"

    pos = find_fazit_position(content)
    return content[:pos] + link_section + content[pos:]

def process_article(article_path=None):
    """Process articles and add interlinks."""
    all_articles = find_all_articles()

    if not all_articles:
        print("⚠️  No articles found")
        return

    keyword_map = build_keyword_map(all_articles)
    base_url = "/homelab-blog"  # GitHub Pages subdirectory

    if article_path:
        # Process only the specified article
        targets = [a for a in all_articles if a["path"] == article_path]
    else:
        # Process all articles that don't have interlinks yet
        targets = [a for a in all_articles if not has_interlinks(a["content"])]

    if not targets:
        print("✅ All articles already have interlinks")
        return

    updated = 0
    for article in targets:
        links = find_relevant_links(article, all_articles, keyword_map)
        if not links:
            print(f"  ⏭️  {article['slug']}: no relevant links found")
            continue

        new_content = insert_interlinks(article["content"], links, base_url)
        if new_content != article["content"]:
            with open(article["path"], "w") as f:
                f.write(new_content)
            print(f"  ✅ {article['slug']}: {len(links)} interlinks added → {[l['slug'] for l in links]}")
            updated += 1
        else:
            print(f"  ⏭️  {article['slug']}: no changes needed")

    print(f"\n📊 {updated}/{len(targets)} articles updated with interlinks")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_article(os.path.abspath(sys.argv[1]))
    else:
        process_article()
