def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__} is called.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage:
@prefix_printer("Log:")
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Bob")
