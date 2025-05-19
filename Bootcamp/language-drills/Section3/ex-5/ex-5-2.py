class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def from_string(cls, s: str):
        """Create a Book instance from a string like 'Title|Author'"""
        try:
            title, author = s.split("|")
            return cls(title.strip(), author.strip())
        except ValueError:
            raise ValueError("Input string must be in 'Title|Author' format")

# Test the class method
book_data = "The Alchemist | Paulo Coelho"
book = Book.from_string(book_data)

print(book)  # Output: The Alchemist by Paulo Coelho
