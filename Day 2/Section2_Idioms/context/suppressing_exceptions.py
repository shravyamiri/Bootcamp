from contextlib import suppress

# Try to open a file and suppress the FileNotFoundError exception
with suppress(FileNotFoundError):
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
        print(content)

# If the file does not exist, no exception is raised, and the program continues
print("Continuing execution despite the file not being found.")
