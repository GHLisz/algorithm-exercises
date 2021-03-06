class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """

    def candyCrush(self, board):
        # Write your code here
        R, C, changed = len(board), len(board[0]), True

        while changed:
            changed = False

            for r in range(R):
                for c in range(C - 2):
                    if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                        board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                        changed = True

            for r in range(R - 2):
                for c in range(C):
                    if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                        board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                        changed = True

            for c in range(C):
                i = R - 1
                for r in reversed(range(R)):
                    if board[r][c] > 0:
                        board[i][c] = board[r][c]
                        i -= 1
                for r in reversed(range(i + 1)):
                    board[r][c] = 0
        return board
