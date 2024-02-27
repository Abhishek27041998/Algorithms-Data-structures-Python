"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/tutorial/
"""

"""
Accepted Solution
"""

"""
This is an implementation of bubble sort
"""


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        swaps = 0
        for i in range(len(self.arr) - 1):
            for j in range(len(self.arr) - i - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swaps += 1

        return swaps


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    bs = BubbleSort(arr)

    print(bs.sort())
