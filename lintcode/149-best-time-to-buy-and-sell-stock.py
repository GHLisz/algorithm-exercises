class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        max_ending_here = max_so_far = 0

        for i in range(1, len(prices)):
            max_ending_here = max(0, max_ending_here + prices[i] - prices[i - 1])
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far
