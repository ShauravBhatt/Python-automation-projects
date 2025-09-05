"""
Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

import os 
import shutil 

EXTENSION_MAP = {
    "PDFs": ['.pdf'],
    "Images": ['.png' , '.jpg' , '.jpeg' , '.svg'],
    "Text": ['.txt']
}

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()

    if ext == '.py':
        return None 

    for folder,extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(file):
            dest_folder = get_destination_folder(file)
            
            if dest_folder == None:
                print("Skipping file because it\'s a '.py' file !!")
                continue

            dest_path = os.path.join(folder_path, dest_folder)
            os.makedirs(dest_path, exist_ok=True)
            shutil.move(full_path, os.path.join(dest_path,file))
            print(f"Moved {file} to {dest_folder}/")

if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid Directory !!")
    else:
        sort_files(folder)
        print("Sorting of files completed !!")

