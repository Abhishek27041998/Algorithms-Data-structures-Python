import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]

        result = []
        for i in range(len(nums)):
            result.append(left_product[i] * right_product[i])

        return result


if __name__ == '__main__':
    # Input 1
    arr = [1, 2, 3, 4]

    sol = Solution()
    result = sol.productExceptSelf(arr)

    print(f"Output: {result}")

    # Input 2
    arr = [-1, 1, 0, -3, 3]

    sol = Solution()
    result = sol.productExceptSelf(arr)

    print(f"Output: {result}")

