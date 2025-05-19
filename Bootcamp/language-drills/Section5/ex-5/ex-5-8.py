import subprocess
import time

# Long-running subprocess (e.g., ping for 10 seconds)
proc = subprocess.Popen(["ping", "localhost", "-t"], stdout=subprocess.PIPE)

time.sleep(3)
proc.terminate()
print("Subprocess terminated.")
