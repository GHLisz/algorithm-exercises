"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        if not root:
            return
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None

        while root.right:
            root = root.right

        root.right = tmp
