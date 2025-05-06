class Book:
    # Class variable
    category = "Fiction"

    # Constructor to initialize the title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to return a formatted description of the book
    def describe(self):
        return f"Book Title: {self.title}, Author: {self.author}"

# Creating an object of the Book class with the title "1984" and author "Orwell"
my_book = Book("1984", "Orwell")

# Accessing the class variable through the object
print(f"Category: {my_book.category}")

# Accessing the describe method
print(my_book.describe())
