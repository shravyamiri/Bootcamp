from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select SELF
from models.user import User
from schemas.user import UserUpdateSchema, UserResponseSchema
from typing import Optional

async def update_profile(db: AsyncSession, user_id: int, update_data: UserUpdateSchema) -> Optional[UserResponseSchema]:
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    if not user:
        return None
    user.name = update_data.name
    user.email = update_data.email
    await db.commit()
    await db.refresh(user)
    return UserResponseSchema.from_orm(user)