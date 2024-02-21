"""
This is an implementation of Binary Search Tree
"""


# This is a node of a tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self, data=-9999):
        self.root = None

        if data != -9999:
            node = Node(data)
            self.root = node

    def insert_node(self, root, data):
        if root is None:
            return Node(data)

        if data <= root.data:
            root.left_child = self.insert_node(root.left_child, data)
        else:
            root.right_child = self.insert_node(root.right_child, data)

        return root

    def inorder_traversal(self, node):
        if node is None:
            return

        self.inorder_traversal(node.left_child)
        print(f"{node.data}")
        self.inorder_traversal(node.right_child)

    def preorder_traversal(self, node):
        if node is None:
            return

        print(f"{node.data}")
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)

    def postorder_traversal(self, node):
        if node is None:
            return

        self.postorder_traversal(node.left_child)
        self.postorder_traversal(node.right_child)
        print(f"{node.data}")


if __name__ == '__main__':
    tree = BinarySearchTree()

    # Add nodes to the trees and print traversals
    tree.root = tree.insert_node(tree.root, 6)
    tree.root = tree.insert_node(tree.root, 5)
    tree.root = tree.insert_node(tree.root, 4)
    tree.root = tree.insert_node(tree.root, 3)
    tree.root = tree.insert_node(tree.root, 2)
    tree.root = tree.insert_node(tree.root, 1)
    tree.root = tree.insert_node(tree.root, 7)
    tree.root = tree.insert_node(tree.root, 8)
    tree.root = tree.insert_node(tree.root, 9)

    # Traversals
    print('##### Inorder Traversal : Gives sorted list #####')
    tree.inorder_traversal(tree.root)

    print('##### Preorder Traversal #####')
    tree.preorder_traversal(tree.root)

    print('##### Post Order Traversal #####')
    tree.postorder_traversal(tree.root)

