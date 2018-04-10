class Solution:
    """
    @param L: A positive integer
    @param R: A positive integer
    @return:  the number of interesting subranges of [L,R]
    """

    def PalindromicRanges(self, L, R):
        # write your code here
        def is_palindromic(n):
            return list(str(n)) == list(reversed(str(n)))

        if L > R: return 0
        if L == R: return 1

        dp, res = [0] * (R - L + 2), 0

        for i in range(L, R + 1):
            dp[i - L + 1] = dp[i - L]
            if is_palindromic(i):
                dp[i - L + 1] += 1

        for i in range(1, R - L + 2):
            for j in range(i - 1, -1, -1):
                count = dp[i] - dp[j]
                if count % 2 == 0:
                    res += 1

        return res
