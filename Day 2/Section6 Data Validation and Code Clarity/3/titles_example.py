from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., title="User ID", example=1)
    name: str = Field(..., title="Full Name", example="Alice")
    age: int = Field(..., title="Age of User", example=30)
    email: str = Field(..., description="User's email address", example="alice@example.com")

# Example usage
user_dict = {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"}
user = User(**user_dict)
print(user)
