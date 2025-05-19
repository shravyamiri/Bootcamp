numbers = [1, 2, 3, 4, 5, 6]

# Use map to double each number
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Use filter to keep only odd numbers (i.e., remove even numbers)
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odds)
