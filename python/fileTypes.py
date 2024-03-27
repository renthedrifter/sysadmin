import os

def identify_file_types(directory):
    file_types = {}

    # Walk through the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = os.path.splitext(file)[1].lower()

            # Update file_types dictionary
            if file_type in file_types:
                file_types[file_type].append(file_path)
            else:
                file_types[file_type] = [file_path]

    return file_types

def main():
    directory = input("Enter the directory to scan: ")
    file_types = identify_file_types(directory)

    print("File types found:")
    for file_type, files in file_types.items():
        print(f"{file_type}: {len(files)} files")

if __name__ == "__main__":
    main()

