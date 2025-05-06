import itertools

# Generate infinite IDs starting from 1
id_generator = itertools.count(start=1)

# Example usage: Get first 5 IDs
for _ in range(5):
    print(next(id_generator))  # Outputs: 1, 2, 3, 4, 5
