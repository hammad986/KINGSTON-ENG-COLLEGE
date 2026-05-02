
import os
import re
import json
from collections import defaultdict

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

def get_all_files():
    all_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "node_modules", "backup_legacy"]):
            continue
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def analyze_links(all_files):
    pdf_usage = defaultdict(list)
    html_links = defaultdict(list)
    js_nav = defaultdict(list)
    absolute_paths = []
    
    # regex patterns
    patterns = {
        "href": r'href=["\']([^"\']+)["\']',
        "src": r'src=["\']([^"\']+)["\']',
        "js_open": r'window\.open\(["\']([^"\']+)["\']',
        "js_location": r'location\.href\s*=\s*["\']([^"\']+)["\']'
    }

    for file_path in all_files:
        rel_file_path = os.path.relpath(file_path, workspace_root)
        if file_path.lower().endswith(('.html', '.js', '.css')):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for key, pattern in patterns.items():
                        matches = re.findall(pattern, content)
                        for m in matches:
                            # Normalize
                            clean_m = m.split('?')[0].split('#')[0]
                            
                            # Detect absolute paths
                            if clean_m.startswith('/') and not clean_m.startswith('//'):
                                absolute_paths.append({"file": rel_file_path, "link": m})
                            
                            if clean_m.lower().endswith('.pdf'):
                                pdf_usage[clean_m].append(rel_file_path)
                            
                            if key.startswith('js_'):
                                js_nav[rel_file_path].append(m)
                            
                            if file_path.lower().endswith('.html') and key in ('href', 'src'):
                                html_links[rel_file_path].append(m)
                                
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                
    return {
        "pdf_usage": dict(pdf_usage),
        "html_links": dict(html_links),
        "js_nav": dict(js_nav),
        "absolute_paths": absolute_paths
    }

def detect_collisions(all_files):
    collisions = defaultdict(list)
    for f in all_files:
        name = os.path.basename(f)
        collisions[name].append(os.path.relpath(f, workspace_root))
    
    return {k: v for k, v in collisions.items() if len(v) > 1}

def run_analysis():
    all_files = get_all_files()
    analysis = analyze_links(all_files)
    collisions = detect_collisions(all_files)
    
    report = {
        "summary": {
            "total_files": len(all_files),
            "html_files": len([f for f in all_files if f.endswith('.html')]),
            "pdf_files": len([f for f in all_files if f.endswith('.pdf')]),
            "js_files": len([f for f in all_files if f.endswith('.js')]),
            "py_files": len([f for f in all_files if f.endswith('.py')]),
        },
        "pdf_usage": analysis["pdf_usage"],
        "js_navigation": analysis["js_nav"],
        "absolute_paths": analysis["absolute_paths"],
        "collisions": collisions,
        "all_files_rel": [os.path.relpath(f, workspace_root) for f in all_files]
    }
    
    with open("comprehensive_analysis.json", "w") as f:
        json.dump(report, f, indent=4)
    print("Comprehensive Pre-Analysis Complete. Saved to comprehensive_analysis.json")

if __name__ == "__main__":
    run_analysis()
