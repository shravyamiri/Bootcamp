# EAFP with `getattr()` to handle missing attributes
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

# Using getattr with a fallback value
print(getattr(p, "name", "Attribute not found"))
print(getattr(p, "age", "Attribute not found"))
