import json

data = {"name": "Shravya", "age": 25, "location": "India"}
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print("Pretty JSON:\n", pretty_json)
