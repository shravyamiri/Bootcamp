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


# Create a Book instance
book1 = Book("1984", "George Orwell", 1949)

# Printing the object (calls __str__ method)
print(book1)  # This will call the __str__ method

# Inspecting the object (this will call __repr__ method)
print(repr(book1))  # This will call the __repr__ method

# You can also check how the object is displayed in an interactive shell (e.g., Jupyter Notebook or Python shell)
book_list = [book1]
print(book_list)  # When printing a list, __repr__ of the objects in the list is used
