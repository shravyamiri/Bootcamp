import itertools

# Cycle through colors
color_cycle = itertools.cycle(["red", "green", "blue"])

# Example usage: Print first 6 colors
for _ in range(6):
    print(next(color_cycle))  # Outputs: red, green, blue, red, green, blue
