class Solution:
    """
    @param g: children's greed factor
    @param s: cookie's size
    @return: the maximum number
    """

    def findContentChildren(self, g, s):
        # Write your code here
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        while s and g:
            if g[-1] <= s[-1]:
                res += 1
                g.pop()
                s.pop()
            else:
                s.pop()
        return res
