import os
import glob
import re

def fix_logo_dimensions():
    base_dir = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
    html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)
    
    count = 0
    # We are looking to remove width="100" height="150" from the blue-horizontal logo
    target = 'width="100" height="150"'
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original = content
            
            # Simple replace since ONLY THAT ONE LOGO had this exact string in the entire site template.
            # But to be extremely safe, let's only do it near 'blue-horizontal.png'
            if 'blue-horizontal.png' in content and target in content:
                content = content.replace(target, '')

            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
        except Exception as e:
            pass
            
    print(f"Removed inline dimensions from {count} files.")

if __name__ == "__main__":
    fix_logo_dimensions()
