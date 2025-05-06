from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)  # Factory default for lists

# Example usage
user = User(name="John", age=25)
user.tags.append("developer")
print(user.tags)  # ['developer']
