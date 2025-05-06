from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int = 0  # Default value for age

# Create an instance of User
user1 = User("Alice", 30)

# Print the object
print(user1)  # Output: User(name='Alice', age=30)

# Try to modify the attribute (will raise an error)
try:
    user1.age = 35  # This will raise a FrozenInstanceError
except AttributeError as e:
    print(f"Error: {e}")
