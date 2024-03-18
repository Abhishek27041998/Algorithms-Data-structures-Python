from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                max_profit += (prices[i-1] - prices[buy_day])
                buy_day = i
            elif i == len(prices) - 1:
                max_profit += (prices[i] - prices[buy_day])

        return max_profit


if __name__ == '__main__':
    # Input 1
    arr = [7, 1, 5, 3, 6, 4]

    sol = Solution()
    result = sol.maxProfit(arr)

    print(f"Output: {result}")

    # Input 2
    arr = [7, 6, 4, 3, 1]

    sol = Solution()
    result = sol.maxProfit(arr)

    print(f"Output: {result}")

    # Input 3
    arr = [1, 2, 3, 4, 5]

    sol = Solution()
    result = sol.maxProfit(arr)

    print(f"Output: {result}")
