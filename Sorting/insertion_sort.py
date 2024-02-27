"""
This is an implementation of insertion sort
"""


class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            temp = self.arr[i]
            j = i

            while j > 0 and temp < self.arr[j-1]:
                self.arr[j] = self.arr[j-1]
                j -= 1

            self.arr[j] = temp


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    print(f"Array before sorting : {arr}")

    ins_sort = InsertionSort(arr)
    ins_sort.sort()

    print(f"Sorted array : {ins_sort.arr}")

