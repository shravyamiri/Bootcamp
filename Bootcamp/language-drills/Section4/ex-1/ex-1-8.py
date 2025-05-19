def make_multiplier(factor):
    return lambda x: x * factor

# Example usage:
doubler = make_multiplier(2)
print(doubler(5))  # Output: 10
