class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        # write your code here
        if not costs: return 0

        for i in range(1, len(costs)):
            for a, b, c in ((0, 1, 2), (1, 0, 2), (2, 0, 1)):
                costs[i][a] += min(costs[i - 1][b], costs[i - 1][c])

        return min(costs[-1])
