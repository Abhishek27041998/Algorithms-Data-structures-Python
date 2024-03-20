from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/jump-game-ii/solutions/3158169/clean-codes-full-explanation-implicit-bfs-c-java-python3/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = farthest

        return ans


if __name__ == '__main__':
    # Input 1
    arr = [2, 3, 1, 1, 4]

    sol = Solution()
    result = sol.jump(arr)

    print(f"Output: {result}")

    # Input 2
    arr = [3, 2, 1, 0, 4]

    sol = Solution()
    result = sol.jump(arr)

    print(f"Output: {result}")

    # Input 3
    arr = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]

    sol = Solution()
    result = sol.jump(arr)

    print(f"Output: {result}")

    # Input 4
    arr = [3, 0, 8, 2, 0, 0, 1]

    sol = Solution()
    result = sol.jump(arr)

    print(f"Output: {result}")