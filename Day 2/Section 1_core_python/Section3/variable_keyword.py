# Variable Keyword Args:
def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with keyword arguments
show_settings(language="Python", version=3.9, os="Windows")
