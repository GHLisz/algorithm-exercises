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
            res, q, dic = [], [], {}

            for node in graph:
                for neighbor in node.neighbors:
                    dic[neighbor] = dic.get(neighbor, 0) + 1

            for node in graph:
                if node not in dic:
                    q.append(node)
                    res.append(node)

            while len(q):
                node = q.pop()
                for n in node.neighbors:
                    dic[n] -= 1
                    if dic[n] == 0:
                        res.append(n)
                        q.append(n)

            return res

        return sol2()
