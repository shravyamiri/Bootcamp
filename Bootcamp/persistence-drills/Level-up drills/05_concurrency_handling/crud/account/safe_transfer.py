from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import Select
from models.account import Account
from schemas.account import TransferSchema, AccountResponseSchema
from typing import Optional


async def safe_transfer(db: AsyncSession, transfer_data: TransferSchema, dialect: str) -> Optional[
    AccountResponseSchema]:
    async with db.begin():  # Begin transaction
        # Lock accounts in consistent order to prevent deadlocks
        account_ids = sorted([transfer_data.from_account_id, transfer_data.to_account_id])
        query = select(Account).filter(Account.id.in_(account_ids))
        if dialect == "postgresql":
            query = query.with_for_update()  # SELECT FOR UPDATE
        result = await db.execute(query)
        accounts = result.scalars().all()

        # Map accounts
        accounts_dict = {account.id: account for account in accounts}
        from_account = accounts_dict.get(transfer_data.from_account_id)
        to_account = accounts_dict.get(transfer_data.to_account_id)

        if not from_account or not to_account or from_account.balance < transfer_data.amount:
            await db.rollback()
            return None

        # Update balances
        from_account.balance -= transfer_data.amount
        to_account.balance += transfer_data.amount
        await db.commit()

        return AccountResponseSchema.from_orm(from_account)