class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        # write your code here
        if not any(board): return

        m, n = len(board), len(board[0])
        save = list({ij for k in range(max(m, n)) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))})
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        board[:] = [['XO'[col == 'S'] for col in row] for row in board]
