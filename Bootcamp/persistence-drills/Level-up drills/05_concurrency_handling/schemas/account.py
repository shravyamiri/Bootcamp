from pydantic import BaseModel

class TransferSchema(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float

class AccountResponseSchema(BaseModel):
    id: int
    balance: float

    class Config:
        from_attributes = True