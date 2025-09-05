"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""

import os 

def batch_rename(folder , base_name , ext = ".png"):
    files = [file for file in os.listdir(folder) if file.lower().endswith(extension.lower())]
    files.sort()

    if not files:
        print("\nNo files found in the current directory !!")
        return 

    for indx,file in enumerate(files,start=1):
        new_name = f"{base_name}_{indx}{extension}"
        print(f"{file} -> {new_name}")

    choice = input("\nWant to proceed with these names (y/n) : ").strip().lower()
    
    if choice != 'y':
        print("\nAborted the image batch processing !!")
        exit()

    for indx,file in enumerate(files,start=1):
        src = os.path.join(folder,file)
        new_name = f"{base_name}_{indx}{extension}"
        dest = os.path.join(folder,new_name)
        os.rename(src,dest)
    print(f"\nRenamed {len(files)} files successfully !!")


if __name__ == "__main__":
    folder = input("Enter folder path or blank for current folder : ").strip() or os.getcwd()
    
    if not os.path.isdir(folder):
        print("Invalid Folder !!")
    else:
        base_name=input("Enter base name for files : ").strip()
        extension=input("Enter extension name of your images: ").strip().lower()
        batch_rename(folder,base_name,extension)
