import time

def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(1)
            print("Max retry attempts reached.")
        return wrapper
    return decorator

# Example usage:
@retry(max_attempts=5)
def test_function():
    if time.time() % 2 < 1:
        raise ValueError("Random error")
    return "Success!"

print(test_function())
