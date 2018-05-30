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
    @return: the minimum absolute difference between values of any two nodes
    """

    def getMinimumDifference(self, root):
        # Write your code here
        def inorder(node):
            nonlocal pre, res
            if not node: return
            inorder(node.left)
            if pre != -1:
                res = min(res, node.val - pre)
            pre = node.val
            inorder(node.right)

        import math
        res, pre = math.inf, -1
        inorder(root)
        return res
