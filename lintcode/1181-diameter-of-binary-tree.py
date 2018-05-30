"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """

    def diameterOfBinaryTree(self, root):
        # write your code here
        def t(node):
            nonlocal res
            if not node: return 0
            left, right = t(node.left), t(node.right)
            res = max(res, left + right)
            return max(left, right) + 1

        res = 0
        t(root)
        return res
