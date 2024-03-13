from typing import List

"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = 0
        q = 0

        temp_sorted_array = []

        for i in range(m+n):
            if p >= m:
                temp_sorted_array.append(nums2[q])
                q += 1
            elif q >= n:
                temp_sorted_array.append(nums1[p])
                p += 1
            elif nums1[p] < nums2[q]:
                temp_sorted_array.append(nums1[p])
                p += 1
            else:
                temp_sorted_array.append(nums2[q])
                q += 1

        for i in range(len(nums1)):
            nums1[i] = temp_sorted_array[i]


if __name__ == '__main__':
    # Input 1
    arr_1 = [1, 2, 3, 0, 0, 0]
    m = 3

    arr_2 = [2, 5, 6]
    n = 3

    merge_sort = Solution()
    merge_sort.merge(arr_1, m, arr_2, n)

    print(f"Sorted array : {arr_1}")

    # Input 2
    arr_1 = [1]
    m = 1

    arr_2 = []
    n = 0

    merge_sort = Solution()
    merge_sort.merge(arr_1, m, arr_2, n)

    print(f"Sorted array : {arr_1}")

    # Input 3
    arr_1 = [0]
    m = 0

    arr_2 = [1]
    n = 1

    merge_sort = Solution()
    merge_sort.merge(arr_1, m, arr_2, n)

    print(f"Sorted array : {arr_1}")

