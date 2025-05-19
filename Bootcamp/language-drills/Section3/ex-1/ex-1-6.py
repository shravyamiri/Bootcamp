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

# Create an instance of the Book class with specified arguments
book_with_args = Book("1984", "Orwell")
print("With specified arguments:")
print(book_with_args.describe())  # Expected: Book Title: 1984, Author: Orwell, Category: Fiction

# Create an instance of the Book class without any arguments (default values)
book_without_args = Book()
print("\nWith default arguments:")
print(book_without_args.describe())  # Expected: Book Title: Untitled, Author: Unknown, Category: Fiction
