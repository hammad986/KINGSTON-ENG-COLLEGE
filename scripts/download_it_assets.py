import requests
import os

def download_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Get filename from URL, but handle potential query params/encoded chars
    name = url.split('/')[-1]
    local_filename = os.path.join(folder, name)
    try:
        r = requests.get(url, stream=True, timeout=10)
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {local_filename}")
        return local_filename
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

urls = [
    "https://engineering.kingston.ac.in/assets/images/departments/IT/R2021-B.TECH-IT.pdf",
    "https://engineering.kingston.ac.in/assets/images/departments/IT/R2017-B.TECH-IT.pdf",
    "https://engineering.kingston.ac.in/assets/images/departments/IT/R2013-B.TECH-IT.pdf",
    "https://engineering.kingston.ac.in/assets/pdf/placement-report/campus-hiring.pdf"
]

current_dir = os.getcwd()
asset_dir = os.path.join(current_dir, "assets", "it")

for url in urls:
    download_file(url, asset_dir)
