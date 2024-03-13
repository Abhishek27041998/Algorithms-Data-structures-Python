from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def removeElement(self, nums: List[int], val: int) -> int:
        removed_arr = []

        for x in nums:
            if x != val:
                removed_arr.append(x)

        for i in range(len(nums)):
            if i < len(removed_arr):
                nums[i] = removed_arr[i]
            else:
                nums[i] = -1

        return len(removed_arr)


if __name__ == '__main__':
    # Input 1
    arr = [3, 2, 2, 3]
    val = 3

    sol = Solution()
    result = sol.removeElement(arr, val)

    print(f"Output: {result}, Nums: {arr}")

    # Input 2
    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    result = sol.removeElement(arr, val)

    print(f"Output: {result}, Nums: {arr}")

    # Input 3
