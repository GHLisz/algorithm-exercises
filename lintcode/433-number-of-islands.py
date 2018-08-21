class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        def sol1():
            def dfs(grid, i, j):
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1: return
                grid[i][j] = '#'
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    dfs(grid, i + di, j + dj)

            if not grid: return 0
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs(grid, i, j)
                        count += 1
            return count

        def sol2():
            def sink(i, j):
                if not (0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1): return 0
                grid[i][j] = 0
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1

            return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

        return sol2()
