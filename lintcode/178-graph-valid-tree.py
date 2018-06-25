class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        def sol1():
            def find(roots, i):
                while roots[i] != -1:
                    i = roots[i]
                return i

            roots = [-1] * n
            for a in edges:
                x, y = find(roots, a[0]), find(roots, a[1])
                if x == y: return False
                roots[x] = y

            return len(edges) == n - 1

        def sol2():
            def dfs(g, v, cur, pre):
                if v[cur]: return False
                v[cur] = True
                for a in g[cur]:
                    if a != pre:
                        if not dfs(g, v, a, cur):
                            return False
                return True

            g = [[] for _ in range(n)]
            v = [False] * n
            for a in edges:
                g[a[0]].append(a[1])
                g[a[1]].append(a[0])
            if not dfs(g, v, 0, -1): return False
            return all(v)

        return sol2()
