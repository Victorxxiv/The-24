# Social Network Example
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)



class SocialNetwork(Graph):
    def find_shortest_path(self, start, goal):
        visited = set()
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in set(self.graph[vertex]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

# Example Usage
network = SocialNetwork()
network.add_edge("Alice", "Bob")
network.add_edge("Bob", "Charlie")
network.add_edge("Charlie", "David")
network.add_edge("David", "Eve")

print("\nShortest path from Alice to Eve:")
for path in network.find_shortest_path("Alice", "Eve"):
    print(path)
