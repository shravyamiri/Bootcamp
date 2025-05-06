import logging

logging.basicConfig(level=logging.ERROR)

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        logging.error("Division by zero attempted")
        raise  # Re-raise the exception

divide(10, 0)
