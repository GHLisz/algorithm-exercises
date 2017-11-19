class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        result = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and not visited[r][c]:
                    result += 1
                    self.bfs(grid, visited, r, c)
        return result

    def bfs(self, grid, visited, row, col):
        if 0 <= row < len(grid) \
                and 0 <= col < len(grid[0]) \
                and not visited[row][col] \
                and grid[row][col] == 1:
            visited[row][col] = True
            self.bfs(grid, visited, row - 1, col)
            self.bfs(grid, visited, row, col + 1)
            self.bfs(grid, visited, row + 1, col)
            self.bfs(grid, visited, row, col - 1)
