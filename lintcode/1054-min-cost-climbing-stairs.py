class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        f1 = f2 = 0
        for c in reversed(cost):
            f1, f2 = c + min(f1, f2), f1
        return min(f1, f2)
