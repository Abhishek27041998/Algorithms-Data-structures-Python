"""
The following problem is taken from Hacker earth practice problems set.
Refer the link for the question: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/
"""

"""
Partially Accepted Solution
"""


"""
This is an implementation of merge sort
"""


class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.ordered_pairs = 0

    def merge(self, start, mid, end):
        p = start
        q = mid + 1

        temp_sorted_array = []
        for i in range(start, end+1, 1):
            if p > mid:  # Checks if first sub part comes to an end
                temp_sorted_array.append(self.arr[q])
                q += 1
            elif q > end:  # Checks if second sub part comes to an end
                temp_sorted_array.append(self.arr[p])
                p += 1
            elif self.arr[p] < self.arr[q]:
                temp_sorted_array.append(self.arr[p])
                p += 1
            else:
                temp_sorted_array.append(self.arr[q])
                q += 1
                self.ordered_pairs += mid - p + 1

        return self.ordered_pairs

    def merge_sort(self, start, end):
        if start < end:
            mid = (start + end) // 2

            self.merge_sort(start, mid)
            self.merge_sort(mid+1, end)

            # Merge both sorted sub-parts
            return self.merge(start, mid, end)

    def sort(self):
        return self.merge_sort(0, len(self.arr) - 1)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    merge_sort = MergeSort(arr)
    ordered_pairs = merge_sort.sort()

    print(ordered_pairs)
