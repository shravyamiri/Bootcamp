from pydantic import BaseModel

class ProductUpsertSchema(BaseModel):
    name: str
    price: float

class ProductResponseSchema(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True