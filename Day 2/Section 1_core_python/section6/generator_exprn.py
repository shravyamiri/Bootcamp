# Generator expression that filters even numbers from 0 to 9
even_numbers = (x for x in range(10) if x % 2 == 0)

# Print the even numbers from the generator
for num in even_numbers:
    print(num)
