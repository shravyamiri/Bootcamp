from pydantic import BaseModel

class EmailHistorySchema(BaseModel):
    id: int
    user_id: int
    email: str
    changed_at: str  # Converted to string for API compatibility

    class Config:
        from_attributes = True