"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/tutorial/
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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, root, data):
        if root is None:
            return Node(data)

        if data <= root.data:
            root.left_child = self.insert_node(root.left_child, data)
        else:
            root.right_child = self.insert_node(root.right_child, data)

        return root

    def level_order_search(self, elem):
        if self.root is None:
            return

        # Need to maintain a queue for level order traversal
        queue = [self.root]

        while len(queue) != 0:
            temp_root = queue[0]
            queue.pop(0)

            if temp_root.data == elem:
                return temp_root

            # Add left child to queue if data exists
            if temp_root.left_child is not None:
                queue.append(temp_root.left_child)

            # Similarly for right child
            if temp_root.right_child is not None:
                queue.append(temp_root.right_child)

    def preorder_traversal(self, node):
        if node is None:
            return

        print(f"{node.data}", sep=' ')
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)


if __name__ == '__main__':
    tree = BinarySearchTree()

    no_of_elements = int(input())

    elements = map(int, input().split())

    for element in elements:
        tree.root = tree.insert_node(tree.root, element)

    # Subtree node to search
    subtree_node_element = int(input())

    # Use level order traversal to find the node
    subtree_node = tree.level_order_search(subtree_node_element)

    # Once you retrieve node, run pre-order traversal
    tree.preorder_traversal(subtree_node)
