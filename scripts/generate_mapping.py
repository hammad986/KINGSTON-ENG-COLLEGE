
import os
import json
import re
from collections import defaultdict

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"

with open("comprehensive_analysis.json", "r") as f:
    analysis = json.load(f)

all_files = analysis["all_files_rel"]

DEPT_PREFIXES = ["aids_", "aiml_", "arch_", "chem_", "civil_", "csbs_", "cse_", "ece_", "eee_", "eng_", "it_", "maths_", "mba_", "mecht_", "mech_", "phy_", "sh_"]

def sanitize_name(name):
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    return re.sub(r'_+', '_', name).strip('_').lower()

def get_html_dest(filename):
    main_pages = [
        "index.html", "about.html", "contact.html", "admission.html", 
        "academics.html", "achievements.html", "alumni.html", "careers.html", 
        "events.html", "news.html", "privacy_policy.html", "sitemap.html", 
        "testimonials.html", "faq.html", "apply_now.html", 
        "admission_enquiry.html", "campus_tour.html", "ai-assistant.html", 
        "public_self_disclosure.html", "facilities.html", "grievance_helpdesk.html",
        "grievance_helpdesk_raw.html", "policies.html"
    ]
    if filename.lower() in [p.lower() for p in main_pages]:
        return filename

    for prefix in DEPT_PREFIXES:
        if filename.lower().startswith(prefix):
            dept_name = prefix.rstrip('_')
            return os.path.join("departments", dept_name, filename)

    categories = {
        "naac_": "naac", "iqac_": "iqac", "ugc_": "ugc", 
        "placement_": "placements", "facilities_": "facilities", 
        "about_": "about", "admission_": "admission", 
        "academic_": "academics", "alumni_": "alumni"
    }
    for prefix, folder in categories.items():
        if filename.lower().startswith(prefix):
            return os.path.join(folder, filename)
    return filename

def get_pdf_dest(old_rel_path):
    path_parts = old_rel_path.replace('\\', '/').split('/')
    filename = path_parts[-1]
    name_no_ext = os.path.splitext(filename)[0]
    
    category = "general"
    description = sanitize_name(name_no_ext)
    
    if "naac" in old_rel_path.lower(): category = "naac"
    elif "ugc" in old_rel_path.lower() or "public_self_disclosure" in old_rel_path.lower(): category = "ugc"
    elif "iqac" in old_rel_path.lower(): category = "iqac"
    elif "admission" in old_rel_path.lower(): category = "admission"
    elif "placement" in old_rel_path.lower(): category = "placements"
    else:
        for prefix in DEPT_PREFIXES:
            dept = prefix.rstrip('_')
            if dept in old_rel_path.lower():
                category = f"departments/{dept}"
                break

    # Refine description if generic
    if description in ["main_page", "final", "doc1", "1", "2", "3"]:
        context = sanitize_name("_".join(path_parts[-3:-1]))
        description = f"{context}_{description}"
    
    new_filename = f"{category.replace('/', '_')}_{description}.pdf"
    # Special overrides for stability
    if "public_self_disclosure" in old_rel_path.lower():
        new_filename = f"ugc_ps_{description}.pdf"
        
    return os.path.join("assets", "pdfs", category, new_filename)

movement_mapping = {}
pdf_mapping = {}
link_map = {}

for rel_path in all_files:
    if any(x in rel_path for x in [".git", "backup_legacy", "backup_mapping", "assets/css", "assets/js", "assets/images", "assets/vendor"]):
        continue
    if rel_path.startswith("assets/pdfs") or rel_path.startswith("assets\\pdfs"):
        continue

    filename = os.path.basename(rel_path)
    ext = os.path.splitext(filename)[1].lower()
    
    dest = None
    if ext == ".html":
        # Overwrite protection: If duplicate exists in root, ignore the one in subfolders
        if rel_path.startswith("pages\\") and os.path.exists(os.path.join(workspace_root, filename)):
            continue
        dest = get_html_dest(filename)
    elif ext == ".pdf":
        dest = get_pdf_dest(rel_path)
        pdf_mapping[rel_path] = dest
    elif ext == ".py":
        if filename not in ["refactor_workspace.py", "pre_analysis.py", "generate_mapping.py", "comprehensive_pre_analysis.py", "restore_workspace.py"]:
            dest = os.path.join("scripts", filename)
    elif ext in [".txt", ".json", ".csv", ".log"]:
        if rel_path.count(os.sep) == 0 and filename not in ["package.json"]:
            dest = os.path.join("logs", filename)

    if dest:
        movement_mapping[rel_path] = dest
        # For links, we need to map the relative reference
        # This is tricky because links can be relative. We'll store the absolute mapping of the file itself.
        link_map[rel_path] = dest


# Final collision and overwrite check
dest_to_src = defaultdict(list)
for src, dest in movement_mapping.items():
    # Normalize path separators for the final mapping file
    normalized_dest = dest.replace('/', os.sep).replace('\\', os.sep)
    movement_mapping[src] = normalized_dest
    dest_to_src[normalized_dest].append(src)

# Filter out legitimate collisions (exact same destination requested by multiple sources)
# We will just print a note about these, as they represent the consolidation requested.
final_mapping = movement_mapping
pdf_mapping_final = {src: dest for src, dest in pdf_mapping.items()}

# Validation: Check if any dest would OVERWRITE a file that isn't in movement_mapping
# (i.e. a file that is staying put but will be clobbered by something moving in)
all_destinations = set(movement_mapping.values())
staying_files = set(all_files) - set(movement_mapping.keys())
overwrites = all_destinations.intersection(staying_files)

if overwrites:
    print(f"CRITICAL: Movement would overwrite existing files that are not being moved: {overwrites}")
    with open("mapping_errors.json", "w") as f:
        json.dump(list(overwrites), f, indent=4)
else:
    with open("movement_mapping.json", "w") as f:
        json.dump(movement_mapping, f, indent=4)
    with open("pdf_mapping.json", "w") as f:
        # Sort for deterministic output
        json.dump(dict(sorted(pdf_mapping.items())), f, indent=4)
    with open("link_map.json", "w") as f:
        json.dump(dict(sorted(link_map.items())), f, indent=4)
    print("All mapping files generated successfully (Consolidation permitted).")
