import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_safe_json(self):
        return json.dumps({"username": self.username})

user = User("admin", "secret")
print(user.to_safe_json())