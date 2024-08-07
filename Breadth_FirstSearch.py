class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Example Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("\nBreadth-First Search starting from vertex 2:")
g.bfs(2)