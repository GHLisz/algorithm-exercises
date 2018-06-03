"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root:
    @return: the length of the longest path where each node in the path has the same value
    """

    def longestUnivaluePath(self, root):
        # Write your code here
        def t(node, parent):
            if not node or node.val != parent: return 0
            return 1 + max(t(node.left, node.val), t(node.right, node.val))

        if not root: return 0
        sub = max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
        return max(sub, t(root.left, root.val) + t(root.right, root.val))
