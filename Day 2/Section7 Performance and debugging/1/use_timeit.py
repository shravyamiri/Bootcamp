import timeit

duration = timeit.timeit("sum(range(10000))", number=100)
print(f"Time taken: {duration:.5f} seconds")
