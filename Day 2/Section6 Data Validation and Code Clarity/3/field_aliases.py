from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")
    name: str
    age: int

# Example usage
user_dict = {"user_id": 1, "name": "Alice", "age": 30}
user = User(**user_dict)
print(user)
