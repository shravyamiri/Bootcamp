class LogContextManager:
    def __enter__(self):
        # Code that runs when entering the context (before the block starts)
        print("Entering the context...")

        # Return the object itself, if needed
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Code that runs when exiting the context (after the block ends)
        print("Exiting the context...")

        # Handling exceptions if any (exc_type, exc_value, traceback)
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  # Return False to propagate exceptions, True to suppress them

# Using the custom context manager
with LogContextManager():
    print("Inside the context...")
    # Uncomment the next line to see how exception handling works
    # raise ValueError("Something went wrong!")  # Uncomment to test exception handling

print("Outside the context.")
