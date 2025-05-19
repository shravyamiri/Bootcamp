def compose(f, g):
    return lambda x: f(g(x))

# Example functions:
def add_one(x):
    return x + 1

def square(x):
    return x * x

composed_function = compose(add_one, square)
print(composed_function(4))  # Output: 17 (add_one(square(4)) -> 16 + 1)
