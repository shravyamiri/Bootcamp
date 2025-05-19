from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Example usage
user_dict = {"name": "Alice", "age": "42"}  # age as a string
user = User(**user_dict)
print(user)
