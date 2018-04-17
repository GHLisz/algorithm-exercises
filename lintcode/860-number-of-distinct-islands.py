class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """

    def numberofDistinctIslands(self, grid):
        # write your code here
        def dfs(grid, x, y, i, j, island):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] > 0): return
            grid[i][j] *= -1
            island.append((i - x, j - y))
            for d in directs:
                dfs(grid, x, y, i + d[0], j + d[1], island)

        directs = ((0, -1), (-1, 0), (0, 1), (1, 0))
        m, n = len(grid), len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                island = []
                dfs(grid, i, j, i, j, island)
                res.add(tuple(island))
        return len(res)
