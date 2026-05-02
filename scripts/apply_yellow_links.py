import os
import re

def update_notice_links():
    root_dir = r'c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main'
    
    # Very permissive regex to catch variations:
    # 1. Backslash or no backslash before the quote in Govt's
    # 2. White or yellow or no style in the anchor
    # 3. Standard text or anchor version
    
    # This pattern matches any variant of the notice span content
    pattern = re.compile(r'Tamil Nadu Govt\\?\'s En kanavu En Ethirkaalam - (?:<a href="events\.html"[^>]*>)?Click Here(?:</a>)?', re.IGNORECASE | re.DOTALL)
    
    # We want to replace the WHOLE content inside the span if possible, or just the matching part.
    # To be safe and standardize, we'll replace the matching part with the perfect version.
    standard_notice = r'Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: #ffc107; text-decoration: underline;">Click Here</a>'

    files_updated = 0
    for filename in os.listdir(root_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(root_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                if pattern.search(content):
                    # Standardize backslashes and colors
                    new_content = pattern.sub(standard_notice, content)
                    
                    # Also ensure the span itself has style="color: white;" if it doesn't already
                    # (This is harder with just regex if the span is outside the match, but most already have it)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_updated += 1
                        # print(f"Updated: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    update_notice_links()
