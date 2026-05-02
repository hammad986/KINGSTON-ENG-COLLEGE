
import os
import re
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
missing_dir = os.path.join(workspace_root, "missing")

def find_references():
    # 1. Get files in /missing/
    missing_files = os.listdir(missing_dir)
    print(f"Missing Files: {missing_files}")
    
    # 2. Get all HTML files
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "backup_mapping", "assets/css", "node_modules"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    mapping = []
    
    # 3. Scan for every missing file in every HTML
    for html_path in html_files:
        rel_html = os.path.relpath(html_path, workspace_root)
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Look for ANY .pdf link
            links = re.findall(r'href=["\']([^"\':]+\.pdf)["\']', content)
            
            for link in links:
                # Check if this link's basename matches any missing file
                basename = os.path.basename(link)
                for missing in missing_files:
                    # Try fuzzy match since naming might differ slightly (e.g. spaces vs underscores)
                    if missing.lower().replace('_', '').replace(' ', '') == basename.lower().replace('_', '').replace(' ', ''):
                        mapping.append({
                            "html_file": rel_html,
                            "original_link": link,
                            "missing_file": missing
                        })
        except: pass

    # 4. Save mapping
    with open("missing_pdf_mapping.json", "w") as f:
        json.dump(mapping, f, indent=4)
    print(f"Mapped {len(mapping)} references to missing PDFs. Saved to missing_pdf_mapping.json")

if __name__ == "__main__":
    find_references()
