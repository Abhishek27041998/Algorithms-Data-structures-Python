"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150

"""
from typing import List

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass


    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water


if __name__ == '__main__':
    # Input 1
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    sol = Solution()
    result = sol.trap(height)

    print(f"Output: {result}")

    # Input 2
    height = [4,2,0,3,2,5]

    sol = Solution()
    result = sol.trap(height)

    print(f"Output: {result}")

