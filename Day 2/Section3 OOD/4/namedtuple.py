from collections import namedtuple

# Define a namedtuple called Point
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p = Point(3, 4)

# Access fields by name
print(f'Point x: {p.x}, y: {p.y}')  # Output: Point x: 3, y: 4

# Access fields like regular tuple elements
print(f'Point[0]: {p[0]}, Point[1]: {p[1]}')  # Output: Point[0]: 3, Point[1]: 4
