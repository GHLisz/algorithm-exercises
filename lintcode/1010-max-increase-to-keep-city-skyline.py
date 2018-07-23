class Solution:
    """
    @param grid: a 2D array
    @return: the maximum total sum that the height of the buildings can be increased
    """

    def maxIncreaseKeepingSkyline(self, grid):
        # Write your code here
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]
        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
