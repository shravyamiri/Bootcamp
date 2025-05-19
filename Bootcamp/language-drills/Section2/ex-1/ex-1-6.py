# Using `__getattr__` in a custom class to handle missing attributes
class CustomObject:
    def __getattr__(self, name):
        print(f"Attribute {name} not found. Returning a default value.")
        return f"Default value for {name}"

obj = CustomObject()
print(obj.some_attribute)  # This will trigger `__getattr__`
