from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) // 2
        frequency = {}
        maj_elem = nums[0]

        for element in nums:
            frequency[element] = frequency.get(element, 0) + 1

            if frequency[element] > limit:
                maj_elem = element

        return maj_elem


if __name__ == '__main__':
    # Input 1
    arr = [3, 2, 3]

    sol = Solution()
    result = sol.majorityElement(arr)

    print(f"Output: {result}, Nums: {arr}")

    # Input 2
    arr = [2, 2, 1, 1, 1, 2, 2]

    sol = Solution()
    result = sol.majorityElement(arr)

    print(f"Output: {result}, Nums: {arr}")
