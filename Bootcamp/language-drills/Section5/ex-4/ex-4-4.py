import csv

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
