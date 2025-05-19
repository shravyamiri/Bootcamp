from database import SessionLocal
from models import User

def update_user_email(user_id: int, new_email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        print("Email updated.")
    else:
        print("User not found.")
    db.close()

update_user_email(1, "alice_updated@example.com")
