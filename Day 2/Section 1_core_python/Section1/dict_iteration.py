# 5. Dictionary Iteration: Print all keys and values
person = {"name": "Bob", "age": 30}

print("5. Dictionary contents:")
# Loop through the dictionary using .items() to get both key and value
for key, value in person.items():
    print(f"   {key}: {value}")
