"""
This is an implementation of Kruskals Algorithm for Minimum spanning tree
"""


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = []
        self.parent = [i for i in range(num_nodes)]
        self.mst = []

    def insert_edge(self, i, j, weight):
        self.edges.append((i, j, weight))

    def find_set(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_set(self.parent[i])

        return self.parent[i]

    def union_sets(self, u, v):
        root_u = self.find_set(u)
        root_v = self.find_set(v)
        self.parent[root_u] = root_v

    def kruskal(self):
        self.edges = sorted(self.edges, key=lambda edge: edge[2])  # Sort by Weight

        for edge in self.edges:
            u, v, w = edge

            if self.find_set(u) != self.find_set(v):
                self.mst.append((u, v, w))
                self.union_sets(u, v)

        return self.mst


if __name__ == '__main__':
    num_nodes = 9
    num_edges = 14

    graph = Graph(num_nodes)

    edges = [(7, 6, 1), (8, 2, 2), (6, 5, 2), (0, 1, 4), (2, 5, 4), (8, 6, 6), (2, 3, 7), (7, 8, 7), (0, 7, 8), (1, 2, 8), (3, 4, 9), (5, 4, 10), (1, 7, 11), (3, 5, 14)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1], edge[2])

    print("Kruskal Algorithm running... Edges in MST are:")

    mst = graph.kruskal()

    for edge in mst:
        print(f"{edge[0]} ---- {edge[1]} = {edge[2]}")

    print(f"Total cost = {sum(edge[2] for edge in mst)}")


