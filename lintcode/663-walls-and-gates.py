class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        # write your code here
        def sol1():  # bfs
            q, dirs = [], ((0, -1), (-1, 0), (0, 1), (1, 0))
            for i in range(len(rooms)):
                for j in range(len(rooms[i])):
                    if rooms[i][j] == 0:
                        q.append((i, j))
            while q:
                i, j = q.pop()
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if ((x in range(len(rooms)))
                            and (y in range(len(rooms[0])))
                            and (rooms[x][y] >= rooms[i][j] + 1)):
                        rooms[x][y] = rooms[i][j] + 1
                        q.append((x, y))

        def sol2():  # dfs
            def dfs(rooms, i, j, val):
                if ((i in range(len(rooms)))
                        and (j in range(len(rooms[0])))
                        and (rooms[i][j] >= val)):
                    rooms[i][j] = val
                    for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                        dfs(rooms, i + dx, j + dy, val + 1)

            for i in range(len(rooms)):
                for j in range(len(rooms[i])):
                    if rooms[i][j] == 0:
                        dfs(rooms, i, j, 0)

        sol1()
