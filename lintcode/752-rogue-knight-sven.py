class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """

    def getNumberOfWays(self, n, m, limit, cost):
        # Write your code here
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][m] = 1
        for i in range(n + 1):
            for j in range(m + 1):
                for t in range(max(0, i - limit), i):
                    if j + cost[i] <= m:
                        dp[i][j] += dp[t][j + cost[i]]
        return sum(dp[n])
