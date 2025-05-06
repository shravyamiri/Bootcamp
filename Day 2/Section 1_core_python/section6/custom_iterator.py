class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Create an instance of the Counter class
counter = Counter(5)

# Iterate through the Counter using a for loop
for num in counter:
    print(num)
