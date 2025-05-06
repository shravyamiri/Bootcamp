# Create a list
my_list = [10, 20, 30, 40]

# Convert the list into an iterator
iterator = iter(my_list)

# Manually call next() to get elements one by one
print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
print(next(iterator))  # Output: 40

# Uncommenting the next line will raise StopIteration
# print(next(iterator))  # This will raise StopIteration as the iterator is exhausted
