import os

target_link_old = '<a href="#">Grievance & Help Desk</a>'
target_link_new = '<a href="grievance_helpdesk.html">Grievance & Help Desk</a>'

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated = 0

for file in html_files:
    if file == 'grievance_helpdesk_raw.html': 
        continue
        
    content = None
    for enc in ['utf-8', 'cp1252', 'latin-1']:
        try:
            with open(file, 'r', encoding=enc) as f:
                content = f.read()
            break
        except Exception:
            pass
            
    if content and target_link_old in content:
        new_content = content.replace(target_link_old, target_link_new)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1
        
print(f"Successfully updated Grievance link in {updated} files out of {len(html_files)} HTML files.")

# Also doing a quick verification that the grievance_helpdesk.html was created properly
if os.path.exists('grievance_helpdesk.html'):
    size = os.path.getsize('grievance_helpdesk.html')
    print(f"grievance_helpdesk.html exists - Size: {size} bytes")
    
    # Check if header & footer injected correctly
    with open('grievance_helpdesk.html', 'r', encoding='utf-8') as f:
        gh_content = f.read()
        has_header = 'main-header' in gh_content
        has_footer = 'main-footer' in gh_content
        has_cards = 'grievance-grid' in gh_content
        print(f"Contains Base header: {has_header}, footer: {has_footer}, cards: {has_cards}")
else:
    print("WARNING: grievance_helpdesk.html not found!")

