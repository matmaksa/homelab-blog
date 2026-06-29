#!/usr/bin/env python3
"""Shared utilities for blog pipeline: logging, review storage, retry, status tracking."""
import os, json, time
from datetime import datetime

BLOG_DIRS = "/root/homelab-blog"
LOGS_DIR = os.path.join(BLOG_DIRS, "logs")
REVIEWS_DIR = os.path.join(BLOG_DIRS, "reviews")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REVIEWS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, "pipeline.log")

# ─── Pipeline Status ───────────────────────────────────────────────

PIPELINE_STATUS = "RUNNING"  # RUNNING | COMPLETED | BLOCKED | FAILED

def set_status(status: str):
    global PIPELINE_STATUS
    PIPELINE_STATUS = status
    log("INFO", f"PIPELINE STATUS: {status}")

# ─── Logging ───────────────────────────────────────────────────────

def log(level: str, message: str):
    """Write a log entry. Never blocks the pipeline."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}]\n{level}\n{message}\n"
    try:
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass  # Logging darf nie blockieren

def log_step(step: str, status: str, detail: str = ""):
    """Convenience: log a pipeline step with status."""
    msg = f"{step} | {status}"
    if detail:
        msg += f" | {detail}"
    log("INFO", msg)
    print(f"  [{status}] {step}" + (f" - {detail}" if detail else ""))

# ─── API Retry ─────────────────────────────────────────────────────

def is_retryable(error: Exception) -> bool:
    """Check if an error should be retried."""
    msg = str(error).lower()
    # Retry bei temporären Fehlern
    if "timeout" in msg:
        return True
    if "connection" in msg or "reset" in msg or "refused" in msg:
        return True
    if "429" in msg or "rate limit" in msg or "too many" in msg:
        return True
    if "500" in msg or "502" in msg or "503" in msg or "504" in msg:
        return True
    if "service unavailable" in msg:
        return True
    if "temporarily" in msg:
        return True
    # Nicht retryen bei:
    if "401" in msg or "unauthorized" in msg or "403" in msg:
        return False
    if "402" in msg or "payment" in msg:
        return False
    if "invalid" in msg or "not found" in msg:
        return False
    # HTTP errors: nur 5xx und 429 retryen
    if "http error" in msg:
        for code in ["429", "500", "502", "503", "504"]:
            if code in msg:
                return True
        return False  # Andere HTTP-Fehler nicht retryen
    return False  # Default: nicht retryen (sicher)

def retry_api(max_attempts=3):
    """Decorator for API calls with exponential backoff."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            delays = [0, 5, 15]  # attempt 1: sofort, 2: 5s, 3: 15s
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if not is_retryable(e):
                        # Nicht retrybar -> sofort abbrechen
                        log("ERROR", f"Non-retryable error: {e}")
                        raise
                    if attempt < max_attempts:
                        delay = delays[attempt] if attempt < len(delays) else 15
                        log("WARNING", f"{func.__name__} failed attempt {attempt}/{max_attempts}, retrying in {delay}s: {str(e)[:100]}")
                        time.sleep(delay)
                    else:
                        log("ERROR", f"{func.__name__} failed after {max_attempts} attempts: {e}")
                        raise
            return None  # Never reached
        return wrapper
    return decorator

# ─── Review Artifacts ──────────────────────────────────────────────

def save_review(slug: str, review_data: dict, image_status: str = "unknown"):
    """Save Claude review result as a permanent artifact."""
    record = {
        "slug": slug,
        "timestamp": datetime.now().isoformat(),
        "image_status": image_status,
        "status": PIPELINE_STATUS,
        "review": review_data
    }
    path = os.path.join(REVIEWS_DIR, f"{slug}.json")
    try:
        with open(path, "w") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        return path
    except Exception as e:
        log("ERROR", f"Failed to save review artifact: {e}")
        return None

def load_review(slug: str) -> dict:
    """Load a saved review artifact."""
    path = os.path.join(REVIEWS_DIR, f"{slug}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

# ─── Image Status ──────────────────────────────────────────────────

def determine_image_status(featured_path: str, generated: bool) -> str:
    """Returns 'generated', 'placeholder', or 'missing'."""
    if generated and os.path.exists(featured_path):
        sz = os.path.getsize(featured_path)
        if sz > 20000:
            return "generated"
    if os.path.exists(featured_path) and os.path.getsize(featured_path) < 20000:
        return "placeholder"
    return "missing"
