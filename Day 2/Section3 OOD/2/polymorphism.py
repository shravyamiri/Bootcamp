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

# Create instances of both Book and Novel
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
novel1 = Novel("1984", "George Orwell", "Dystopian")

# List of books and novels
items = [book1, novel1]

# Loop through the list and call describe() on each item
for item in items:
    print(item.describe())  # This will call the appropriate describe() method for each object
