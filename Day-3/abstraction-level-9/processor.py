def process_file(file_path):
    print(f"Processing {file_path}")
    # Add your processing logic here

def watch_directory(folder_path):
    import time, os
    print(f"Watching directory: {folder_path}")
    seen = set()
    while True:
        files = set(os.listdir(folder_path))
        new_files = files - seen
        for f in new_files:
            process_file(os.path.join(folder_path, f))
        seen = files
        time.sleep(5)
