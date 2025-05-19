from functools import lru_cache

@lru_cache(None)  # Using an unlimited cache size
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Example usage:
print(fib(10))  # Outputs: 55
