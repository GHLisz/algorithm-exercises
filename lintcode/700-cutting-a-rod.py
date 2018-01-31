class Solution:
    """
    @param: : the prices
    @param: : the length of rod
    @return: the max value
    """

    def cutting(self, prices, n):
        # Write your code here
        r = [0] * (n+1)
        for j in range(1, n+1):
            q = -999999
            for i in range(j):
                q = max(q, prices[i] + r[j-i-1])
            r[j] = q
        return r[n]
