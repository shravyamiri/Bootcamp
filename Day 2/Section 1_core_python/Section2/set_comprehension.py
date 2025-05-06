# Set Comprehension: From "hello world", get all unique vowels
text = "hello world"

# Using set comprehension to get unique vowels
vowels = {char for char in text if char in 'aeiou'}

# Display the result
print("Set Comprehension:", vowels)
