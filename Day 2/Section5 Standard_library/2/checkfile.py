from pathlib import Path

file = Path("example.txt")

print("Exists:", file.exists())
print("Is file:", file.is_file())
