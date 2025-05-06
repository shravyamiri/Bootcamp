#@profile
def slow_function():
    total = 0
    for i in range(10000):
        for j in range(100):
            total += i * j
    return total

slow_function()
