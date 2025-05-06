x = 5  # Global variable

def modify_global():
    global x       # Tells Python to use the global x, not a local one
    x = 100        # Modifies the global variable
    print("Inside function, modified x to:", x)

modify_global()
print("Outside function, global x is now:", x)
