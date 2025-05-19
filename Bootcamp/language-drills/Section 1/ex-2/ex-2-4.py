# Generator Expression: Use (n*n for n in range(5)) to build a generator and print its items
generator = (n * n for n in range(5))

# Print the generated values
print("Generator Expression:")
for value in generator:
    print(value)
