from database import SessionLocal
from models import User
from schemas import UserSchema

def get_user_by_email(email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    if user:
        return UserSchema.from_orm(user)
    return None

user = get_user_by_email("alice@example.com")
if user:
    print(user.json())
else:
    print("User not found.")
