import os
import shutil

def copy_folder_structure(src, dst):
    for root, dirs, files in os.walk(src):
        for dir in dirs:
            # Construct the full path of the source and destination directories
            src_dir = os.path.join(root, dir)
            dst_dir = os.path.join(dst, os.path.relpath(src_dir, src))
            # Create the destination directory
            os.makedirs(dst_dir, exist_ok=True)

if __name__ == "__main__":
    src_folder = r"D:\YK\Downloads\REPORT\REPORT"  # Replace with your source folder path
    dst_folder = r"D:\YK\Downloads\REPORT\REPORT1"  # Replace with your destination folder path
    copy_folder_structure(src_folder, dst_folder)