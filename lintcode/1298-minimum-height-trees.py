class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """

    def findMinHeightTrees(self, n, edges):
        # Wirte your code here
        if n <= 1: return [0]

        degrees, graph = [0] * n, {x: [] for x in range(n)}

        for u, v in edges:
            for x, y in (u, v), (v, u):
                degrees[x] += 1
                graph[x].append(y)

        res, queue = [], [x for x in range(n) if degrees[x] == 1]

        while queue:
            tmp, res = [], queue[:]
            for x in queue:
                for n in graph[x]:
                    degrees[n] -= 1
                    if degrees[n] == 1: tmp.append(n)
            queue = tmp

        return res
