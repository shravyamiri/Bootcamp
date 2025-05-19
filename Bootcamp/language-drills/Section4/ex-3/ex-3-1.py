import functools

# Fix the base argument of int(x, base) to 2
int_base2 = functools.partial(int, base=2)

# Example usage:
print(int_base2('1010'))  # Outputs: 10 (binary to decimal)
