from pydantic import BaseModel
from typing import List

class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    posts: List[PostSchema] = []

    class Config:
        orm_mode = True
