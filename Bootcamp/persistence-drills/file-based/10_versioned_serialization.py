import pickle

class PersonV1:
    def __init__(self, name):
        self.name = name

class PersonV2:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

with open("person_v1.pkl", "wb") as f:
    pickle.dump(PersonV1("Alice"), f)

with open("person_v1.pkl", "rb") as f:
    old_data = pickle.load(f)
    person_v2 = PersonV2(old_data.name)
    print(person_v2.__dict__)