class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        def dfs(s, idx, tmp, res):
            if idx == len(s):
                res.append(tmp[:])
                return
            for i in range(idx, min(idx+2, len(s))):
                tmp.append(s[idx:i+1])
                dfs(s, i+1, tmp, res)
                tmp.pop()

        res = []
        dfs(s, 0, [], res)
        return res
