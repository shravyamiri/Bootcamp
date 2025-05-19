from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.email_history import EmailHistory
from schemas.email_history import EmailHistorySchema
from typing import List

async def get_email_history(db: AsyncSession, user_id: int, latest_only: bool = False) -> List[EmailHistorySchema]:
    query = select(EmailHistory).filter(EmailHistory.user_id == user_id).order_by(EmailHistory.changed_at.desc())
    if latest_only:
        query = query.limit(1)
    result = await db.execute(query)
    history = result.scalars().all()
    return [EmailHistorySchema.from_orm(entry) for entry in history]