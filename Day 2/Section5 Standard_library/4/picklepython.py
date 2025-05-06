import pickle

data = {"language": "Python", "version": 3.11}

# Save to file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Load from file
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)

print("Loaded from pickle:", loaded)
