class Solution:
    """
    @param grid: an integer matrix
    @return: an integer
    """

    def numIslandCities(self, grid):
        # Write your code here
        def dfs(grid, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return False
            if grid[x][y] == 0:
                return False

            have_city = False
            if grid[x][y] == 2:
                have_city = True
            grid[x][y] = 0
            have_city = dfs(grid, x + 1, y) or have_city
            have_city = dfs(grid, x - 1, y) or have_city
            have_city = dfs(grid, x, y + 1) or have_city
            have_city = dfs(grid, x, y - 1) or have_city
            return have_city

        if not grid or not grid[0]:
            return 0

        m, n, cnt = len(grid[0]), len(grid), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if dfs(grid, i, j):
                        cnt += 1
        return cnt
