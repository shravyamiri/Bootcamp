import asyncio
import time
import psutil
import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database.postgres import AsyncSessionLocal as PostgresSession, init_db as init_postgres
from database.sqlite import AsyncSessionLocal as SqliteSession, init_db as init_sqlite
from models.product import Product


def get_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss / 1024 / 1024  # MB


async def single_inserts(db: AsyncSession, num_records: int):
    start_time = time.time()
    start_memory = get_memory_usage()

    for i in range(num_records):
        product = Product(name=f"Product_{i}", price=random.uniform(10, 1000))
        db.add(product)
        await db.commit()  # Commit each insert

    end_time = time.time()
    end_memory = get_memory_usage()

    return {
        "time_seconds": end_time - start_time,
        "memory_mb": end_memory - start_memory
    }


async def batch_inserts(db: AsyncSession, num_records: int, batch_size: int = 10000):
    start_time = time.time()
    start_memory = get_memory_usage()

    async with db.begin():  # Single transaction
        for i in range(0, num_records, batch_size):
            products = [
                Product(name=f"Product_{j}", price=random.uniform(10, 1000))
                for j in range(i, min(i + batch_size, num_records))
            ]
            db.add_all(products)
            await db.flush()  # Flush to DB without committing
        await db.commit()  # Commit once at the end

    end_time = time.time()
    end_memory = get_memory_usage()

    return {
        "time_seconds": end_time - start_time,
        "memory_mb": end_memory - start_memory
    }


async def test_generate_products(dialect: str, num_records: int = 1000000):
    session = PostgresSession() if dialect == "postgresql" else SqliteSession()
    init_func = init_postgres if dialect == "postgresql" else init_sqlite

    await init_func()

    # Clear products table
    async with session as db:
        await db.execute(text("DELETE FROM products"))
        await db.commit()

    # Test single inserts
    async with session as db:
        result = await single_inserts(db, num_records)
        print(f"{dialect} - Single inserts: {result['time_seconds']:.2f} seconds, {result['memory_mb']:.2f} MB")

    # Clear products table
    async with session as db:
        await db.execute(text("DELETE FROM products"))
        await db.commit()

    # Test batch inserts
    async with session as db:
        result = await batch_inserts(db, num_records)
        print(f"{dialect} - Batch inserts: {result['time_seconds']:.2f} seconds, {result['memory_mb']:.2f} MB")

    # Verify record count
    async with session as db:
        result = await db.execute(text("SELECT COUNT(*) FROM products"))
        count = result.scalar()
        print(f"{dialect} - Total records: {count}")


if __name__ == "__main__":
    asyncio.run(test_generate_products("postgresql"))
    asyncio.run(test_generate_products("sqlite"))