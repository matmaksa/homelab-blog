#!/usr/bin/env python3
"""Deploy: Generate images -> Claude review (w/ DB fact-check) -> Interlinking -> Commit -> Push."""
import subprocess, os, time, sys

BLOG_DIR = "/root/homelab-blog"

with open("/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt") as f:
    token = f.read().strip()

os.chdir(BLOG_DIR)

r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
new_files = [l.split()[-1] for l in r.stdout.split("\n") if l.strip() and "index.md" in l and l.startswith("??")]

if new_files:
    for ap in new_files:
        fp = os.path.join(BLOG_DIR, ap)
        if not os.path.exists(fp):
            continue

        slug = os.path.basename(os.path.dirname(fp))
        article_dir = os.path.dirname(fp)
        featured = os.path.join(article_dir, "featured.jpg")

        gen = os.path.join(BLOG_DIR, "generate_image.py")
        if os.path.exists(gen):
            if not os.path.exists(featured):
                prompt = "Blog image for: " + slug.replace("-", " ") + ". Modern tech, clean product photography style."
                result = subprocess.run(["python3", gen, prompt, featured], capture_output=True, text=True, timeout=120)
                if result.returncode == 0:
                    print(f"  ✅ Image -> featured.jpg ({slug})")
                else:
                    print(f"  ⚠️  Image gen failed: {result.stderr.strip()[:200]}")

        rev = os.path.join(BLOG_DIR, "claude_review.py")
        if os.path.exists(rev):
            print(f"📤 Running Claude review (w/ device DB fact-check)...")
            result = subprocess.run(["python3", rev, fp], capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(f"  ⚠️  Review stderr: {result.stderr[:300]}")
            time.sleep(2)

    # STEP 2: Interlinking - update existing + new articles
    il = os.path.join(BLOG_DIR, "interlink.py")
    if os.path.exists(il):
        print(f"🔗 Running interlinking...")
        result = subprocess.run(["python3", il], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"  ⚠️  Interlink stderr: {result.stderr[:300]}")

subprocess.run(["git", "config", "user.email", "makmatas@users.noreply.github.com"], capture_output=True)
subprocess.run(["git", "config", "user.name", "makmatas"], capture_output=True)
git_url = "https://makmatas:" + token + "@github.com/makmatas/homelab-blog.git"
subprocess.run(["git", "remote", "set-url", "origin", git_url], capture_output=True)
subprocess.run(["git", "add", "-A"])
r = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)
if r.returncode != 0:
    subprocess.run(["git", "commit", "-m", "Blog Update"])
    push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    print("✅ Deployed: https://makmatas.github.io/homelab-blog/")
else:
    print("ℹ️  Nothing to commit")
