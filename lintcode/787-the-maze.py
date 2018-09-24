class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def hasPath(self, maze, start, destination):
        # write your code here
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        dirs = ((0, 1), (0, -1), (-1, 0), (1, 0))
        que = [start]
        visited[start[0]][start[1]] = True

        while que:
            sx, sy = que.pop()
            if sx == destination[0] and sy == destination[1]: return True

            for dx, dy in dirs:
                x, y = sx + dx, sy + dy
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x, y = x + dx, y + dy
                if not visited[x - dx][y - dy]:
                    que.append((x - dx, y - dy))
                    visited[x - dx][y - dy] = True
        return False
