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
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        # write your code here
        def dfs(i, countrd, graph, t):
            if countrd[i] == 1:
                return False
            if i == t:
                return True
            countrd[i] = 1
            for j in i.neighbors:
                if countrd[j] == 0 and dfs(j, countrd, graph, t):
                    return True
            return False

        countrd = {}
        for x in graph:
            countrd[x] = 0
        return dfs(s, countrd, graph, t)
