import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def lengthOfLastWord(self, s: str) -> int:
        stripped_string = s.strip()

        split_string = stripped_string.split(' ')

        return len(split_string[-1])


if __name__ == '__main__':
    # Input 1
    s = "Hello World"

    sol = Solution()
    result = sol.lengthOfLastWord(s)

    print(f"Output: {result}")

    # Input 2
    s = "   fly me   to   the moon  "

    sol = Solution()
    result = sol.lengthOfLastWord(s)

    print(f"Output: {result}")

    # Input 3
    s = "luffy is still joyboy"

    sol = Solution()
    result = sol.lengthOfLastWord(s)

    print(f"Output: {result}")
