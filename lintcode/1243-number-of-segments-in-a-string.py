class Solution:
    """
    @param s: a string
    @return: the number of segments in a string
    """

    def countSegments(self, s):
        # write yout code here
        def sol1():
            return len(s.split())

        def sol2():
            res = 0
            for i in range(len(s)):
                if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                    res += 1
            return res

        return sol2()
