import traceback

try:
    1 / 0
except Exception:
    print(traceback.format_exc())
