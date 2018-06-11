class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):
        # write your code here
        if not costs: return 0

        pre_min1, pre_min2, pre_idx, inf = 0, 0, -1, float('inf')

        for i in range(len(costs)):
            cur_min1, cur_min2, cur_idx = inf, inf, -1
            for j in range(len(costs[0])):
                costs[i][j] += pre_min2 if pre_idx == j else pre_min1

                if costs[i][j] < cur_min1:
                    cur_min2, cur_min1, cur_idx = cur_min1, costs[i][j], j
                elif costs[i][j] < cur_min2:
                    cur_min2 = costs[i][j]
            pre_min1, pre_min2, pre_idx = cur_min1, cur_min2, cur_idx

        return pre_min1
