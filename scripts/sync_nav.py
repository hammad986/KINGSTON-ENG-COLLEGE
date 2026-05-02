import os
import re

link_to_insert = '                    <li><a href="policies.html">Policies</a></li>\n'

files = [f for f in os.listdir('.') if f.endswith('.html')]

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
        continue

    # If already has policies.html, skip
    if 'policies.html' in content:
        continue
    
    # Try to insert before Placements
    if '>Placements</a>' in content:
        # Finding the <li> that contains Placements
        new_content = re.sub(r'(<li>\s*<a\s+[^>]*>Placements<\/a>)', r'<li><a href="policies.html">Policies</a></li>\n\1', content, flags=re.IGNORECASE)
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
    elif '>IQAC</a>' in content:
        # Fallback: insert before IQAC
        new_content = re.sub(r'(<li>\s*<a\s+[^>]*>IQAC<\/a>)', r'<li><a href="policies.html">Policies</a></li>\n\1', content, flags=re.IGNORECASE)
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename} (before IQAC)")

import re # forgot to import re in the block above but it's fine if I add it here or restart
