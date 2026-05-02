import os
import re
import json

html_dir = r"."
pdf_links = {} # {html_file: [linked_pdfs]}
all_found_pdfs = set()

# Regex to find links to PDFs in assets/pdfs/
pdf_pattern = re.compile(r'href=["\'](assets/pdfs/(?:[^"\'>]+)\.pdf)["\']', re.IGNORECASE)

for root, dirs, files in os.walk(html_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = pdf_pattern.findall(content)
                    if matches:
                        # Normalize paths to use forward slashes for the report
                        normalized_matches = [m.replace('\\', '/') for m in matches]
                        pdf_links[path] = normalized_matches
                        for m in normalized_matches:
                            all_found_pdfs.add(m)
            except Exception as e:
                print(f"Error reading {path}: {e}")

# Save the results
with open('html_pdf_links.json', 'w', encoding='utf-8') as f:
    json.dump({"links": pdf_links, "referenced_pdfs": list(all_found_pdfs)}, f, indent=2)

print(f"Found {len(all_found_pdfs)} unique PDF links across {len(pdf_links)} HTML files.")
