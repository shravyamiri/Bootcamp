import time

class DBConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.locked = False  # Simulating if the DB is locked or not

    def __enter__(self):
        # Simulate acquiring the database connection (lock)
        if self.locked:
            raise Exception(f"Database {self.db_name} is already in use.")
        print(f"Opening connection to {self.db_name}...")
        self.locked = True
        time.sleep(1)  # Simulating the connection time
        print(f"Connection to {self.db_name} established.")
        return self  # Returning self, which represents the 'resource'

    def __exit__(self, exc_type, exc_value, traceback):
        # Simulate releasing the database connection (unlock)
        print(f"Closing connection to {self.db_name}...")
        time.sleep(1)  # Simulating the disconnection time
        self.locked = False
        print(f"Connection to {self.db_name} closed.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress the exception if any (optional)

# Using the DBConnection context manager
try:
    with DBConnection("MyDB") as db:
        print("Performing operations on the database...")
        # Simulate some DB operations
        time.sleep(2)
        print("Operations complete.")
except Exception as e:
    print(f"Error: {e}")

# Attempting to acquire the DB connection again while it's still open
try:
    with DBConnection("MyDB") as db1:
        print("Performing operations on MyDB again...")
except Exception as e:
    print(f"Error: {e}")
