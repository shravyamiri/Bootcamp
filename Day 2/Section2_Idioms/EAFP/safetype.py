# EAFP: Convert string input to int safely using try/except
input_str = "123a"

try:
    num = int(input_str)
    print("Converted number:", num)
except ValueError:
    print(f"Error: '{input_str}' is not a valid integer.")
