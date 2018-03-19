class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = r // 3 * 3 + c // 3
                if board[r][c] in grid[g]:
                    return False

                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])

        return True
