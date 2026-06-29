#!/usr/bin/env python3
"""Deploy: Generate images -> Claude review -> Publish check -> Interlinking -> Commit -> Push."""
import subprocess, os, time, json, sys

BLOG_DIR = "/root/homelab-blog"
PLACEHOLDER = os.path.join(BLOG_DIR, "static", "images", "placeholder.jpg")

# Pipeline utilities
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from pipeline_utils import log, log_step, save_review, determine_image_status, set_status

with open("/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt") as f:
    token = f.read().strip()

os.chdir(BLOG_DIR)

log("INFO", "=== Blog Pipeline Start ===")

# Step 0: Learning Engine – analysiere vergangene Reviews
le = os.path.join(BLOG_DIR, "learning_engine.py")
if os.path.exists(le):
    subprocess.run(["python3", le], capture_output=True, text=True, timeout=30)

r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
new_lines = [l for l in r.stdout.split("\n") if l.strip()]
new_files = [l.split()[-1] for l in new_lines if "index.md" in l and l.startswith("??")]

if not new_files:
    log("INFO", "No new articles found")
    print("Nothing to deploy")
    sys.exit(0)

for ap in new_files:
    fp = os.path.join(BLOG_DIR, ap)
    if not os.path.exists(fp):
        continue

    slug = os.path.basename(os.path.dirname(fp))
    article_dir = os.path.dirname(fp)
    featured = os.path.join(article_dir, "featured.jpg")

    log_step("PROCESS", "START", f"slug={slug}")

    # ── Step 1: Cover-Bild generieren (non-blocking) ──────────
    image_generated = False
    gen = os.path.join(BLOG_DIR, "generate_image.py")
    if os.path.exists(gen) and not os.path.exists(featured):
        prompt = f"Blog image for: {slug.replace('-', ' ')}. Commercial product photography, single mini PC on dark desk, homelab atmosphere, professional studio lighting, dramatic rim lighting, premium tech review look. Dark background, no people, no logos, no text, no fantasy hardware. Sharp focus."
        log("INFO", f"Generating image for: {slug}")
        result = subprocess.run(["python3", gen, prompt, featured], capture_output=True, text=True, timeout=120)
        if result.returncode == 0 and os.path.exists(featured) and os.path.getsize(featured) > 20000:
            fsize = os.path.getsize(featured)
            log_step("IMAGE", "GENERATED", f"{fsize/1024:.0f} KB")
            image_generated = True
        else:
            # Fallback: Platzhalter
            log_step("IMAGE", "WARNING", "Generation failed, using placeholder")
            log("WARNING", f"Image gen failed for {slug}: {result.stdout.strip()[:100]}")
            if os.path.exists(PLACEHOLDER):
                subprocess.run(["cp", PLACEHOLDER, featured])
                log("INFO", "Placeholder image deployed")

    image_status = determine_image_status(featured, image_generated)
    log("INFO", f"Image status: {image_status}")

    # ── Step 2: Claude Review (consolidated JSON) ───────────
    rev = os.path.join(BLOG_DIR, "claude_review.py")
    review_result = None
    if os.path.exists(rev):
        log("INFO", f"Starting Claude review for: {slug}")
        result = subprocess.run(["python3", rev, fp], capture_output=True, text=True, timeout=180)
        print(result.stdout)
        if result.stderr:
            log("WARNING", f"Review stderr: {result.stderr[:200]}")

        review_path = os.path.join(article_dir, "review_result.json")
        if os.path.exists(review_path):
            with open(review_path) as rf:
                review_result = json.load(rf)

            # Review als Artefakt speichern
            artifact_path = save_review(slug, review_result, image_status)
            if artifact_path:
                log("INFO", f"Review artifact saved: {artifact_path}")

            # Log review results
            log("INFO", f"Claude review: facts_ok={review_result.get('facts_ok')} "
                       f"reader={review_result.get('reader_score')}/10 "
                       f"purchase={review_result.get('purchase_clarity_score')}/10 "
                       f"quality={review_result.get('overall_quality_score')}/10 "
                       f"publish_ready={review_result.get('publish_ready')}")

            # ── Step 3: Publish-Kontrolle (non-blocking quality gate) ──
            publish_ready = review_result.get("publish_ready", True)
            if not publish_ready:
                log_step("PUBLISH", "BLOCKED_FOR_REVIEW", f"Quality={review_result.get('overall_quality_score','?')}/10")
                log("WARNING", f"Article {slug} blocked by quality gate (publish_ready=false)")
                set_status("BLOCKED")
                save_review(slug, review_result, image_status)
                print(f"\n  ⏸ BLOCKED_FOR_REVIEW | Quality: {review_result.get('overall_quality_score', '?')}/10")
                if review_result.get("required_changes"):
                    print(f"     Required changes:")
                    for c in review_result["required_changes"]:
                        print(f"       - {c}")
                print(f"  No deployment. Fix issues and re-run.")
                # Kein sys.exit(1) – sauberer Abbruch
                time.sleep(2)
                continue
            log_step("PUBLISH", "PASS", f"Quality={review_result.get('overall_quality_score','?')}/10")
            time.sleep(2)

# ── Step 4: Interlinking ────────────────────────────────
interlink = os.path.join(BLOG_DIR, "interlink.py")
if os.path.exists(interlink):
    log("INFO", "Running interlinking")
    subprocess.run(["python3", interlink], capture_output=True, text=True)

# ── Step 5: Commit + Push ───────────────────────────────
subprocess.run(["git", "config", "user.email", "matmaksa@users.noreply.github.com"], capture_output=True)
subprocess.run(["git", "config", "user.name", "matmaksa"], capture_output=True)
git_url = f"https://matmaksa:{token}@github.com/matmaksa/homelab-blog.git"
subprocess.run(["git", "remote", "set-url", "origin", git_url], capture_output=True)
subprocess.run(["git", "add", "-A"])
r = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)
if r.returncode != 0:
    subprocess.run(["git", "commit", "-m", "Blog Update"])
    push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    deploy_msg = f"Deployed: https://matmaksa.github.io/homelab-blog/"
    log_step("DEPLOY", "SUCCESS", deploy_msg)
    print(f"\n{deploy_msg}")
else:
    log_step("DEPLOY", "SKIP", "Nothing to commit")
    print("Nothing to commit")

log("INFO", "=== Blog Pipeline End ===")
# Abschliessenden Pipeline-Status setzen falls nicht bereits gesetzt
from pipeline_utils import PIPELINE_STATUS
if PIPELINE_STATUS == "RUNNING":
    set_status("COMPLETED")
