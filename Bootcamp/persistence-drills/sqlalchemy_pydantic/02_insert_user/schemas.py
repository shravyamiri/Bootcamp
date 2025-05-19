from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
