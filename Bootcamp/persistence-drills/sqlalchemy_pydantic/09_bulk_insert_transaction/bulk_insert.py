from database import SessionLocal
from models import User

def bulk_insert_users(user_list):
    db = SessionLocal()
    try:
        db.bulk_save_objects([User(**user) for user in user_list])
        db.commit()
        print("Users inserted successfully.")
    except Exception as e:
        db.rollback()
        print("Error during bulk insert:", e)
    finally:
        db.close()

bulk_insert_users([
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
])
