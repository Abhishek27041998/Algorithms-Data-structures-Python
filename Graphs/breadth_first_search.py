"""
This is an implementation of BFS
"""


class Graph:
    def __init__(self, num_nodes):
        self.adj_list = [list() for _ in range(num_nodes+1)]
        self.num_nodes = num_nodes

    def insert_edge(self, i, j):
        self.adj_list[i].append(j)
        self.adj_list[j].append(i)

    def bfs(self, source):
        queue = [source]

        visited = [0 for _ in range(self.num_nodes+1)]
        visited[source] = 1
        while len(queue) != 0:
            node = queue.pop(0)
            print(node)

            for adj_node in self.adj_list[node]:
                if visited[adj_node] != 1:
                    queue.append(adj_node)
                    visited[adj_node] = 1


if __name__ == '__main__':
    num_nodes = 4
    num_edges = 5

    graph = Graph(num_nodes)

    edges = [(1, 2), (2, 4), (3, 1), (3, 4)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1])

    print("BFS Traversal")
    graph.bfs(1)



