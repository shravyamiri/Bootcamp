from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


# Example usage
try:
    user = User(name="John", age=-1)
except ValueError as e:
    print(e)
