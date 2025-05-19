# Mixed Args:
def mixed_args(arg1, *args, kwarg1="default", **kwargs):
    print(f"First argument: {arg1}")
    print("Additional positional arguments:", args)
    print("Keyword argument kwarg1:", kwarg1)
    print("Additional keyword arguments:", kwargs)

# Calling with both *args and **kwargs
mixed_args(1, 2, 3, 4, kwarg1="changed", extra="extra_value", another="another_value")
