import os

# Check if the input file exists in the current working directory
input_file = "input.txt"
output_file = "output.txt"

# Attempt to open and process the files
try:
    # Check if input.txt exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' does not exist in the current directory!")

    # Open both input.txt and output.txt
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        data = infile.read()  # Read content from input.txt
        outfile.write(data.upper())  # Write the uppercase version to output.txt

    print(f"Content from '{input_file}' has been written to '{output_file}' in uppercase.")

except FileNotFoundError as e:
    print(e)  # Print the error message if the input file is not found
except Exception as e:
    print(f"An unexpected error occurred: {e}")
