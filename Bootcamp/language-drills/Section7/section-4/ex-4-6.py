metrics = {
    "requests": 0,
    "errors": 0,
    "total_time": 0.0
}

def handle_request():
    import time
    start = time.time()
    metrics["requests"] += 1
    try:
        # simulate processing
        time.sleep(0.2)
    except Exception:
        metrics["errors"] += 1
    finally:
        metrics["total_time"] += time.time() - start

handle_request()
print(metrics)
