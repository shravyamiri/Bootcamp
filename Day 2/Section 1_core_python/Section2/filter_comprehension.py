# Filter with Comprehension:
words = ["hi", "hello", "bye"]

# Using list comprehension to filter words with even lengths
even_length_words = [word for word in words if len(word) % 2 == 0]

# Displaying the result
print("Filter with Comprehension:", even_length_words)
