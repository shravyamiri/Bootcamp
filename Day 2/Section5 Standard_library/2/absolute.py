from pathlib import Path

relative = Path("example.txt")
absolute = relative.resolve()

print("Relative:", relative)
print("Absolute:", absolute)
