
import os
import shutil
import re

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
missing_dir = os.path.join(workspace_root, "missing")

# Precise mapping for the 11 files found in /missing/
mapping_data = [
    {"file": "accredited_by_cycle_grade_year_link_for_details (1).pdf", "dest": "assets/pdfs/naac/"},
    {"file": "act_and_statutes (1).pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "annual_accounts_statement.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "annual_reports_s.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "department_faculty_details.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "establishment_of_grievances_redressal_mechanism.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "national_service_scheme.pdf", "dest": "assets/pdfs/general/"},
    {"file": "research_and_development_cell_1.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "sponsoring_body_details.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "statutesordinances_pertaining_to.pdf", "dest": "assets/pdfs/ugc/"},
    {"file": "the_tamil_nadu_societies_registration_act_1975_tam_1.pdf", "dest": "assets/pdfs/ugc/"}
]

def calculate_relative_path(from_file, to_file):
    from_dir = os.path.dirname(from_file)
    try:
        # Normalize paths for Windows/Linux consistency
        rel_path = os.path.relpath(to_file, from_dir)
        return rel_path.replace('\\', '/')
    except:
        return to_file

def execute():
    # 1. Clean Move Files
    print("Step 1: Moving exactly 11 files from /missing/ to centralized folders...")
    for item in mapping_data:
        src = os.path.join(missing_dir, item['file'])
        dest_dir = os.path.join(workspace_root, item['dest'])
        dest_file = os.path.join(dest_dir, item['file'])
        
        if os.path.exists(src):
            os.makedirs(dest_dir, exist_ok=True)
            # Safe copy
            shutil.copy2(src, dest_file)
            print(f"Restored: {item['file']} -> {item['dest']}")
        else:
            print(f"Warning: File {item['file']} not found in /missing/")

    # 2. Universal Link Refactoring
    print("\nStep 2: Universal link refactoring across all HTML files...")
    html_files = []
    for root, dirs, files in os.walk(workspace_root):
        if any(x in root for x in [".git", "backup_legacy", "backup_mapping", "node_modules"]): continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    total_updates = 0
    for html_path in html_files:
        rel_html = os.path.relpath(html_path, workspace_root)
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            new_content = content
            changed = False
            
            # Find any broken PDF links in the content
            # We look for links that mention the filenames (even partially or with legacy paths)
            for item in mapping_data:
                # Search for original filename occurrences in hrefs
                # Pattern: href="...filename.pdf"
                # We handle variants like (1) and spaces
                base = item['file'].replace('(1)', '').replace(' ', '').lower()
                
                # Regex to find hrefs that likely point to this file
                # Match links ending in .pdf and containing parts of our filename
                links = re.findall(r'href=["\']([^"\']+\.pdf)["\']', content)
                for link in set(links):
                    link_base = os.path.basename(link).lower().replace(' ', '')
                    # If the link basename contains a significant part of our target filename
                    if (re.sub(r'[^a-z0-9]', '', base) in re.sub(r'[^a-z0-9]', '', link_base)) or \
                       (re.sub(r'[^a-z0-9]', '', link_base) in re.sub(r'[^a-z0-9]', '', base)):
                        
                        target_new_rel = os.path.join(item['dest'], item['file'])
                        new_link = calculate_relative_path(rel_html, target_new_rel)
                        
                        if new_link != link:
                            escaped_old = re.escape(link)
                            new_content = re.sub(f'href=["\']{escaped_old}["\']', f'href="{new_link}"', new_content)
                            changed = True
                            
            if changed:
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated links in: {rel_html}")
                total_updates += 1
                
        except Exception as e:
            print(f"Error processing {rel_html}: {e}")

    print(f"\nRestoration and Refactoring Complete. Updated {total_updates} files.")

if __name__ == "__main__":
    execute()
