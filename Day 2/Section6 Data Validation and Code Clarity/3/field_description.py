from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int
    email: str = Field(..., description="User's email address")

# Example usage
user_dict = {"name": "Alice", "age": 30, "email": "alice@example.com"}
user = User(**user_dict)
print(user)
