import os

def final_standardize():
    root_dir = r'c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main'
    
    # Simple replacement of the two specific variants we've seen
    # 1. Standardizing to no backslash and yellow color
    
    # Target 1: With backslash and yellow color (from my previous run)
    target1 = 'Tamil Nadu Govt\\\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: #ffc107; text-decoration: underline;">Click Here</a>'
    # Target 2: No backslash and white color (legacy)
    target2 = 'Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: white; text-decoration: underline;">Click Here</a>'
    # Target 3: With backslash and white color (very rare but possible)
    target3 = 'Tamil Nadu Govt\\\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: white; text-decoration: underline;">Click Here</a>'
    
    replacement = 'Tamil Nadu Govt\'s En kanavu En Ethirkaalam - <a href="events.html" style="color: #ffc107; text-decoration: underline;">Click Here</a>'

    files_updated = 0
    for filename in os.listdir(root_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(root_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                new_content = content
                if target1 in new_content:
                    new_content = new_content.replace(target1, replacement)
                if target2 in new_content:
                    new_content = new_content.replace(target2, replacement)
                if target3 in new_content:
                    new_content = new_content.replace(target3, replacement)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    files_updated += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"Total files updated for final standardization: {files_updated}")

if __name__ == "__main__":
    final_standardize()
