def factorial(n, level=0):
    print("  " * level + f"factorial({n})")
    if n == 0:
        return 1
    return n * factorial(n - 1, level + 1)

print(factorial(4))
