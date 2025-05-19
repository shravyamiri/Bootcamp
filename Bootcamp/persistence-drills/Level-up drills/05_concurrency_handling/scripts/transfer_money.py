import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database.postgres import AsyncSessionLocal as PostgresSession, init_db as init_postgres
from database.sqlite import AsyncSessionLocal as SqliteSession, init_db as init_sqlite
from schemas.account import TransferSchema
from crud.account.naive_transfer import naive_transfer
from crud.account.safe_transfer import safe_transfer
from models.account import Account


async def concurrent_transfers(session: AsyncSession, transfer_func, dialect: str, transfer_data: TransferSchema,
                               count: int):
    tasks = [transfer_func(session, transfer_data, dialect) for _ in range(count)]
    await asyncio.gather(*tasks)


async def test_transfers(dialect: str):
    session = PostgresSession() if dialect == "postgresql" else SqliteSession()
    init_func = init_postgres if dialect == "postgresql" else init_sqlite

    await init_func()

    # Setup accounts
    async with session as db:
        db.add(Account(id=1, balance=1000.0))
        db.add(Account(id=2, balance=1000.0))
        await db.commit()

    transfer_data = TransferSchema(from_account_id=1, to_account_id=2, amount=100.0)

    # Test naive transfer
    async with session as db:
        await concurrent_transfers(db, naive_transfer, dialect, transfer_data, count=5)
        result = await db.execute(select(Account).filter(Account.id == 1))
        account = result.scalars().first()
        print(f"{dialect} - Naive transfer: Account 1 balance = {account.balance}")

    # Reset accounts
    async with session as db:
        await db.execute(update(Account).filter(Account.id == 1).values(balance=1000.0))
        await db.execute(update(Account).filter(Account.id == 2).values(balance=1000.0))
        await db.commit()

    # Test safe transfer
    async with session as db:
        await concurrent_transfers(db, safe_transfer, dialect, transfer_data, count=5)
        result = await db.execute(select(Account).filter(Account.id == 1))
        account = result.scalars().first()
        print(f"{dialect} - Safe transfer: Account 1 balance = {account.balance}")


if __name__ == "__main__":
    asyncio.run(test_transfers("postgresql"))
    asyncio.run(test_transfers("sqlite"))