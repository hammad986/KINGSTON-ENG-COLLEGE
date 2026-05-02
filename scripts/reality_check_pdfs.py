
import re
import os
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
pdf_assets_root = os.path.join(workspace_root, "assets", "pdfs")

results = {
    "total_html_scanned": 0,
    "total_pdf_links_found": 0,
    "links": []
}

# 1. Index actual PDFs on disk
pdf_on_disk = {}
for root, dirs, files in os.walk(pdf_assets_root):
    for f in files:
        if f.lower().endswith(".pdf"):
            rel_path = os.path.relpath(os.path.join(root, f), workspace_root).replace("\\", "/")
            basename = f.lower()
            if basename not in pdf_on_disk:
                pdf_on_disk[basename] = []
            pdf_on_disk[basename].append(rel_path)

# 2. Scan HTML files
for root, dirs, files in os.walk(workspace_root):
    if "backup" in root or "node_modules" in root or ".git" in root or "scripts" in root:
        continue
    
    for f in files:
        if f.lower().endswith(".html"):
            results["total_html_scanned"] += 1
            html_path = os.path.join(root, f)
            rel_html_path = os.path.relpath(html_path, workspace_root).replace("\\", "/")
            
            try:
                with open(html_path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                
                # Extract links
                found = re.finditer(r'href=["\']([^"\'\s]+\.pdf)["\']', content)
                for m in found:
                    results["total_pdf_links_found"] += 1
                    original_link = m.group(1)
                    basename = os.path.basename(original_link.split('?')[0].split('#')[0]).lower()
                    
                    # Verify physical existence at the EXACT path in the HTML
                    # First, calculate where the browser thinks it is
                    html_dir = os.path.dirname(html_path)
                    target_physical_path = os.path.abspath(os.path.join(html_dir, original_link.replace("/", os.sep)))
                    exists = os.path.exists(target_physical_path)
                    
                    results["links"].append({
                        "html_file": rel_html_path,
                        "original_link": original_link,
                        "exists_as_is": exists,
                        "basename": basename,
                        "found_on_disk": pdf_on_disk.get(basename, [])
                    })
            except Exception as e:
                print(f"Error reading {f}: {e}")

with open("scripts/reality_check_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"Reality Check Complete.")
print(f"Total HTML Scanned: {results['total_html_scanned']}")
print(f"Total PDF Links Found: {results['total_pdf_links_found']}")
broken = [l for l in results["links"] if not l["exists_as_is"]]
print(f"Broken Links (Physical 404): {len(broken)}")
