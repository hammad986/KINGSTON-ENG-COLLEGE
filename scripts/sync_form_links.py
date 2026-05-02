import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# Patterns for the buttons and links
# <a href="#" class="btn-side bg-light-gray text-black rotate-text">Apply Now</a>
# <a href="#" class="btn-side bg-brand-yellow text-black rotate-text">Admission Enquiry</a>

patterns = [
    (r'<a href="[^"]*"([^>]*?)>Apply Now</a>', r'<a href="apply_now.html"\1>Apply Now</a>'),
    (r'<a href="[^"]*"([^>]*?)>Admission Enquiry</a>', r'<a href="admission_enquiry.html"\1>Admission Enquiry</a>'),
    # Also catch some top bar links if they exist
    (r'<li><a href="[^"]*">Apply Now</a></li>', r'<li><a href="apply_now.html">Apply Now</a></li>'),
    (r'<li><a href="[^"]*">Admission Enquiry</a></li>', r'<li><a href="admission_enquiry.html">Admission Enquiry</a></li>'),
]

for filename in files:
    content = None
    for enc in ['utf-8', 'cp1252', 'latin-1']:
        try:
            with open(filename, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        continue

    new_content = content
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
