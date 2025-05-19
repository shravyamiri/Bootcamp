from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int = 0  # Default value for age

    def is_adult(self) -> bool:
        """Returns True if the user is 18 or older."""
        return self.age >= 18

# Create instances of User
user1 = User("Alice", 30)
user2 = User("Bob", 15)

# Check if the users are adults
print(user1.is_adult())  # Output: True, because Alice is 30
print(user2.is_adult())  # Output: False, because Bob is 15
