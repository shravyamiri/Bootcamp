# abstraction_level_2/utils.py
from typing import List, Optional

def read_lines(file_path: str) -> List[str]:
    """Reads lines from a file."""
    with open(file_path, "r") as f:
        return [line.strip() for line in f]

def write_output(lines: List[str], output_path: Optional[str] = None):
    """Writes lines to a file or prints to stdout."""
    if output_path:
        with open(output_path, "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"Output written to: {output_path}")
    else:
        for line in lines:
            print(line)