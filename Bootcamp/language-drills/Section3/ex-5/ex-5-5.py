import json
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(title=data.get("title", "Unknown"), author=data.get("author", "Unknown"))

    @classmethod
    def from_json(cls, json_str: str):
        try:
            data = json.loads(json_str)
            return cls.from_dict(data)
        except json.JSONDecodeError:
            print("Invalid JSON!")
            return cls("Invalid", "Invalid")

# Usage
book1 = Book.from_dict({"title": "1984", "author": "George Orwell"})
print(book1)

book2 = Book.from_json('{"title": "Brave New World", "author": "Aldous Huxley"}')
print(book2)

book3 = Book.from_json('invalid json')
print(book3)
