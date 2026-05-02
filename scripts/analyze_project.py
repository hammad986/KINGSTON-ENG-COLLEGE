
import os
import re
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

def get_all_files():
    all_files = []
    for root, dirs, files in os.walk(workspace_root):
        if ".git" in root or "node_modules" in root:
            continue
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def get_references(all_files):
    refs = set()
    # Patterns for links in HTML/CSS/JS
    patterns = [
        r'href=["\']([^"\']+)["\']',
        r'src=["\']([^"\']+)["\']',
        r'url\(["\']?([^"\'\)]+)["\']?\)',
    ]
    
    for file_path in all_files:
        if file_path.lower().endswith(('.html', '.css', '.js')):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for pattern in patterns:
                        matches = re.findall(pattern, content)
                        for m in matches:
                            # Normalize path: ignore external links, data-uris, hashes
                            if m.startswith(('http', 'https', 'mailto:', 'tel:', '#', 'data:')):
                                continue
                            # Clean potential query params or hashes
                            clean_m = m.split('?')[0].split('#')[0]
                            refs.add(clean_m)
            except Exception:
                pass
    return refs

def analyze():
    all_files = get_all_files()
    refs = get_references(all_files)
    
    analysis = {
        "py_files": [],
        "html_files": [],
        "css_files": [],
        "js_files": [],
        "image_files": [],
        "pdf_files": [],
        "metadata_files": [], # .txt, .json, .csv, .md
        "unused_files": [],
        "total_files": len(all_files)
    }
    
    # Normalize refs for searching (convert to absolute paths or relative from root)
    # This is tricky because refs are relative to the file they are in.
    # For now, let's just collect names to see what's used.
    ref_names = {os.path.basename(r) for r in refs}

    for file_path in all_files:
        rel_path = os.path.relpath(file_path, workspace_root)
        file_name = os.path.basename(file_path)
        ext = file_name.split('.')[-1].lower() if '.' in file_name else ''
        
        if file_path.startswith(os.path.join(workspace_root, ".git")) or "node_modules" in file_path:
            continue
            
        if ext == 'py':
            analysis["py_files"].append(rel_path)
        elif ext == 'html':
            analysis["html_files"].append(rel_path)
        elif ext == 'css':
            analysis["css_files"].append(rel_path)
        elif ext == 'js':
            analysis["js_files"].append(rel_path)
        elif ext in ('png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'ico'):
            analysis["image_files"].append(rel_path)
        elif ext == 'pdf':
            analysis["pdf_files"].append(rel_path)
        elif ext in ('txt', 'json', 'csv', 'md'):
            analysis["metadata_files"].append(rel_path)
            
        # Check if unused (Very simplistic check: if filename is in any ref)
        if ext in ('png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'pdf', 'mp4'):
            if file_name not in ref_names:
                analysis["unused_files"].append(rel_path)
                
    return analysis

if __name__ == "__main__":
    result = analyze()
    with open("project_analysis.json", "w") as f:
        json.dump(result, f, indent=4)
    print("Analysis complete. See project_analysis.json")
