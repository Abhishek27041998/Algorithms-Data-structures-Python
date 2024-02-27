"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/
"""

"""
Accepted Solution
"""

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
    n = int(input())

    arr = list(map(int, input().split()))

    temp_arr = arr.copy()

    ins_sort = InsertionSort(arr)
    ins_sort.sort()

    for element in temp_arr:
        print(ins_sort.arr.index(element)+1, sep=' ', end=' ')



