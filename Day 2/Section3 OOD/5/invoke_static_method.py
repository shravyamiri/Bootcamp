class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def is_valid_isbn(isbn):
        """Simple check: valid if it's a string of 10 or 13 digits"""
        return isbn.isdigit() and len(isbn) in (10, 13)

# Call static method from the class
print(Book.is_valid_isbn("1234567890"))    # True

# Call static method from an instance
b = Book("1984", "George Orwell")
print(b.is_valid_isbn("9781234567897"))    # True

# Invalid example
print(b.is_valid_isbn("invalid-isbn"))     # False
