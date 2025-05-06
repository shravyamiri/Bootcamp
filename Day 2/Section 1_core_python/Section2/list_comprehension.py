# List Comprehension with Condition: From [1, 2, 3, 4], make [4, 16]
original_list = [1, 2, 3, 4]

# List comprehension to square only the even numbers
squared_numbers = [x**2 for x in original_list if x % 2 == 0]

# Display the result
print("List Comprehension with Condition:", squared_numbers)
