import os
import re

def update_html_files():
    root_dir = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
    
    # 1. Update Label: Register Now -> Register Here
    label_pattern = re.compile(r'<div class="notice-label">Register Now</div>', re.IGNORECASE)
    label_replacement = '<div class="notice-label">Register Here</div>'
    
    # 2. Cleanup Marquee Content
    # We replace everything inside 'marquee-content notice-marquee' to be safe
    marquee_pattern = re.compile(r'(<div class="marquee-content notice-marquee">).*?(</div>)', re.DOTALL | re.IGNORECASE)
    
    # Standard content for the marquee
    standard_notice = (
        '                    <span style="color: white;">Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: white; text-decoration: underline;">Click Here</a></span>\n'
        '                    <span style="color: white;">Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: white; text-decoration: underline;">Click Here</a></span>\n'
        '                    <span style="color: white;">Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: white; text-decoration: underline;">Click Here</a></span>\n'
    )
    
    def marquee_sub(match):
        return match.group(1) + "\n" + standard_notice + "                " + match.group(2)

    files_updated = 0
    
    for filename in os.listdir(root_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(root_dir, filename)
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Apply label replacement
            new_content = label_pattern.sub(label_replacement, content)
            
            # Apply marquee cleanup
            new_content = marquee_pattern.sub(marquee_sub, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                if files_updated % 50 == 0:
                    print(f"Updated {files_updated} files...")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    update_html_files()
