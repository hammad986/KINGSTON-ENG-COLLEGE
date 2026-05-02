import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# We want to find patterns like <a href="..." ...>Policies</a>
# And replace the href with policies.html
pattern = r'(<a\s+[^>]*href=["\'])([^"\']*?)(["\'][^>]*>\s*Policies\s*<\/a>)'

for filename in files:
    if filename == 'policies.html':
        continue
    
    content = None
    for enc in ['utf-8', 'cp1252', 'latin-1']:
        try:
            with open(filename, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        print(f"Skipping {filename} due to encoding issues")
        continue

    new_content = re.sub(pattern, r'\1policies.html\3', content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
