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
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        if (not root) or (not root.left): return root
        l, r = root.left, root.right
        res = self.upsideDownBinaryTree(l)
        l.left, l.right = r, root
        root.left, root.right = None, None
        return res
