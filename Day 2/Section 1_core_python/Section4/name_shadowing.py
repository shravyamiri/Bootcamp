len = 5  # Shadowing the built-in len function

# This will raise a TypeError because `len` is now an integer, not the built-in function
try:
    print(len("abc"))  # Trying to use the overridden len function
except TypeError as e:
    print("Error due to shadowing:", e)

# Best practice: don't shadow built-ins
