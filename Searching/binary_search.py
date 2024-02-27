"""
This is an implementation of binary search
"""


class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, search):
        return self.binary_search(0, len(self.arr) - 1, search)

    def binary_search(self, low, high, key):
        while low <= high:
            mid = (low + high) // 2

            if key > self.arr[mid]:
                low = mid + 1
            elif key < self.arr[mid]:
                high = mid - 1
            else:
                return mid

        return -1


if __name__ == '__main__':
    arr = list(range(1000))
    search = 55

    bs = BinarySearch(arr)
    print(f"Element found at Index : {bs.search(search)}. If -1 then not found")

    search = 1001  # not present
    print(f"Element found at Index : {bs.search(search)}. If -1 then not found")


