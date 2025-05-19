numbers = [3, 7, -2, 5, 9]

# Check if **any** number is negative
if any(n < 0 for n in numbers):
    print("There is at least one negative number.")
else:
    print("All numbers are non-negative.")

# Check if **all** numbers are positive
if all(n > 0 for n in numbers):
    print("All numbers are positive.")
else:
    print("Not all numbers are positive.")
