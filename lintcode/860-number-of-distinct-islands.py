class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """

    def numberofDistinctIslands(self, grid):
        # write your code here
        def dfs(x, y, i, j, island):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] > 0): return
            grid[i][j] *= -1
            island.append((i - x, j - y))
            for d in (0, -1), (-1, 0), (0, 1), (1, 0):
                dfs(x, y, i + d[0], j + d[1], island)

        res, m, n = set(), len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                island = []
                dfs(i, j, i, j, island)
                res.add(tuple(island))
        return len(res)
