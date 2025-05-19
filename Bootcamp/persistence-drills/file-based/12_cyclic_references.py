import pickle

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node("A")
b = Node("B")
a.next = b
b.next = a

with open("cyclic.pkl", "wb") as f:
    pickle.dump(a, f)

with open("cyclic.pkl", "rb") as f:
    node = pickle.load(f)
    print(node.value, node.next.value, node.next.next.value)