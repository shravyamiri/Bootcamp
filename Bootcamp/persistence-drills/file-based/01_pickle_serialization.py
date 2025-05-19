import pickle

class Person:
    def __init__(self, name, institutions, colleagues):
        self.name = name
        self.institutions = institutions
        self.colleagues = colleagues

person = Person("Alice", ["MIT", "Harvard"], ["Bob", "Charlie"])

with open("person.pkl", "wb") as f:
    pickle.dump(person, f)