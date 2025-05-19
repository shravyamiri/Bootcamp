from collections import defaultdict

default_lambda = defaultdict(lambda: "N/A")
default_lambda["name"] = "Alice"

print(default_lambda["name"])  # Output: Alice
print(default_lambda["age"])   # Output: N/A
