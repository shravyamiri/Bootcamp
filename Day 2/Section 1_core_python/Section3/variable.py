# Variable Positional Args:
def add_all(*args):
    return sum(args)

# Calling with different numbers of arguments
print("Sum of numbers:", add_all(1, 2, 3))
print("Sum of numbers:", add_all(10, 20))
