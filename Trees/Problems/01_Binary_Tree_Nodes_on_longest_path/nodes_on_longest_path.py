"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/tutorial/
"""

"""
Accepted Solution
"""


# This is a node of a tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def max_depth(self, node):
        if node is None:
            return 0
        else:
            left_subtree_depth = self.max_depth(node.left_child)
            right_subtree_depth = self.max_depth(node.right_child)

            if left_subtree_depth > right_subtree_depth:
                return left_subtree_depth + 1
            else:
                return right_subtree_depth + 1

    def add_node(self, data, path):
        # Starting node
        node = self.root

        # Modify node until last character in the path
        for i in range(len(path) - 1):
            if path[i] == 'L':
                node = node.left_child
            else:
                node = node.right_child

        # Use last character of the path to add node
        if path[-1] == 'L':
            node.left_child = Node(data)
        else:
            node.right_child = Node(data)

    def longest_path(self, root):
        if root is None:
            return 0

        longest_path_root = self.max_depth(root.left_child) + self.max_depth(root.right_child) + 1

        longest_path_lc = self.longest_path(root.left_child)

        longest_path_rc = self.longest_path(root.right_child)

        return max(longest_path_root, longest_path_lc, longest_path_rc)


if __name__ == '__main__':
    num_of_nodes, root = map(int, input().split())

    tree = Tree(root)

    inputs_list = []

    for i in range(num_of_nodes - 1):
        path = str(input())
        element = int(input())

        inputs_list.append((path, element))

    sorted_list = sorted(inputs_list, key=lambda x: (len(x[0]), x[0]))

    for item in sorted_list:
        path = item[0]
        element = item[1]

        tree.add_node(element, path)

    longest_path_nodes = tree.longest_path(tree.root)

    print(longest_path_nodes)
