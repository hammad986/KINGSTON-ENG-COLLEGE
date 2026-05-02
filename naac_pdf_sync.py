import os
import re
from bs4 import BeautifulSoup

# Define root paths
ROOT_DIR = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
NAAC_PDF_DIR = os.path.join(ROOT_DIR, "assets", "pdfs", "naac")
NAAC_HTML_DIR = os.path.join(ROOT_DIR, "naac")

# Metric Regex
METRIC_REGEX = re.compile(r'\d+\.\d+(\.\d+)?')

def get_naac_pdf_mapping():
    mapping = {}
    for root, dirs, files in os.walk(NAAC_PDF_DIR):
        for file in files:
            if "front sheet" in file.lower() and file.endswith(".pdf"):
                full_path = os.path.join(root, file)
                # Try to extract metric from path
                # Example path: ...\Criteria 1\1.1-New\Front Sheet.pdf
                # Example path: ...\Criteria 6\...\4.1.1\Front Sheet.pdf
                
                parts = full_path.replace(NAAC_PDF_DIR, "").split(os.sep)
                metric = None
                for part in reversed(parts):
                    match = METRIC_REGEX.search(part)
                    if match:
                        metric = match.group()
                        break
                
                if metric:
                    if metric not in mapping:
                        mapping[metric] = []
                    # Create relative path from naac/ directory
                    rel_path = os.path.relpath(full_path, NAAC_HTML_DIR).replace("\\", "/")
                    mapping[metric].append(rel_path)
    return mapping

def update_naac_pages(mapping):
    html_files = [f for f in os.listdir(NAAC_HTML_DIR) if f.endswith(".html")]
    
    for filename in html_files:
        filepath = os.path.join(NAAC_HTML_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        
        # 1. Handle standard metric-card
        # <div class="metric-text">... (1.1.1)</div>
        # <div class="metric-links-list">...</div>
        metric_cards = soup.find_all(class_="metric-card")
        for card in metric_cards:
            text_el = card.find(class_="metric-text")
            if text_el:
                metric_match = METRIC_REGEX.search(text_el.get_text())
                if metric_match:
                    metric = metric_match.group()
                    if metric in mapping:
                        links_list = card.find(class_="metric-links-list")
                        if links_list:
                            # Clear existing for this metric as per "hata do us format ko"
                            # But only if we have new front sheets
                            links_list.clear() 
                            for pdf_path in mapping[metric]:
                                new_link = soup.new_tag("a", href=pdf_path, target="_blank", attrs={"class": "evidence-link"})
                                icon = soup.new_tag("i", attrs={"class": "fas fa-file-pdf"})
                                new_link.append(icon)
                                new_link.append(f" {metric} Front Sheet")
                                links_list.append(new_link)
                            modified = True

        # 2. Handle Governance ki-card
        # <div class="ki-code">KI 6.1</div>
        # <div class="metric-links-list">...</div>
        ki_cards = soup.find_all(class_="ki-card")
        for card in ki_cards:
            code_el = card.find(class_="ki-code")
            if code_el:
                metric_match = METRIC_REGEX.search(code_el.get_text())
                if metric_match:
                    metric = metric_match.group()
                    if metric in mapping:
                        links_list = card.find(class_="metric-links-list")
                        if links_list:
                            links_list.clear()
                            for pdf_path in mapping[metric]:
                                new_link = soup.new_tag("a", href=pdf_path, target="_blank", attrs={"class": "evidence-link"})
                                icon = soup.new_tag("i", attrs={"class": "fa-solid fa-file-pdf"})
                                new_link.append(icon)
                                new_link.append(f" {metric} Front Sheet")
                                links_list.append(new_link)
                            modified = True

        # 3. Add toggleKI script if missing (specifically for governance)
        if "naac_governance.html" in filename:
            if "function toggleKI" not in content:
                script_tag = soup.new_tag("script")
                script_tag.string = """
        function toggleKI(header) {
            const card = header.parentElement;
            const allCards = document.querySelectorAll('.ki-card');
            
            allCards.forEach(c => {
                if (c !== card) c.classList.remove('active');
            });
            
            card.classList.toggle('active');
            
            if (card.classList.contains('active')) {
                setTimeout(() => {
                    const rect = card.getBoundingClientRect();
                    const isOutside = rect.top < 100 || rect.bottom > window.innerHeight;
                    if (isOutside) {
                        window.scrollTo({
                            top: window.pageYOffset + rect.top - 120,
                            behavior: 'smooth'
                        });
                    }
                }, 300);
            }
        }
                """
                soup.body.append(script_tag)
                modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            print(f"Updated {filename}")

if __name__ == "__main__":
    mapping = get_naac_pdf_mapping()
    print(f"Found {len(mapping)} metrics with front sheets.")
    update_naac_pages(mapping)
