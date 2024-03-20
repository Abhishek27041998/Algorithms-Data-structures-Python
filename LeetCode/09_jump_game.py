from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def canJump(self, nums: List[int]) -> bool:
        current = 0
        return_back = 0
        visited = [False for _ in range(len(nums))]
        visited[0] = True
        zero_idx = 0
        while True:
            leap = current + nums[current]

            if leap >= len(nums) - 1:
                return True

            if visited[leap]:
                current -= 1
                if current <= 0:
                    return False
                continue

            visited[leap] = True

            if nums[leap] != 0:
                current = leap
            else:
                if leap != zero_idx:
                    return_back = 0

                current = leap - 1 - return_back
                return_back += 1
                zero_idx = leap

            if current <= 0:
                return False


if __name__ == '__main__':
    # Input 1
    arr = [2, 3, 1, 1, 4]

    sol = Solution()
    result = sol.canJump(arr)

    print(f"Output: {result}")

    # Input 2
    arr = [3, 2, 1, 0, 4]

    sol = Solution()
    result = sol.canJump(arr)

    print(f"Output: {result}")

    # Input 3
    arr = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]

    sol = Solution()
    result = sol.canJump(arr)

    print(f"Output: {result}")

    # Input 4
    arr = [3, 0, 8, 2, 0, 0, 1]

    sol = Solution()
    result = sol.canJump(arr)

    print(f"Output: {result}")