import threading

def greet():
    print("Hello from thread!")

thread = threading.Thread(target=greet)
thread.start()
thread.join()
