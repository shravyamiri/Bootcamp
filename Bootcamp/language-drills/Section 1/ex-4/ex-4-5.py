# LEGB Rule:
x = 10  # Global variable

def show_local_x():
    x = 20  # Local variable (shadows global inside this function)
    print("Local x:", x)

show_local_x()
print("Global x:", x)
