# Define the dictionary
my_dict = {"name": "John", "city": "New York"}

# Look Before You Leap (LBYL)
if "age" in my_dict:
    print(my_dict["age"])  # Safely access key
else:
    print("Key not found!")
