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
    @return: the minimum difference between the values of any two different nodes in the tree
    """

    def minDiffInBST(self, root):
        # Write your code here
        def inorder(root):
            nonlocal res, pre
            if not root: return
            inorder(root.left)
            if pre:
                res = min(res, root.val - pre)
            pre = root.val
            inorder(root.right)

        import math
        res = math.inf
        pre = None
        inorder(root)
        return res
