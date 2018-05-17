class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        # write your code here
        def search(board, i, j, word, start):
            if start == len(word): return True
            if (i not in range(len(board))) \
                    or (j not in range(len(board[0]))) \
                    or board[i][j] != word[start]:
                return False
            board[i][j] = True
            res = search(board, i - 1, j, word, start + 1) \
                  or search(board, i, j - 1, word, start + 1) \
                  or search(board, i + 1, j, word, start + 1) \
                  or search(board, i, j + 1, word, start + 1)
            board[i][j] = word[start]
            return res

        if not board: return False
        if not word: return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(board, i, j, word, 0):
                        return True
        return False
