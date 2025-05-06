from pathlib import Path

py_files = Path(".").glob("*.py")
for file in py_files:
    print(file)
