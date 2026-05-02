import os
from PyPDF2 import PdfReader
import json
import re

def clean_filename(text):
    # Remove special characters and replace spaces with underscores
    text = re.sub(r'[^\w\s-]', '', text).strip()
    text = re.sub(r'[-\s]+', '_', text)
    # Limit length and lowercase
    return text[:50].lower().strip('_') + ".pdf"

pdf_dir = r"assets\pdfs"
mapping = {}
all_pdfs = []

# Recursively find all PDFs
for root, dirs, files in os.walk(pdf_dir):
    for file in files:
        if file.endswith(".pdf"):
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            all_pdfs.append(rel_path)
            old_path = os.path.join(root, file)
            try:
                reader = PdfReader(old_path)
                if len(reader.pages) > 0:
                    first_page = reader.pages[0]
                    text = first_page.extract_text()
                    lines = [line.strip() for line in text.split('\n') if line.strip()]
                    
                    found_heading = False
                    for line in lines:
                        # Skip college name or common headers
                        if any(x in line.upper() for x in ["KINGSTON ENGINEERING COLLEGE", "ISO 9001", "NBA", "NAAC", "AUTONOMOUS"]):
                            continue
                        if len(line) > 5:
                            new_name = clean_filename(line)
                            found_heading = True
                            break
                    
                    if not found_heading:
                        # Fallback to cleaning current name
                        base = os.path.basename(old_path).replace(".pdf", "")
                        # Remove common long prefixes
                        base = re.sub(r'^engineering-resources_.*?_', '', base)
                        base = re.sub(r'^assets_pdf_.*?_', '', base)
                        new_name = clean_filename(base)
                else:
                    new_name = clean_filename(file.replace(".pdf", ""))
            except Exception as e:
                new_name = clean_filename(file.replace(".pdf", ""))
            
            # Ensure unique names in mapping
            target_name = new_name
            counter = 1
            while target_name in mapping.values():
                name_part = new_name.replace(".pdf", "")
                target_name = f"{name_part}_{counter}.pdf"
                counter += 1
            
            mapping[rel_path] = target_name

# Scan HTML files for links
html_links = {}
referenced_pdfs = set()
pdf_pattern = re.compile(r'href=["\'](assets/pdfs/(?:[^"\'>]+)\.pdf)["\']', re.IGNORECASE)

for root, dirs, files in os.walk("."):
    # Skip assets, .git, etc.
    if any(x in root for x in [".git", "assets", ".gemini"]):
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = pdf_pattern.findall(content)
                    if matches:
                        normalized_matches = [m.replace('\\', '/') for m in matches]
                        html_links[path] = normalized_matches
                        for m in normalized_matches:
                            referenced_pdfs.add(m)
            except Exception as e:
                pass

# Compare all_pdfs with referenced_pdfs to find extras
all_pdfs_norm = [p.replace('\\', '/') for p in all_pdfs]
extra_pdfs = [p for p in all_pdfs_norm if p not in referenced_pdfs]

output = {
    "mapping": mapping,
    "html_links": html_links,
    "referenced_pdfs": list(referenced_pdfs),
    "extra_pdfs": extra_pdfs
}

with open('pdf_audit_results.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print(f"Audit complete. Formatted results in pdf_audit_results.json")
print(f"Total PDFs: {len(all_pdfs)}")
print(f"Referenced PDFs: {len(referenced_pdfs)}")
print(f"Extra PDFs: {len(extra_pdfs)}")
