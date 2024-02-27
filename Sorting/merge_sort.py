"""
This is an implementation of merge sort
"""


class MergeSort:
    def __init__(self, arr):
        self.arr = arr

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

        # Once you have sorted the sub parts and merged into temporary array, merge with real one
        for i in range(len(temp_sorted_array)):
            self.arr[start+i] = temp_sorted_array[i]

    def merge_sort(self, start, end):
        if start < end:
            mid = (start + end) // 2

            self.merge_sort(start, mid)
            self.merge_sort(mid+1, end)

            # Merge both sorted sub-parts
            self.merge(start, mid, end)

    def sort(self):
        self.merge_sort(0, len(self.arr) - 1)


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    print(f"Array before sorting : {arr}")

    merge_sort = MergeSort(arr)
    merge_sort.sort()

    print(f"Sorted array : {merge_sort.arr}")

