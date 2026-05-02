import os
import re
import json

html_dir = r"."
pdf_dir = r"assets\pdfs"

pdf_pattern = re.compile(r'href=["\'](assets/pdfs/(?:[^"\'>]+)\.pdf)["\']', re.IGNORECASE)

referenced_pdfs = set()
for root, dirs, files in os.walk(html_dir):
    if any(x in root for x in [".git", "assets", ".gemini"]):
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = pdf_pattern.findall(content)
                    for m in matches:
                        # Normalize to forward slashes for matching
                        referenced_pdfs.add(m.replace('\\', '/').lower())
            except Exception:
                pass

all_pdfs = []
for root, dirs, files in os.walk(pdf_dir):
    for file in files:
        if file.endswith(".pdf"):
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace('\\', '/').lower()
            all_pdfs.append(rel_path)

extra_pdfs = [p for p in all_pdfs if p not in referenced_pdfs]

# Final verification: check for broken links
broken_links = []
for root, dirs, files in os.walk(html_dir):
    if any(x in root for x in [".git", "assets", ".gemini"]):
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = pdf_pattern.findall(content)
                    for m in matches:
                        # Check if the file exists on disk
                        full_path = os.path.join(os.getcwd(), m.replace('/', os.sep))
                        if not os.path.exists(full_path):
                            broken_links.append({"html": path, "link": m})
            except Exception:
                pass

with open('final_pdf_audit_report.json', 'w', encoding='utf-8') as f:
    json.dump({
        "extra_pdfs": extra_pdfs,
        "broken_links": broken_links,
        "total_pdfs": len(all_pdfs),
        "total_referenced": len(referenced_pdfs)
    }, f, indent=2)

print(f"Final audit complete. Extra PDFs: {len(extra_pdfs)}. Broken Links: {len(broken_links)}")
