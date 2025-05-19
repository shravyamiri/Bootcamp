
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from models.product import Product
from schemas.product import ProductUpsertSchema, ProductResponseSchema
from typing import Optional

async def upsert_product(db: AsyncSession, product_data: ProductUpsertSchema, dialect: str) -> ProductResponseSchema:
    if dialect == "postgresql":
        insert_stmt = pg_insert(Product).values(
            name=product_data.name,
            price=product_data.price
        )
        upsert_stmt = insert_stmt.on_conflict_do_update(
            constraint="uq_products_name",
            set_=dict(price=product_data.price)
        )
    else:  # sqlite
        insert_stmt = sqlite_insert(Product).values(
            name=product_data.name,
            price=product_data.price
        )
        upsert_stmt = insert_stmt.prefix_with("OR REPLACE")

    await db.execute(upsert_stmt)
    await db.commit()

    result = await db.execute(select(Product).filter(Product.name == product_data.name))
    product = result.scalars().first()
    return ProductResponseSchema.from_orm(product)