import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        idx = 0
        while True:
            if idx >= len(strs[0]):
                break

            present_char = strs[0][idx]

            stop_loop = False

            for i in range(1, len(strs)):
                if idx == len(strs[i]):
                    stop_loop = True
                    break

                if present_char == strs[i][idx]:
                    continue
                else:
                    stop_loop = True
                    break

            if stop_loop:
                break

            prefix.append(present_char)
            idx += 1

            if idx >= len(strs[0]):
                break

        return ''.join(prefix)


if __name__ == '__main__':
    # Input 1
    strs = ["flower","flow","flight"]

    sol = Solution()
    result = sol.longestCommonPrefix(strs)

    print(f"Output: {result}")

    # Input 2
    strs = ["dog","racecar","car"]

    sol = Solution()
    result = sol.longestCommonPrefix(strs)

    print(f"Output: {result}")

    # Input 3
    strs = ["aba", "ababca", "abc"]

    sol = Solution()
    result = sol.longestCommonPrefix(strs)

    print(f"Output: {result}")