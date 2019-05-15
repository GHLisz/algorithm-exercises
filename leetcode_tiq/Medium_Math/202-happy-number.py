"""
202. Happy Number
Easy


Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def sol1(n):  # Floyd Cycle detection algorithm
            func = lambda n: sum([int(x) ** 2 for x in list(str(n))])
            slow = fast = n
            while True:
                slow = func(slow)
                fast = func(fast)
                fast = func(fast)
                if slow == fast:
                    break
            return slow == 1

        def sol2(n):
            showed_nums = set()
            while True:
                showed_nums.add(n)
                n = sum([int(x) ** 2 for x in list(str(n))])
                if n == 1 or n in showed_nums:
                    break
            return n == 1

        return sol1(n)
