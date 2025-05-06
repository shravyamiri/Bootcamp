# Conditional Assignment in Comprehension:
numbers = [-1, 2, -3, 4, -5]

# Using list comprehension with conditional assignment
modified_list = [num if num >= 0 else 0 for num in numbers]

# Displaying the result
print("Conditional Assignment in Comprehension:", modified_list)
