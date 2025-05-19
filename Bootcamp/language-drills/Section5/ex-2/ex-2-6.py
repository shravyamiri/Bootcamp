import shutil

# Ensure the source file exists
with open("source.txt", "w") as f:
    f.write("This is the content of the source file.")

# Copy the file
shutil.copy("source.txt", "copied.txt")
print("File copied successfully!")
