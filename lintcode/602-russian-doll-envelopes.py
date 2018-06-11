class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here
        def sol1():  # nlogn
            import bisect
            envelopes.sort(key=lambda e: (e[0], -e[1]))
            dp = [float('inf')] * len(envelopes)
            for e in envelopes:
                dp[bisect.bisect_left(dp, e[1])] = e[1]
            return bisect.bisect_left(dp, float('inf'))

        return sol1()
