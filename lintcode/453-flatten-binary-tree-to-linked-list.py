"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """

    def flatten(self, root):
        # write your code here
        self.lastNode = None
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        if self.lastNode:
            self.lastNode.left = None
            self.lastNode.right = root

        self.lastNode = root
        right = root.right
        self.helper(root.left)
        self.helper(right)
