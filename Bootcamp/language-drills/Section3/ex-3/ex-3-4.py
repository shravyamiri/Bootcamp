class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Informal string representation (for print())
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    # Official string representation (for debugging and inspection)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    # Equality check (compare title and author)
    def __eq__(self, other):
        if isinstance(other, Book):  # Check if the other object is also a Book
            return self.title == other.title and self.author == other.author
        return False

    # Hash function (based on title and author)
    def __hash__(self):
        return hash((self.title, self.author))  # Use a tuple to generate a combined hash

    # Less than comparison for sorting (by title)
    def __lt__(self, other):
        if isinstance(other, Book):  # Ensure we're comparing with another Book
            return self.title < other.title
        return NotImplemented


# Create some Book instances
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Animal Farm", "George Orwell", 1945)
book3 = Book("Brave New World", "Aldous Huxley", 1932)

# Create a list of books
books = [book1, book2, book3]

# Sort books by title
sorted_books = sorted(books)

# Print the sorted books
for book in sorted_books:
    print(book)
