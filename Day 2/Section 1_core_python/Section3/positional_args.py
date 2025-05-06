# Positional-Only Args: Define a function using / to enforce positional arguments
def pos_only_args(a, b, /, c):
    print(f"a: {a}, b: {b}, c: {c}")

# Calling with positional arguments
pos_only_args(1, 2, c=3)

# The following will result in an error because a and b are positional-only:
# pos_only_args(a=1, b=2, c=3)
