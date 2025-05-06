from pydantic import BaseModel

class Profile(BaseModel):
    bio: str
    website: str

class User(BaseModel):
    name: str
    age: int
    profile: Profile

# Example usage
user_dict = {
    "name": "Alice",
    "age": 30,
    "profile": {
        "bio": "Software Developer",
        "website": "https://alice.dev"
    }
}
user = User(**user_dict)
print(user)
