from contextlib import suppress

my_dict = {"name": "Alice"}

# Suppressing KeyError when trying to access a non-existent key
with suppress(KeyError):
    value = my_dict["age"]  # This will not raise an error

print("No error raised despite missing key!")
