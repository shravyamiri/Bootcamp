# Example of applying multiple decorators
@simple_logger
@timer
@debug_info
def complex_function(x, y):
    return x + y

complex_function(3, 5)
