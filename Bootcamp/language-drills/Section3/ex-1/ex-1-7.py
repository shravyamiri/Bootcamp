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
print("Before adding dynamic attribute:")
print(book.describe())  # Expected: Book Title: 1984, Author: Orwell, Category: Fiction

# Add a dynamic attribute after the object is created
book.publisher = "Secker & Warburg"
print("\nAfter adding dynamic attribute:")
print(f"Publisher: {book.publisher}")  # Expected: Publisher: Secker & Warburg
