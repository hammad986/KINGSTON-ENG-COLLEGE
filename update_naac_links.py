import os
import re
import json

def get_metric_id(path):
    path = path.replace('\\', '/')
    filename = os.path.basename(path).lower()
    m = re.findall(r'(\d+[.-]\d+(?:[.-]\d+)?)', filename)
    if m:
        return m[-1][0].replace('-', '.')
    parts = path.split('/')
    for part in reversed(parts[:-1]):
        m = re.search(r'(\d+[.-]\d+(?:[.-]\d+)?)', part)
        if m:
            return m.group(1).replace('-', '.')
    return None

def build_mapping():
    mapping = {}
    root = 'assets/pdfs/naac'
    if not os.path.exists(root):
        print(f"Directory {root} not found")
        return {}
        
    for r, dirs, files in os.walk(root):
        for f in files:
            f_lower = f.lower()
            if f_lower.endswith('.pdf') and ('front sheet' in f_lower or 'front page' in f_lower):
                path = os.path.join(r, f).replace('\\', '/')
                mid = get_metric_id(path)
                if mid:
                    if mid not in mapping:
                        mapping[mid] = []
                    mapping[mid].append(path)
    return mapping

def update_html(filepath, mapping):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    container_pattern = r'metric-links-list|iv-pdf-list|ki-links|pdf-grid|metric-action'
    found_ids = re.findall(r'(\d+\.\d+(?:\.\d+)?)', content)
    unique_ids = sorted(list(set(found_ids)), key=len, reverse=True)

    for search_id in unique_ids:
        target_mids = []
        if len(search_id.split('.')) == 2:
            for m_id in mapping:
                if m_id == search_id or m_id.startswith(search_id + '.'):
                    target_mids.append(m_id)
        else:
            if search_id in mapping:
                target_mids = [search_id]
        
        if not target_mids:
            continue
            
        safe_id = re.escape(search_id)
        pattern = re.compile(
            r'((?:KI\s+|Metric\s+|\()?' + safe_id + r'(?:\))?)'
            r'([\s\S]*?)'
            r'(<(div|ul)\s+class="([^"]*(?:' + container_pattern + r')[^"]*)">)'
            r'([\s\S]*?)'
            r'(</\4>)',
            re.IGNORECASE
        )

        def repl(m):
            header_full = m.group(1)
            intervening = m.group(2)
            start_tag = m.group(3)
            css_class = m.group(5)
            end_tag = m.group(7)
            
            all_paths = []
            for mid in sorted(target_mids):
                all_paths.extend(mapping[mid])
            all_paths = sorted(list(set(all_paths)))
            
            new_links_html = []
            for p in all_paths:
                p_mid = get_metric_id(p)
                label = "Front Sheet"
                if p_mid and len(target_mids) > 1:
                    label = f"Front Sheet ({p_mid})"
                elif 'front page' in p.lower():
                    label = "Front Page"
                
                if "iv-pdf-list" in css_class or "pdf-grid" in css_class:
                    l_class = "iv-pdf-btn" if "iv-pdf-list" in css_class else "pdf-btn"
                    icon = "fa-solid fa-file-pdf"
                else:
                    l_class = "evidence-link"
                    icon = "fas fa-file-pdf"
                
                link = f'<a href="../{p}" target="_blank" class="{l_class}"><i class="{icon}"></i> {label}</a>'
                new_links_html.append(link)
            
            indent = "                        "
            if "iv-pdf-list" in css_class: indent = "                            "
            elif "pdf-grid" in css_class: indent = "                                "
            
            join_str = "\n" + indent
            links_str = join_str.join(new_links_html)
            
            return f"{header_full}{intervening}{start_tag}\n{indent}{links_str}\n{indent[:-4]}{end_tag}"

        new_content, count = pattern.subn(repl, content)
        if count > 0:
            content = new_content
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        # print(f"No changes in {filepath}") # Silencing No changes to focus on updates
        pass

def main():
    mapping = build_mapping()
    html_dir = 'naac'
    if not os.path.exists(html_dir): return
    files = [f for f in os.listdir(html_dir) if f.endswith('.html')]
    for f in files:
        update_html(os.path.join(html_dir, f), mapping)

if __name__ == "__main__":
    main()
