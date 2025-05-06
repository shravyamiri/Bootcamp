from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def is_adult(self):
        return self.age >= 18

# Example usage
user = User(name="John", age=25)
print(user.is_adult())  # True

user2 = User(name="Alice", age=17)
print(user2.is_adult())  # False
