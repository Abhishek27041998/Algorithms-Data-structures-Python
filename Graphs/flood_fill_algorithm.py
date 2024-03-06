"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/algorithms/graphs/flood-fill-algorithm/tutorial/
"""

"""
Accepted Solution
"""

"""
This is an implementation of Flood Fill Algorithm
"""


class Maze:
    def __init__(self, n, m):
        self.N = n
        self.M = m

        self.maze = []
        self.visited = [[False] * self.M for _ in range(self.N)]

    def insert_maze_row(self, row):
        self.maze.append(row)

    def dfs(self, src_x, src_y, dest_x, dest_y):
        if src_x == dest_x and src_y == dest_y:
            return True

        if src_x >= self.N or src_y >= self.M:
            return False

        if src_x < 0 or src_y < 0:
            return False

        if self.visited[src_x][src_y]:
            return False

        if self.maze[src_x][src_y] == 0:
            return False

        self.visited[src_x][src_y] = True

        if self.dfs(src_x, src_y-1, dest_x, dest_y):
            return True

        if self.dfs(src_x-1, src_y, dest_x, dest_y):
            return True

        if self.dfs(src_x, src_y+1, dest_x, dest_y):
            return True

        if self.dfs(src_x+1, src_y, dest_x, dest_y):
            return True

        return False


if __name__ == '__main__':
    n, m = 3, 3

    maze = Maze(n, m)

    for row in [[1, 0, 1], [1, 0, 0], [1, 1, 1]]:
        maze.insert_maze_row(row)

    src_x = 1
    src_y = 1
    dest_x = n
    dest_y = m

    if maze.dfs(src_x-1, src_y-1, dest_x-1, dest_y-1):
        print('Yes')
    else:
        print('No')
