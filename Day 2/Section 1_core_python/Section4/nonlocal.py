# Demonstration of 'nonlocal' in nested functions
def outer_nonlocal():
    count = 0  # This is in the enclosing scope of inner()

    def inner():
        nonlocal count  # Refers to 'count' in the outer_nonlocal() function
        count += 1
        print("Inner count:", count)

    inner()
    print("Outer count after inner():", count)

outer_nonlocal()
