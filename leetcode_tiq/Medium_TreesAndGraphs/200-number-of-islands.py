"""
200. Number of Islands
Medium


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sol1():  # dfs
            def sink(i, j):
                if not (0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1'):
                    return 0
                grid[i][j] = '0'
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1

            return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

        def sol2():  # bfs
            from collections import deque

            def bfs(grid, r, c):
                queue = deque()
                queue.append((r, c))
                grid[r][c] = '0'
                while queue:
                    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == '1':
                            queue.append((nr, nc))
                            grid[nr][nc] = '0'

            if not grid or not grid[0]:
                return 0
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        bfs(grid, i, j)
                        count += 1
            return count

        def sol3():  # union find
            class UnionFind:
                def __init__(self, grid):
                    m, n = len(grid), len(grid[0])
                    self.count = 0
                    self.father = [0] * (m * n)
                    for i in range(m):
                        for j in range(n):
                            if grid[i][j] == '1':
                                self.father[i * n + j] = i * n + j
                                self.count += 1

                def union(self, node1, node2):
                    find1, find2 = self.find(node1), self.find(node2)
                    if find1 != find2:
                        self.father[find1] = find2
                        self.count -= 1

                def find(self, node):
                    if self.father[node] == node:
                        return node
                    self.father[node] = self.find(self.father[node])
                    return self.father[node]

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            if not grid or not grid[0]:
                return 0

            uf = UnionFind(grid)

            rows, cols = len(grid), len(grid[0])
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == '1':
                        for dx, dy in directions:
                            x, y = i + dx, j + dy
                            if x in range(rows) and y in range(cols) and grid[x][y] == '1':
                                id1, id2 = i * cols + j, x * cols + y
                                uf.union(id1, id2)
            return uf.count

        return sol3()
