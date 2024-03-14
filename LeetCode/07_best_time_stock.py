from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        buy_price = prices[0]

        sell_price = prices[0]

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > sell_price and i > buy_day:
                sell_price = prices[i]
                max_profit = max(max_profit, sell_price - buy_price)

            if prices[i] < buy_price:
                buy_price = prices[i]
                buy_day = i
                sell_price = prices[i]

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
