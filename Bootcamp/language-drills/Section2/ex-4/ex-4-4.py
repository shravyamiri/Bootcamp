import time
from contextlib import contextmanager


@contextmanager
def timer():
    # Code before entering the context
    start_time = time.time()  # Record the start time
    print("Timer started...")

    # Yield control back to the block inside the 'with' statement
    yield

    # Code after the block ends
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f"Timer stopped. Elapsed time: {elapsed_time:.4f} seconds.")


# Using the custom context manager
with timer():
    # Simulate some work
    time.sleep(2)  # Sleep for 2 seconds (you can replace this with your own code)

print("Outside the timer context.")
