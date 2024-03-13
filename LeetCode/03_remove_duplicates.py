from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements_list = list(set(nums))

        unique_elements_list.sort()

        for i in range(len(nums)):
            if i < len(unique_elements_list):
                nums[i] = unique_elements_list[i]
            else:
                nums[i] = -1

        return len(unique_elements_list)


if __name__ == '__main__':
    # Input 1
    arr = [1, 1, 2]

    sol = Solution()
    result = sol.removeDuplicates(arr)

    print(f"Output: {result}, Nums: {arr}")

    # Input 2
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    sol = Solution()
    result = sol.removeDuplicates(arr)

    print(f"Output: {result}, Nums: {arr}")

    # Input 3
