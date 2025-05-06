def accumulator():
    total = 0
    while True:
        num = yield total  # Receives input from .send()
        if num is not None:
            total += num

# Create an instance of the generator
gen = accumulator()

# Start the generator and send values
next(gen)  # Prime the generator
print(gen.send(5))  # Output: 5
print(gen.send(10))  # Output: 15
print(gen.send(15))  # Output: 30
