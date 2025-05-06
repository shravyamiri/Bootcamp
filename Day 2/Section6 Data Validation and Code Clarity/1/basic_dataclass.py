from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Example usage
user = User(name="John", age=25)
print(user)
