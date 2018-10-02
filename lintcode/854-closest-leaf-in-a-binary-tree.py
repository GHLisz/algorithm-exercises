"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """

    def findClosestLeaf(self, root, k):
        # Write your code here
        from collections import defaultdict

        graph, start = defaultdict(list), None

        def build_graph(node, parent, k):
            nonlocal graph, start

            if not node: return
            if node.val == k: start = node
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node, k)
            build_graph(node.right, node, k)

        build_graph(root, None, k)
        queue, seen = [start], set()

        while queue:
            cur = queue.pop(0)
            seen.add(cur)
            if not any([cur.left, cur.right]):
                return cur.val
            for node in graph[cur]:
                if node not in seen:
                    queue.append(node)

        return 0
