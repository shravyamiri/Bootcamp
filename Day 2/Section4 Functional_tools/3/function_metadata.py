from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserve metadata like name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Example usage:
@my_decorator
def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}")

greet("Alice")
print(greet.__name__)  # Outputs: greet
print(greet.__doc__)   # Outputs: Greets the user by name.
