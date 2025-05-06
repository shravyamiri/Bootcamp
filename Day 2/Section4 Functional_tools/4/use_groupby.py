import itertools

# List of dictionaries
data = [
    {'name': 'Alice', 'group': 'A'},
    {'name': 'Bob', 'group': 'B'},
    {'name': 'Charlie', 'group': 'A'},
    {'name': 'David', 'group': 'B'}
]

# Sort data by 'group' and group by 'group' key
data.sort(key=lambda x: x['group'])
grouped = itertools.groupby(data, key=lambda x: x['group'])

# Example usage: Print grouped items
for key, group in grouped:
    print(key)
    for item in group:
        print(item)
