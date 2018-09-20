class Solution:
    """
    @param graph: a 2D array
    @return: all possible paths from node 0 to node N-1
    """

    def allPathsSourceTarget(self, graph):
        # Write your code here
        n = len(graph)

        def solve(node):
            if node == n - 1: return [[n - 1]]
            ans = []
            for nei in graph[node]:
                for path in solve(nei):
                    ans.append([node] + path)
            return ans

        return solve(0)
