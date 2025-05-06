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


# Create some Book instances
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Animal Farm", "George Orwell", 1945)

# Add the books to a set
book_set = {book1, book2, book3}

# Print the set to see unique elements (no duplicates)
print(book_set)

# Check if book1 and book2 are equal and have the same hash
print(book1 == book2)  # True
print(hash(book1) == hash(book2))  # True
