class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __bool__(self):
        # Book is considered truthy if it has a title
        return bool(self.title)

# Create a Book object
book1 = Book("1984", "George Orwell")
book2 = Book("", "Unknown Author")

# Check boolean value of the objects
print(bool(book1))  # Output: True, because book1 has a title "1984"
print(bool(book2))  # Output: False, because book2 has no title
