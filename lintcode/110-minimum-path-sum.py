class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        r = [[0 for _ in range(n)] for _ in range(m)]
        r[0][0] = grid[0][0]
        for i in range(1, m):
            r[i][0] = r[i - 1][0] + grid[i][0]
        for i in range(1, n):
            r[0][i] = r[0][i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                r[i][j] = min(r[i - 1][j], r[i][j - 1]) + grid[i][j]
        return r[m - 1][n - 1]
