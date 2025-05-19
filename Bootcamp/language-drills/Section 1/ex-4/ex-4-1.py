def make_multiplier(n):
    def multiplier(x):
        return n * x  # n is remembered from the outer function's scope
    return multiplier

# Creating a closure
times3 = make_multiplier(3)
print("5 x 3 =", times3(5))  # Output: 5 x 3 = 15
