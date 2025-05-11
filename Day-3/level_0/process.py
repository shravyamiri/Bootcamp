import sys

for line in sys.stdin:
    stripped_line = line.strip()
    upper_line = stripped_line.upper()
    print(upper_line)
