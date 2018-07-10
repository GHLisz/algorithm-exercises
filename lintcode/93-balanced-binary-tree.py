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
        def max_depth(root):
            if root is None: return 0
            ld, rd = max_depth(root.left), max_depth(root.right)
            if (ld is None) or (rd is None) or (abs(ld - rd) > 1): return None
            return max(ld, rd) + 1

        return max_depth(root) is not None
