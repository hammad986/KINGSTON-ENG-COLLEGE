import os
import glob
import re

base_dir = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

files_to_delete = [
    "csbs_non_teaching_faculty.html",
    "csbs_research.html",
    "csbs_research_publications.html",
    "csbs_best_practices.html",
    "csbs_ipr.html",
    "csbs_research_projects.html",
    "csbs_consultancy.html",
    "csbs_higher_education.html",
    "csbs_entrepreneurship.html",
    "csbs_guest_lectures.html",
    "csbs_professional_societies.html",
    "csbs_clubs.html",
    "csbs_association.html"
]

# 1. Delete files
for filename in files_to_delete:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            print(f"Deleted: {filename}")
        except Exception as e:
            print(f"Failed to delete {filename}: {e}")
    else:
        print(f"File not found for deletion: {filename}")

# 2. Extract remaining csbs_*.html and dept_csbs.html
all_files = glob.glob(os.path.join(base_dir, "csbs_*.html"))
all_files.append(os.path.join(base_dir, "dept_csbs.html"))

# 3. Form a regex pattern to match any <li> containing links to the deleted files
# Pattern looks like: <li>\s*<a href="csbs_non_teaching_faculty\.html".*?</li>
escaped_filenames = [re.escape(f) for f in files_to_delete]
# Grouping the filenames (file1|file2|file3)
filename_pattern = "|".join(escaped_filenames)
# Match <li>...<a href="filenam.html"...>...</li>
regex_pattern = re.compile(rf'<li>\s*<a href="({filename_pattern})".*?</li>\n?\s*', re.IGNORECASE | re.DOTALL)

for filepath in all_files:
    # Only process files that still exist and aren't about to crash us
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    content = regex_pattern.sub('', content)
    
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated sidebar links in: {os.path.basename(filepath)}")
        
print("Cleanup complete.")
