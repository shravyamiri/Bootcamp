class Book:
    # Class variable (shared by all instances of the class)
    category = "Fiction"

    # Constructor with default values for title and author
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    # Method to return a formatted description of the book
    def describe(self):
        return f"Book Title: {self.title}, Author: {self.author}, Category: {self.category}"

# Subclass that inherits from Book
class Novel(Book):
    # Additional attribute specific to the Novel class
    def __init__(self, title="Untitled", author="Unknown", genre="General"):
        super().__init__(title, author)  # Calling the parent class's constructor
        self.genre = genre  # Novel-specific attribute

    # Overriding the describe method to include genre
    def describe(self):
        return f"Novel Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Category: {self.category}"

# Create an instance of the Novel class
novel = Novel("1984", "Orwell", "Dystopian")

# Call the describe method from the Novel class
print(novel.describe())
