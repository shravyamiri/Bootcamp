# Using pathlib
from pathlib import Path

Path("example.txt").write_text("hello")

# OR using open
with open("example_open.txt", "w") as f:
    f.write("hello")
