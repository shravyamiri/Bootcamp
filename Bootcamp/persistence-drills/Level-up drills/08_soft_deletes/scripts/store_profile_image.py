import asyncio
import aiofiles
from database.postgres import AsyncSessionLocal as PostgresSession, init_db as init_postgres
from database.sqlite import AsyncSessionLocal as SqliteSession, init_db as init_sqlite
from schemas.user_profile import UserProfileBlobSchema, UserProfileFileSchema
from crud.user_profile.store_blob import store_blob
from crud.user_profile.store_file import store_file
from models.user import User


async def test_store_image(dialect: str):
    session = PostgresSession() if dialect == "postgresql" else SqliteSession()
    init_func = init_postgres if dialect == "postgresql" else init_sqlite

    await init_func()

    # Read sample image
    async with aiofiles.open("test_image.jpg", "rb") as f:
        image_data = await f.read()

    # Insert sample user
    async with session as db:
        user = User(name="Charlie", email="charlie@example.com")
        db.add(user)
        await db.commit()

        # Test BLOB storage
        blob_data = UserProfileBlobSchema(user_id=user.id, image_data=image_data)
        blob_result = await store_blob(db, blob_data)
        print(f"{dialect} - BLOB stored: user_id={blob_result.user_id}, blob_size={len(blob_result.image_blob or b'')}")

        # Test file storage
        file_data = UserProfileFileSchema(user_id=user.id, image_filename=f"user_{user.id}_image.jpg")
        file_result = await store_file(db, file_data, image_data)
        print(f"{dialect} - File stored: user_id={file_result.user_id}, path={file_result.image_path}")


if __name__ == "__main__":
    asyncio.run(test_store_image("postgresql"))
    asyncio.run(test_store_image("sqlite"))