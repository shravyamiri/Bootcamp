import re

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        # Check for ISBN-10
        if len(isbn) == 10 and re.match(r'^\d{9}[\dX]$', isbn):
            # ISBN-10 checksum calculation
            total = 0
            for i in range(9):
                total += int(isbn[i]) * (10 - i)
            checksum = 11 - (total % 11)
            if checksum == 10:
                checksum = 'X'
            elif checksum == 11:
                checksum = '0'
            if str(checksum) == isbn[-1]:
                return True

        # Check for ISBN-13
        elif len(isbn) == 13 and re.match(r'^\d{13}$', isbn):
            # ISBN-13 checksum calculation
            total = 0
            for i in range(12):
                total += int(isbn[i]) * (1 if i % 2 == 0 else 3)
            checksum = (10 - (total % 10)) % 10
            if str(checksum) == isbn[-1]:
                return True

        # If neither valid ISBN-10 nor ISBN-13
        return False

# Create a Book object
book = Book("1984", "George Orwell", "123456789X")

# Validate ISBN
print(f"Is the ISBN valid? {Book.validate_isbn(book.isbn)}")
