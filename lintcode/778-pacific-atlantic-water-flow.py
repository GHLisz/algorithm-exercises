class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """

    def pacificAtlantic(self, matrix):
        # write your code here
        if not matrix: return []

        m, n = len(matrix), len(matrix[0])

        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]

        def dfs(i, j, visited):
            visited[i][j] = True
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] >= matrix[i][j] and (not visited[x][y]):
                    dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)

        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)

        return [[i, j] for i in range(m) for j in range(n) if p_visited[i][j] and a_visited[i][j]]
