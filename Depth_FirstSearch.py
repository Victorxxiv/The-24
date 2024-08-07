class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


# Example Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Search starting from vertex 2:")
g.dfs(2)