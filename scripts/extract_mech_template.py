import os

def extract_template():
    try:
        with open('dept_mechanical.html', 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Robust splitting
        start_tag = '<main class="dept-main-content">'
        end_tag = '</main>'
        
        if start_tag in html and end_tag in html:
            parts = html.split(start_tag)
            header = parts[0] + start_tag
            
            rest = parts[1].split(end_tag)
            footer = end_tag + rest[1]
            
            with open('mech_header.txt', 'w', encoding='utf-8') as f: f.write(header)
            with open('mech_footer.txt', 'w', encoding='utf-8') as f: f.write(footer)
            print("MECH Templates extracted successfully to mech_header.txt and mech_footer.txt")
        else:
            print("Error: Could not find split tags in dept_mechanical.html")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_template()
