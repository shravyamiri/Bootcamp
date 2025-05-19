import itertools

# Create an iterator and duplicate it
original = itertools.count(start=1)
copy1, copy2 = itertools.tee(original, 2)

# Example usage: Iterate over both copies
for _ in range(3):
    print(next(copy1), next(copy2))  # Outputs: 1 1, 2 2, 3 3
