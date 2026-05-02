import os
import re

def normalize_paths(content, prefix):
    if not prefix:
        return content
    
    def repl(match):
        attr = match.group(1)
        path = match.group(2)
        if path.startswith(('http', '#', 'mailto:', 'tel:', 'javascript:', 'https')) or path.startswith(prefix):
            return f'{attr}="{path}"'
        return f'{attr}="{prefix}{path}"'

    pattern = r'(src|href)="([^"]+)"'
    return re.sub(pattern, repl, content)

def strip_redundant_styles(content):
    pattern = r'<style[^>]*>.*?(?:\.hero-slides-wrap|\.ai-widget-box).*?<\/style>'
    return re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)

def extract_master_blocks():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
    if not body_match:
        raise ValueError("Could not find <body> in index.html")
    body_end_pos = body_match.end()

    hero_start = content.find('<section class="hero-section">')
    if hero_start == -1:
        raise ValueError("Could not find <section class=\"hero-section\"> in index.html")
    
    hero_end = content.find('</section>', hero_start) + len('</section>')
    
    top_block = content[body_end_pos:hero_end]

    footer_start = content.find('<footer class="main-footer">')
    if footer_start == -1:
        raise ValueError("Could not find <footer class=\"main-footer\"> in index.html")
    
    body_close_start = content.lower().find('</body>', footer_start)
    if body_close_start == -1:
        raise ValueError("Could not find </body> in index.html")
    
    bottom_block = content[footer_start:body_close_start]
    
    return top_block, bottom_block

def sync_file(filepath, top_block, bottom_block):
    rel_path = os.path.relpath(filepath, '.')
    depth = rel_path.count(os.sep)
    prefix = "../" * depth

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = strip_redundant_styles(content)

    top_shell = normalize_paths(top_block, prefix)
    bottom_shell = normalize_paths(bottom_block, prefix)

    new_content = content
    
    body_match = re.search(r'<body[^>]*>', new_content, re.IGNORECASE)
    if body_match:
        body_end_pos = body_match.end()
        hero_start = new_content.find('<section class="hero-section">')
        if hero_start != -1:
             hero_end = new_content.find('</section>', hero_start) + len('</section>')
             new_content = new_content[:body_end_pos] + top_shell + new_content[hero_end:]
        else:
             header_end = new_content.lower().find('</header>', body_end_pos)
             if header_end != -1:
                 next_section_end = new_content.lower().find('</section>', header_end)
                 if next_section_end != -1:
                     stop_pos = next_section_end + len('</section>')
                     new_content = new_content[:body_end_pos] + top_shell + new_content[stop_pos:]
                 else:
                     stop_pos = header_end + len('</header>')
                     new_content = new_content[:body_end_pos] + top_shell + new_content[stop_pos:]

    footer_start = new_content.lower().find('<footer')
    body_end_start = new_content.lower().find('</body>')
    
    if footer_start != -1 and body_end_start != -1:
         new_content = new_content[:footer_start] + bottom_shell + new_content[body_end_start:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Synced: {filepath}")

def main():
    top_block, bottom_block = extract_master_blocks()
    print(f"Extracted Top Block length: {len(top_block)}")
    print(f"Extracted Bottom Block length: {len(bottom_block)}")
    
    skip_files = ['index.html']
    count = 0
    for root, dirs, files in os.walk('.'):
        if '.git' in dirs: dirs.remove('.git')
        if 'assets' in dirs: dirs.remove('assets') 

        for file in files:
            if file.endswith('.html') and file not in skip_files:
                filepath = os.path.join(root, file)
                try:
                    sync_file(filepath, top_block, bottom_block)
                    count += 1
                except Exception as e:
                    print(f"Error syncing {filepath}: {e}")
                    
    print(f"Total files synced: {count}")

if __name__ == "__main__":
    main()
