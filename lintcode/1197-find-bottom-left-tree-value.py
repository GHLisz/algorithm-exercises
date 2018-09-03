"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """

    def findBottomLeftValue(self, root):
        # write your code here
        def sol1():  # bfs
            queue = [root]
            for node in queue:
                queue += list(filter(bool, (node.right, node.left)))
            return node.val

        def sol2():  # dfs
            if not root: return
            max_depth, stack = 0, [(root, 1)]
            while stack:
                cur, level = stack.pop()
                if cur:
                    if level > max_depth:
                        max_depth = level
                        res = cur.val
                    stack.append((cur.right, level + 1))
                    stack.append((cur.left, level + 1))
            return res

        return sol2()
