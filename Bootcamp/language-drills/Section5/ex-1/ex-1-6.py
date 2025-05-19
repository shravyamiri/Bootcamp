from collections import OrderedDict

ordered = OrderedDict()
ordered['one'] = 1
ordered['two'] = 2
ordered['three'] = 3

for key, value in ordered.items():
    print(f"{key}: {value}")
# Output:
# one: 1
# two: 2
# three: 3
