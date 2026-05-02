import os
import re

# ─── Final 10 Departments in priority order ───────────────────────────────────
DEPARTMENTS = [
    {"name": "Computer Science and Engineering",           "file": "dept_cse.html"},
    {"name": "Artificial Intelligence and Data Science",   "file": "dept_AI&DS.html"},
    {"name": "Computer Science Engineering with AI & ML",  "file": "dept_AI&ML.html"},
    {"name": "Information Technology",                     "file": "dept_IT.html"},
    {"name": "Electronics and Communication Engineering",  "file": "dept_ece.html"},
    {"name": "Computer Science and Business Systems",      "file": "dept_csbs.html"},
    {"name": "Mechanical Engineering",                     "file": "dept_mechanical.html"},
    {"name": "Bachelor of Architecture",                   "file": "dept_BA.html"},
    {"name": "Masters in Business Administration",         "file": "dept_MBA.html"},
    {"name": "Science and Humanities",                     "file": "dept_S&H.html"},
]

# ─── Icons for departments.html grid ─────────────────────────────────────────
ICONS = [
    "fa-solid fa-desktop",
    "fa-solid fa-brain",
    "fa-solid fa-robot",
    "fa-solid fa-mobile-screen",
    "fa-solid fa-wifi",
    "fa-solid fa-laptop",
    "fa-solid fa-car-side",
    "fa-solid fa-archway",
    "fa-solid fa-briefcase",
    "fa-solid fa-flask",
]

# ─── 1. Build the new nav dropdown snippet ────────────────────────────────────
nav_items = "\n".join(
    f'                            <li><a href="{d["file"]}">{d["name"]}</a></li>'
    for d in DEPARTMENTS
)
NAV_SNIPPET = (
    '                        <ul class="dropdown dropdown-columns js-exclude-dropdown">\n'
    + nav_items + "\n"
    + "                        </ul>"
)

# ─── 2. Build the new departments.html grid snippet ───────────────────────────
grid_items = []
for i, (dept, icon) in enumerate(zip(DEPARTMENTS, ICONS)):
    delay = i * 80
    grid_items.append(
        f'                <a href="{dept["file"]}" class="dept-card" data-aos="fade-up" data-aos-delay="{delay}">\n'
        f'                    <i class="{icon}"></i>\n'
        f'                    <span>{dept["name"]}</span>\n'
        f'                </a>'
    )
GRID_SNIPPET = "\n".join(grid_items)

# ─── 3. Update nav dropdown in every HTML file ────────────────────────────────
print("Updating nav dropdowns across all HTML files...")
all_html = [f for f in os.listdir(".") if f.endswith(".html")]
updated_nav = 0

for filename in all_html:
    content = None
    for enc in ["utf-8", "cp1252", "latin-1"]:
        try:
            with open(filename, "r", encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue

    if content is None:
        print(f"  [SKIP] Cannot decode: {filename}")
        continue

    new_content = re.sub(
        r'<ul class="dropdown dropdown-columns js-exclude-dropdown">.*?</ul>',
        NAV_SNIPPET,
        content,
        flags=re.DOTALL,
    )

    if new_content != content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_nav += 1

print(f"  Nav updated in {updated_nav} files.")

# ─── 4. Update departments.html grid ─────────────────────────────────────────
print("Updating departments.html grid...")
DEPT_FILE = "departments.html"
content = None
for enc in ["utf-8", "cp1252", "latin-1"]:
    try:
        with open(DEPT_FILE, "r", encoding=enc) as f:
            content = f.read()
        break
    except UnicodeDecodeError:
        continue

if content is None:
    print("  [ERROR] Cannot read departments.html")
else:
    new_content = re.sub(
        r'(<div class="dept-grid">).*?(</div>)',
        r'\1\n' + GRID_SNIPPET + r'\n            \2',
        content,
        flags=re.DOTALL,
        count=1,
    )

    if new_content != content:
        with open(DEPT_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("  departments.html grid updated successfully.")
    else:
        print("  [WARNING] departments.html grid pattern not found — no change made.")

print("\nAll done!")
