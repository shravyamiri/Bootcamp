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


# Create Book instances
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Animal Farm", "George Orwell", 1945)

# Equality checks
print(book1 == book2)  # True, same title and author
print(book1 == book3)  # False, different title
