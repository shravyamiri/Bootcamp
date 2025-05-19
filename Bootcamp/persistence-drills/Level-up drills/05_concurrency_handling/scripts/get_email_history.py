import asyncio
from database.postgres import AsyncSessionLocal as PostgresSession, init_db as init_postgres
from database.sqlite import AsyncSessionLocal as SqliteSession, init_db as init_sqlite
from crud.user.get_email_history import get_email_history
from models.email_history import EmailHistory
from models.user import User


async def test_email_history(dialect: str):
    session = PostgresSession() if dialect == "postgresql" else SqliteSession()
    init_func = init_postgres if dialect == "postgresql" else init_sqlite

    await init_func()
    async with session as db:
        # Insert sample data
        user = User(name="Bob", email="bob@example.com")
        db.add(user)
        await db.commit()
        db.add(EmailHistory(user_id=user.id, email="bob@example.com"))
        db.add(EmailHistory(user_id=user.id, email="bob.updated@example.com"))
        await db.commit()

        # Fetch latest email
        latest = await get_email_history(db, user_id=user.id, latest_only=True)
        print(f"{dialect} - Latest email: {latest[0].email} at {latest[0].changed_at}")

        # Fetch all history
        history = await get_email_history(db, user_id=user.id, latest_only=False)
        print(f"{dialect} - Email history:")
        for entry in history:
            print(f"  {entry.email} at {entry.changed_at}")


if __name__ == "__main__":
    asyncio.run(test_email_history("postgresql"))
    asyncio.run(test_email_history("sqlite"))