from pydantic import BaseModel, EmailStr

class UserUpdateSchema(BaseModel):
    name: str
    email: EmailStr

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: str  # Converted to string for API compatibility

    class Config:
        from_attributes = True