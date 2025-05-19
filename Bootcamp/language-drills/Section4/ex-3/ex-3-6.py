from functools import reduce

# Using reduce to compute factorial
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# Example usage:
print(factorial(5))  # Outputs: 120
