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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        def valid(root, mn, mx):
            if not root:
                return True
            if root.val <= mn or root.val >= mx:
                return False
            return valid(root.left, mn, root.val) and \
                   valid(root.right, root.val, mx)

        import math
        return valid(root, -math.inf, math.inf)
