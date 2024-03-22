import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        i = 0

        while i < len(s):
            s1 = roman_values.get(s[i], -1)
            if i + 1 < len(s):
                s2 = roman_values.get(s[i + 1], -1)
                if s1 >= s2:
                    result += s1
                    i += 1
                else:
                    result += s2 - s1
                    i += 2
            else:
                result += s1
                i += 1
        return result


if __name__ == '__main__':
    # Input 1
    s = "III"

    sol = Solution()
    result = sol.romanToInt(s)

    print(f"Output: {result}")

    # Input 2
    s = "LVIII"

    sol = Solution()
    result = sol.romanToInt(s)

    print(f"Output: {result}")

    # Input 3
    s = "MCMXCIV"

    sol = Solution()
    result = sol.romanToInt(s)

    print(f"Output: {result}")
