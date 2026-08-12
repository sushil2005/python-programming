import os
import json
import hashlib

DATABASE = "file_hashes.json"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_folder(folder):
    hashes = {}

    for root, _, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)

            if filepath == DATABASE:
                continue

            hashes[filepath] = calculate_hash(filepath)

    return hashes


def load_previous_hashes():
    if not os.path.exists(DATABASE):
        return {}

    with open(DATABASE, "r") as file:
        return json.load(file)


def save_hashes(hashes):
    with open(DATABASE, "w") as file:
        json.dump(hashes, file, indent=4)


def detect_changes(old, new):
    old_files = set(old)
    new_files = set(new)

    for file in new_files - old_files:
        print(f"[NEW]     {file}")

    for file in old_files - new_files:
        print(f"[DELETED] {file}")

    for file in old_files & new_files:
        if old[file] != new[file]:
            print(f"[MODIFIED] {file}")


def main():
    folder = input("Enter folder path to monitor: ")

    previous = load_previous_hashes()
    current = scan_folder(folder)

    if not previous:
        print("\nFirst scan completed.")
        print("File signatures have been saved.")
    else:
        print("\nChecking for changes...\n")
        detect_changes(previous, current)

    save_hashes(current)


if __name__ == "__main__":
    main()