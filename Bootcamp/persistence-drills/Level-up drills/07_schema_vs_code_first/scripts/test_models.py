import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.postgres import AsyncSessionLocal as PostgresSession, init_db as init_postgres
from database.sqlite import AsyncSessionLocal as SqliteSession, init_db as init_sqlite
from models.user import User
from models.product import Product
from models.order import Order


async def test_models(dialect: str):
    session = PostgresSession() if dialect == "postgresql" else SqliteSession()
    init_func = init_postgres if dialect == "postgresql" else init_sqlite

    await init_func()

    async with session as db:
        # Insert a user
        user = User(username="alice", email="alice@example.com")
        db.add(user)
        await db.commit()
        await db.refresh(user)

        # Insert a product
        product = Product(name="Laptop", price=999.99, stock=10)
        db.add(product)
        await db.commit()
        await db.refresh(product)

        # Insert an order
        order = Order(user_id=user.id, product_id=product.id, quantity=2)
        db.add(order)
        await db.commit()
        await db.refresh(order)

        # Query data
        result = await db.execute(select(User).filter_by(username="alice"))
        user_fetched = result.scalars().first()
        result = await db.execute(select(Product).filter_by(name="Laptop"))
        product_fetched = result.scalars().first()
        result = await db.execute(select(Order).filter_by(user_id=user.id))
        order_fetched = result.scalars().first()

        # Verify
        print(f"{dialect} - User: {user_fetched.username}, {user_fetched.email}")
        print(f"{dialect} - Product: {product_fetched.name}, ${product_fetched.price}, Stock: {product_fetched.stock}")
        print(
            f"{dialect} - Order: user_id={order_fetched.user_id}, product_id={order_fetched.product_id}, quantity={order_fetched.quantity}")


if __name__ == "__main__":
    asyncio.run(test_models("postgresql"))
    asyncio.run(test_models("sqlite"))