import itertools

# List of items
items = [1, 2, 3]

# Generate all pairs (2-length permutations)
pairs = itertools.permutations(items, 2)

# Generate all triples (3-length combinations)
triples = itertools.combinations(items, 3)

# Example usage: Print all pairs
print("Pairs:")
for pair in pairs:
    print(pair)  # Outputs: (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

# Example usage: Print all triples
print("Triples:")
for triple in triples:
    print(triple)  # Outputs: (1, 2, 3)
