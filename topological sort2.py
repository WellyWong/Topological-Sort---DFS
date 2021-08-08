"""
https://www.youtube.com/watch?v=AfSk24UTFS8     Erik Demaine
job scheduling:
Given DAG (Directed Acyclic Graph), sort/order Vertices so that all edges point from lower order to higher order
Topological sort:
-Run DFS
-Output reverse of finishing times of Vertices
"""
class Graph:
    def __init__(self, vertices):
        self._graph = {vertex: [] for vertex in vertices}
        self._visited = {vertex: False for vertex in vertices}
        self.n = len(vertices)

    def add_edge(self, u, v, bidirectional=False):
        self._graph[u].append(v)
        if bidirectional:
            self._graph[v].append(u)

    def __repr__(self):
        return str(self._graph)

    def top_sort(self):
        stack = []
        for u in self._graph:
            if self._visited[u] == False:
                self.top_sort_visit(u, stack)
        return stack[::-1]

    def top_sort_visit(self, u, stack):
        self._visited[u] = True
        for v in self._graph[u]:
            if self._visited[v] == False:
                self.top_sort_visit(v, stack)

        stack.append(u)

V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
g1 = Graph(V)
g1.add_edge('A', 'B')
g1.add_edge('A', 'H')
g1.add_edge('G', 'H')
g1.add_edge('B', 'C')
g1.add_edge('D', 'B')
g1.add_edge('D', 'E')
g1.add_edge('E', 'F')
g1.add_edge('C', 'F')
"""
G-->H           I
   ^
  /
A-->B-->C-->F 
   ^       ^
  /       /
  D ---> E
"""
path = g1.top_sort()
print(path)
