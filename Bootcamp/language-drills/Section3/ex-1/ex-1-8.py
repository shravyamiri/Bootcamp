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

# Create an instance of the Book class
book = Book("1984", "Orwell")

# Check if the object is an instance of the Book class
print(isinstance(book, Book))  # Expected: True

# Create a non-Book object (e.g., a string)
non_book = "This is a string"

# Check if the non_book object is an instance of Book
print(isinstance(non_book, Book))  # Expected: False
