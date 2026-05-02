
import re
import os

file_to_check = r'c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main\ugc\ugc_ps_annual_accounts.html'
with open(file_to_check, 'r', encoding='utf-8') as f:
    content = f.read()

patterns = [
    r'(href|src)=["\']([^"\']+\.pdf)["\']',
    r'window\.open\(["\']([^"\']+\.pdf)["\']'
]

print(f"Checking {file_to_check}...")
for p in patterns:
    matches = list(re.finditer(p, content))
    print(f"Pattern {p}: {len(matches)} matches")
    for m in matches:
        print(f" - Found: {m.group(0)}")
        print(f" - Link part: {m.group(2)}")
