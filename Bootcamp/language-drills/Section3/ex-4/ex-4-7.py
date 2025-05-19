from collections import namedtuple

# Define a namedtuple with invalid field names
Point = namedtuple('Point', ['x', '1y', 'invalid field', 'class'])

# Print the renamed fields
print(Point._fields)  # Output: ('x', '1y', 'invalid_field', 'class')

# Create an instance with invalid field names
p = Point(3, 4, 5, 6)

# Access the renamed fields
print(f'Point x: {p.x}, 1y: {p[1]}, invalid_field: {p[2]}, class: {p[3]}')
