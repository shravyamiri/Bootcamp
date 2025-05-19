import json

data = {"name": "Shravya", "age": 25}
json_string = json.dumps(data)
print("Serialized JSON:", json_string)

loaded_data = json.loads(json_string)
print("Deserialized Data:", loaded_data)
