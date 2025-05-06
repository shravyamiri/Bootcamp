import functools

# Partial function to add a custom prefix
add_prefix = functools.partial(print, "Prefix:")

# Further apply partial to add a custom suffix
add_suffix = functools.partial(add_prefix, end="!!!")

# Example usage:
add_suffix("Hello")  # Outputs: Prefix: Hello!!!
