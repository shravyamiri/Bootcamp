from dataclasses import dataclass

@dataclass(slots=True)
class User:
    name: str
    age: int
    country: str = "India"

# Example usage
user = User(name="John", age=25)
print(user)

# Trying to add an attribute outside the defined fields will raise an error
try:
    user.gender = "Male"
except AttributeError as e:
    print(f"Error: {e}")
