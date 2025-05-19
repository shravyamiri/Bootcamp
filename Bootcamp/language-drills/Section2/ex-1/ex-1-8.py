# LBYL with `isinstance()` to guard against method calls on incompatible types
def add_numbers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        print("Error: Both inputs must be integers.")

print(add_numbers(5, 10))  # Valid
print(add_numbers(5, "10"))  # Invalid
