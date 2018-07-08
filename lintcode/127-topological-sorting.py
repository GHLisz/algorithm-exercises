"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        def sol1():  # dfs
            def dfs(node, visited, res):
                visited.add(node)
                for n in node.neighbors:
                    if n not in visited: dfs(n, visited, res)
                res.insert(0, node)

            res, visited = [], set()
            for node in graph:
                if node not in visited: dfs(node, visited, res)
            return res

        def sol2():  # bfs
            pass  # todo

        return sol1()
