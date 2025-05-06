import tempfile

with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmpfile:
    tmpfile.write("Temporary data")
    tmpfile.seek(0)
    print(tmpfile.read())
