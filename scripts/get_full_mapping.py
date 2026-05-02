
import os
import re
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
missing_dir = os.path.join(workspace_root, "missing")

def get_mapping():
    missing_files = os.listdir(missing_dir)
    print(f"Missing Files: {missing_files}")
    
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "backup_mapping", "assets/css", "node_modules"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    full_mapping = []
    
    for html_path in html_files:
        rel_html = os.path.relpath(html_path, workspace_root)
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Match href="path/to/file.pdf"
            matches = re.findall(r'href=["\']([^"\':]+\.pdf)["\']', content)
            for link in matches:
                target_full = os.path.normpath(os.path.join(os.path.dirname(html_path), link))
                if not os.path.exists(target_full):
                    # It's a broken link. Does it match any missing file?
                    link_basename = os.path.basename(link)
                    for missing in missing_files:
                        # Fuzzy match: 
                        # normalized_link contains normalized_missing
                        l_norm = link_basename.lower().replace('_', '').replace(' ', '').replace('-', '')
                        m_norm = missing.lower().replace('_', '').replace(' ', '').replace('-', '')
                        
                        if l_norm == m_norm or m_norm in l_norm or l_norm in m_norm:
                            full_mapping.append({
                                "html": rel_html,
                                "link": link,
                                "missing_file": missing,
                                "target_category": "ugc" if "ugc" in rel_html.lower() or "ps_" in rel_html.lower() else "general"
                            })
                            break
        except: pass

    with open("full_restoration_mapping.json", "w") as f:
        json.dump(full_mapping, f, indent=4)
    
    # Identify orphans (missing files NOT mapped to any HTML)
    mapped_files = set(m["missing_file"] for m in full_mapping)
    unmapped = set(missing_files) - mapped_files
    print(f"Mapped: {len(mapped_files)} files.")
    print(f"Unmapped: {unmapped}")

if __name__ == "__main__":
    get_mapping()
