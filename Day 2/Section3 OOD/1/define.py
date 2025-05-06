class Book:
    # Constructor to initialize the title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Example of creating an object of the Book class
my_book = Book("1984", "George Orwell")

# Accessing the attributes of the object
print(f"Title: {my_book.title}")
print(f"Author: {my_book.author}")
