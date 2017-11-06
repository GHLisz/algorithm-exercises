"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        return self.max_depth(root) is not None

    def max_depth(self, root):
        if root is None:
            return 0

        left_h = self.max_depth(root.left)
        right_h = self.max_depth(root.right)

        if (left_h is None) or (right_h is None) or (abs(left_h - right_h) > 1):
            return None

        return max(left_h, right_h) + 1
