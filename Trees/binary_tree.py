"""
This is an implementation of Binary Tree
"""


# This is a node of a tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self, data=-9999):
        self.root = None

        if data != -9999:
            node = Node(data)
            self.root = node

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

    # This method adds node in sequential manner from Left to Right of each parent
    # i.e Level Order Traversal manner
    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        # Need to maintain a queue for level order traversal
        queue = [self.root]

        while len(queue) != 0:
            temp_root = queue[0]
            queue.pop(0)

            # Add data to left child if empty or add to queue if not
            if temp_root.left_child is not None:
                queue.append(temp_root.left_child)
            else:
                temp_root.left_child = Node(data)
                return

            # Similarly for right child
            if temp_root.right_child is not None:
                queue.append(temp_root.right_child)
            else:
                temp_root.right_child = Node(data)
                return

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

    def level_order_traversal(self, node):
        if node is None:
            return

        queue = [node]

        while len(queue) != 0:
            parent = queue.pop(0)
            print(parent.data)

            if parent.left_child is not None:
                queue.append(parent.left_child)

            if parent.right_child is not None:
                queue.append(parent.right_child)

if __name__ == '__main__':
    tree = Tree()

    # Add nodes to the trees and print traversals
    tree.add_node(1)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(4)
    tree.add_node(5)
    tree.add_node(6)
    tree.add_node(7)
    tree.add_node(8)
    tree.add_node(9)

    # Traversals
    print('##### Inorder Traversal #####')
    tree.inorder_traversal(tree.root)

    print('##### Preorder Traversal #####')
    tree.preorder_traversal(tree.root)

    print('##### Post Order Traversal #####')
    tree.postorder_traversal(tree.root)

    print('##### Level Order Traversal #####')
    tree.level_order_traversal(tree.root)

    print('##### Max Depth of the Tree #####')
    print(tree.max_depth(tree.root))


