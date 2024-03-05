"""
This is an implementation of Dijkstra's Algorithm for Shortest path from source to every vertex
"""
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(self.V)]

    def insert_edge(self, i, j, weight):
        self.adj_list[i].append((j, weight))
        self.adj_list[j].append((i, weight))  # Add this line only for undirected graphs with weights

    def dijkstra_algorithm(self, source):
        distance = [float('inf') for _ in range(self.V)]
        distance[source] = 0

        min_priority_queue = []
        heapq.heappush(min_priority_queue, (0, source))

        while min_priority_queue:
            curr_weight, curr_node = heapq.heappop(min_priority_queue)

            for v, weight in self.adj_list[curr_node]:
                if distance[curr_node] + weight < distance[v]:
                    distance[v] = distance[curr_node] + weight
                    heapq.heappush(min_priority_queue, (distance[v], v))

        return distance


if __name__ == '__main__':
    num_nodes = 9
    num_edges = 14

    graph = Graph(num_nodes)

    edges = [(7, 6, 1), (8, 2, 2), (6, 5, 2), (0, 1, 4), (2, 5, 4), (8, 6, 6), (2, 3, 7), (7, 8, 7), (0, 7, 8), (1, 2, 8), (3, 4, 9), (5, 4, 10), (1, 7, 11), (3, 5, 14)]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1], edge[2])

    print("Shortest Path from Vertex 0 to all vertex is: ")

    distance = graph.dijkstra_algorithm(source=0)

    for i in range(len(distance)):
        print(f"Source: {0} ---> Destination {i} = {distance[i]}")


