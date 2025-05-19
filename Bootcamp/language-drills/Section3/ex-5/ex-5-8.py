class Book:
    def __init__(self, title):
        self.title = title

    @classmethod
    def describe_class(cls):
        print(f"This is a {cls.__name__} class")

class Novel(Book):
    @classmethod
    def describe_class(cls):
        print(f"Subclass: This is a {cls.__name__} class")

# Calling on base class
Book.describe_class()      # Output: This is a Book class

# Calling on subclass
Novel.describe_class()     # Output: Subclass: This is a Novel class
