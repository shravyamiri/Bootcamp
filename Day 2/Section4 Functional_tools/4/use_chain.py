import itertools

# Combine multiple iterables into one
combined = itertools.chain([1, 2], [3, 4], [5])

# Example usage: Print combined items
for item in combined:
    print(item, end=' ')  # Outputs: 1 2 3 4 5
