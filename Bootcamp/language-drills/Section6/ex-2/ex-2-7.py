from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Example usage
user_dict = {"name": "Alice", "age": 30}
user = User(**user_dict)

# Convert to dictionary and JSON
user_dict_out = user.dict()
user_json_out = user.json()

print("User as dict:", user_dict_out)
print("User as JSON:", user_json_out)
