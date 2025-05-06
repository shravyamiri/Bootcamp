import itertools

# Repeat None 10 times
none_repeat = itertools.repeat(None, 10)

# Example usage: Print the list of Nones
for _ in none_repeat:
    print(_, end=' ')  # Outputs: None None None None None None None None None None
