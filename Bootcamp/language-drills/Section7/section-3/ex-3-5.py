import warnings

def old_function():
    warnings.warn("old_function() is deprecated", DeprecationWarning)

old_function()
