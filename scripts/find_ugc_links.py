
import os
import re

root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
ugc_dir = os.path.join(root, "ugc")
missing_dir = os.path.join(root, "missing")

missing_files = os.listdir(missing_dir)
html_files = [os.path.join(ugc_dir, f) for f in os.listdir(ugc_dir) if f.endswith('.html')]

mapping = []

for h in html_files:
    with open(h, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract all .pdf links and some surrounding text
    matches = re.finditer(r'href=["\']([^"\':]+\.pdf)["\']', content)
    for m in matches:
        link = m.group(1)
        # Check if the link target exists
        target_path = os.path.normpath(os.path.join(ugc_dir, link))
        if not os.path.exists(target_path):
            basename = os.path.basename(link)
            # Find closest match in missing_files
            best_match = None
            for mf in missing_files:
                # Match logic: if parts of missing file name are in link
                mf_clean = mf.lower().replace("_", "").replace("-", "").replace(" ", "").replace(".pdf", "")
                link_clean = basename.lower().replace("_", "").replace("-", "").replace(" ", "").replace(".pdf", "")
                
                if mf_clean in link_clean or link_clean in mf_clean:
                    best_match = mf
                    break
            
            if best_match:
                mapping.append({
                    "html": os.path.basename(h),
                    "link": link,
                    "file": best_match
                })
            else:
                # Log the broken link even if no match found
                mapping.append({
                    "html": os.path.basename(h),
                    "link": link,
                    "file": "MISSING_NO_MATCH"
                })

# Output for planning
for item in mapping:
    print(f"{item['html']} -> {item['link']} (Suggest: {item['file']})")
