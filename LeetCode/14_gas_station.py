import random
from typing import List
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0
        surplus = 0
        start_index = 0

        for i in range(len(gas)):
            total_surplus += (gas[i] - cost[i])
            surplus += (gas[i] - cost[i])

            if surplus < 0:
                surplus = 0
                start_index = i+1

        if total_surplus < 0:
            return -1

        return start_index


if __name__ == '__main__':
    # Input 1
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    sol = Solution()
    result = sol.canCompleteCircuit(gas, cost)

    print(f"Output: {result}")

    # Input 2
    gas = [2, 3, 4]
    cost = [3, 4, 3]

    sol = Solution()
    result = sol.canCompleteCircuit(gas, cost)

    print(f"Output: {result}")

