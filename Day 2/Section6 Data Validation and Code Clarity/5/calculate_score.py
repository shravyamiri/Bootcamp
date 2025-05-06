# Bad
def do_it(data):
    return sum(data)

# Good
def calculate_score(scores):
    return sum(scores)

print(calculate_score([10, 20, 30]))
