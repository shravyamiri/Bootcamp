from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]
most_common = Counter(numbers).most_common(2)

print(most_common)
# Output: [(3, 3), (2, 2)]
