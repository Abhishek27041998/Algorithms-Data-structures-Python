"""
This is an implementation of Binary Max Heap Tree using Array representation
"""


class MinHeapTree:
    def __init__(self, arr):
        self.arr = arr
        self.num_of_nodes = len(arr) - 1

    def min_heapify(self, idx):
        left_child = 2 * idx
        right_child = 2 * idx + 1
        smallest = idx

        if left_child <= self.num_of_nodes and self.arr[left_child] < self.arr[smallest]:
            smallest = left_child

        if right_child <= self.num_of_nodes and self.arr[right_child] < self.arr[smallest]:
            smallest = right_child

        if smallest != idx:
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self.min_heapify(smallest)

    def build_min_heap(self):
        idx = self.num_of_nodes // 2

        while idx >= 1:
            self.min_heapify(idx)
            idx = idx - 1

        return self.arr


if __name__ == '__main__':
    sample_array = [None, 10, 8, 9, 7, 6, 5, 4]
    print(f'Sample Array before building Heap Tree: {sample_array}')

    min_heap_obj = MinHeapTree(sample_array)
    min_heap_arr = min_heap_obj.build_min_heap()

    print(f'Min Heap Tree Array: {min_heap_arr}')




