#!/usr/bin/env python3
"""
Image Generator with Provider Abstraction Layer.
Model is resolved from image_config.ini at runtime - no hardcoded model names.

Usage: python3 generate_image.py "prompt" /path/to/output.jpg

Config: image_config.ini
  [image]
  provider = google         # google | flux | stable-diffusion
  model = latest            # arbitrary label; actual model from provider-specific key
  style = product-photo
  google_model = google/gemini-3-pro-image-preview  # actual API model ID
"""
import json, urllib.request, urllib.error, sys, os, base64, configparser
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "references" / "image_config.ini"

# ─── Abstract Base ─────────────────────────────────────────────────

class ImageGenerator:
    def generate(self, prompt: str, output_path: str) -> bool:
        raise NotImplementedError

# ─── Google Gemini Provider ────────────────────────────────────────

class GeminiImageProvider(ImageGenerator):
    NAME = "google"

    def __init__(self, model="gemini-image", style="product-photo"):
        self.model = "google/gemini-3-pro-image-preview"
        self.style = style

    def generate(self, prompt: str, output_path: str) -> bool:
        api_key = self._get_openrouter_key()
        if not api_key:
            print("ERROR: No OpenRouter API key")
            return False

        payload = {
            "model": self.model,
            "messages": [{
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }]
        }

        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=json.dumps(payload).encode(),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read())
                msg = result.get("choices", [{}])[0].get("message", {})
                for img in msg.get("images", []):
                    url = img.get("image_url", {}).get("url", "")
                    if url.startswith("data:"):
                        b64 = url.split(",", 1)[1]
                        with open(output_path, "wb") as f:
                            f.write(base64.b64decode(b64))
                        size_kb = os.path.getsize(output_path) / 1024
                        print(f"  Image saved: {size_kb:.0f} KB via {self.model}")
                        return True
            print(f"  No images in response")
            return False
        except urllib.error.HTTPError as e:
            print(f"  Gemini HTTP {e.code}: {e.read().decode()[:200]}")
            return False
        except Exception as e:
            print(f"  Gemini error: {e}")
            return False

    def _get_openrouter_key(self) -> str:
        env_path = "/root/.hermes/.env"
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if "OPENROUTER_API_KEY" in line and not line.startswith("#"):
                        parts = line.split("=", 1)
                        if len(parts) == 2:
                            return parts[1]
        return None

# ─── FLUX Provider (Stub) ──────────────────────────────────────────

class FluxProvider(ImageGenerator):
    NAME = "flux"
    def generate(self, prompt: str, output_path: str) -> bool:
        print("  FLUX provider not yet implemented")
        return False

# ─── Stable Diffusion Provider (Stub) ──────────────────────────────

class StableDiffusionProvider(ImageGenerator):
    NAME = "stable-diffusion"
    def generate(self, prompt: str, output_path: str) -> bool:
        print("  Stable Diffusion provider not yet implemented")
        return False

# ─── Factory ───────────────────────────────────────────────────────

_PROVIDERS = {
    p.NAME: p
    for p in [GeminiImageProvider, FluxProvider, StableDiffusionProvider]
}

def get_generator() -> ImageGenerator:
    """Load image_config.ini and return the appropriate generator."""
    config = configparser.ConfigParser()
    config_path = str(CONFIG_PATH)
    if os.path.exists(config_path):
        config.read(config_path)
    else:
        print(f"WARN: {config_path} not found, using defaults")
        config["image"] = {"provider": "google", "model": "latest", "style": "product-photo"}

    provider_name = config.get("image", "provider", fallback="google").lower()
    model = config.get("image", "model", fallback="latest")
    style = config.get("image", "style", fallback="product-photo")

    # Provider-spezifisches API-Modell aus Config lesen (z.B. google_model)
    provider_model_key = f"{provider_name}_model"
    actual_model = config.get("image", provider_model_key, fallback=None)
    if actual_model:
        print(f"  Provider: {provider_name} | Config-Model: {model} | API-Model: {actual_model} | Style: {style}")
    else:
        print(f"  Provider: {provider_name} | Model: {model} | Style: {style}")

    cls = _PROVIDERS.get(provider_name)
    if cls:
        return cls(model=actual_model or model, style=style)

    print(f"  Unknown provider '{provider_name}', falling back to Gemini")
    return GeminiImageProvider(model=model, style=style)

# ─── CLI ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image.py 'prompt' /path/to/output.jpg")
        sys.exit(1)

    os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
    generator = get_generator()
    success = generator.generate(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 1)
