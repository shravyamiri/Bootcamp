from pathlib import Path

file_path = Path("myfile.txt")

# Create file with sample content if it doesn't exist
if not file_path.exists():
    file_path.write_text("This is sample content.")

# Now read it
content = file_path.read_text()
print(content)
