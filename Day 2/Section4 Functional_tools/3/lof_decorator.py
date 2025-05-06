from functools import wraps

def log_decorator(func):
    @wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

# Example usage:
@log_decorator
def say_goodbye(name):
    print(f"Goodbye, {name}")

say_goodbye("Charlie")
