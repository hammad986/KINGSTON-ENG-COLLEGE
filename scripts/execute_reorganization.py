
import os
import json
import shutil
import re

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
mapping_file = "movement_mapping.json"

def calculate_relative_path(from_file, to_file):
    # Both paths are relative to workspace_root
    from_dir = os.path.dirname(from_file)
    try:
        rel_path = os.path.relpath(to_file, from_dir)
        return rel_path.replace('\\', '/')
    except ValueError:
        return to_file

def refactor_links():
    with open(mapping_file, "r") as f:
        mapping = json.load(f)

    # Flatten categories for easier lookup
    # mapping is old_rel -> new_rel
    
    # We need to know which new files exist
    # (Including those that stayed in root)
    all_files_new_location = {}
    for old, new in mapping.items():
        all_files_new_location[old] = new
    
    # For files that stayed in root (and weren't in mapping), we need them too
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "backup_mapping", "assets/css", "assets/js"]): continue
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), workspace_root)
            if rel not in all_files_new_location:
                all_files_new_location[rel] = rel

    # Pass 1: Move Files
    print("Step 1: Moving Files...")
    moved_count = 0
    for old, new in mapping.items():
        src = os.path.join(workspace_root, old)
        dest = os.path.join(workspace_root, new)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            # Use copy2 then remove to handle cross-drive if necessary (shutil.move does this anyway)
            shutil.move(src, dest)
            moved_count += 1
    print(f"Moved {moved_count} files.")

    # Pass 2: Update Links in HTML
    print("Step 2: Refactoring Links...")
    # New locations of all HTML files
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "assets/css"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    patterns = [
        (r'href=["\']([^"\':]+)["\']', 'href'), # Exclude external links with ':'
        (r'src=["\']([^"\':]+)["\']', 'src'),
    ]

    for html_path in html_files:
        rel_html_path = os.path.relpath(html_path, workspace_root)
        changed = False
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            new_content = content
            # Find all potential links
            for pattern, attr in patterns:
                matches = re.findall(pattern, content)
                for old_link in set(matches):
                    # Skip anchor-only or absolute web links
                    if old_link.startswith('#') or '://' in old_link or old_link.startswith('mailto:'):
                        continue
                    
                    # Resolve what file this link points to RELATIVE to the OLD location of the HTML file
                    # This is the hard part. We need to know where the HTML file WAS.
                    # Let's find the old path of this HTML file
                    old_rel_html = None
                    for o, n in mapping.items():
                        if n.replace('/', os.sep).replace('\\', os.sep) == rel_html_path:
                            old_rel_html = o
                            break
                    if not old_rel_html:
                        old_rel_html = rel_html_path # It stayed in root
                    
                    # Target relative to old host
                    target_old_rel = os.path.normpath(os.path.join(os.path.dirname(old_rel_html), old_link))
                    
                    # Does this target exist in our mapping?
                    target_new_rel = None
                    # Search mapping (case invariant for windows)
                    for o, n in all_files_new_location.items():
                        if o.lower().replace('/', os.sep).replace('\\', os.sep) == target_old_rel.lower().replace('/', os.sep).replace('\\', os.sep):
                            target_new_rel = n
                            break
                    
                    if target_new_rel:
                        # Calculate NEW relative link
                        new_link = calculate_relative_path(rel_html_path, target_new_rel)
                        if new_link != old_link:
                            # Strict replacement to avoid partial matches
                            # We use re.sub with escaped old_link to be safe
                            escaped_old = re.escape(old_link)
                            placeholder = f'{attr}="{new_link}"'
                            # Handle both single and double quotes
                            new_content = re.sub(f'{attr}=["\']{escaped_old}["\']', placeholder, new_content)
                            changed = True
            
            if changed:
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Refactored: {rel_html_path}")
                
        except Exception as e:
            print(f"Error processing {html_path}: {e}")

    print("Reorganization and Refactoring Complete.")

if __name__ == "__main__":
    refactor_links()
