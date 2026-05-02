import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# The target block to replace
# We focus on the Facilities dropdown structure
# We'll use a more flexible regex to find the Facilities li and its ul

pattern = r'(<li class="has-dropdown">\s*<a href=")#(">\s*Facilities\s*<\/a>\s*<ul class="dropdown js-exclude-dropdown">)(\s*<li><a href="facilities_infrastructure.html">Infrastructure<\/a><\/li>)(\s*<li><a href="facilities.html">Facilities<\/a><\/li>)?(\s*<li><a href=")#(">\s*Event Gallery\s*<\/a><\/li>)(\s*<li><a href=")#(">\s*Blog\s*<\/a><\/li>)(\s*<li><a href=")#(">\s*IT Infrastructure\s*<\/a><\/li>)(\s*<li><a href=")#(">\s*Library\s*<\/a><\/li>)(\s*<li><a href=")#(">\s*Welfare Measures\s*<\/a><\/li>)'

# Replacement parts
# 1: link for Facilities -> facilities.html
# 5: link for Event Gallery -> facilities_event_gallery.html
# 9: link for Blog -> blog.html
# 13: link for IT -> facilities_it.html
# 17: link for Library -> facilities_library.html
# 21: link for Welfare -> facilities_welfare.html

# Wait, the numbering in regex above is:
# 1: (<li class="has-dropdown">\s*<a href=")
# 2: (#)
# 3: (">\s*Facilities\s*<\/a>\s*<ul class="dropdown js-exclude-dropdown">)
# 4: (\s*<li><a href="facilities_infrastructure.html">Infrastructure<\/a><\/li>)
# 5: (\s*<li><a href="facilities.html">Facilities<\/a><\/li>)?  <-- This is the duplicate one to remove
# 6: (\s*<li><a href=")
# 7: (#)
# 8: (">\s*Event Gallery\s*<\/a><\/li>)
# ... and so on

def get_replacement(match):
    # Construct the new navigation block
    indent = "                    "
    res = f'<li class="has-dropdown">\n{indent}    <a href="facilities.html">Facilities</a>\n'
    res += f'{indent}    <ul class="dropdown js-exclude-dropdown">\n'
    res += f'{indent}        <li><a href="facilities_infrastructure.html">Infrastructure</a></li>\n'
    res += f'{indent}        <li><a href="facilities_event_gallery.html">Event Gallery</a></li>\n'
    res += f'{indent}        <li><a href="blog.html">Blog</a></li>\n'
    res += f'{indent}        <li><a href="facilities_it.html">IT Infrastructure</a></li>\n'
    res += f'{indent}        <li><a href="facilities_library.html">Library</a></li>\n'
    res += f'{indent}        <li><a href="facilities_welfare.html">Welfare Measures</a></li>\n'
    res += f'{indent}    </ul>\n{indent}</li>'
    return res

# Re-evaluating the regex. Let's make it simpler and more robust.
# Find the specific block starting with <a href="#">Facilities</a> and containing the sub-items.

simple_pattern = r'<li class="has-dropdown">\s*<a href="[^"]*">Facilities</a>\s*<ul class="dropdown js-exclude-dropdown">[\s\S]*?<\/ul>\s*<\/li>'

replacement_block = """<li class="has-dropdown">
                        <a href="facilities.html">Facilities</a>
                        <ul class="dropdown js-exclude-dropdown">
                            <li><a href="facilities_infrastructure.html">Infrastructure</a></li>
                            <li><a href="facilities_event_gallery.html">Event Gallery</a></li>
                            <li><a href="blog.html">Blog</a></li>
                            <li><a href="facilities_it.html">IT Infrastructure</a></li>
                            <li><a href="facilities_library.html">Library</a></li>
                            <li><a href="facilities_welfare.html">Welfare Measures</a></li>
                        </ul>
                    </li>"""

for filename in files:
    content = None
    for enc in ['utf-8', 'cp1252', 'latin-1']:
        try:
            with open(filename, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        continue

    # Use a slightly more specific pattern to ensure we only match the main nav Facilities
    # We look for "Infrastructure" inside to be sure.
    if 'Facilities' in content and 'Infrastructure' in content:
        new_content = re.sub(simple_pattern, replacement_block, content, flags=re.MULTILINE)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
