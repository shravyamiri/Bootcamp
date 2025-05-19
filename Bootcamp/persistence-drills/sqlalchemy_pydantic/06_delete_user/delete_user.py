from database import SessionLocal
from models import User

def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        print("User deleted.")
    else:
        print("User not found.")
    db.close()

delete_user(1)
