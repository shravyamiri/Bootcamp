# Define the base class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"Book: '{self.title}' by {self.author}"

# Define a subclass Novel that inherits from Book
class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)  # Call the constructor of the parent class
        self.genre = genre

    def describe(self):
        return f"Novel: '{self.title}' by {self.author}, Genre: {self.genre}"

# Create an instance of Novel
novel = Novel("1984", "George Orwell", "Dystopian")

# Check if the instance is a Book
print(isinstance(novel, Book))  # Should return True because Novel is a subclass of Book
