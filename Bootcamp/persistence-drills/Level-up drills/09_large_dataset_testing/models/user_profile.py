from sqlalchemy import Column, Integer, LargeBinary, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    image_blob = Column(LargeBinary, nullable=True)
    image_path = Column(String, nullable=True)