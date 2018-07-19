"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """

    def convertBST(self, root):
        # write your code here
        def helper(node):
            nonlocal total
            if not node: return
            helper(node.right)
            total += node.val
            node.val = total
            helper(node.left)

        total = 0
        helper(root)
        return root
