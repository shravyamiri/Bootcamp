import pickle

class MyCollection:
    def __init__(self, items):
        self.items = items

    def save(self, filename="collection.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename="collection.pkl"):
        with open(filename, "rb") as f:
            return pickle.load(f)

collection = MyCollection([1, 2, 3])
collection.save()
loaded = MyCollection.load()
print(loaded.items)