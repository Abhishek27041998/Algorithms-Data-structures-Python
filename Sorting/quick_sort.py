"""
This is an implementation of quick sort
"""


class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, start, end):
        i = start + 1
        piv = self.arr[start]

        for j in range(start+1, end+1, 1):
            if self.arr[j] < piv:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1

        self.arr[start], self.arr[i-1] = self.arr[i-1], self.arr[start]

        return i-1

    def quick_sort(self, start, end):
        if start < end:
            piv_pos = self.randomized_partition(start, end)

            self.quick_sort(start, piv_pos - 1)
            self.quick_sort(piv_pos + 1, end)

    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)

    def randomized_partition(self, start, end):
        import random
        random = start + random.randint(0, end-start)

        self.arr[start], self.arr[random] = self.arr[random], self.arr[start]

        return self.partition(start, end)


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    print(f"Array before sorting : {arr}")

    quick_sort = QuickSort(arr)
    quick_sort.sort()

    print(f"Sorted array : {quick_sort.arr}", end=' ')

