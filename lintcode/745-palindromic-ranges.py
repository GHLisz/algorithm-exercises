class Solution:
    """
    @param L: A positive integer
    @param R: A positive integer
    @return:  the number of interesting subranges of [L,R]
    """

    def PalindromicRanges(self, L, R):
        # write your code here
        is_pal = lambda n: str(n) == str(n)[::-1]

        if L > R: return 0
        if L == R: return 1

        dp, res = [0] * (R - L + 2), 0

        for i in range(L, R + 1):
            dp[i - L + 1] = dp[i - L] + 1 if is_pal(i) else dp[i - L]

        for i in range(1, R - L + 2):
            for j in range(i - 1, -1, -1):
                count = dp[i] - dp[j]
                res += 1 if count % 2 == 0 else 0

        return res
