from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def hIndex(self, citations: List[int]) -> int:
        ans = 0

        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        citations.sort(reverse=True)

        for i in range(len(citations)):
            if i+1 > citations[i]:
                break
            ans += 1

        return ans


if __name__ == '__main__':
    # Input 1
    arr = [3, 0, 6, 1, 5]

    sol = Solution()
    result = sol.hIndex(arr)

    print(f"Output: {result}")

    # Input 2
    arr = [1, 3, 1]

    sol = Solution()
    result = sol.hIndex(arr)

    print(f"Output: {result}")

    # Input 3
    arr = [10, 8, 5, 4, 3]

    sol = Solution()
    result = sol.hIndex(arr)

    print(f"Output: {result}")

