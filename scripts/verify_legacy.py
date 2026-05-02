
import os
import re

# TARGET THE BACKUP
workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main\backup_legacy_full"

def verify():
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "node_modules"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    broken_links = []
    total_links = 0
    
    patterns = [
        r'href=["\']([^"\':]+)["\']',
        r'src=["\']([^"\':]+)["\']',
    ]

    for html_path in html_files:
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for link in matches:
                    if link.startswith('#') or '://' in link or link.startswith('mailto:'): continue
                    total_links += 1
                    target_full = os.path.normpath(os.path.join(os.path.dirname(html_path), link))
                    if not os.path.exists(target_full):
                        broken_links.append(link)
        except: pass

    print(f"LEGACY BACKUP AUDIT:")
    print(f"Total links: {total_links}")
    print(f"Broken links: {len(broken_links)}")

if __name__ == "__main__":
    verify()
