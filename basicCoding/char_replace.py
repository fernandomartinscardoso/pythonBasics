import os
from pathlib import Path

def rename_files(directory_path, old_char, new_char):
    """
    Replaces specified characters or substrings in all filenames within a directory.
    """
    # Convert string path to a Path object
    dir_path = Path(directory_path)
    
    # Ensure the provided path exists and is a directory
    if not dir_path.is_dir():
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    counter = 0

    # Iterate through all items in the directory (files only)
    for file_path in dir_path.iterdir():
        if file_path.is_file():
            old_name = file_path.name
            
            # Check if the target character/substring is present in the filename
            if old_char in old_name:
                # Generate the new name with replaced characters
                new_name = old_name.replace(old_char, new_char)
                new_file_path = file_path.with_name(new_name)
                
                try:
                    # Rename the file on the system
                    file_path.rename(new_file_path)
                    print(f"Renamed: '{old_name}' -> '{new_name}'")
                    counter += 1
                except Exception as e:
                    print(f"Failed to rename '{old_name}': {e}")

    print(f"\nTask completed. Total files renamed: {counter}")

# --- Configuration & Execution ---
if __name__ == "__main__":
    # Replace these values with your actual folder path and target characters
    TARGET_DIR = r"C:\Users\UserName\Downloads"
    CHARACTER_TO_FIND = " "
    REPLACEMENT_CHARACTER = "_"

    rename_files(TARGET_DIR, CHARACTER_TO_FIND, REPLACEMENT_CHARACTER)
