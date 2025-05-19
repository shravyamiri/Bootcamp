# Nested List Comprehension: Flatten [[1, 2], [3, 4]] into [1, 2, 3, 4]
nested_list = [[1, 2], [3, 4]]

# Using nested list comprehension to flatten the list
flattened_list = [item for sublist in nested_list for item in sublist]

# Display the result
print("Nested List Comprehension:", flattened_list)
