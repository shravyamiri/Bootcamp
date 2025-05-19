from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"

# Example usage
user = User(name="John", age=25)
print(user)

# Trying to modify a field (this will raise an error)
try:
    user.age = 30
except Exception as e:
    print(f"Error: {e}")
