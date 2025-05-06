# Keyword Arguments:
def info(name, age=0):
    print(f"Name: {name}, Age: {age}")

# Calling with keyword arguments in any order
info(age=25, name="Bob")     # Order doesn't matter
info(name="Charlie")         # Age defaults to 0
