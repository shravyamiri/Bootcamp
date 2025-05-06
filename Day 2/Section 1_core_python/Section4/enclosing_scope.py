# Demonstration of Enclosing Scope (LEGB)
def outer():
    msg = "Hello from outer"  

    def inner():
        print(msg)  # Accessing the variable from the enclosing scope

    inner()

outer()
