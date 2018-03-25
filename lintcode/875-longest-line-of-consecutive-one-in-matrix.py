class Solution:
    """
    @param M: the 01 matrix
    @return: the longest line of consecutive one in the matrix
    """

    def longestLine(self, M):
        # Write your code here
        def diagonal_order(matrix):  # upward right
            row, col = len(matrix), len(matrix[0])
            # There will be ROW+COL-1 lines in the output
            for line in range(1, row + col):
                tmp = []
                # Get column index of the first element
                # in this line of output. The index is 0
                # for first ROW lines and line - ROW for
                # remaining lines
                start_col = max(0, line - row)
                # Get count of elements in this line.
                # The count of elements is equal to
                # minimum of line number, COL-start_col and ROW
                count = min(line, col - start_col, row)
                for j in range(count):
                    start_row = min(row, line) - 1
                    tmp.append(matrix[start_row - j][start_col + j])
                yield tmp

        def anti_diagonal_order(matrix):  # upward left
            row, col = len(matrix), len(matrix[0])
            for line in range(1, row + col):
                tmp = []
                start_col = min(col, line) - 1
                start_row = row - max(0, line - col) - 1
                count = min(line, start_row + 1, col)
                for j in range(count):
                    tmp.append(matrix[start_row - j][start_col - j])
                yield tmp

        def get_max1(lis):
            res, tmp = 0, 0
            for a in lis:
                tmp = tmp + 1 if a else 0
                res = max(tmp, res)
            return res

        if not M or not M[0]:
            return 0

        h = max(map(get_max1, M))
        v = max(map(get_max1,
                    [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]))
        d = max(map(get_max1, diagonal_order(M)))
        a = max(map(get_max1, anti_diagonal_order(M)))

        return max(h, v, d, a)
