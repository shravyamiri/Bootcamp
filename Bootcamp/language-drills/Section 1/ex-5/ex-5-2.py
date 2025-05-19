try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Division successful")
finally:
    print("Cleanup done")
