from database import SessionLocal
from models import User
from schemas import UserSchema

db = SessionLocal()
users = db.query(User).all()
db.close()

user_schemas = [UserSchema.from_orm(user) for user in users]

for user in user_schemas:
    print(user.json())
