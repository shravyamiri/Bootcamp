from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., description="User's full name")
    age: int = Field(..., description="User's age in years")

# Example usage
user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)
print(user)
