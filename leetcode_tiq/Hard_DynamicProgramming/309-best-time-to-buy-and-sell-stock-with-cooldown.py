"""
309. Best Time to Buy and Sell Stock with Cooldown
Medium


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def sol1():  # state machine
            if not prices:
                return 0

            s0, s1, s2 = ([0] * len(prices) for _ in range(3))
            s0[0] = 0  # at the start
            s1[0] = -prices[0]  # after buy
            s2[0] = -float('inf')  # after sell

            for i in range(1, len(prices)):
                s0[i] = max(s0[i - 1], s2[i - 1])
                s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
                s2[i] = s1[i - 1] + prices[i]
            return max(s0[-1], s2[-1])

        def sol2():
            buy, sell, rest = -float('inf'), 0, 0
            for p in prices:
                buy, sell, rest = max(buy, rest - p), max(buy + p, sell), max(buy, sell, rest)
            return max(buy, sell, rest)

        return sol1()
