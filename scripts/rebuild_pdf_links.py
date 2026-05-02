
import os
import re
import json

# Normalize workspace root
workspace_root = os.path.normpath(r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main").lower()
ignore_dirs = [".git", "node_modules", "backup_legacy_full", "backup_mapping", "scripts", "docs"]

# Report Data
report = {
    "updated": [],
    "skipped": [],
    "ambiguous": [],
    "missing": [],
    "errors": []
}

def get_pdf_index():
    index = {}
    dups = {}
    pdf_root = os.path.join(workspace_root, "assets", "pdfs")
    for root, dirs, files in os.walk(pdf_root):
        for f in files:
            if f.lower().endswith(".pdf"):
                full_path = os.path.join(root, f)
                rel_to_root = os.path.relpath(full_path, workspace_root).replace("\\", "/")
                basename = f # Exact case from disk
                
                b_key = basename.lower()
                if b_key in index:
                    if b_key not in dups:
                        dups[b_key] = [index[b_key]]
                    dups[b_key].append(rel_to_root)
                else:
                    index[b_key] = rel_to_root
    return index, dups

def calculate_rel_link(from_file_abs, to_pdf_rel_root):
    from_dir = os.path.dirname(from_file_abs)
    target_abs = os.path.join(workspace_root, to_pdf_rel_root.replace("/", os.sep))
    try:
        rel_path = os.path.relpath(target_abs, from_dir)
        return rel_path.replace("\\", "/")
    except:
        return to_pdf_rel_root

def rebuild():
    index, dups = get_pdf_index()
    print(f"Found {len(index)} unique PDF basenames. {len(dups)} duplicate clusters found.")

    files_to_scan = []
    for root, dirs, files in os.walk(workspace_root):
        norm_root = os.path.normpath(root).lower()
        # Skip ignore dirs
        skip = False
        for d in ignore_dirs:
            if os.sep + d + os.sep in norm_root or norm_root.endswith(os.sep + d):
                skip = True
                break
        if skip: continue
            
        for f in files:
            if f.lower().endswith(('.html', '.js')):
                files_to_scan.append(os.path.join(root, f))

    print(f"Scanning {len(files_to_scan)} files...")

    for file_path in files_to_scan:
        file_path_abs = os.path.abspath(file_path)
        rel_file_for_log = os.path.relpath(file_path_abs, workspace_root).replace("\\", "/")
        
        try:
            with open(file_path_abs, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            new_content = content
            # Pattern capturing any linked PDF
            # group 1: delimiter/prefix
            # group 2: path
            # group 3: suffix
            pattern = r'(href=["\']|src=["\']|window\.open\(["\']|["\'])([^"\']+\.pdf)(["\'])'
            
            modified = False
            # Find all matches
            matches = list(re.finditer(pattern, content))
            
            # Process matches in reverse to maintain offsets
            for m in reversed(matches):
                prefix = m.group(1)
                original_link = m.group(2)
                suffix = m.group(3)
                
                # Normalize link for extraction
                clean_link = original_link.split('?')[0].split('#')[0]
                # Replace %20 with spaces for matching file on disk
                clean_link = clean_link.replace("%20", " ")
                basename = os.path.basename(clean_link).lower()
                
                if basename in index:
                    target_pdf = None
                    if basename in dups:
                        # Context matching: Check if HTML file folder name exists in the PDF path
                        file_context = rel_file_for_log.split('/')[0].lower() if '/' in rel_file_for_log else ""
                        for path in dups[basename]:
                            if file_context and file_context in path.lower():
                                target_pdf = path
                                break
                        if not target_pdf:
                            # If no context match, check if current folder matches depth 2
                            file_context_deeper = rel_file_for_log.split('/')[:2]
                            for path in dups[basename]:
                                if any(c.lower() in path.lower() for c in file_context_deeper if c):
                                    target_pdf = path
                                    break
                        
                        if not target_pdf:
                            report["ambiguous"].append({"file": rel_file_for_log, "link": original_link, "options": dups[basename]})
                            continue
                    else:
                        target_pdf = index[basename]
                    
                    correct_link = calculate_rel_link(file_path_abs, target_pdf)
                    
                    # Force update if casing differs or path is wrong
                    if original_link != correct_link:
                        start, end = m.span(2)
                        new_content = new_content[:start] + correct_link + new_content[end:]
                        modified = True
                        report["updated"].append({"file": rel_file_for_log, "from": original_link, "to": correct_link})
                    else:
                        report["skipped"].append({"file": rel_file_for_log, "link": original_link})
                else:
                    report["missing"].append({"file": rel_file_for_log, "link": original_link})

            if modified:
                with open(file_path_abs, 'w', encoding='utf-8') as f:
                    f.write(new_content)

        except Exception as e:
            report["errors"].append({"file": rel_file_for_log, "error": str(e)})

    # Final Report
    report_file = os.path.join(workspace_root, 'scripts', 'pdf_rebuild_report_v2.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    # Summary Table for the AI to read
    print("\n--- FINAL REBUILD SUMMARY ---")
    print(f"Total Files Scanned: {len(files_to_scan)}")
    print(f"Links Updated:        {len(report['updated'])}")
    print(f"Links Already Correct: {len(report['skipped'])}")
    print(f"Links Missing on Disk: {len(report['missing'])}")
    print(f"Ambiguous Links:       {len(report['ambiguous'])}")
    print(f"Processing Errors:     {len(report['errors'])}")
    print(f"\nDetailed report: {report_file}")

if __name__ == "__main__":
    rebuild()
