class Solution:
    """
    @param str: the given string
    @return: the maximum value
    """

    def calcMaxValue(self, str):
        # write your code here
        if not str: return 0
        res, s = int(str[0]), str

        for i in range(1, len(s)):
            if (s[i] in '01') or (res <= 1):
                res += int(s[i])
            else:
                res *= int(s[i])
        return res
