data = [("apple", 3), ("banana", 1), ("cherry", 2)]

# Sort by the second item in each tuple
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
