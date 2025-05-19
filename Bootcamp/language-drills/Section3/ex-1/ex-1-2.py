class Book:
    # Constructor to initialize the title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Creating an object of the Book class with the title "1984" and author "Orwell"
my_book = Book("1984", "Orwell")

# Accessing and printing the attributes of the object
print(f"Title: {my_book.title}")
print(f"Author: {my_book.author}")
