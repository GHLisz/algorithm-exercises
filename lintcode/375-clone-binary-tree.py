"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if root is None: return None
        cloned_root = TreeNode(root.val)
        cloned_root.left = self.cloneTree(root.left)
        cloned_root.right = self.cloneTree(root.right)
        return cloned_root
