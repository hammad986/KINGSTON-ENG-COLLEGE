import os
from PyPDF2 import PdfReader
import json
import re

def clean_filename(text):
    # Remove special characters and replace spaces with underscores
    text = re.sub(r'[^\w\s-]', '', text).strip()
    text = re.sub(r'[-\s]+', '_', text)
    return text.lower()

pdf_dir = r"assets\pdfs"
mapping = {}

# Recursively find all PDFs
for root, dirs, files in os.walk(pdf_dir):
    for file in files:
        if file.endswith(".pdf"):
            old_path = os.path.join(root, file)
            try:
                reader = PdfReader(old_path)
                first_page = reader.pages[0]
                text = first_page.extract_text()
                
                # Try to find a heading in the first few lines
                lines = [line.strip() for line in text.split('\n') if line.strip()]
                if lines:
                    # Often the first line is the name of the college, so check next lines
                    heading = lines[0]
                    if "KINGSTON" in heading.upper() and len(lines) > 1:
                        heading = lines[1]
                    
                    new_name = clean_filename(heading) + ".pdf"
                else:
                    new_name = clean_filename(file.replace(".pdf", "")) + ".pdf"
            except Exception as e:
                new_name = clean_filename(file.replace(".pdf", "")) + ".pdf"
            
            mapping[old_path] = new_name

print(json.dumps(mapping, indent=2))
