from pydantic import BaseModel

class UserProfileBlobSchema(BaseModel):
    user_id: int
    image_data: bytes

class UserProfileFileSchema(BaseModel):
    user_id: int
    image_filename: str

class UserProfileResponseSchema(BaseModel):
    id: int
    user_id: int
    image_blob: bytes | None
    image_path: str | None

    class Config:
        from_attributes = True