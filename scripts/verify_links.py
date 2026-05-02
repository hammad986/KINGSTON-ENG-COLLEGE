
import os
import re

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

def verify():
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "backup_mapping", "assets/css", "node_modules"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    broken_links = []
    total_links = 0
    pdf_count = 0
    
    patterns = [
        r'href=["\']([^"\':]+)["\']',
        r'src=["\']([^"\':]+)["\']',
    ]

    print(f"Auditing {len(html_files)} files...")

    for html_path in html_files:
        rel_html = os.path.relpath(html_path, workspace_root)
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for link in matches:
                    if link.startswith('#') or '://' in link or link.startswith('mailto:'):
                        continue
                    
                    total_links += 1
                    # Resolve link relative to HTML file
                    target_full = os.path.normpath(os.path.join(os.path.dirname(html_path), link))
                    
                    if not os.path.exists(target_full):
                        # Potential broken link
                        broken_links.append({
                            "file": rel_html,
                            "link": link,
                            "resolved": os.path.relpath(target_full, workspace_root) if target_full.startswith(workspace_root) else target_full
                        })
                    
                    if link.lower().endswith('.pdf'):
                        pdf_count += 1
                        
        except Exception as e:
            print(f"Error reading {html_path}: {e}")

    print("\n--- AUDIT REPORT ---")
    print(f"Total links checked: {total_links}")
    print(f"Total PDF links found: {pdf_count}")
    print(f"Broken links found: {len(broken_links)}")
    
    if broken_links:
        print("\nBroken Link Details:")
        for b in broken_links[:20]: # Show first 20
            print(f"  [{b['file']}] -> {b['link']} (points to non-existent {b['resolved']})")
        
        if len(broken_links) > 20:
            print(f"  ... and {len(broken_links)-20} more.")
            
    return len(broken_links) == 0

if __name__ == "__main__":
    success = verify()
    if success:
        print("\nSUCCESS: 0 broken links detected.")
    else:
        print("\nFAILURE: Broken links detected. Recheck mapping/refactor logic.")
