from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.account import Account
from schemas.account import TransferSchema, AccountResponseSchema
from typing import Optional


async def naive_transfer(db: AsyncSession, transfer_data: TransferSchema) -> Optional[AccountResponseSchema]:
    # Fetch source account
    result = await db.execute(select(Account).filter(Account.id == transfer_data.from_account_id))
    from_account = result.scalars().first()
    if not from_account or from_account.balance < transfer_data.amount:
        return None

    # Fetch destination account
    result = await db.execute(select(Account).filter(Account.id == transfer_data.to_account_id))
    to_account = result.scalars().first()
    if not to_account:
        return None

    # Update balances without transaction
    from_account.balance -= transfer_data.amount
    to_account.balance += transfer_data.amount
    await db.commit()

    return AccountResponseSchema.from_orm(from_account)