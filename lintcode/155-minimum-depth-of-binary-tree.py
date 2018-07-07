"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if root is None: return 0

        if root.left is not None:
            left = self.minDepth(root.left)
        else:
            return self.minDepth(root.right) + 1

        if root.right is not None:
            right = self.minDepth(root.right)
        else:
            return left + 1

        return min(left, right) + 1
