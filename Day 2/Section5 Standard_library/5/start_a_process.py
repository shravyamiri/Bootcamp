from multiprocessing import Process

def compute():
    print("Running in another process")

if __name__ == '__main__':  # This guards the entry point
    p = Process(target=compute)
    p.start()
    p.join()
