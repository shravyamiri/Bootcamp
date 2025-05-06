import csv

def filter_csv(filepath):
    """
    Generator function to read and filter CSV rows
    where 'age' is greater than 30.
    """
    try:
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    if int(row["age"]) > 30:
                        yield row
                except ValueError:
                    print(f"Skipping row with invalid age: {row}")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    for row in filter_csv("people.csv"):
        print(row)
