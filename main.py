from datetime import datetime
import os
import subprocess
import pathlib
from pathlib import Path




def compare_folders(f1_path: str, f2_path: str):
    dir_path = 'reports/'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    icloud_archive = open(f1_path, "r")
    local_documents = open(f2_path, "r")

    existing_in_local = []
    missing_in_local = []
    for i, file in enumerate(icloud_archive):
        if file in local_documents:
            existing_in_local.append(file)
            print("File", file, "exists in local")
        else:
            missing_in_local.append(file)
            print("File", file, "does not exist in local")

    # closing files
    icloud_archive.close()
    local_documents.close()

    # Write comparison report to TXT files
    with open(r"reports/existing_in_local.txt", "w") as fp:
        for item in existing_in_local:
            fp.write(item + "\n")

    with open(r"reports/missing_in_local.txt", "w") as fp:
        for item in missing_in_local:
            fp.write(item + "\n")


if __name__ == "__main__":
    icloud_archive_path = "data/icloud-archive-13:04:2024.txt"
    local_documents_path = "data/local-documents-13:04:2024.txt"
    compare_folders(icloud_archive_path, local_documents_path)

    # I can't get this file using ls -R icloud_docs from terminal. How do I get SSH access? Or who can run this for me?
    # icloud_docs = "iCloud/Documents"
