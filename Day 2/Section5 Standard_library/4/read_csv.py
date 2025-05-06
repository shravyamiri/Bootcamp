import csv
from collections import namedtuple

with open('data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    Row = namedtuple("Row", headers)
    for row in reader:
        record = Row(*row)
        print(record.name, record.age)  # Access like attributes
