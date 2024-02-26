"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/
"""

"""
Accepted Solution
"""


class MaxPriorityQueue:
    def __init__(self):
        self.arr = []
        self.arr.append(None)
        self.num_of_nodes = len(self.arr) - 1

    def max_heapify(self, idx):
        left_child = 2 * idx
        right_child = 2 * idx + 1
        largest = idx

        if left_child <= self.num_of_nodes and self.arr[left_child] > self.arr[largest]:
            largest = left_child

        if right_child <= self.num_of_nodes and self.arr[right_child] > self.arr[largest]:
            largest = right_child

        if largest != idx:
            self.arr[idx], self.arr[largest] = self.arr[largest], self.arr[idx]
            self.max_heapify(largest)

    def max_element(self):
        return self.arr[1]

    def extract_maximum(self):
        if len(self.arr) == 0:
            print('Cant remove element as queue is empty')
            return -1

        max_element = self.arr[1]
        self.arr[1] = self.arr[self.num_of_nodes]
        self.arr.pop()
        self.num_of_nodes -= 1

        self.max_heapify(1)

        return max_element

    def increase_value(self, idx, val):
        if val < self.arr[idx]:
            print("New value is less than current value, can't be increased")

        self.arr[idx] = val

        while idx > 1 and self.arr[idx // 2] < self.arr[idx]:
            self.arr[idx//2], self.arr[idx] = self.arr[idx], self.arr[idx//2]

            idx = idx // 2

    def insert_value(self, val):
        self.num_of_nodes += 1

        self.arr.append(-1)  # Assuming all elements are greater than 0

        self.increase_value(self.num_of_nodes, val)


if __name__ == '__main__':
    max_priority_queue = MaxPriorityQueue()

    n = int(input())
    initial_elements = map(int, input().split())

    for elem in initial_elements:
        max_priority_queue.insert_value(elem)

    q = int(input())

    while q != 0:
        inp_query = str(input())

        if inp_query[0] == '1':
            val = int(inp_query.split(' ')[1])
            max_priority_queue.insert_value(val)
        else:
            print(max_priority_queue.extract_maximum())

        q = q - 1

