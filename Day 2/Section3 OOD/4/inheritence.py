from dataclasses import dataclass

# Base dataclass User
@dataclass
class User:
    name: str
    age: int = 0  # Default age is 0

# Subclass AdminUser that extends User
@dataclass
class AdminUser(User):
    access_level: str  # Non-default argument should come first

# Create an instance of AdminUser
admin = AdminUser(name="Alice", access_level="Admin", age=30)

# Print the instance
print(admin)

# Access the attributes
print(f"Name: {admin.name}, Age: {admin.age}, Access Level: {admin.access_level}")
