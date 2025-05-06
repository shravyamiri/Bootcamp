# 4. Dictionary Access: Using .get() and .setdefault()
user = {"name": "Alice"}
print("Original dictionary:", user)

# Using .get() for existing and missing keys
print("\nUsing .get():")
print("Get 'name':", user.get("name"))  # Existing key
print("Get 'age' (not present, default 25):", user.get("age", 25))  # Missing key with default

# Using .setdefault() to insert a default value if key is missing
print("\nUsing .setdefault():")
user.setdefault("age", 30)  # Adds 'age': 30 only if 'age' is not already in the dictionary
print("Dictionary after setdefault('age', 30):", user)
