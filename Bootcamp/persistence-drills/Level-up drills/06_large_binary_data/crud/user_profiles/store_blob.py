from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user_profile import UserProfile
from schemas.user_profile import UserProfileBlobSchema, UserProfileResponseSchema
from typing import Optional


async def store_blob(db: AsyncSession, profile_data: UserProfileBlobSchema) -> Optional[UserProfileResponseSchema]:
    result = await db.execute(select(UserProfile).filter(UserProfile.user_id == profile_data.user_id))
    profile = result.scalars().first()

    if profile:
        profile.image_blob = profile_data.image_data
        profile.image_path = None
    else:
        profile = UserProfile(user_id=profile_data.user_id, image_blob=profile_data.image_data)
        db.add(profile)

    await db.commit()
    await db.refresh(profile)
    return UserProfileResponseSchema.from_orm(profile)