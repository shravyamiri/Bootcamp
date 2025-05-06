def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Using cached result")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Example usage:
@memoize
def expensive_computation(x):
    print("Computing...")
    return x * x

print(expensive_computation(5))  # First call
print(expensive_computation(5))  # Cached result
