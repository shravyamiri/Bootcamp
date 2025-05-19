from itertools import islice

def file_lines(filepath):
    """
    Generator that yields stripped lines from the given file.
    """
    try:
        with open(filepath, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    for line in islice(file_lines("largefile.txt"), 10):
        print(line)
