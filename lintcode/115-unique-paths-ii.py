class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        a = [[0 for col in range(m)] for row in range(n)]

        for col in range(m):
            if obstacleGrid[0][col] != 1:
                a[0][col] = 1
            else:
                break
        for row in range(n):
            if obstacleGrid[row][0] != 1:
                a[row][0] = 1
            else:
                break
        for col in range(1, m):
            for row in range(1, n):
                if obstacleGrid[row][col] != 1:
                    a[row][col] = a[row-1][col] + a[row][col-1]
                else:
                    a[row][col] = 0
        return a[n-1][m-1]
