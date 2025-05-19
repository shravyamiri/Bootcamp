from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    nickname: Optional[str] = None  # Nullable field with default None

# Example usage
user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)
print(user)
