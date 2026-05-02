import os
import re

def update_html_files():
    root_dir = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
    
    # regex for header notice
    # Target: <span>Tamil Nadu Govt's En kanavu En Ethirkaalam - Click Here</span>
    # Note: Using regex to handle potential whitespace or small variations
    header_pattern = re.compile(r'<span>Tamil Nadu Govt\'s En kanavu En Ethirkaalam - Click Here</span>', re.IGNORECASE)
    header_replacement = '<span style="color: white;">Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: white; text-decoration: underline;">Click Here</a></span>'
    
    # regex for footer privacy policy
    # Target: <a href="#">Privacy Policy</a> or similar links in footer-bottom-links
    # We want to ensure it points to privacy_policy.html
    footer_pattern = re.compile(r'<a\s+href=["\'](?:#|privacy_policy\.html)?["\']\s*>Privacy Policy</a>', re.IGNORECASE)
    footer_replacement = '<a href="privacy_policy.html">Privacy Policy</a>'

    files_updated = 0
    
    for filename in os.listdir(root_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(root_dir, filename)
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            new_content = header_pattern.sub(header_replacement, content)
            new_content = footer_pattern.sub(footer_replacement, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f"Updated: {filename}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    update_html_files()
