import subprocess

# Run echo command through the shell
result = subprocess.run('echo Hello, world!', capture_output=True, text=True, shell=True)
print("Captured Output:", result.stdout)
