import os
import aiofiles
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user_profile import UserProfile
from schemas.user_profile import UserProfileFileSchema, UserProfileResponseSchema
from typing import Optional


async def store_file(db: AsyncSession, profile_data: UserProfileFileSchema, image_data: bytes) -> Optional[
    UserProfileResponseSchema]:
    # Save file to disk
    file_path = os.path.join("images", profile_data.image_filename)
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(image_data)

    # Update database
    result = await db.execute(select(UserProfile).filter(UserProfile.user_id == profile_data.user_id))
    profile = result.scalars().first()

    if profile:
        profile.image_path = file_path
        profile.image_blob = None
    else:
        profile = UserProfile(user_id=profile_data.user_id, image_path=file_path)
        db.add(profile)

    await db.commit()
    await db.refresh(profile)
    return UserProfileResponseSchema.from_orm(profile)