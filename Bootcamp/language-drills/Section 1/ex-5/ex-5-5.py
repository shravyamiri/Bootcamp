def risky_function():
    try:
        result = 10 / 0  # Division by zero
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")
        raise  # Reraise the exception

try:
    risky_function()
except ZeroDivisionError:
    print("Handled re-raised exception.")
