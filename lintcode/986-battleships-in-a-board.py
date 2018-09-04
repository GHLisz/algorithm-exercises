class Solution:
    """
    @param board: the given 2D board
    @return: the number of battle ships
    """

    def countBattleships(self, board):
        # Write your code here
        if not board: return 0

        count, m, n = 0, len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.': continue
                if i > 0 and board[i - 1][j] == 'X': continue
                if j > 0 and board[i][j - 1] == 'X': continue
                count += 1
        return count
