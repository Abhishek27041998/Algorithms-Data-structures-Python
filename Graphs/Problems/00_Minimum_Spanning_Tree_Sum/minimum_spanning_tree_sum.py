"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
"""

"""
Accepted Solution
"""

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
    num_nodes, num_edges = map(int, input().split())

    graph = Graph(num_nodes)

    for _ in range(num_edges):
        u, v, w = map(int, input().split())

        graph.insert_edge(u-1, v-1, w)

    mst = graph.prims_mst(0)

    print(f"{sum(edge[2] for edge in mst)}")

