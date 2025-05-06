def scope_error():
    try:
        print(x)  # Trying to access before assignment
        x = 10    # Local variable assignment
    except UnboundLocalError as e:
        print("Scope error:", e)

scope_error()
