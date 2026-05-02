
import os
import re
import json
import shutil

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
pdf_target_root = os.path.join(workspace_root, "assets", "pdfs")

# Ensure target folder exists
if not os.path.exists(pdf_target_root):
    os.makedirs(pdf_target_root)

stats = {
    "total_links": 0,
    "fixed_links": 0,
    "moved_from_legacy": 0,
    "missing_links": 0,
    "samples": []
}

# 1. Map ALL PDFs on disk
pdf_on_disk = {} # basename -> current_rel_path

def index_pdfs():
    global pdf_on_disk
    pdf_on_disk = {}
    for root, dirs, files in os.walk(workspace_root):
        if any(d in root for d in [".git", "node_modules", "backup", "scripts"]): continue
        for f in files:
            if f.lower().endswith(".pdf"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, workspace_root).replace("\\", "/")
                basename = f.lower()
                if basename not in pdf_on_disk:
                    pdf_on_disk[basename] = []
                # Prioritize /assets/pdfs if duplicate
                if "assets/pdfs" in rel_path:
                    pdf_on_disk[basename].insert(0, rel_path)
                else:
                    pdf_on_disk[basename].append(rel_path)

index_pdfs()

def get_best_category(html_file_path, basename):
    # Try to guess category based on HTML location
    parts = html_file_path.split('/')
    if len(parts) > 1:
        category = parts[0].lower()
        if category in ["ugc", "naac", "iqac", "departments", "placements", "facilities"]:
            return category
    return "general"

def resolve_pdf(html_file_rel, original_link):
    basename = os.path.basename(original_link.split('?')[0].split('#')[0]).lower()
    
    if basename not in pdf_on_disk:
        return None # Missing
    
    current_paths = pdf_on_disk[basename]
    best_path = current_paths[0]
    
    # Step 2: If in legacy /college-detail/, move it
    if "college-detail" in best_path:
        category = get_best_category(html_file_rel, basename)
        target_dir = os.path.join(pdf_target_root, category)
        if not os.path.exists(target_dir): os.makedirs(target_dir)
        
        target_file_path = os.path.join(target_dir, os.path.basename(best_path))
        source_file_path = os.path.join(workspace_root, best_path.replace("/", os.sep))
        
        if not os.path.exists(target_file_path):
            shutil.copy2(source_file_path, target_file_path)
            stats["moved_from_legacy"] += 1
        
        # Re-index
        new_rel = os.path.relpath(target_file_path, workspace_root).replace("\\", "/")
        pdf_on_disk[basename] = [new_rel]
        best_path = new_rel

    # Step 3: Calculate relative path
    html_abs_dir = os.path.dirname(os.path.join(workspace_root, html_file_rel.replace("/", os.sep)))
    target_abs_path = os.path.join(workspace_root, best_path.replace("/", os.sep))
    
    rel_link = os.path.relpath(target_abs_path, html_abs_dir).replace("\\", "/")
    return rel_link

def process_html():
    for root, dirs, files in os.walk(workspace_root):
        if any(d in root for d in [".git", "node_modules", "backup", "scripts"]): continue
        for f in files:
            if f.lower().endswith(".html"):
                file_path = os.path.join(root, f)
                rel_file = os.path.relpath(file_path, workspace_root).replace("\\", "/")
                
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                        content = file.read()
                    
                    new_content = content
                    # Pattern for <a> tags
                    # Pattern for window.open
                    patterns = [
                        (r'href=["\']([^"\'\s]+\.pdf)["\']', 'href="{new_path}"'),
                        (r'window\.open\(["\']([^"\'\s]+\.pdf)["\']', 'window.open("{new_path}"')
                    ]
                    
                    modified = False
                    for pattern, template in patterns:
                        for m in re.finditer(pattern, content):
                            stats["total_links"] += 1
                            original_match = m.group(0)
                            original_link = m.group(1)
                            
                            new_rel_link = resolve_pdf(rel_file, original_link)
                            
                            if new_rel_link:
                                new_match = template.format(new_path=new_rel_link)
                                stats["fixed_links"] += 1
                                if len(stats["samples"]) < 10:
                                    stats["samples"].append(f"{rel_file}: {original_link} -> {new_rel_link}")
                            else:
                                # Missing logic
                                new_match = original_match.replace(f'href="{original_link}"', 'href="#"').replace(f"href='{original_link}'", "href='#'")
                                if 'href="#"' in new_match or "href='#'" in new_match:
                                    if 'onclick' not in new_match:
                                        new_match = new_match.replace('>', " onclick=\"alert('File not available')\">")
                                stats["missing_links"] += 1
                            
                            if original_match != new_match:
                                new_content = new_content.replace(original_match, new_match)
                                modified = True
                    
                    if modified:
                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(new_content)
                            
                except Exception as e:
                    print(f"Error processing {f}: {e}")

process_html()
with open("scripts/rebuild_stats.json", "w") as f:
    json.dump(stats, f, indent=2)

print("Forced Rebuild Complete.")
print(f"Total Found: {stats['total_links']}")
print(f"Total Fixed: {stats['fixed_links']}")
print(f"Missing (Handled): {stats['missing_links']}")
print(f"Recovered from Legacy: {stats['moved_from_legacy']}")
