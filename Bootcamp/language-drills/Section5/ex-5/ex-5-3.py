import subprocess

result = subprocess.run(["python", "--version"])
print("Exit Code:", result.returncode)
