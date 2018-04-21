class Solution:
    """
    @param s: a string
    @return: return a list of integers
    """
    def findPermutation(self, s):
        # write your code here
        res, i = [1] * (len(s) + 1), 1
        while i <= len(s):
            res[i], j = i + 1, i
            if s[i - 1] == 'D':
                while i <= len(s) and s[i - 1] == 'D':
                    i += 1
                k, c = j - 1, i
                while k <= i - 1:
                    res[k] = c
                    k += 1
                    c -= 1
            else:
                i += 1
        return res
