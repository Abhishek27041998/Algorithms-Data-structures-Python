"""
This is an implementation of Binary Max Heap Tree using Array representation
"""


class MaxHeapTree:
    def __init__(self, arr):
        self.arr = arr
        self.num_of_nodes = len(arr) - 1

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

    def build_max_heap(self):
        idx = self.num_of_nodes // 2

        while idx >= 1:
            self.max_heapify(idx)
            idx = idx - 1

        return self.arr


if __name__ == '__main__':
    sample_array = [None, 1, 4, 3, 7, 8, 9, 10]
    print(f'Sample Array before building Heap Tree: {sample_array}')

    max_heap_obj = MaxHeapTree(sample_array)
    max_heap_arr = max_heap_obj.build_max_heap()

    print(f'Max Heap Tree Array: {max_heap_arr}')




