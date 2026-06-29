#!/usr/bin/env python3
"""Load AI context files for blog pipeline roles.
Non-blocking: returns empty strings on error, never crashes."""
import os
from pathlib import Path

CONTEXT_DIR = Path("/root/.hermes/skills/monetization/homelab-seo-blog/references/ai_context")

def load_context(filename: str) -> str:
    """Load a single context file. Returns empty string if not found."""
    path = CONTEXT_DIR / filename
    try:
        if path.exists():
            return path.read_text().strip()
    except Exception:
        pass
    return ""

def load_contexts(*filenames: str) -> dict[str, str]:
    """Load multiple context files at once. Returns {name: content} dict."""
    result = {}
    for name in filenames:
        content = load_context(name)
        if content:
            result[name] = content
    return result

def format_context_block(contexts: dict[str, str]) -> str:
    """Format context dict as a single prompt block."""
    if not contexts:
        return ""
    lines = []
    for name, content in contexts.items():
        label = name.replace(".md", "").replace("_", " ").title()
        lines.append(f"=== {label} ===")
        lines.append(content)
        lines.append("")
    return "\n".join(lines)

def get_deepseek_context() -> str:
    """Context for DeepSeek article writing."""
    ctx = load_contexts("blog_identity.md", "audience.md", "writing_style.md",
                        "quality_examples.md", "quality_learnings.md",
                        "performance_learnings.md")
    return format_context_block(ctx)

def get_claude_context() -> str:
    """Context for Claude quality review."""
    ctx = load_contexts("blog_identity.md", "audience.md", "review_criteria.md",
                        "quality_examples.md", "quality_learnings.md")
    return format_context_block(ctx)
# Test
if __name__ == "__main__":
    ctx = get_claude_context()
    print(f"Claude Context: {len(ctx)} chars")
    print(ctx[:200] + "..." if len(ctx) > 200 else ctx)
    print()
    dsc = get_deepseek_context()
    print(f"DeepSeek Context: {len(dsc)} chars")
