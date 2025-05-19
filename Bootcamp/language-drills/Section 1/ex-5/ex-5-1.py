class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    print("Age is valid:", age)

try:
    check_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")
