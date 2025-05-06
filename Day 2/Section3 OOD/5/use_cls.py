class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def from_string(cls, s: str):
        """Create an instance of Book or subclass from a string like 'Title|Author'"""
        try:
            title, author = s.split("|")
            return cls(title.strip(), author.strip())
        except ValueError:
            raise ValueError("Input string must be in 'Title|Author' format")

# Subclass
class Novel(Book):
    def __init__(self, title: str, author: str, genre="Fiction"):
        super().__init__(title, author)
        self.genre = genre

    def __str__(self):
        return f"Novel: {self.title} by {self.author} [{self.genre}]"

# Works with Book
b = Book.from_string("1984 | George Orwell")
print(b)  # Output: 1984 by George Orwell

# Works with Novel because of cls(...)
n = Novel.from_string("The Alchemist | Paulo Coelho")
print(n)  # Output: Novel: The Alchemist by Paulo Coelho [Fiction]
