"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given tree
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        # write your code here
        if root is None: return True
        if bool(root.left) ^ bool(root.right): return False
        return self.isFullTree(root.left) and self.isFullTree(root.right)
