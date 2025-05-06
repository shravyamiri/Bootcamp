import time

# Without LRU Cache
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# With LRU Cache
from functools import lru_cache

@lru_cache(None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n-1) + fib_cached(n-2)

# Performance Comparison
start = time.time()
fib_recursive(35)
end = time.time()
print(f"Time without cache: {end - start:.5f} seconds")

start = time.time()
fib_cached(35)
end = time.time()
print(f"Time with cache: {end - start:.5f} seconds")
