import json

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_edge(self, u, v):
        self.nodes.update([u, v])
        self.edges.append((u, v))

    def to_json(self):
        return json.dumps({"nodes": list(self.nodes), "edges": self.edges})

graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
print(graph.to_json())