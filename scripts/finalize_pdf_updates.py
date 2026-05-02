import os
import json
import re

# Set encoding for entire process
import sys
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

def clean_filename(text):
    text = re.sub(r'[^\w\s-]', '', text).strip()
    text = re.sub(r'[-\s]+', '_', text)
    return text.lower()

# Load the audit results
try:
    with open('pdf_audit_results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading pdf_audit_results.json: {e}")
    sys.exit(1)

mapping = data.get('mapping', {})
html_links = data.get('html_links', {})
extra_pdfs = data.get('extra_pdfs', [])

# 1. Rename PDF files in assets/pdfs/
renamed_count = 0
for old_rel_path, new_name in mapping.items():
    old_full_path = os.path.abspath(old_rel_path)
    new_full_path = os.path.join(os.path.dirname(old_full_path), new_name)
    
    # Skip if file already has the target name or doesn't exist
    if not os.path.exists(old_full_path):
        continue
    if old_full_path.lower() == new_full_path.lower():
        continue
        
    try:
        # Check if target already exists (handle collisions)
        if os.path.exists(new_full_path):
            base, ext = os.path.splitext(new_full_path)
            counter = 1
            while os.path.exists(f"{base}_{counter}{ext}"):
                counter += 1
            new_full_path = f"{base}_{counter}{ext}"
            new_name = os.path.basename(new_full_path)

        os.rename(old_full_path, new_full_path)
        # Update mapping with final name used
        mapping[old_rel_path] = new_name
        renamed_count += 1
        print(f"Renamed: {os.path.basename(old_rel_path)} -> {new_name}")
    except Exception as e:
        print(f"Error renaming {old_rel_path}: {e}")

# 2. Update HTML files
updated_html_count = 0
for html_file, links in html_links.items():
    if not os.path.exists(html_file):
        continue
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        updated_content = content
        for old_link in links:
            # old_link is like "assets/pdfs/something.pdf"
            # we need to find the mapping entry for it
            # paths in mapping are OS specific, let's normalize
            target_key = None
            for k in mapping:
                if k.replace('\\', '/') == old_link:
                    target_key = k
                    break
            
            if target_key:
                new_filename = mapping[target_key]
                new_link = old_link.rsplit('/', 1)[0] + '/' + new_filename
                updated_content = updated_content.replace(old_link, new_link)
        
        if updated_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_html_count += 1
            print(f"Updated: {os.path.basename(html_file)}")
    except Exception as e:
        print(f"Error updating {html_file}: {e}")

print(f"\nSummary:")
print(f"Renamed {renamed_count} PDF files.")
print(f"Updated {updated_html_count} HTML files.")
print(f"\nExtra PDFs (unreferenced):")
for p in extra_pdfs:
    print(f"- {p}")
