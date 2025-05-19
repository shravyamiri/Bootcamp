def make_doubler():
    return lambda x: x * 2

# Example usage:
doubler = make_doubler()
print(doubler(5))  # Output: 10
