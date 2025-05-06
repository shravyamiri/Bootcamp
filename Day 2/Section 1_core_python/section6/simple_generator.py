def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Test the countdown generator
for number in countdown(5):
    print(number)
