import os
import re
import urllib.request
import urllib.parse
import ssl

def download_and_map_pdfs(source_file, dest_folder):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    urls = re.findall(r'https://[^\s\'"]+\.pdf', content)
    urls = list(set(urls))
    
    os.makedirs(dest_folder, exist_ok=True)
    mapping = {}
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    for url in urls:
        parsed = urllib.parse.urlparse(url)
        safe_name = parsed.path.strip('/').replace('/', '_')
        if not safe_name.endswith('.pdf'):
            safe_name += '.pdf'
            
        local_path = os.path.join(dest_folder, safe_name)
        relative_path = os.path.relpath(local_path, r"d:\clg website new").replace('\\', '/')
        
        mapping[url] = relative_path
        
        if not os.path.exists(local_path):
            print(f"Downloading {url} ...")
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, context=ctx, timeout=15) as response, open(local_path, 'wb') as out_file:
                    out_file.write(response.read())
                print(f"Success: {safe_name}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                
    new_content = content
    for url, rel_path in mapping.items():
        new_content = new_content.replace(url, rel_path)
        
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {source_file} with local PDF links.")

base = r"d:\clg website new"
download_and_map_pdfs(os.path.join(base, "generate_iqac.py"), os.path.join(base, "assets", "pdfs", "iqac"))
