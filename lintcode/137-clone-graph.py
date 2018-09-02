"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        def clone(node, umap):
            if not node: return node
            if node.label in umap: return umap[node.label]

            new_node = UndirectedGraphNode(node.label)
            umap[node.label] = new_node
            new_node.neighbors.extend([clone(n, umap) for n in node.neighbors])
            return new_node

        return clone(node, {})
