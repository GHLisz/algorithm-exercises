"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the new root
    """

    def convertBST(self, root):
        # write your code here
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        self.helper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)
