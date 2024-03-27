import os
import shutil

def find_and_copy_jpeg(source_dir, dest_dir):
    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Recursively search for JPEG files and copy them
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.copy2(source_path, dest_path)
                print(f"Copied {source_path} to {dest_path}")

def main():
    source_dir = input("Enter the source directory: ")
    dest_dir = input("Enter the destination directory: ")

    find_and_copy_jpeg(source_dir, dest_dir)
    print("JPEG files copied successfully.")

if __name__ == "__main__":
    main()

