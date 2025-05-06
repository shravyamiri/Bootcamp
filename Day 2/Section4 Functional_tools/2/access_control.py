def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                print(f"Access Denied. Required role: {role}")
                return
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

# Example usage:
@role_required("admin")
def access_admin_panel(user_role):
    print("Accessing admin panel")

access_admin_panel("admin")
access_admin_panel("user")
