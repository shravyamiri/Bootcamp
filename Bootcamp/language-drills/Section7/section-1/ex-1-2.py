import timeit

list_time = timeit.timeit("[x*x for x in range(1000000)]", number=10)
gen_time = timeit.timeit("(x*x for x in range(1000000))", number=10)

print(f"List comprehension time: {list_time:.5f}")
print(f"Generator expression time: {gen_time:.5f}")
