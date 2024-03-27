import os
import re

def search_directory(keyword, directory):
    results = []
    keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_number, line in enumerate(f, start=1):
                    if keyword_pattern.search(line):
                        results.append((file_path, line_number, line.strip()))
    return results

def main():
    directory = input("Enter the directory to search: ")
    keyword = input("Enter the keyword to search for: ")
    results = search_directory(keyword, directory)

    if results:
        print("Search results:")
        for file_path, line_number, line_content in results:
            print(f"{file_path}:{line_number} - {line_content}")
    else:
        print("No matching results found.")

if __name__ == "__main__":
    main()

