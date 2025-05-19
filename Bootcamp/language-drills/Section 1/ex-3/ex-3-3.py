# Keyword-Only Args: 
def kw_only_args(a, b, *, c):
    print(f"a: {a}, b: {b}, c: {c}")

# Correct: 'c' passed as a keyword argument
kw_only_args(1, 2, c=3)

# Incorrect: This will raise a TypeError because 'c' is keyword-only
# kw_only_args(1, 2, 3)
