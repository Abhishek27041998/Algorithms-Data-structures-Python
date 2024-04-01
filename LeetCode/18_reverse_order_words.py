import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def reverseWords(self, s: str) -> str:
        stripped_string = s.strip()

        split_string = stripped_string.split(' ')

        split_string_without_spaces = []

        for i in range(len(split_string)):
            if split_string[i] != ' ' and split_string[i] != '':
                split_string_without_spaces.append(split_string[i].strip())

        split_string_without_spaces.reverse()

        return ' '.join(split_string_without_spaces)


if __name__ == '__main__':
    # Input 1
    strs = "the sky is blue"

    sol = Solution()
    result = sol.reverseWords(strs)

    print(f"Output: {result}")

    # Input 2
    strs = "  hello world  "

    sol = Solution()
    result = sol.reverseWords(strs)

    print(f"Output: {result}")

    # Input 3
    strs = "a good   example"

    sol = Solution()
    result = sol.reverseWords(strs)

    print(f"Output: {result}")
