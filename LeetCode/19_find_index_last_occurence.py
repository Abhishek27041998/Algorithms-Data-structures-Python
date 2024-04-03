import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    # Input 1
    haystack = "sadbutsad"
    needle = "sad"
    sol = Solution()
    result = sol.strStr(haystack, needle)

    print(f"Output: {result}")

    # Input 2
    haystack = "leetcode"
    needle = "leeto"
    sol = Solution()
    result = sol.strStr(haystack, needle)

    print(f"Output: {result}")

    # Input 3
    haystack = "abababab"
    needle = "bab"
    sol = Solution()
    result = sol.strStr(haystack, needle)

    print(f"Output: {result}")
