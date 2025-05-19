from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])
    print("Squares:", list(results))
