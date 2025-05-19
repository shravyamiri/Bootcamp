import pickle

with open("person.pkl", "rb") as f:
    person = pickle.load(f)
    print(person.__dict__)