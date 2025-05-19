def read_large_file(filepath):
    """
    Generator function to read a large file line by line.
    """
    try:
        with open(filepath, "r") as f:
            for line in f:
                yield line
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    for line in read_large_file("largefile.txt"):
        print(line.strip())
