import sys

gen = (x for x in range(1000000))
lst = [x for x in range(1000000)]

print("Generator size:", sys.getsizeof(gen))
print("List size:", sys.getsizeof(lst))
