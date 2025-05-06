from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User model representing a system user.

    Fields:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        age (int): Age of the user.
        email (str): Email address of the user.
    """
    id: int = Field(..., alias="user_id")
    name: str
    age: int
    email: str


# Example usage
user_dict = {"user_id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"}
user = User(**user_dict)
print(user)
