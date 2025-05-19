functions = [abs, str, hex]

# Applying each function to -42
results = [func(-42) for func in functions]
print(results)  # Output: [42, '-42', '-0x2a']
