class Book:
    # Class variable (shared by all instances of the class)
    category = "Fiction"

    # Constructor with default values for title and author
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    # Method to return a formatted description of the book
    def describe(self):
        return f"Book Title: {self.title}, Author: {self.author}, Category: {self.category}"

    # __str__ method to provide a custom string representation
    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, Category: {self.category}"

# Create an instance of the Book class
book = Book("1984", "Orwell")

# Print the book object, which will automatically call the __str__ method
print(book)
