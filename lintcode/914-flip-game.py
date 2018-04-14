class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        res, l = [], list(s)
        for i in range(len(s)-1):
            if l[i] == l[i+1] == '+':
                l[i] = l[i+1] = '-'
                res.append(''.join(l))
                l[i] = l[i+1] = '+'
        return res
