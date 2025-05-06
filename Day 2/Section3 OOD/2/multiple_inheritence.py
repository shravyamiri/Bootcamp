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

    # __str__ method to provide a custom string representation
    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, Category: {self.category}"

# Mixin class for audio-related functionality
class AudioMixin:
    def __init__(self, audio_length=0):
        self.audio_length = audio_length  # Length in minutes

    # Method to simulate playing audio
    def play_audio(self):
        print(f"Playing audio for {self.audio_length} minutes.")

# Combining Book and AudioMixin to create AudioBook
class AudioBook(Book, AudioMixin):
    def __init__(self, title, author, audio_length):
        Book.__init__(self, title, author)  # Initialize the Book part
        AudioMixin.__init__(self, audio_length)  # Initialize the AudioMixin part

    # Overriding the describe method to include audio length information
    def describe(self):
        book_description = super().describe()
        return f"{book_description}, Audio Length: {self.audio_length} minutes"

# Create an instance of AudioBook
audio_book = AudioBook("1984", "Orwell", 720)

# Print the details of the audiobook
print(audio_book)

# Play the audio of the audiobook
audio_book.play_audio()
