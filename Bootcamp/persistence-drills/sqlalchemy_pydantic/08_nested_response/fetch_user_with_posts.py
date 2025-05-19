from database import SessionLocal
from models import User
from schemas import UserSchema

db = SessionLocal()
user = db.query(User).filter(User.id == 1).first()
db.close()

if user:
    user_schema = UserSchema.from_orm(user)
    print(user_schema.json(indent=4))
else:
    print("User not found.")
