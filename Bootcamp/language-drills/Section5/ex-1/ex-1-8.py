from collections import defaultdict

nested = defaultdict(lambda: defaultdict(int))
nested["group1"]["itemA"] += 1
nested["group1"]["itemB"] += 2
nested["group2"]["itemA"] += 3

print(dict(nested))
# Output: {'group1': {'itemA': 1, 'itemB': 2}, 'group2': {'itemA': 3}}
