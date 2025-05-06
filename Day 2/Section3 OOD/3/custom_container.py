class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

class Library:
    def __init__(self):
        # Initialize with an empty list of books
        self.books = []

    def add_book(self, book):
        # Add a Book to the library
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book objects can be added to the library.")

    def __len__(self):
        # Return the number of books in the library
        return len(self.books)

# Create some Book instances
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Animal Farm", "George Orwell", 1945)
book3 = Book("Brave New World", "Aldous Huxley", 1932)

# Create a Library instance
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Check the number of books in the library using len()
print(f"The library contains {len(library)} books.")  # Output: 3
