import asyncio
from database.postgres import AsyncSessionLocal as PostgresSession, init_db as init_postgres
from database.sqlite import AsyncSessionLocal as SqliteSession, init_db as init_sqlite
from schemas.product import ProductUpsertSchema
from crud.product.upsert_product import upsert_product


async def test_upsert(dialect: str):
    session = PostgresSession() if dialect == "postgresql" else SqliteSession()
    init_func = init_postgres if dialect == "postgresql" else init_sqlite

    await init_func()
    async with session as db:
        # First upsert: insert
        product_data = ProductUpsertSchema(name="Laptop", price=999.99)
        result = await upsert_product(db, product_data, dialect)
        print(f"{dialect} - Inserted: {result.name}, ${result.price}")

        # Second upsert: update price
        product_data = ProductUpsertSchema(name="Laptop", price=1099.99)
        result = await upsert_product(db, product_data, dialect)
        print(f"{dialect} - Updated: {result.name}, ${result.price}")


if __name__ == "__main__":
    asyncio.run(test_upsert("postgresql"))
    asyncio.run(test_upsert("sqlite"))