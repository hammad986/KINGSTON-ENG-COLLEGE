import requests
import os

def download_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    name = url.split('/')[-1]
    local_filename = os.path.join(folder, name)
    try:
        r = requests.get(url, stream=True, timeout=15)
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
    "https://engineering.kingston.ac.in/assets/pdf/departments/mech/R2021-B.E-MECH.pdf",
    "https://engineering.kingston.ac.in/assets/pdf/departments/mech/R2017-B.E-MECH.pdf",
    "https://engineering.kingston.ac.in/assets/pdf/departments/mech/R2013-B.E-MECH.pdf",
    "https://engineering.kingston.ac.in/assets/pdf/departments/mech/R2021-M.E-MECH.pdf",
    "https://engineering.kingston.ac.in/assets/pdf/departments/mech/R2017-M.E-MECH.pdf"
]

current_dir = os.getcwd()
asset_dir = os.path.join(current_dir, "assets", "mech")

for url in urls:
    download_file(url, asset_dir)
