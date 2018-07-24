class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """

    def numsofIsland(self, grid, k):
        # Write your code here
        def t(i, j):
            nonlocal res
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                res += 1
                grid[i][j] = False
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    t(i + di, j + dj)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res = 0
                    t(i, j)
                    count += 1 if res >= k else 0
        return count
