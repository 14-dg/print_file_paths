import os

def print_file_paths(root_folder, exclude_folders=None):
    """
    Print all file paths in the root_folder and its subfolders,
    excluding the folders specified in exclude_folders.
    """
    for root, dirs, files in os.walk(root_folder):
        if exclude_folders:
            dirs[:] = [d for d in dirs if d not in exclude_folders]  # Exclude specified folders from further traversal
            for exclude_folder in exclude_folders:
                if exclude_folder in dirs:
                    print(f"Excluding folder: {exclude_folder}")
                    dirs.remove(exclude_folder)
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            
            
def print_folder_paths(root_folder, exclude_folders=None):
    for root, dirs, files in os.walk(root_folder):
        if exclude_folders:
            dirs[:] = [d for d in dirs if d not in exclude_folders]  # Exclude specified folders from further traversal
            for exclude_folder in exclude_folders:
                if exclude_folder in dirs:
                    print(f"Excluding folder: {exclude_folder}")
                    dirs.remove(exclude_folder)
                    
        print(root)

if __name__ == "__main__":
    only_folders = input("Only show folders y/n: ")=="y"
    root_folder = input("Enter the root folder path: ").strip()
    
    exclude_folders = []
    exclude_input = input("Enter folders to exclude (comma-separated): ").strip()
    if exclude_input:
        exclude_folders = [folder.strip() for folder in exclude_input.split(",")]

    if only_folders:
        print_folder_paths(root_folder, exclude_folders)
    else:
        print_file_paths(root_folder, exclude_folders)
