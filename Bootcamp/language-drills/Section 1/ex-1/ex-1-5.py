# 3. List Copying Pitfall: Difference between assignment and slicing
a = [1, 2, 3]
print("Original list a:", a)

# b is assigned directly to a (both refer to the same object)
b = a
print("b = a (same reference):", b)

# c is a shallow copy of a (new object with same values)
c = a[:]
print("c = a[:] (copy):", c)

# Modify the original list a
a.append(4)
print("\nAfter appending 4 to 'a':")
print("a (modified):", a)
print("b (same reference, reflects change):", b)
print("c (independent copy, unchanged):", c)
