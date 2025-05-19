import time


class CleanupContextManager:
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def __enter__(self):
        # Simulate acquiring a resource
        print(f"Acquiring {self.resource_name}...")
        time.sleep(1)  # Simulating setup time
        print(f"{self.resource_name} acquired.")
        return self  # Return the resource (self) to use within the 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure cleanup, regardless of whether an exception occurred
        print(f"Cleaning up {self.resource_name}...")
        time.sleep(1)  # Simulating cleanup time
        print(f"{self.resource_name} cleaned up.")

        # If an exception occurred, log the details
        if exc_type:
            print(f"An error occurred: {exc_value}")

        # Return False so the exception is not suppressed
        return False  # This ensures the exception is not suppressed; change to True to suppress it


# Using the context manager with an error occurring inside the block
try:
    with CleanupContextManager("Database Connection") as resource:
        print("Performing some operations on the resource...")
        time.sleep(2)  # Simulate some work
        # Simulating an error inside the context block
        raise ValueError("Something went wrong during the operation!")
except Exception as e:
    print(f"Error caught: {e}")

# Another example, this time without an error
try:
    with CleanupContextManager("File Handler") as resource:
        print("Performing some file operations...")
        time.sleep(2)  # Simulate some work
        print("Operations completed successfully.")
except Exception as e:
    print(f"Error caught: {e}")
