# Example of manually raising and catching StopIteration
my_list = [1, 2, 3]

# Create an iterator
iterator = iter(my_list)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        print("End of iterator reached!")
        break
