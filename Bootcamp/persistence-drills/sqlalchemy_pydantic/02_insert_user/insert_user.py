from database import SessionLocal
from models import User
from schemas import UserSchema

db = SessionLocal()

user_data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
user_schema = UserSchema(**user_data)

new_user = User(**user_schema.dict())
db.add(new_user)
db.commit()
db.close()
