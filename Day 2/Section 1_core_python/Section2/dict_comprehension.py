# Dict Comprehension: Convert ["a", "b"] into {"a": 1, "b": 1}
keys = ["a", "b"]

# Using dictionary comprehension to assign 1 to each key
dict_comprehension = {key: 1 for key in keys}

# Display the result
print("Dict Comprehension:", dict_comprehension)
