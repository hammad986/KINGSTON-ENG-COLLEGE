import os
import re
import requests
import urllib.parse

def download_and_map_pdfs(source_file, dest_folder):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    urls = re.findall(r'https://[^\s\'"]+\.pdf', content)
    urls = list(set(urls))
    
    os.makedirs(dest_folder, exist_ok=True)
    mapping = {}
    
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
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                # Use stream to download in chunks, with a timeout for the stream itself
                r = requests.get(url, headers=headers, stream=True, timeout=10)
                r.raise_for_status()
                with open(local_path, 'wb') as pdf_file:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            pdf_file.write(chunk)
                print(f"Success: {safe_name}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                
    # Now replace the URLs in the original file
    new_content = content
    for url, rel_path in mapping.items():
        new_content = new_content.replace(url, rel_path)
        
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {source_file} with {len(mapping)} local PDF links.")

base = r"d:\clg website new"
download_and_map_pdfs(os.path.join(base, "generate_iqac.py"), os.path.join(base, "assets", "pdfs", "iqac"))
