"""
This is an implementation of Bellman ford Algorithm for Shortest path from source to every vertex
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def insert_edge(self, i, j, weight):
        self.edges.append((i, j, weight))
        self.edges.append((j, i, weight))  # Add this line only for undirected graphs with weights

    def bellman_ford(self, source):
        distance = [float('inf') for _ in range(self.V)]

        distance[source] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        for u, v, w in self.edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print('Graph contains negative cycle, Shortest path cannot be calculated')
                return

        return distance


if __name__ == '__main__':
    num_nodes = 9
    num_edges = 14

    graph = Graph(num_nodes)

    edges = [(7, 6, 1), (8, 2, 2), (6, 5, 2), (0, 1, 4), (2, 5, 4), (8, 6, 6), (2, 3, 7), (7, 8, 7), (0, 7, 8), (1, 2, 8), (3, 4, 9), (5, 4, 10), (1, 7, 11), (3, 5, 14)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1], edge[2])

    print("Shortest Path from Vertex 0 to all vertex is: ")

    distance = graph.bellman_ford(0)

    for i in range(len(distance)):
        print(f"Source: {0} ---> Destination {i} = {distance[i]}")


