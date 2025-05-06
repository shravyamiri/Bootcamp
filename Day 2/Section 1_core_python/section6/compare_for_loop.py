# Using a list comprehension to filter even numbers
list_even_numbers = [x for x in range(10) if x % 2 == 0]
print("List comprehension:", list_even_numbers)

# Using a generator expression to filter even numbers
gen_even_numbers = (x for x in range(10) if x % 2 == 0)
print("Generator expression:", list(gen_even_numbers))  # Convert to list to see the output
