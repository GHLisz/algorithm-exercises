class Solution:
    """
    @param n: a Integer
    @return: a spiral array
    """

    def spiralArray(self, n):
        # write your code here
        if n == 0:
            return []

        res = [[0] * n for _ in range(n)]

        u, d, l, r = 0, n - 1, 0, n - 1
        num = 1

        while l < r and u < d:
            for j in range(l, r + 1):
                res[u][j] = num
                num += 1
            u += 1
            for i in range(u, d + 1):
                res[i][r] = num
                num += 1
            r -= 1
            for j in range(r, l - 1, -1):
                res[d][j] = num
                num += 1
            d -= 1
            for i in range(d, u - 1, -1):
                res[i][l] = num
                num += 1
            l += 1

        if l == r:
            res[u][r] = num
        elif u == d:
            res[u][l] = num

        return res
