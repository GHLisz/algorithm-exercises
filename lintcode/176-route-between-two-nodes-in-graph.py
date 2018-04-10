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
        def sol1():  # bfs
            if graph is None or s is None or t is None: return False
            queue, visited = [], set()
            queue.append(s)
            while queue:
                for i in range(len(queue)):
                    node = queue.pop(0)
                    visited.add(node)
                    if node is t:
                        return True
                    for n in node.neighbors:
                        if n in visited:
                            continue
                        queue.append(n)
            return False

        def sol2():  # dfs
            def dfs(graph, s, t, visited):
                if s is None or t is None: return False
                if s == t: return True
                visited.add(s)
                for node in s.neighbors:
                    if node in visited:
                        continue
                    if dfs(graph, node, t, visited):
                        return True
                return False

            visited = set()
            return dfs(graph, s, t, visited)

        return sol1()
