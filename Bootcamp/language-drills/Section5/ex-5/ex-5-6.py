import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]

print("Counter:", counter)
