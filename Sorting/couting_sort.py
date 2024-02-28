"""
This is an implementation of counting sort
"""


class CountingSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        maximum_element = max(self.arr)

        auxillary_arr = [0] * (maximum_element + 1)

        for element in self.arr:
            auxillary_arr[element] += 1

        sorted_arr = []

        for idx, value in enumerate(auxillary_arr):
            if value != 0:
                tmp = value
                while tmp != 0:
                    sorted_arr.append(idx)

                    tmp -= 1

        self.arr = sorted_arr


if __name__ == '__main__':
    arr = [10, 20, 5, 9, 100, 25]
    print(f"Array before sorting : {arr}")

    count_sort = CountingSort(arr)
    count_sort.sort()

    print(f"Sorted array : {count_sort.arr}")

