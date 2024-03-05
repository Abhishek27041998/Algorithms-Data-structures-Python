"""
This is an implementation of Prims Algorithm for Minimum spanning tree
"""
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = {i: [] for i in range(self.V)}

    def insert_edge(self, u, v, weight):
        self.edges[u].append((weight, v))
        self.edges[v].append((weight, u))

    def prims_mst(self, starting_vector):
        min_heap = []
        visited = set()
        mst_edges = []

        visited.add(starting_vector)

        for edge in self.edges[starting_vector]:
            heapq.heappush(min_heap, (edge[0], starting_vector, edge[1]))

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            if v not in visited:
                mst_edges.append((u, v, weight))
                visited.add(v)

                for edge in self.edges[v]:
                    heapq.heappush(min_heap, (edge[0], v, edge[1]))

        return mst_edges


if __name__ == '__main__':
    num_nodes = 9
    num_edges = 14

    graph = Graph(num_nodes)

    edges = [(7, 6, 1), (8, 2, 2), (6, 5, 2), (0, 1, 4), (2, 5, 4), (8, 6, 6), (2, 3, 7), (7, 8, 7), (0, 7, 8), (1, 2, 8), (3, 4, 9), (5, 4, 10), (1, 7, 11), (3, 5, 14)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1], edge[2])

    print("Prims Algorithm: Edges in Minimum spanning tree are")

    mst = graph.prims_mst(0)

    for edge in mst:
        print(f"{edge[0]} ---- {edge[1]} = {edge[2]}")

    print(f"Total cost = {sum(edge[2] for edge in mst)}")

