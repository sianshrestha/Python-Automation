import os
import time

# Folder to be organized
folder_path = '/path/to/directory'

# Dictionary of file categories and their extensions
file_categories = {
    'Images': ['jpeg', 'jpg', 'png'],
    'PDFs': ['pdf'],
    'Datasets': ['csv', 'xlsx', 'json'],
    'Videos': ['mp4']
}

for category in ['Images', 'PDFs', 'Datasets', 'Videos']:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

# Function to organize a file
def organize_file(filename):
    # Find the file extension
    extension = filename.split('.')[-1].lower()

    # Iterate over the categories
    for category, extensions in file_categories.items():
        # If the extension matches one of the extensions in the category, move the file
        if extension in extensions:
            # Construct the file paths
            source_path = os.path.join(folder_path, filename)
            dest_path = os.path.join(folder_path, category, filename)

            # Move the file
            os.rename(source_path, dest_path)
            print(f'Moved {filename} to {category}')
            break

# Classify all existing files in the directory
for filename in os.listdir(folder_path):
    organize_file(filename)

# Initial list of files in the directory
initial_files = os.listdir(folder_path)

while True:
    # List of files in the directory after a short sleep
    time.sleep(5)
    current_files = os.listdir(folder_path)

    # Find the new files
    new_files = list(set(current_files) - set(initial_files))

    # Classify the new files
    for filename in new_files:
        organize_file(filename)

    # Update the initial list of files
    initial_files = current_files
