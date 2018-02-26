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
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        return self.getMin(root)

    def getMin(self, root):
        if root is None:
            return 0

        left, right = 0, 0

        if root.left is not None:
            left = self.getMin(root.left)
        else:
            return self.getMin(root.right) + 1

        if root.right is not None:
            right = self.getMin(root.right)
        else:
            return left + 1

        return min(left, right) + 1
