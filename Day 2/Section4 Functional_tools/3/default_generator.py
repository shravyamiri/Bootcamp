import functools

# Create a dictionary that generates a new dictionary for every missing key
default_dict = functools.partial(dict, **{'nested': {}})

# Example usage:
nested_dict = default_dict()
nested_dict['nested']['key'] = 'value'
print(nested_dict)  # Outputs: {'nested': {'key': 'value'}}
