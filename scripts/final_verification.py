
import os
import re
import json

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

verification = {
    "total_checked": 0,
    "pass": 0,
    "fail": 0,
    "broken_links": []
}

for root, dirs, files in os.walk(workspace_root):
    if any(d in root for d in [".git", "node_modules", "backup", "scripts"]): continue
    for f in files:
        if f.lower().endswith(".html"):
            file_path = os.path.join(root, f)
            rel_file = os.path.relpath(file_path, workspace_root).replace("\\", "/")
            
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                
                # Check EVERY href and window.open
                links = re.findall(r'href=["\']([^"\'#\s]+\.pdf)["\']', content)
                links += re.findall(r'window\.open\(["\']([^"\'#\s]+\.pdf)["\']', content)
                
                for link in links:
                    verification["total_checked"] += 1
                    # Resolve relative to HTML file
                    html_dir = os.path.dirname(file_path)
                    target_abs = os.path.abspath(os.path.join(html_dir, link.replace("/", os.sep)))
                    
                    if os.path.exists(target_abs):
                        verification["pass"] += 1
                    else:
                        verification["fail"] += 1
                        verification["broken_links"].append({
                            "html": rel_file,
                            "link": link,
                            "resolved_to": os.path.relpath(target_abs, workspace_root)
                        })
            except Exception as e:
                print(f"Error checking {f}: {e}")

with open("scripts/final_verification.json", "w") as f:
    json.dump(verification, f, indent=2)

print("Final Verification Complete.")
print(f"Total PDF Links Checked: {verification['total_checked']}")
print(f"Passed (Physically Opens): {verification['pass']}")
print(f"Failed (404 Broken): {verification['fail']}")
