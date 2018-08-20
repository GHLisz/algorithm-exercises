class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """

    def maxProfit(self, prices, fee):
        # write your code here
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
