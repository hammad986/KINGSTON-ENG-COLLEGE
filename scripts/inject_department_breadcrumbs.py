from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEPARTMENTS_DIR = ROOT / "departments"

DEPARTMENT_LABELS = {
    "aids": "Artificial Intelligence and Data Science",
    "aiml": "Computer Science Engineering with AI & ML",
    "arch": "Bachelor of Architecture",
    "csbs": "Computer Science and Business Systems",
    "cse": "Computer Science and Engineering",
    "ece": "Electronics and Communication Engineering",
    "it": "Information Technology",
    "mba": "Masters in Business Administration",
    "mech": "Mechanical Engineering",
    "sh": "Science and Humanities",
}

MAIN_PATTERN = re.compile(
    r'(<main\b[^>]*class="[^"]*\bdept-main-content\b[^"]*"[^>]*>\s*)',
    re.IGNORECASE,
)
FALLBACK_MAIN_PATTERN = re.compile(r'(<main\b[^>]*>\s*)', re.IGNORECASE)
HEADER_PATTERN = re.compile(r'(</header>\s*)', re.IGNORECASE)


def breadcrumb_markup(prefix: str, label: str) -> str:
    return (
        f'            <section class="dept-section dept-breadcrumb-section" data-aos="fade-up">\n'
        f'                <nav class="pch-breadcrumb" aria-label="Breadcrumb">\n'
        f'                    <a href="{prefix}index.html">Home</a>\n'
        f'                    <span>/</span>\n'
        f'                    <a href="{prefix}departments.html">Departments</a>\n'
        f'                    <span>/</span>\n'
        f'                    <span class="pch-breadcrumb-current">{label}</span>\n'
        f'                </nav>\n'
        f'            </section>\n\n'
    )


def department_label(path: Path) -> str:
    department_key = path.relative_to(DEPARTMENTS_DIR).parts[0]
    return DEPARTMENT_LABELS.get(department_key, department_key.replace("_", " ").title())


def inject_breadcrumb(file_path: Path) -> bool:
    original = file_path.read_text(encoding="utf-8")

    if 'pch-breadcrumb' in original:
        return False

    relative_depth = len(file_path.relative_to(ROOT).parts) - 1
    prefix = "../" * relative_depth
    label = department_label(file_path)
    breadcrumb = breadcrumb_markup(prefix, label)

    updated, inserted = MAIN_PATTERN.subn(r"\1" + breadcrumb, original, count=1)
    if inserted == 0:
        updated, inserted = FALLBACK_MAIN_PATTERN.subn(r"\1" + breadcrumb, original, count=1)
    if inserted == 0:
        updated, inserted = HEADER_PATTERN.subn(r"\1" + breadcrumb, original, count=1)

    if inserted == 0:
        updated = original.rstrip() + "\n\n" + breadcrumb
        inserted = 1

    if updated != original:
        file_path.write_text(updated, encoding="utf-8")
        return True

    return False


def main() -> None:
    html_files = sorted(DEPARTMENTS_DIR.glob("**/*.html"))
    updated_count = 0
    skipped_existing = 0
    skipped_missing_anchor = []

    for file_path in html_files:
        try:
            changed = inject_breadcrumb(file_path)
        except RuntimeError:
            skipped_missing_anchor.append(str(file_path.relative_to(ROOT)))
            continue

        if changed:
            updated_count += 1
        else:
            skipped_existing += 1

    print(f"Updated: {updated_count}")
    print(f"Already present: {skipped_existing}")
    print(f"Total scanned: {len(html_files)}")

    if skipped_missing_anchor:
        print("Missing main anchor:")
        for item in skipped_missing_anchor:
            print(f"- {item}")


if __name__ == "__main__":
    main()