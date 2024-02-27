"""
This is an implementation of selection sort
"""


class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            minimum = i

            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[minimum]:
                    minimum = j

            self.arr[i], self.arr[minimum] = self.arr[minimum], self.arr[i]


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    print(f"Array before sorting : {arr}")
    ss = SelectionSort(arr)
    ss.sort()

    print(f"Sorted array : {ss.arr}")

