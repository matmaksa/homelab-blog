#!/bin/bash
set -e

BLOG_DIR="/root/homelab-blog"
GH_USER="makmatas"
GH_REPO="homelab-blog"
TOKEN_FILE="/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt"

cd "$BLOG_DIR"

GH_TOKEN=$(cat "$TOKEN_FILE")

git config user.email "makmatas@users.noreply.github.com" 2>/dev/null || true
git config user.name "makmatas" 2>/dev/null || true

git remote set-url origin "https://${GH_USER}:${GH_TOKEN}@github.com/${GH_USER}/${GH_REPO}.git"

git add -A
if ! git diff --cached --quiet; then
  git commit -m "Blog Update: $(date +%Y-%m-%d_%H:%M)"
  git push origin main
  echo "OK Deployed to: https://${GH_USER}.github.io/${GH_REPO}/"

  # ── Search Engine Pings ──
  SITEMAP="https://${GH_USER}.github.io/${GH_REPO}/sitemap.xml"
  INDEXNOW_KEY="4d6302cc551849e2a4cdd84223a1b2f1"

  echo "Pinging Google..."
  curl -s -o /dev/null -w "Google: %{http_code}\n" "https://www.google.com/ping?sitemap=${SITEMAP}"

  # Neue Artikel erkennen und an IndexNow melden
  for f in $(git diff --name-only HEAD~1 HEAD 2>/dev/null | grep '/index.md$' || echo ""); do
    slug=$(basename "$(dirname "$f")")
    article_url="https://${GH_USER}.github.io/${GH_REPO}/posts/${slug}/"
    curl -s -o /dev/null -w "IndexNow ${slug}: %{http_code}\n" \
      "https://www.bing.com/indexnow?url=${article_url}&key=${INDEXNOW_KEY}"
  done
  echo "Search engine pings done."
else
  echo "Nothing to commit"
fi
