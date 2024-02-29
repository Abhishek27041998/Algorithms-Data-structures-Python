"""
This is an implementation of DFS
"""


class Graph:
    def __init__(self, num_nodes):
        self.adj_list = [list() for _ in range(num_nodes+1)]
        self.num_nodes = num_nodes
        self.visited = [0 for _ in range(self.num_nodes+1)]

    def insert_edge(self, i, j):
        self.adj_list[i].append(j)
        self.adj_list[j].append(i)

    def dfs(self, source):
        print(source)
        self.visited[source] = 1

        for adj_node in self.adj_list[source]:
            if self.visited[adj_node] != 1:
                self.dfs(adj_node)


if __name__ == '__main__':
    num_nodes = 4
    num_edges = 5

    graph = Graph(num_nodes)

    edges = [(1, 2), (2, 4), (3, 1), (3, 4)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1])

    print("DFS Traversal")
    graph.dfs(1)



