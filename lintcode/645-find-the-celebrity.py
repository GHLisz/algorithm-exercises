"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        knows = Celebrity.knows
        res = 0
        for i in range(n):
            if knows(res, i):
                res = i
        for i in range(n):
            if (res != i and knows(res, i)) or (not knows(i, res)):
                return -1
        return res
