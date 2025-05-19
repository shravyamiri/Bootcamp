def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if any(arg <= 0 for arg in args):
            raise ValueError("Arguments must be positive")
        return func(self, *args, **kwargs)
    return wrapper

# Example usage:
class Calculator:
    @validate_args
    def multiply(self, x, y):
        return x * y

calc = Calculator()
print(calc.multiply(3, 4))  # Valid
print(calc.multiply(-3, 4))  # Raises ValueError
