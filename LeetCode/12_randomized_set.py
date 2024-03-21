import random
"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.data.append(val)
            self.index_map[val] = len(self.data) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            index = self.index_map[val]
            last_element = self.data[-1]
            self.data[index] = last_element
            self.index_map[last_element] = index
            self.data.pop()
            del self.index_map[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.data)


if __name__ == '__main__':
    pass

