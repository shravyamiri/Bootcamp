import tempfile

# Using tempfile.TemporaryFile() inside a 'with' block
with tempfile.TemporaryFile(mode='w+t') as temp_file:
    # Writing some data to the temporary file
    temp_file.write("Hello, this is some temporary data!\n")
    temp_file.write("This data will be discarded after the block.")

    # Move the cursor to the beginning of the file to read the data
    temp_file.seek(0)

    # Reading the data from the temporary file
    content = temp_file.read()
    print("Content of the temporary file:")
    print(content)

# After the 'with' block, the temporary file is automatically closed and deleted
print("The temporary file has been automatically deleted after the 'with' block.")
