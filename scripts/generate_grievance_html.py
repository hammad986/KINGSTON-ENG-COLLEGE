import re, os

print("Starting HTML generation.")
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Try to find header
header_match = re.search(r'(<div class="floating-side-buttons">.*?</header>)', index_content, re.DOTALL)
if header_match:
    header_html = header_match.group(1)
    print("Extracted header successfully.")
else:
    header_html = ''
    print("Failed to extract header.")

# Try to find footer
footer_match = re.search(r'(<footer class="main-footer">.*?</html>)', index_content, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    print("Extracted footer successfully.")
else:
    footer_html = ''
    print("Failed to extract footer.")

with open('grievance_helpdesk_raw.html', 'r', encoding='utf-8') as f:
    raw_content = f.read()

hero_start = raw_content.find('<section class="grievance-hero">')

if hero_start != -1:
    top_part = raw_content[:hero_start]
    # Clean up the old floating buttons or placeholders from the raw file
    top_part = re.sub(r'<div class="floating-side-buttons">.*?</div>', '', top_part, flags=re.DOTALL)
    top_part = re.sub(r'<div class="mobile-sticky-cta">.*?</div>', '', top_part, flags=re.DOTALL)
    top_part = top_part.replace('<!-- Placeholder for HEADER -->', '')
    
    # Bottom part starts from the hero section
    bottom_part = raw_content[hero_start:]
    
    # Replace the end with footer by finding where AI assistant starts
    ai_widget_start = bottom_part.find('<!-- AI Assistant Widget -->')
    if ai_widget_start != -1:
        bottom_part = bottom_part[:ai_widget_start]
    else:
        # If AI widget isn't found, find the closing body tag
        body_end = bottom_part.find('</body>')
        if body_end != -1:
            bottom_part = bottom_part[:body_end]
            
    final_html = top_part + '\n' + header_html + '\n' + bottom_part + '\n' + footer_html
    
    with open('grievance_helpdesk.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully generated grievance_helpdesk.html!")
else:
    print("Could not find grievance-hero section in the raw file.")
