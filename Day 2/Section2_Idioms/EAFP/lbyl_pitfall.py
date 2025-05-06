# LBYL Pitfall in File Handling with Race Conditions

import os
import time

# Simulate checking and opening a file in a race condition
file_path = "temp.txt"

if os.path.exists(file_path):  # Checking if file exists (LBYL)
    with open(file_path, "r") as file:
        print(file.read())
else:
    print("File does not exist!")

# This code can lead to a race condition if the file is deleted after the check but before opening.
