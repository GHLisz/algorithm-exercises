class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        def sol1():
            is_pal = lambda x: x == x[::-1]

            def dfs(s, path, res):
                if not s:
                    res.append(path)
                    return
                for i in range(1, len(s) + 1):
                    if is_pal(s[:i]):
                        dfs(s[i:], path + [s[:i]], res)

            res = []
            dfs(s, [], res)
            return res

        return sol1()
