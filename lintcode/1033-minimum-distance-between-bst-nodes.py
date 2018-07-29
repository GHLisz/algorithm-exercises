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
        def inorder(node):
            nonlocal res, pre
            if not node: return

            inorder(node.left)
            res = min(res, node.val - pre) if pre else res
            pre = node.val
            inorder(node.right)

        res, pre = float('inf'), None
        inorder(root)
        return res
