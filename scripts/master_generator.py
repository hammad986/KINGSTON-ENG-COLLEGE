import os
import re

# Configuration
TEMPLATES_PREFIX = "cse_"
DEPARTMENTS = [
    {"name": "Information Technology", "prefix": "it_", "main": "dept_IT.html", "title": "Information Technology"},
    {"name": "Electronics and Communication Engineering", "prefix": "ece_", "main": "dept_ece.html", "title": "Electronics and Communication Engineering"},
    {"name": "Electrical and Electronics Engineering", "prefix": "eee_", "main": "dept_eee.html", "title": "Electrical and Electronics Engineering"},
    {"name": "Mechanical Engineering", "prefix": "mech_", "main": "dept_mechanical.html", "title": "Mechanical Engineering"},
    {"name": "Civil Engineering", "prefix": "civil_", "main": "dept_civil.html", "title": "Civil Engineering"},
    {"name": "Masters in Business Administration", "prefix": "mba_", "main": "dept_MBA.html", "title": "MBA"},
    {"name": "Artificial Intelligence and Data Science", "prefix": "aids_", "main": "dept_AI&DS.html", "title": "AI & DS"},
    {"name": "Computer Science Engineering with AI & ML", "prefix": "aiml_", "main": "dept_AI&ML.html", "title": "AI & ML"},
    {"name": "Computer Science and Business Systems", "prefix": "csbs_", "main": "dept_csbs.html", "title": "CSBS"},
    {"name": "Bachelor of Architecture", "prefix": "arch_", "main": "dept_BA.html", "title": "Architecture"},
    {"name": "Science and Humanities", "prefix": "sh_", "main": "dept_S&H.html", "title": "Science and Humanities"},
    {"name": "Mathematics", "prefix": "maths_", "main": "dept_maths.html", "title": "Mathematics"},
    {"name": "Physics", "prefix": "phy_", "main": "dept_physics.html", "title": "Physics"},
    {"name": "Chemistry", "prefix": "chem_", "main": "dept_chemistry.html", "title": "Chemistry"},
    {"name": "English", "prefix": "eng_", "main": "dept_english.html", "title": "English"},
    {"name": "Mechatronics Engineering", "prefix": "mecht_", "main": "dept_mechatronics.html", "title": "Mechatronics"}
]

# Get template files
template_files = [f for f in os.listdir('.') if f.startswith(TEMPLATES_PREFIX) and f.endswith('.html')]

def process_content(content, dept):
    # Replace Department Names
    content = content.replace("COMPUTER SCIENCE AND ENGINEERING", dept["name"].upper())
    content = content.replace("Computer Science and Engineering", dept["name"])
    
    # Replace Titles in <title> tag
    content = re.sub(r'<title>(.*?) - CSE \| Kingston Engineering College</title>', 
                     f'<title>\\1 - {dept["title"]} | Kingston Engineering College</title>', content)
    # Also handle simpler titles if any
    content = content.replace("<title>Kingston Engineering College - Autonomous</title>", f"<title>{dept['title']} - Kingston Engineering College</title>")
    
    # Replace Links (e.g., cse_about.html -> it_about.html)
    content = content.replace("cse_", dept["prefix"])
    
    return content

def generate_main_file(dept):
    TEMPLATE_MAIN = "dept_cse.html"
    if not os.path.exists(TEMPLATE_MAIN):
        print(f"Template main {TEMPLATE_MAIN} not found!")
        return
        
    with open(TEMPLATE_MAIN, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process content
    new_content = process_content(content, dept)
    
    # Fix sidebar active link and hrefs
    # In dept_cse.html, the sidebar has # links. We need to replace them with Prefix_about.html etc.
    # Actually, process_content already replaces cse_ with Prefix_
    # But wait, dept_cse.html sidebar currently has # links? Let's check again.
    # Looking at my previous view_file of dept_cse.html:
    # 448: <li><a href="#" class="active">...
    
    # So I need to replace those # with the actual links.
    # I'll use the sidebar from one of the generated subpages as a master.
    subpage_template = f"{dept['prefix']}about.html"
    if not os.path.exists(subpage_template):
        print(f"Error: {subpage_template} not found. Generate subpages first.")
        return
        
    with open(subpage_template, 'r', encoding='utf-8') as f:
        sub_content = f.read()
    
    sidebar_match = re.search(r'<aside class="dept-sidebar">.*?</aside>', sub_content, re.DOTALL)
    if sidebar_match:
        sidebar_content = sidebar_match.group(0)
        # Ensure 'about.html' is active
        sidebar_content = sidebar_content.replace(' class="active"', '')
        sidebar_content = sidebar_content.replace('href="' + dept['prefix'] + 'about.html"', 'href="' + dept['prefix'] + 'about.html" class="active"')
        
        # Replace sidebar in main file content
        new_content = re.sub(r'<aside class="dept-sidebar">.*?</aside>', sidebar_content, new_content, flags=re.DOTALL)

    with open(dept["main"], 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Generated/Updated main file {dept['main']}")

# 1. Generate all subpages
print("Generating subpages...")
for dept in DEPARTMENTS:
    print(f"Processing subpages for {dept['name']}...")
    for t_file in template_files:
        new_filename = t_file.replace(TEMPLATES_PREFIX, dept["prefix"])
        with open(t_file, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = process_content(content, dept)
        with open(new_filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    # 2. Generate/Update main file
    generate_main_file(dept)

# 3. Synchronize Navigation Menu
print("Synchronizing navigation menu...")

nav_menu_snippet = """                        <ul class="dropdown dropdown-columns js-exclude-dropdown">
                            <li><a href="dept_cse.html">Computer Science and Engineering</a></li>
                            <li><a href="dept_BA.html">Bachelor of Architecture</a></li>
                            <li><a href="dept_AI&ML.html">Computer Science Engineering with AI & ML</a></li>
                            <li><a href="dept_ece.html">Electronics and Communication Engineering</a></li>
                            <li><a href="dept_eee.html">Electrical and Electronics Engineering</a></li>
                            <li><a href="dept_mechanical.html">Mechanical Engineering</a></li>
                            <li><a href="dept_IT.html">Information Technology</a></li>
                            <li><a href="dept_AI&DS.html">Artificial Intelligence and Data Science</a></li>
                            <li><a href="dept_csbs.html">Computer Science and Business Systems</a></li>
                            <li><a href="dept_S&H.html">Science and Humanities</a></li>
                            <li><a href="dept_MBA.html">Masters in business administration</a></li>
                        </ul>"""

all_html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in all_html_files:
    try:
        content = None
        for enc in ['utf-8', 'cp1252', 'latin-1']:
            try:
                with open(filename, 'r', encoding=enc) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if content is None: continue

        new_content = re.sub(r'<ul class="dropdown dropdown-columns js-exclude-dropdown">.*?</ul>', 
                             nav_menu_snippet, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# 4. Update departments.html grid links
print("Updating departments.html grid links...")
if os.path.exists('departments.html'):
    with open('departments.html', 'r', encoding='utf-8') as f:
        dept_page = f.read()
    dept_page = dept_page.replace('<a href="dept_ece.html" class="dept-card" data-aos="fade-up" data-aos-delay="350">',
                                    '<a href="dept_eee.html" class="dept-card" data-aos="fade-up" data-aos-delay="350">')
    with open('departments.html', 'w', encoding='utf-8') as f:
        f.write(dept_page)

print("All tasks completed successfully.")
