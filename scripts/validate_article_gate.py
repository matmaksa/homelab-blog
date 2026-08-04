#!/usr/bin/env python3
"""Read-only validator for MATMAKSA article preview/public gates.

It only reads one explicitly named Markdown article. It never writes files,
invokes Git, deploys, publishes, promotes, or calls indexing services.
"""
from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path
from typing import Any, NoReturn

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ARTICLE GATE: BLOCKED\n\nBlocker:\n* PyYAML is required to parse YAML frontmatter", file=sys.stderr)
    sys.exit(2)

VALID_STATUS = {"open", "pass", "blocked"}
VALID_STATES = {"idea", "draft_generated", "audit_required", "audit_done", "user_review_required", "approved_for_publish", "published", "parked"}


def fail(message: str) -> NoReturn:
    print("ARTICLE GATE: BLOCKED\n\nBlocker:\n* " + message)
    raise SystemExit(2)


def read_frontmatter(path: Path) -> dict[str, Any]:
    """Read Hugo YAML (---) or TOML (+++) frontmatter without writing."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        fail(f"cannot read article: {exc}")
    if text.startswith("---\n"):
        delimiter, parser_name = "---", "YAML"
        end = text.find("\n---", 4)
        if end < 0:
            fail("YAML frontmatter closing delimiter is missing")
        try:
            value = yaml.safe_load(text[4:end])
        except yaml.YAMLError as exc:
            fail(f"invalid YAML frontmatter: {exc}")
    elif text.startswith("+++\n"):
        delimiter, parser_name = "+++", "TOML"
        end = text.find("\n+++", 4)
        if end < 0:
            fail("TOML frontmatter closing delimiter is missing")
        try:
            value = tomllib.loads(text[4:end])
        except tomllib.TOMLDecodeError as exc:
            fail(f"invalid TOML frontmatter: {exc}")
    else:
        fail("valid YAML or TOML frontmatter is missing")
    if not isinstance(value, dict):
        fail(f"{parser_name} frontmatter must be a mapping")
    workflow = value.get("workflow", {})
    if not isinstance(workflow, dict):
        fail("workflow must be a mapping")
    return value | {"workflow": workflow}


def bool_value(workflow: dict[str, Any], key: str, blockers: list[str]) -> bool:
    value = workflow.get(key)
    if value is not True:
        blockers.append(f"{key} is not true")
        return False
    return True


def status_value(workflow: dict[str, Any], key: str, blockers: list[str], require_pass: bool) -> str:
    value = workflow.get(key, "open")
    if value not in VALID_STATUS:
        blockers.append(f"{key} has invalid value {value!r}")
        return "INVALID"
    if value == "blocked":
        blockers.append(f"{key} is blocked")
    elif require_pass and value != "pass":
        blockers.append(f"{key} is {value}")
    return value.upper()


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only MATMAKSA article gate validator")
    parser.add_argument("--gate", choices=("preview", "public"), required=True)
    parser.add_argument("--article", type=Path, required=True)
    args = parser.parse_args()

    frontmatter = read_frontmatter(args.article)
    workflow = frontmatter["workflow"]
    blockers: list[str] = []
    report: list[tuple[str, str]] = []

    state = workflow.get("content_state", "")
    if state not in VALID_STATES:
        blockers.append("content_state is missing or invalid")
    if workflow.get("editorial_status", "open") not in VALID_STATUS:
        blockers.append("editorial_status is missing or invalid")

    is_preview = frontmatter.get("preview") is True
    noindex = frontmatter.get("noindex") is True and frontmatter.get("robotsNoIndex") is True
    sitemap = frontmatter.get("sitemap")
    sitemap_excluded = isinstance(sitemap, dict) and sitemap.get("exclude") is True
    if args.gate == "preview":
        if not is_preview:
            blockers.append("preview is not true")
        if not noindex:
            blockers.append("noindex and robotsNoIndex must both be true")
        if not sitemap_excluded:
            blockers.append("sitemap.exclude is not true")
        editorial = status_value(workflow, "editorial_status", blockers, False)
        report.extend([("Editorial", editorial), ("Preview protection", "PASS" if is_preview and noindex and sitemap_excluded else "BLOCKED")])
    else:
        for key, label in (("editorial_status", "Editorial"), ("technical_status", "Technical"), ("visual_status", "Visual"), ("seo_status", "SEO")):
            report.append((label, status_value(workflow, key, blockers, True)))
        for key, label in (("external_preview_verified", "External preview"), ("user_publish_approval", "User approval"), ("links_verified", "Links"), ("canonical_verified", "Canonical"), ("sitemap_verified", "Sitemap"), ("robots_verified", "Robots")):
            report.append((label, "PASS" if bool_value(workflow, key, blockers) else "MISSING"))
        if workflow.get("external_images_used") is True:
            bool_value(workflow, "image_licenses_verified", blockers)
        if workflow.get("affiliate_review_required") is True:
            bool_value(workflow, "affiliate_review_passed", blockers)
        if workflow.get("screenshots_required") is True:
            for key in ("screenshots_complete", "desktop_visual_check", "mobile_visual_check"):
                bool_value(workflow, key, blockers)
        if workflow.get("claims_practical_test") is True:
            for key in ("commands_executed_on", "commands_verified_at"):
                if not isinstance(workflow.get(key), str) or not workflow[key].strip():
                    blockers.append(f"{key} is empty for practical-test claim")
        if workflow.get("public_placeholders_present") is True:
            blockers.append("public_placeholders_present is true")

    print("ARTICLE GATE: " + ("PASS" if not blockers else "BLOCKED"))
    print()
    for label, status in report:
        print(f"{label}: {status}")
    if blockers:
        print("\nBlocker:")
        for blocker in blockers:
            print(f"* {blocker}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
