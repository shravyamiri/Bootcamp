import platform

def health_check():
    return {
        "status": "OK",
        "system": platform.system(),
        "release": platform.release()
    }

print(health_check())
