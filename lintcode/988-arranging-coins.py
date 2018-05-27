class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        from math import sqrt
        return (sqrt(8*n+1)-1) // 2
