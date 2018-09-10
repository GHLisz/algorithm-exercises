class Solution:
    """
    @param str: the str
    @return: the sum of bytes in the last word
    """

    def judgeTheLastNumber(self, str):
        # Write your code here
        i, n = 0, len(str)
        while i < n:
            if i == n - 1:
                return 1
            elif str[i] == '1':
                i += 2
            else:
                i += 1
        return 2
