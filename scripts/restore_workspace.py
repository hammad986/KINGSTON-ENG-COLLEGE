
import os
import json
import shutil

workspace_root = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
mapping_file = os.path.join(workspace_root, "backup_mapping", "movement_mapping.json")
backup_dir = os.path.join(workspace_root, "backup_legacy_full")

def restore():
    if not os.path.exists(mapping_file):
        print("Error: movement_mapping.json not found in backup_mapping/")
        return

    with open(mapping_file, "r") as f:
        mapping = json.load(f)

    # Reverse the mapping: new_path -> old_path
    reverse_mapping = {v: k for k, v in mapping.items()}

    print(f"Starting restoration of {len(reverse_mapping)} files...")

    for new_path, old_path in reverse_mapping.items():
        src = os.path.join(workspace_root, new_path)
        dest = os.path.join(workspace_root, old_path)
        
        # 1. Try to move from current location
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.move(src, dest)
            print(f"Restored: {new_path} -> {old_path}")
        else:
            # 2. If missing, try to restore from legacy backup
            legacy_src = os.path.join(backup_dir, old_path)
            if os.path.exists(legacy_src):
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(legacy_src, dest)
                print(f"Restored from legacy backup: {old_path}")
            else:
                print(f"Warning: Could not find {old_path} anywhere!")

    print("Restoration complete.")

if __name__ == "__main__":
    restore()
