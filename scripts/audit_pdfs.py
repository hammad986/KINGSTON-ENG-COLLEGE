
import os
import re
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

results = {
    "pdfs_on_disk": [],
    "links_in_html": [],
    "missing_pdfs": [],
    "available_missing": []
}

# 1. Audit Files on Disk
for root, dirs, files in os.walk(workspace_root):
    if any(d in root for d in [".git", "node_modules", "backup"]): continue
    for f in files:
        if f.lower().endswith(".pdf"):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, workspace_root).replace("\\", "/")
            results["pdfs_on_disk"].append({
                "filename": f.lower(),
                "real_case": f,
                "rel_path": rel_path
            })

# 2. Audit Links in HTML
patterns = [
    r'href=["\']([^"\'\s]+\.pdf)["\']',
    r'src=["\']([^"\'\s]+\.pdf)["\']',
    r'window\.open\(["\']([^"\'\s]+\.pdf)["\']'
]

for root, dirs, files in os.walk(workspace_root):
    if any(d in root for d in [".git", "node_modules", "backup", "scripts"]): continue
    for f in files:
        if f.lower().endswith(".html"):
            html_path = os.path.join(root, f)
            rel_html = os.path.relpath(html_path, workspace_root).replace("\\", "/")
            try:
                with open(html_path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                
                for pattern in patterns:
                    for m in re.finditer(pattern, content):
                        original_link = m.group(1)
                        basename = os.path.basename(original_link.split('?')[0].split('#')[0]).lower()
                        
                        # Find if it exists on disk
                        matches = [p for p in results["pdfs_on_disk"] if p["filename"] == basename]
                        
                        results["links_in_html"].append({
                            "html_file": rel_html,
                            "original_link": original_link,
                            "basename": basename,
                            "exists": len(matches) > 0,
                            "potential_paths": [m["rel_path"] for m in matches]
                        })
            except Exception as e:
                print(f"Error reading {f}: {e}")

# 3. Analyze gaps
missing = [l for l in results["links_in_html"] if not l["exists"]]
resolved = [l for l in results["links_in_html"] if l["exists"]]

with open("scripts/audit_report.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"Audit Complete.")
print(f"Total PDFs on Disk: {len(results['pdfs_on_disk'])}")
print(f"Total PDF Links Found: {len(results['links_in_html'])}")
print(f"Links pointing to existing files: {len(resolved)}")
print(f"Links pointing to MISSING files: {len(missing)}")
