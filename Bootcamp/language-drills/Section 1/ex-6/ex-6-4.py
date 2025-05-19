def running_total(lst):
    total = 0
    for number in lst:
        total += number
        yield total

# Test the running total generator
for total in running_total([1, 2, 3, 4]):
    print(total)
