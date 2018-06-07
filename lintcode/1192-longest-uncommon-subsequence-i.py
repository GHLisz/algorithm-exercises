class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return a integer
    """

    def findLUSlength(self, a, b):
        # write your code here
        return max(len(a), len(b)) if a != b else -1
