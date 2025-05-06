from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

# Example usage
user1 = User(name="John", age=25)
user2 = User(name="John", age=25)

print(user1 == user2)  # True (compares based on data in fields)
