"""
This is an implementation of Articulation Points Algorithm using Back Edges
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = {i: [] for i in range(self.V)}
        self.time = 0

    def insert_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def articulation_bridges(self, u, visited, disc, low, parent, ab):
        children = 0
        disc[u] = self.time
        low[u] = self.time
        visited[u] = True
        self.time += 1

        for v in self.edges[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                self.articulation_bridges(v, visited, disc, low, parent, ab)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    ab.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_articulation_bridges(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        ab = []
        parent = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.articulation_bridges(i, visited, disc, low, parent, ab)

        return ab


if __name__ == '__main__':
    num_nodes = 6
    num_edges = 7

    graph = Graph(num_nodes)

    edges = [(0, 1), (0, 5), (1, 3), (1, 2), (3, 2), (3, 4), (2, 4)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1])

    print("Following are the Articulation Bridges of Graph 1")

    articulation_points = graph.find_articulation_bridges()
    print(articulation_points)

    g2 = Graph(5)
    g2.insert_edge(1, 0)
    g2.insert_edge(0, 2)
    g2.insert_edge(2, 1)
    g2.insert_edge(0, 3)
    g2.insert_edge(3, 4)

    articulation_points = g2.find_articulation_bridges()
    print('Following are the Articulation Bridges of Graph 2')
    print(articulation_points)
