"""
This is an implementation of Floyd Warshall's Algorithm for Shortest path from every to every other vertex
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]

    def insert_edge(self, i, j, weight):
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight  # Add this line only for undirected graphs with weights

    def floyd_warshall(self):
        distance_matrix = [[float('inf')] * self.V for _ in range(self.V)]

        for i in range(self.V):
            distance_matrix[i][i] = 0

        for i in range(self.V):
            for j in range(self.V):
                if self.matrix[i][j] != 0:
                    distance_matrix[i][j] = self.matrix[i][j]

        # Floyd-Warshall algorithm
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
                        distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

        return distance_matrix


if __name__ == '__main__':
    num_nodes = 9
    num_edges = 14

    graph = Graph(num_nodes)

    edges = [(7, 6, 1), (8, 2, 2), (6, 5, 2), (0, 1, 4), (2, 5, 4), (8, 6, 6), (2, 3, 7), (7, 8, 7), (0, 7, 8), (1, 2, 8), (3, 4, 9), (5, 4, 10), (1, 7, 11), (3, 5, 14)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1], edge[2])

    print("Distance Matrix post Floyd Warshall Algorithm")

    distance = graph.floyd_warshall()

    print(distance)
