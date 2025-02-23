"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

"""
import string

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass


    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        if len(s) == 0:
            return True

        is_subseq = False
        for _ in range(len(s)):
            curr_ch = s[s_pointer]
            found_curr_ch = False

            for j in range(t_pointer, len(t)):
                t_pointer += 1

                if curr_ch == t[j]:
                    s_pointer += 1
                    found_curr_ch = True
                    break

            if not found_curr_ch:
                return False

        return s_pointer == len(s)


if __name__ == '__main__':
    # Input 1
    s = "abc"
    t = "ahbgdc"

    sol = Solution()
    result = sol.isSubsequence(s, t)

    print(f"Output: {result}")

    # Input 2
    s = "axc"
    t = "ahbgdc"
    sol = Solution()
    result = sol.isSubsequence(s, t)

    print(f"Output: {result}")

