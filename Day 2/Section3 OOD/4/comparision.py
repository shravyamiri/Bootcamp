from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int = 0  # Default value for age

# Create two instances of User
user1 = User("Alice", 30)
user2 = User("Alice", 30)
user3 = User("Bob", 25)

# Compare users
print(user1 == user2)  # Output: True, because both have the same name and age
print(user1 == user3)  # Output: False, because the name and age are different
