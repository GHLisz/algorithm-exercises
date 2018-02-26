class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == n == 1:
            return 1
        a = [[0 for col in range(m)] for row in range(n)]
        for col in range(m):
            a[0][col] = 1
        for row in range(n):
            a[row][0] = 1
        for col in range(1, m):
            for row in range(1, n):
                a[row][col] = a[row-1][col] + a[row][col-1]
        return a[n-1][m-1]
