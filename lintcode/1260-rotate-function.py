class Solution:
    """
    @param A: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """

    def maxRotateFunction(self, A):
        # Write your code here
        total = sum(A)
        f0 = sum(i * A[i] for i in range(len(A)))

        res = pre = f0
        for i in range(1, len(A)):
            cur = pre - total + A[i - 1] * len(A)
            res = max(cur, res)
            pre = cur

        return res
