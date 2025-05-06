class Book:
    # Class variable (shared by all instances of the class)
    category = "Fiction"

    # Constructor to initialize the title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to return a formatted description of the book
    def describe(self):
        return f"Book Title: {self.title}, Author: {self.author}, Category: {self.category}"

    # Method to update the title
    def update_title(self, new_title):
        # Update the title of the book
        self.title = new_title
        print(f"Title updated to: {self.title}")

# Create an instance of the Book class
my_book = Book("1984", "Orwell")

# Print initial description of the book
print("Before title update:")
print(my_book.describe())  # Expected: Book Title: 1984, Author: Orwell, Category: Fiction

# Update the title using the update_title method
my_book.update_title("Animal Farm")

# Print the updated description of the book
print("\nAfter title update:")
print(my_book.describe())  # Expected: Book Title: Animal Farm, Author: Orwell, Category: Fiction
