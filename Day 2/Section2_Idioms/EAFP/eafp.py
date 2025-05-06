# EAFP (Easier to Ask for Forgiveness than Permission)
my_dict = {"name": "Alice", "age": 25}

try:
    print(my_dict["age"])  # Attempt to access key
except KeyError:
    print("Key not found!")
