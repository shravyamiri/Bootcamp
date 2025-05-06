import itertools

# Skip first 3 elements, take next 4 from the range(10)
sliced = itertools.islice(range(10), 3, 7)

# Example usage: Print sliced elements
for item in sliced:
    print(item, end=' ')  # Outputs: 3 4 5 6
