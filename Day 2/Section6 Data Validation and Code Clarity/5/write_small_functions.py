# Good design using small functions
def get_user_input():
    return input("Enter your name: ")

def validate_name(name):
    return len(name.strip()) > 0

def greet_user(name):
    print(f"Hello, {name}!")

def main():
    name = get_user_input()
    if validate_name(name):
        greet_user(name)

main()
