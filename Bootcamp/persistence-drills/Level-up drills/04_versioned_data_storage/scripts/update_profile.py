import asyncio
from database.postgres import AsyncSessionLocal, init_db
from schemas.user import UserUpdateSchema
from crud.user.update_profile import update_profile

async def main():
    await init_db()
    async with AsyncSessionLocal() as db:
        update_data = UserUpdateSchema(name="Alice Updated", email="alice.updated@example.com")
        result = await update_profile(db, user_id=1, update_data=update_data)
        if result:
            print(f"Updated user: {result.name}, {result.email}, {result.created_at}")
        else:
            print("User not found")

if __name__ == "__main__":
    asyncio.run(main())