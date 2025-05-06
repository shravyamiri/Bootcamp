# 1. List Operations: Append 2, remove 3, and sort the list
a = [5, 3, 8]
print("Original list:", a)

# Step 1: Append the number 2
a.append(2)
print("After appending 2:", a)

# Step 2: Remove the number 3 after checking the presence
if 3 in a:
    a.remove(3)
    print("After removing 3:", a)
else:
    print("3 not found in the list. No removal performed.")

# Step 3: Sort the list in ascending order
a.sort()
print("After sorting:", a)
