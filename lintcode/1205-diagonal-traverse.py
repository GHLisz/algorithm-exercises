class Solution:
    """
    @param matrix: a 2D array
    @return: return a list of integers
    """

    def findDiagonalOrder(self, matrix):
        # write your code here
        def sol1():
            entries = [(i + j, (j, i)[(i ^ j) & 1], val)
                       for i, row in enumerate(matrix)
                       for j, val in enumerate(row)
                       ]
            return [e[2] for e in sorted(entries)]

        def sol2():
            if not matrix: return []
            r, c, m, n = 0, 0, len(matrix), len(matrix[0])
            res = [0] * (m * n)
            for i in range(len(res)):
                res[i] = matrix[r][c]
                if (r + c) % 2 == 0:
                    if c == n - 1:
                        r += 1
                    elif r == 0:
                        c += 1
                    else:
                        r -= 1
                        c += 1
                else:
                    if r == m - 1:
                        c += 1
                    elif c == 0:
                        r += 1
                    else:
                        r += 1
                        c -= 1
            return res

        return sol2()
