"""
This is an implementation of Heap Sort using Binary Max Heap Tree using Array representation
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

    def heap_sort(self):

        self.build_max_heap()

        idx = self.num_of_nodes

        while idx >= 2:
            self.arr[1], self.arr[idx] = self.arr[idx], self.arr[1]
            self.num_of_nodes -= 1

            self.max_heapify(1)

            idx -= 1

        return self.arr


if __name__ == '__main__':
    # Example 1
    sample_array = [None, 1, 4, 3, 7, 8, 9, 10]
    print(f'Sample Array: {sample_array}')

    max_heap_obj = MaxHeapTree(sample_array)
    heap_sorted_arr = max_heap_obj.heap_sort()

    print(f'Heap Sorted Array: {heap_sorted_arr}')

    # Example 2
    sample_array = [None, 10, 8, 9, 7, 6, 5, 4]
    print(f'Sample Array: {sample_array}')

    max_heap_obj = MaxHeapTree(sample_array)
    heap_sorted_arr = max_heap_obj.heap_sort()

    print(f'Heap Sorted Array: {heap_sorted_arr}')




