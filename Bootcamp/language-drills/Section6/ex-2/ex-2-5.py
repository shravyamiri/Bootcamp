from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator('name')
    def capitalize_name(cls, v):
        return v.capitalize()

# Example usage
user_dict = {"name": "alice", "age": 30}
user = User(**user_dict)
print(user)
