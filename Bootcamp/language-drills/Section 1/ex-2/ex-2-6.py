import sys

# List vs Generator: Compare memory usage
list_comprehension = [x for x in range(1000000)]  # List comprehension
generator_expression = (x for x in range(1000000))  # Generator expression

# Displaying the memory usage of both
print("List vs Generator:")
print("   Memory size of list comprehension:", sys.getsizeof(list_comprehension))  # List
print("   Memory size of generator expression:", sys.getsizeof(generator_expression))  # Generator
