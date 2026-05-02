
import os
import re
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
missing_dir = os.path.join(workspace_root, "missing")

def find_all_references():
    missing_files = os.listdir(missing_dir)
    print(f"Missing Files: {missing_files}")
    
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "backup_mapping", "assets/css", "node_modules"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    mapping = {}
    
    for html_path in html_files:
        rel_html = os.path.relpath(html_path, workspace_root)
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find all strings that look like they might be PDF links
            links = re.findall(r'href=["\']([^"\':]+\.pdf)["\']', content)
            
            for link in links:
                basename = os.path.basename(link)
                # Fuzzy match for filenames (ignoring underscores/spaces/case)
                clean_link = basename.lower().replace('_', '').replace(' ', '').replace('-', '')
                
                for missing in missing_files:
                    clean_missing = missing.lower().replace('_', '').replace(' ', '').replace('-', '')
                    if clean_link == clean_missing or clean_missing in clean_link or clean_link in clean_missing:
                        if missing not in mapping:
                            mapping[missing] = {
                                "references": [],
                                "target_folder": "assets/pdfs/ugc" # Default for most of these
                            }
                        if rel_html not in mapping[missing]["references"]:
                            mapping[missing]["references"].append(rel_html)
        except: pass

    # Categorize based on content/filename patterns
    for missing, data in mapping.items():
        if "accredited" in missing.lower():
            data["target_folder"] = "assets/pdfs/naac"
        elif "cycle" in missing.lower():
            data["target_folder"] = "assets/pdfs/naac"
        elif "scheme" in missing.lower():
            data["target_folder"] = "assets/pdfs/general"
        elif "india" in missing.lower():
            data["target_folder"] = "assets/pdfs/general"

    with open("final_pdf_mapping.json", "w") as f:
        json.dump(mapping, f, indent=4)
        
    print(f"Deep scan complete. Mapped {len(mapping)} files.")

if __name__ == "__main__":
    find_all_references()
