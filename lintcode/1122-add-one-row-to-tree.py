"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """

    def addOneRow(self, root, v, d):
        # write your code here
        def sol1():  # dfs
            def insert(val, node, depth, n):
                if not node: return
                if depth == n - 1:
                    node.left, node.left.left = TreeNode(val), node.left
                    node.right, node.right.right = TreeNode(val), node.right
                else:
                    insert(val, node.left, depth + 1, n)
                    insert(val, node.right, depth + 1, n)

            if d == 1:
                node = TreeNode(v)
                node.left = root
                return node
            insert(v, root, 1, d)
            return root

        def sol2():  # bfs
            if d == 1:
                node = TreeNode(v)
                node.left = root
                return node
            queue, depth = [root], 1
            while depth < d - 1:
                tmp = []
                while queue:
                    node = queue.pop()
                    if node.left: tmp.append(node.left)
                    if node.right: tmp.append(node.right)
                queue = tmp
                depth += 1
            while queue:
                node = queue.pop()
                node.left, node.left.left = TreeNode(v), node.left
                node.right, node.right.right = TreeNode(v), node.right
            return root

        return sol1()
