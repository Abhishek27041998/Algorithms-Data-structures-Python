from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        if k == 0:
            return

        temp_arr = [nums[len(nums) - k]]
        idx = len(nums) - k + 1

        while idx != len(nums) - k:
            if idx >= len(nums):
                idx = 0

            temp_arr.append(nums[idx])
            idx += 1

        for i in range(len(nums)):
            nums[i] = temp_arr[i]


if __name__ == '__main__':
    # Input 1
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    sol = Solution()
    sol.rotate(arr, k)

    print(f"Output: {arr}")

    # Input 2
    arr = [-1, -100, 3, 99]
    k = 2

    sol = Solution()
    sol.rotate(arr, k)

    print(f"Output: {arr}")
