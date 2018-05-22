class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        # write your code here
        if not s or len(s) == 1: return 0

        n = len(s)
        cut = list(range(-1, n))  # cut[k]: number of cuts for the 1st k chars

        for mid in range(-1, n):
            for low, high in (mid, mid), (mid - 1, mid):  # odd len palindrome and even
                while 0 <= low and high < n and s[low] == s[high]:
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low, high = low - 1, high + 1
        return cut[n]
