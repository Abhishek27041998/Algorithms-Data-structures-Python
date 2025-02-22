
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

"""
import string

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass


    def isPalindrome(self, s: str) -> bool:

        allowed_chars = string.ascii_letters + string.digits

        s_only_letters_digits = ''.join([char for char in s if char in allowed_chars])

        s_only_letters_digits = s_only_letters_digits.lower()

        return s_only_letters_digits == s_only_letters_digits[::-1]



if __name__ == '__main__':
    # Input 1
    s = "A man, a plan, a canal: Panama"

    sol = Solution()
    result = sol.isPalindrome(s)

    print(f"Output: {result}")

    # Input 2
    s = "race a car"

    sol = Solution()
    result = sol.isPalindrome(s)

    print(f"Output: {result}")

    # Input 3
    s = " "

    sol = Solution()
    result = sol.isPalindrome(s)

    print(f"Output: {result}")

