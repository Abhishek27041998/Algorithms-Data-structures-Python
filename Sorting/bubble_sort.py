"""
This is an implementation of bubble sort
"""


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr) - 1):
            for j in range(len(self.arr) - i - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    print(f"Array before sorting : {arr}")
    bs = BubbleSort(arr)
    bs.sort()

    print(f"Sorted array : {bs.arr}")

