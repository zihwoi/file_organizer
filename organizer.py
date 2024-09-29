import os
import shutil
import argparse

# File types and their associated categories
FILE_CATEGORIES = {
    "Documents": ['.pdf', '.docx', '.txt', '.xls', '.ppt'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Others": []
}

def organize_files(directory, dry_run=False):
    """Organize files into folders based on their file type."""
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()
            destination_folder = "Others"

            # Check if the file type matches one of the categories
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    destination_folder = category
                    break
            
            target_dir = os.path.join(directory, destination_folder)

            # Create the target directory if it doesn't exist
            if not os.path.exists(target_dir):
                print(f"Creating directory: {target_dir}")
                if not dry_run:
                    os.makedirs(target_dir)

            # Move the file to the target directory
            new_file_path = os.path.join(target_dir, filename)
            print(f"Moving '{filename}' to '{target_dir}'")
            if not dry_run:
                shutil.move(filepath, new_file_path)

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by type.")
    parser.add_argument("directory", help="Path to the directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    
    args = parser.parse_args()
    
    organize_files(args.directory, args.dry_run)

if __name__ == "__main__":
    main()
