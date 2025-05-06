class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self, greeting="Hello"):
        # Return a greeting message when the instance is called
        return f"{greeting}, {self.name}!"

# Create an instance of Greeter
greeter = Greeter("Alice")

# Now we can use the instance like a function
print(greeter())  # Output: Hello, Alice!
print(greeter("Good morning"))  # Output: Good morning, Alice!
