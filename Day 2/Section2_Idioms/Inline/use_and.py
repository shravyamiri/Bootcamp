is_admin = True

def delete_user(uid):
    print(f"User {uid} deleted")

user_id = 101
is_admin and delete_user(user_id)
