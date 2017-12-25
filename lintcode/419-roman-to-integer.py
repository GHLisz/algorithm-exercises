class Solution:
    """
    @param: s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        r = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                r -= roman[s[i]]
            else:
                r += roman[s[i]]
        return r + roman[s[-1]]
