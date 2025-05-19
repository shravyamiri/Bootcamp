try:
    try:
        num = int(input("Enter a number: "))  # Could raise ValueError
        result = 10 / num  # Could raise ZeroDivisionError
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
