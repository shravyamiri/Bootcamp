def make_multiplier(n):
    def multiplier(x):
        return n * x  # n is captured by the closure
    return multiplier

# Creating a closure with multiplier 3
triple = make_multiplier(3)
print("triple(10):", triple(10))  # Output: 30
