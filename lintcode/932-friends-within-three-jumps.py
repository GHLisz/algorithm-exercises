class Solution:
    """
    @param a: The a tuple
    @param b: The b tuple
    @param c: the c tuple
    @param d: the d tuple
    @return: The answer
    """

    def withinThreeJumps(self, a, b, c, d):
        # Write your code here
        def dfs(x, y, g, step):
            if step > 3: return
            if x == y: return 1
            for i in g[x]:
                if dfs(i, y, g, step + 1) == 1:
                    return 1
            return 0

        g, res = [[] for _ in range(1001)], []
        for i in range(len(a)):
            g[a[i]].append(b[i])
            g[b[i]].append(a[i])
        for i in range(len(c)):
            res.append(dfs(c[i], d[i], g, 0))
        return res
