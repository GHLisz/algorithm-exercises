class Solution:
    """
    @param grid: the grid
    @return: the number of corner rectangles
    """

    def countCornerRectangles(self, grid):
        # Write your code here
        def sol1():
            res, counts = 0, collections.Counter()
            for row in range(len(grid)):
                for col1 in range(1, len(grid[row])):
                    if grid[row][col1] == 1:
                        for col2 in range(col1):
                            if grid[row][col2] == 1:
                                res += counts[col1, col2]
                                counts[col1, col2] += 1
            return res

        def sol2():
            res = 0
            for row1 in range(len(grid) - 1):
                for row2 in range(row1 + 1, len(grid)):
                    cnt = 0
                    for col in range(len(grid[0])):
                        if grid[row1][col] + grid[row2][col] == 2:
                            cnt += 1
                    res += cnt * (cnt - 1) // 2
            return res

        return sol1()
