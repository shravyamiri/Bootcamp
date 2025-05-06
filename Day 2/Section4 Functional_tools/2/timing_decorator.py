import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Example usage:
@timer
def slow_function():
    time.sleep(2)

slow_function()
