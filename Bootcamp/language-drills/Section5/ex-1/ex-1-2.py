from collections import Counter

text = "hello world"
char_freq = Counter(text)

print(char_freq)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
