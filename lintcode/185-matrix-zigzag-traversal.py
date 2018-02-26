class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        if len(matrix) == 0:
            return []

        x, y = 0, 0
        n, m = len(matrix), len(matrix[0])
        rows, cols = range(n), range(m)

        dx = [1, -1]
        dy = [-1, 1]
        direction = 1  # 1 means upward right

        result = []

        for i in range(n*m):
            result.append(matrix[x][y])

            next_x = x + dx[direction]
            next_y = y + dy[direction]

            if next_x not in rows or next_y not in cols:
                if direction == 1:
                    if next_y >= m:
                        next_x, next_y = x + 1, y
                    else:
                        next_x, next_y = x, y + 1
                else:
                    if next_x >= n:
                        next_x, next_y =x, y + 1
                    else:
                        next_x, next_y = x + 1, y
                direction = 1 - direction

            x, y = next_x, next_y

        return result
