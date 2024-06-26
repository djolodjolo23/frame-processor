

import os

def process_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    files.sort()  # Optional: Sort files if specific order is needed
    
    i = 0
    while i < len(files):
        # Keep the current file
        print(f"Keeping: {files[i]}")
        
        # Skip the next four files and delete them

        for _ in range(1):
            i += 1
            if i < len(files):
                file_to_delete = os.path.join(folder_path, files[i])
                os.remove(file_to_delete)
                print(f"Deleted: {files[i]}")
            else:
                break
        
        # Move to the next file to keep
        i += 1

process_files('frames/micro1')
process_files('frames/micro2')
process_files('frames/micro3')
process_files('frames/micro4')
process_files('frames/micro5')
process_files('frames/micro6')
process_files('frames/micro7')
process_files('frames/micro8')
process_files('frames/micro9')
process_files('frames/micro10')


