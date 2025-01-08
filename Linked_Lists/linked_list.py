"""
This is an implementation of Linked List
"""


# This is the class representing nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# This implements linked list functionalities
class LinkedList:
    def __init__(self, first_elem=-9999):
        self.header = None

        if first_elem != -9999:
            self.header = Node(first_elem)

    def add_node(self, data):
        node = Node(data)

        if self.header is None:
            self.header = node
        else:
            temp = self.header

            while temp.next is not None:
                temp = temp.next

            temp.next = node

    def add_node_at_beginning(self, data):
        node = Node(data)

        node.next = self.header
        self.header = node

    def add_node_at_index(self, data, index):
        node = Node(data)

        if self.header is None:
            self.header = node
        elif index == 0:
            node.next = self.header
            self.header = node
        elif index > self.length() - 1:
            self.add_node(data)
        else:
            position = 0
            prev = None
            curr = self.header

            while position != index:
                prev = curr
                curr = curr.next
                position += 1

            prev.next = node
            node.next = curr

    def traverse_list(self):
        start = self.header

        while start is not None:
            print(start.data)
            start = start.next

    def delete_last_element(self):
        if self.header is None:
            print('Linked list is empty')
        elif self.header.next is None:
            print('Linked List has 1 item and deleted')
            self.header = None
        else:
            start = self.header

            while start.next.next is not None:
                start = start.next

            start.next = None

    def length(self):
        if self.header is None:
            return 0

        length = 0
        start = self.header

        while start is not None:
            length += 1
            start = start.next

        return length

    def delete_first_elem(self):
        if self.header is None:
            print('Linked List is empty')
        else:
            self.header = self.header.next

    def delete_at_index(self, index):
        if self.header is None:
            print('Linked List is empty')
        elif index == 0:
            self.delete_first_elem()
        elif index > self.length() - 1:
            print('Index more than length of Linked list, deleting last element')
            self.delete_last_element()
        else:
            position = 0
            prev = None
            curr = self.header

            while position != index:
                position += 1
                prev = curr
                curr = curr.next

            prev.next = curr.next


if __name__ == '__main__':
    linked_list = LinkedList()

    # Add 3 items to linked list
    linked_list.add_node(1)
    linked_list.add_node(3)
    linked_list.add_node(10)
    linked_list.add_node(-10)
    linked_list.add_node(9)

    # Length of Linked list
    print('###################')
    print(f'Length : {linked_list.length()}')

    # Traverse elements of Linked list
    print('###################')
    linked_list.traverse_list()

    # Delete last element and traver
    print('######## Deleting last element ###########')
    linked_list.delete_last_element()
    linked_list.traverse_list()
    print(f'Length : {linked_list.length()}')

    print('######## Deleting last element ###########')
    linked_list.delete_last_element()
    linked_list.traverse_list()
    print(f'Length : {linked_list.length()}')

    print('######## Deleting last element ###########')
    linked_list.delete_last_element()
    linked_list.traverse_list()
    print(f'Length : {linked_list.length()}')

    # Adding elements again
    linked_list.add_node(100)
    linked_list.add_node(200)
    linked_list.add_node(300)
    linked_list.add_node(400)
    linked_list.add_node(500)
    linked_list.add_node(600)
    linked_list.add_node(700)

    # Traversing
    print("######## Adding new nodes ###########")
    linked_list.traverse_list()

    # Deleting specific index
    print("Deleting first index")
    linked_list.delete_at_index(0)
    linked_list.traverse_list()

    print("Deleting Last index")
    linked_list.delete_at_index(15)
    linked_list.traverse_list()

    print("Deleting Index=3")
    linked_list.delete_at_index(3)
    linked_list.traverse_list()

    print("Deleting Index=2")
    linked_list.delete_at_index(2)
    linked_list.traverse_list()

    # Adding at specific index
    print("Adding first index")
    linked_list.add_node_at_index(105,0)
    linked_list.traverse_list()

    print("Adding Last index")
    linked_list.add_node_at_index(205,15)
    linked_list.traverse_list()

    print("Adding Index=3")
    linked_list.add_node_at_index(305, 3)
    linked_list.traverse_list()

    print("Adding node in the beginning")
    linked_list.add_node_at_beginning(1)
    linked_list.traverse_list()
