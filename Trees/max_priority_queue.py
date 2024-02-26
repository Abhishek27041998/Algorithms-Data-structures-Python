"""
This is an implementation of Max Priority Queue using Binary Max Heap Tree using Array representation
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

    # Insert elements
    print('Inserting 10, 8, 20, 5 to queue')
    max_priority_queue.insert_value(10)
    max_priority_queue.insert_value(8)
    max_priority_queue.insert_value(20)
    max_priority_queue.insert_value(5)

    # print elements
    print('\nMax Priority Queue post insertion')
    print(max_priority_queue.arr)

    print('\nExtracting Maximum')
    print(max_priority_queue.extract_maximum())

    print('Max Priority Queue post extracting maximum')
    print(max_priority_queue.arr)

    # Insert elements
    print('\nInserting 25, 1, 2, 80 to queue')
    max_priority_queue.insert_value(25)
    max_priority_queue.insert_value(1)
    max_priority_queue.insert_value(2)
    max_priority_queue.insert_value(80)

    # print elements
    print('\nMax Priority Queue post insertion')
    print(max_priority_queue.arr)

    print('\nExtracting Maximum')
    print(max_priority_queue.extract_maximum())
    print('Max Priority Queue post extracting maximum')
    print(max_priority_queue.arr)

    print('\nExtracting Maximum')
    print(max_priority_queue.extract_maximum())
    print('Max Priority Queue post extracting maximum')
    print(max_priority_queue.arr)

    print('\nExtracting Maximum')
    print(max_priority_queue.extract_maximum())
    print('Max Priority Queue post extracting maximum')
    print(max_priority_queue.arr)

