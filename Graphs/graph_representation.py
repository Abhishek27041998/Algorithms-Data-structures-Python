"""
This is an implementation of Graph representation using the Adjacency matrix and adjacency lists
"""


class AdjacencyMatrix:
    def __init__(self, num_nodes):
        self.matrix = [[0 for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]

    def insert_edge(self, i, j, weight=1):
        self.matrix[i][j] = weight


class AdjacencyList:
    def __init__(self, num_nodes):
        self.adj_list = [list() for _ in range(num_nodes+1)]

    def insert_edge(self, i, j, weight=1):
        edge_weight = (j, weight)

        self.adj_list[i].append(edge_weight)


if __name__ == '__main__':
    num_nodes = 4
    num_edges = 5

    adj_matrix = AdjacencyMatrix(num_nodes)

    edges = [(1, 2), (2, 4), (3, 1), (3, 4), (4, 2)]

    for edge in edges:
        adj_matrix.insert_edge(edge[0], edge[1])

    print('Adjacency Matrix')
    print(adj_matrix.matrix)

    adj_list = AdjacencyList(num_nodes)

    edges = [(1, 2), (2, 4), (3, 1), (3, 4), (4, 2)]

    for edge in edges:
        adj_list.insert_edge(edge[0], edge[1])

    print('Adjacency List')
    print(adj_list.adj_list)

