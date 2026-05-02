import os
import re
import urllib.parse

src = r"d:\clg website new\generate_iqac.py"
with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'https://[^\s\'"]+\.pdf', content)
dest_folder = r"d:\clg website new\assets\pdfs\iqac"

count = 0
for url in set(urls):
    parsed = urllib.parse.urlparse(url)
    safe_name = parsed.path.strip('/').replace('/', '_')
    if not safe_name.endswith('.pdf'):
        safe_name += '.pdf'
    local_path = os.path.join(dest_folder, safe_name)
    
    if os.path.exists(local_path):
        rel_path = f"assets/pdfs/iqac/{safe_name}"
        content = content.replace(url, rel_path)
        count += 1

with open(src, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Mapped {count} PDFs to local assets.")
