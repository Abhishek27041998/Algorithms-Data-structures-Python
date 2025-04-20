"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def convert(self, s: str, numRows: int) -> str:
        list_of_list = [[] for _ in range(numRows)]

        list_idx = 0
        reverse = False

        if numRows == 1:
            return s

        for i in range(len(s)):
            list_of_list[list_idx].append(s[i])

            if reverse:
                list_idx -= 1
            else:
                list_idx += 1

            if list_idx == numRows:
                reverse = True
                list_idx -= 2
            if list_idx == -1:
                reverse = False
                list_idx += 2

        read_line_by_line = ""

        for i in range(numRows):
            read_line_by_line += "".join(list_of_list[i])

        return read_line_by_line


if __name__ == '__main__':
    # Input 1
    s = "PAYPALISHIRING"
    numRows = 3

    sol = Solution()
    result = sol.convert(s, numRows)
    print(result)

    # Input 2
    s = "PAYPALISHIRING"
    numRows = 4

    sol = Solution()
    result = sol.convert(s, numRows)
    print(result)

    # Input 3
    s = "A"
    numRows = 1

    sol = Solution()
    result = sol.convert(s, numRows)
    print(result)

    # Input 4
    s = "AB"
    numRows = 1

    sol = Solution()
    result = sol.convert(s, numRows)
    print(result)