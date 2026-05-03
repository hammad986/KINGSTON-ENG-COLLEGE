from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TARGET_FILES = [
    ROOT / "index.html",
    ROOT / "about.html",
    ROOT / "contact.html",
    ROOT / "departments.html",
]
TARGET_FILES.extend(sorted(ROOT.glob("dept_*.html")))

SECTION_PATTERN = re.compile(r"(<section\b[^>]*>)(.*?)(</section>)", re.IGNORECASE | re.DOTALL)
DIV_PATTERN = re.compile(r"(<div\b[^>]*>)(.*?)(</div>)", re.IGNORECASE | re.DOTALL)

SECTION_EXCLUDES = (
    "hero-section",
    "main-header",
    "main-footer",
    "notice-bar",
    "logo-bar",
    "floating-side-buttons",
    "floating-circle-buttons",
    "mobile-sticky-cta",
    "top-bar",
    "main-nav",
    "carousel",
    "swiper",
    "grid",
    "card",
    "gallery",
    "marquee",
    "map-section",
    "contact-info-box",
    "contact-form-section",
    "ach-glass-section",
)

SECTION_ALLOW = (
    "dept-section",
    "why-choose-section",
    "vision-mission-section",
    "achievements",
    "departments-contact",
)


def add_class_attr(tag: str, class_name: str) -> str:
    if 'class="' in tag:
        return re.sub(
            r'class="([^"]*)"',
            lambda match: f'class="{match.group(1)} {class_name}"'
            if class_name not in match.group(1).split()
            else match.group(0),
            tag,
            count=1,
        )
    return tag[:-1] + f' class="{class_name}">'


def should_wrap_section(start_tag: str, inner_html: str) -> bool:
    class_match = re.search(r'class="([^"]*)"', start_tag)
    classes = class_match.group(1).split() if class_match else []
    joined = " ".join(classes)

    if any(excluded in joined for excluded in SECTION_EXCLUDES):
        return False

    if any(allowed in joined for allowed in SECTION_ALLOW):
        return True

    text = re.sub(r"<[^>]+>", " ", inner_html)
    text = re.sub(r"\s+", " ", text).strip()
    paragraph_count = inner_html.lower().count("<p")

    if paragraph_count >= 1 and len(text) >= 220:
        return True

    return False


def wrap_sections(text: str) -> tuple[str, int]:
    updates = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal updates
        start_tag, inner_html, end_tag = match.groups()
        if 'content-text-wrapper' in start_tag:
            return match.group(0)
        if not should_wrap_section(start_tag, inner_html):
            return match.group(0)
        updates += 1
        return add_class_attr(start_tag, "content-text-wrapper") + inner_html + end_tag

    return SECTION_PATTERN.sub(replacer, text), updates


def wrap_contact_header(text: str) -> tuple[str, int]:
    pattern = re.compile(r'(<div\b[^>]*class="[^"]*\bcontact-header\b[^"]*"[^>]*>)(.*?)(</div>)', re.IGNORECASE | re.DOTALL)

    def replacer(match: re.Match[str]) -> str:
        start_tag, inner_html, end_tag = match.groups()
        if 'content-text-wrapper' in start_tag:
            return match.group(0)
        return add_class_attr(start_tag, "content-text-wrapper") + inner_html + end_tag

    updated_text, count = pattern.subn(replacer, text, count=1)
    return updated_text, count


def wrap_about_specifics(text: str) -> tuple[str, int]:
    updates = 0

    def add_to_classed_paragraphs(pattern_text: str, source: str) -> str:
        nonlocal updates
        pattern = re.compile(pattern_text, re.IGNORECASE | re.DOTALL)

        def replacer(match: re.Match[str]) -> str:
            nonlocal updates
            start_tag = match.group(0)
            if 'content-text-wrapper' in start_tag:
                return start_tag
            updates += 1
            return add_class_attr(start_tag, "content-text-wrapper")

        return pattern.sub(replacer, source)

    text = add_to_classed_paragraphs(r'<p\b[^>]*class="[^"]*\bwhy-desc\b[^"]*"[^>]*>', text)
    text = add_to_classed_paragraphs(r'<p\b[^>]*class="[^"]*\bv-text-body\b[^"]*"[^>]*>', text)
    text = add_to_classed_paragraphs(r'<p\b[^>]*class="[^"]*\bach-subtitle\b[^"]*"[^>]*>', text)

    quality_policy_section = re.compile(
        r'(<section\b[^>]*style="padding:70px 0;background:#f4f6fb;"[^>]*>)(.*?)(</section>)',
        re.IGNORECASE | re.DOTALL,
    )

    def section_replacer(match: re.Match[str]) -> str:
        nonlocal updates
        start_tag, inner_html, end_tag = match.groups()
        if 'content-text-wrapper' in start_tag:
            return match.group(0)
        updates += 1
        return add_class_attr(start_tag, "content-text-wrapper") + inner_html + end_tag

    text = quality_policy_section.sub(section_replacer, text, count=1)
    return text, updates


def wrap_department_sections(text: str) -> tuple[str, int]:
    pattern = re.compile(r'(<section\b[^>]*class="[^"]*\bdept-section\b[^"]*"[^>]*>)(.*?)(</section>)', re.IGNORECASE | re.DOTALL)

    def replacer(match: re.Match[str]) -> str:
        start_tag, inner_html, end_tag = match.groups()
        if 'content-text-wrapper' in start_tag:
            return match.group(0)
        return add_class_attr(start_tag, "content-text-wrapper") + inner_html + end_tag

    return pattern.subn(replacer, text)


def process_file(file_path: Path) -> bool:
    original = file_path.read_text(encoding="utf-8")
    updated = original
    updates = 0

    if file_path.name.startswith("dept_"):
        updated, count = wrap_department_sections(updated)
        updates += count

    if file_path.name == "about.html":
        updated, count = wrap_about_specifics(updated)
        updates += count

    if file_path.name == "contact.html":
        updated, count = wrap_contact_header(updated)
        updates += count

    if file_path.name in {"index.html", "departments.html"}:
        updated, count = wrap_sections(updated)
        updates += count

    if updated != original:
        file_path.write_text(updated, encoding="utf-8")
        print(f"Updated {file_path.relative_to(ROOT)} ({updates} wrappers)")
        return True

    print(f"No wrapper changes for {file_path.relative_to(ROOT)}")
    return False


def main() -> None:
    changed = 0
    for file_path in TARGET_FILES:
        if file_path.exists():
            if process_file(file_path):
                changed += 1
    print(f"Files updated: {changed}")


if __name__ == "__main__":
    main()