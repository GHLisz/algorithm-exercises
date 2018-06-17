class Solution:
    """
    @param s: the given string
    @param numRows: the number of rows
    @return: the string read line by line
    """

    def convert(self, s, numRows):
        # Write your code here
        if numRows == 1: return s
        res, n, cycle_len = '', len(s), 2 * numRows - 2

        for i in range(numRows):
            j = 0
            while i + j < n:
                res += s[i + j]
                if i not in [0, numRows - 1] and j + cycle_len - i < n:
                    res += s[j + cycle_len - i]
                j += cycle_len
        return res
