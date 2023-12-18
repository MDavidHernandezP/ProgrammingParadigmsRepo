# Import necessary libraries/modules
import os
import shutil

def copy_files(source_dir, dest_dir):
    # List all files in the source directory
    files = os.listdir(source_dir)

    # Copy each file to the destination directory
    for file in files:
        source_path = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        shutil.copy(source_path, dest_path)
        print(f"File '{file}' copied to '{dest_dir}'")

# Example usage for Task 1
source_directory = "C:/Users/YourUsername/Documents/source_folder"
destination_directory = "C:/Users/YourUsername/Documents/destination_folder"
copy_files(source_directory, destination_directory)