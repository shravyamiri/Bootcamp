import time

start = time.time()
sum(range(1000000))
end = time.time()

print(f"Execution time: {end - start:.5f} seconds")
