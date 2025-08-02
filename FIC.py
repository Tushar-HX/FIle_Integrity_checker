import os
import hashlib
import json

HASH_FILE = "file_hashes.json"
MONITOR_DIR = "."  # Change to the directory you want to monitor

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def scan_files(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            if os.path.abspath(path) == os.path.abspath(HASH_FILE):
                continue  # Skip the hash file itself
            try:
                hashes[path] = hash_file(path)
            except Exception as e:
                print(f"Could not hash {path}: {e}")
    return hashes

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=2)

def compare_hashes(old, new):
    changed = []
    for path, hash_val in new.items():
        if path not in old:
            changed.append(f"New file: {path}")
        elif old[path] != hash_val:
            changed.append(f"Modified: {path}")
    for path in old:
        if path not in new:
            changed.append(f"Deleted: {path}")
    return changed

if __name__ == "__main__":
    old_hashes = load_hashes()
    new_hashes = scan_files(MONITOR_DIR)
    changes = compare_hashes(old_hashes, new_hashes)
    if changes:
        print("Detected changes:")
        for change in changes:
            print(" -", change)
    else:
        print("No changes detected.")
    save_hashes(new_hashes)