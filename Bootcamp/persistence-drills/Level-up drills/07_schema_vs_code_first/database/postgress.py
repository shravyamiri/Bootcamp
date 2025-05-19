from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models.user import Base
from models.product import Base as ProductBase
from models.order import Base as OrderBase

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/ecommerce_db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(ProductBase.metadata.create_all)
        await conn.run_sync(OrderBase.metadata.create_all)