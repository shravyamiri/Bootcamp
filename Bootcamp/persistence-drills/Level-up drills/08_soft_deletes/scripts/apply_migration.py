import asyncio
from alembic.config import Config
from alembic import command

async def apply_migration():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url",
        "postgresql+asyncpg://user:password@localhost:5432/users_db")
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    asyncio.run(apply_migration())