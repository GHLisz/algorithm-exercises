class Solution:
    """
    @param: n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        # write your code here
        def g(l, r, item, res):
            if r < l:
                return
            if l == 0 and r == 0:
                res.append(item)
            if l > 0:
                g(l - 1, r, item + '(', res)
            if r > 0:
                g(l, r - 1, item + ')', res)

        res = []
        g(n, n, '', res)
        return res
