# Bad
def valid_age(age):
    return age >= 18

# Good
def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
