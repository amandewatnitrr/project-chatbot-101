import os
import csv

root_folder = '/path/to/git/repo'

def categorize_files(root_folder):
    categories = {}
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if ".git" in dirpath:
            continue
        category = dirpath.replace(root_folder, '').strip('/')
        if category == '':
            category = 'uncategorized'
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if category not in categories:
                categories[category] = []
            categories[category].append((filename, full_path))

    return categories

def write_to_csv(categories):
    with open('file_categories.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['file_name', 'category', 'location'])
        for category, files in categories.items():
            for file in files:
                writer.writerow([file[0], category, file[1]])

categories = categorize_files(root_folder)
write_to_csv(categories)