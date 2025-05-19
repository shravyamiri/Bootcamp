import asyncio
from database import AsyncSessionLocal, init_db
from models import User

async def insert_user():
    await init_db()
    async with AsyncSessionLocal() as session:
        new_user = User(name="Async User", email="async@example.com")
        session.add(new_user)
        await session.commit()
        print("Async user added.")

asyncio.run(insert_user())
