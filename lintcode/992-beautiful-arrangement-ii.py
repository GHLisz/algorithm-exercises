class Solution:
    """
    @param n: the number of integers
    @param k: the number of distinct integers
    @return: any of answers meet the requirment
    """

    def constructArray(self, n, k):
        # Write your code here
        res = list(range(1, n - k))
        for i in range(k + 1):
            res.append(n - k + i // 2 if i % 2 == 0 else n - i // 2)
        return res
