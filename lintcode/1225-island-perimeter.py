class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """

    def islandPerimeter(self, grid):
        # Write your code here
        def dfs(i, j):
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1
            return res

        if not grid: return 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    cnt += dfs(i, j)
        return cnt
