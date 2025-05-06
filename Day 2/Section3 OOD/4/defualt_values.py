from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0  # Default value for age

# Create instances of User
user1 = User("Alice", 30)  # Providing both name and age
user2 = User("Bob")         # Providing only name, age will default to 0

# Print instances
print(user1)  # Output: User(name='Alice', age=30)
print(user2)  # Output: User(name='Bob', age=0)
