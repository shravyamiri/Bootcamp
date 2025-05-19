import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

import random
data = [random.randint(0, 1000) for _ in range(500)]

start = time.time()
sorted(data)
print(f"Built-in sort: {time.time() - start:.5f} s")

data = [random.randint(0, 1000) for _ in range(500)]

start = time.time()
bubble_sort(data)
print(f"Bubble sort: {time.time() - start:.5f} s")
