class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if (not grid) or (not grid[0]):
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        row_cnt, col_cnt = 0, [0]*n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    row_cnt = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        elif grid[i][k] == 'E':
                            row_cnt += 1
                if i == 0 or grid[i-1][j] == 'W':
                    col_cnt[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        elif grid[k][j] == 'E':
                            col_cnt[j] += 1
                if grid[i][j] == '0':
                    res = max(res, row_cnt+col_cnt[j])
        return res
