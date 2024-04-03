import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        if len(ratings) == 1:
            return 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i-1] + 1, candies[i])
            elif ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i] + 1, candies[i-1])

        ratings.reverse()
        candies.reverse()

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i - 1] + 1, candies[i])
            elif ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])

        return sum(candies)


if __name__ == '__main__':
    # Input 1
    ratings = [1, 0, 2]

    sol = Solution()
    result = sol.candy(ratings)

    print(f"Output: {result}")

    # Input 2
    ratings = [1, 2, 2]

    sol = Solution()
    result = sol.candy(ratings)

    print(f"Output: {result}")

    # Input 3
    ratings = [1, 3, 4, 5, 2]

    sol = Solution()
    result = sol.candy(ratings)

    print(f"Output: {result}")

    # Input 4
    ratings = [1, 2, 87, 87, 87, 2, 1]

    sol = Solution()
    result = sol.candy(ratings)

    print(f"Output: {result}")
