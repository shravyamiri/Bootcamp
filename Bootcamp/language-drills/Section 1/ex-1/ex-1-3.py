# 8. Immutable Tuples: Attempting to modify an element
immutable_tuple = (1, 2, 3)
print("Original tuple:", immutable_tuple)

# Trying to change an element (will raise a TypeError)
try:
    immutable_tuple[0] = 99  # This will raise an error because tuples are immutable
except TypeError as e:
    print("\n8. Tuple immutability:")
    print("   Cannot modify tuple elements.")
    print("   Error:", e)
