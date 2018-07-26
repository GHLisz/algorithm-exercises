class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """

    def maxProfit(self, prices):
        # write your code here
        buy, pre_buy, sell, pre_sell = -float('inf'), 0, 0, 0
        for p in prices:
            pre_buy = buy
            buy = max(pre_sell - p, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + p, pre_sell)
        return sell
