"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """

    def largestValues(self, root):
        # write your code here
        def sol1():  # bfs
            maxes, row = [], [root]
            while any(row):
                maxes.append(max(node.val for node in row))
                row = [kid for node in row for kid in (node.left, node.right) if kid]
            return maxes

        def sol2():  # dfs
            def helper(root, res, d):
                if not root: return
                if d == len(res):
                    res.append(root.val)
                else:
                    res[d] = max(res[d], root.val)
                helper(root.left, res, d + 1)
                helper(root.right, res, d + 1)

            res = []
            helper(root, res, 0)
            return res

        return sol2()
