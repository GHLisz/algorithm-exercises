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

    def maxPathSum(self, root):
        # write your code here
        def max_path_down(node):
            nonlocal max_val
            if not node: return 0
            left = max(0, max_path_down(node.left))
            right = max(0, max_path_down(node.right))
            max_val = max(max_val, left + right + node.val)
            return max(left, right) + node.val

        import math
        max_val = -math.inf
        max_path_down(root)
        return max_val
