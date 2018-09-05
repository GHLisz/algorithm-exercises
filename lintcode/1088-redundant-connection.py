class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """

    def findRedundantConnection(self, edges):
        # write your code here
        def sol1():  # dfs, O(n**2)
            from collections import defaultdict

            graph = defaultdict(set)

            def dfs(source, target):
                if source not in seen:
                    seen.add(source)
                    if source == target: return True
                    return any(dfs(nei, target) for nei in graph[source])

            for u, v in edges:
                seen = set()
                if u in graph and v in graph and dfs(u, v):
                    return u, v
                graph[u].add(v)
                graph[v].add(u)

        def sol2():  # Union Find (Disjoint Set Union), O(n)
            class DSU:
                def __init__(self):
                    self.par = list(range(1001))
                    self.rnk = [0] * 1001

                def find(self, x):
                    if self.par[x] != x:
                        self.par[x] = self.find(self.par[x])
                    return self.par[x]

                def union(self, x, y):
                    xr, yr = self.find(x), self.find(y)
                    if xr == yr:
                        return False
                    elif self.rnk[xr] < self.rnk[yr]:
                        self.par[xr] = yr
                    elif self.rnk[xr] > self.rnk[yr]:
                        self.par[yr] = xr
                    else:
                        self.par[yr] = xr
                        self.rnk[xr] += 1
                    return True

            dsu = DSU()
            for edge in edges:
                if not dsu.union(*edge):
                    return edge

        return sol2()
