#!/usr/bin/env python3
"""Read-only structural checks for Magento static-page handoff widgets."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class FragmentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.roots: list[tuple[str, dict[str, str]]] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name.lower(): value or "" for name, value in attrs}
        if self.depth == 0:
            self.roots.append((tag.lower(), attrs_dict))
        self.depth += 1
        if tag.lower() in {"style", "script"}:
            self.errors.append(f"fragment contains forbidden <{tag.lower()}> element")
        if "style" in attrs_dict:
            self.errors.append(f"fragment contains inline style on <{tag.lower()}>")
        for name in attrs_dict:
            if name.startswith("on"):
                self.errors.append(f"fragment contains inline event handler {name} on <{tag.lower()}>")
        classes = attrs_dict.get("class", "").split()
        self._classes.append(classes)
        src = attrs_dict.get("src")
        # HTMLParser resolves &quot; in the source directive to a literal quote.
        if src is not None and not src.startswith('{{media url="'):
            self.errors.append(f"fragment source is not a Magento media directive: {src}")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        self.depth = max(0, self.depth - 1)

    def handle_data(self, data: str) -> None:
        if self.depth == 0 and data.strip():
            self.errors.append("fragment contains non-whitespace content outside its root")

    def handle_comment(self, data: str) -> None:
        if self.depth == 0:
            self.errors.append("fragment contains a comment outside its root")

    _classes: list[list[str]] = []


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def exact_wrapper(text: str, tag: str, label: str) -> list[str]:
    tags = re.findall(rf"<\s*/?\s*{tag}\b[^>]*>", text, flags=re.IGNORECASE)
    opens = re.findall(rf"<\s*{tag}\b[^>]*>", text, flags=re.IGNORECASE)
    closes = re.findall(rf"<\s*/\s*{tag}\s*>", text, flags=re.IGNORECASE)
    if len(opens) != 1 or len(closes) != 1 or len(tags) != 2:
        return [f"{label} must contain exactly one <{tag}> wrapper"]
    if not re.match(rf"^\s*<{tag}\b[^>]*>[\s\S]*</{tag}>\s*$", text, flags=re.IGNORECASE):
        return [f"{label} must not contain content outside its <{tag}> wrapper"]
    return []


def declaration_block(css: str, selector: str) -> str | None:
    match = re.search(rf"{re.escape(selector)}\s*\{{([^{{}}]*)\}}", css, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1) if match else None


def validate_html(text: str, root: str) -> list[str]:
    parser = FragmentParser()
    parser._classes = []
    parser.feed(text)
    parser.close()
    errors = parser.errors[:]
    if len(parser.roots) != 1:
        errors.append("fragment must contain exactly one top-level element")
    elif parser.roots[0][0] != "div":
        errors.append("fragment root must be a <div>")
    elif root not in parser.roots[0][1].get("class", "").split():
        errors.append(f"fragment root must include the '{root}' class")
    for classes in parser._classes:
        for class_name in classes:
            if not class_name.startswith(root):
                errors.append(f"class '{class_name}' is not namespaced with '{root}'")
    return errors


def validate_css(text: str, root: str) -> list[str]:
    errors = exact_wrapper(text, "style", "CSS widget")
    css = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    for value in re.findall(r"font-size\s*:\s*([^;}]+)", css, flags=re.IGNORECASE):
        if not re.fullmatch(r"\s*\d+(?:\.\d+)?px\s*", value):
            errors.append(f"font-size must be a fixed pixel value, found '{value.strip()}'")
    body = re.sub(r"^\s*<style\b[^>]*>|</style>\s*$", "", css, flags=re.IGNORECASE)
    for selector_group in re.findall(r"([^{}]+)\{[^{}]*\}", body):
        selector_group = selector_group.strip()
        if not selector_group or selector_group.startswith("@"):
            continue
        for selector in selector_group.split(","):
            selector = selector.strip()
            if not selector.startswith(f".{root}"):
                errors.append(f"CSS selector must begin with '.{root}': {selector}")
    root_block = declaration_block(body, f".{root}")
    if root_block is None or not re.search(r"\bmargin\s*:\s*0\s*;", root_block) or not re.search(r"\bpadding\s*:\s*0\s*;", root_block):
        errors.append("root selector must explicitly set margin: 0 and padding: 0")
    return errors


def validate_script(text: str, root: str) -> list[str]:
    errors = exact_wrapper(text, "script", "JavaScript widget")
    if errors:
        return errors
    expected = f"document.querySelector('.{root}')"
    if expected not in text and f'document.querySelector(".{root}")' not in text:
        errors.append(f"script must query its '.{root}' root before descendant queries")
    if not re.search(r"if\s*\(\s*!\s*root\s*\)\s*(?:\{\s*return\s*;?\s*\}|return\s*;)", text):
        errors.append("script must return when the page root is absent")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Magento static-page handoff widgets without modifying them.")
    parser.add_argument("--html", required=True, type=Path, help="CMS HTML fragment")
    parser.add_argument("--css", required=True, type=Path, help="wrapped CSS widget")
    parser.add_argument("--root", required=True, help="exact page root class, without the leading dot")
    parser.add_argument("--script", type=Path, help="optional wrapped JavaScript widget")
    args = parser.parse_args()

    errors: list[str] = []
    try:
        errors.extend(validate_html(read(args.html), args.root))
        errors.extend(validate_css(read(args.css), args.root))
        if args.script:
            errors.extend(validate_script(read(args.script), args.root))
    except ValueError as exc:
        errors.append(str(exc))
    if errors:
        for error in dict.fromkeys(errors):
            print(f"FAIL: {error}")
        return 1
    print("PASS: handoff structure satisfies the checked Magento static-page rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
