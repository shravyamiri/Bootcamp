from pydantic import BaseModel, conint, constr

class User(BaseModel):
    name: constr(min_length=3)  # Username must have a minimum length of 3
    age: conint(gt=0)  # Age must be greater than 0

# Example usage
user_dict = {"name": "John", "age": 25}
user = User(**user_dict)
print(user)
