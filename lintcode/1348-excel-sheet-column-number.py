class Solution:
    """
    @param s: a string
    @return: return a integer
    """

    def titleToNumber(self, s):
        # write your code here
        from functools import reduce

        return reduce(lambda x, y: x * 26 + y,
                      (ord(c) - ord('A') + 1 for c in s))
