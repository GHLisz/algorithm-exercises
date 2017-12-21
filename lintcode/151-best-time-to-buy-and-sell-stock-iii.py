class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        hold1 = hold2 = -999999
        release1 = release2 = 0
        for i in range(len(prices)):
            release2 = max(release2, hold2+prices[i])
            hold2 = max(hold2, release1-prices[i])
            release1 = max(release1, hold1+prices[i])
            hold1 = max(hold1, -prices[i])
        return release2
