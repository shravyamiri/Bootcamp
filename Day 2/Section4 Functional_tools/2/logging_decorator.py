def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} Before calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message} After calling {func.__name__}")
            return result
        return wrapper
    return decorator

# Example usage:
@custom_logger("Log:")
def process_data(x):
    print(f"Processing {x}")
    return x * 2

process_data(10)
c