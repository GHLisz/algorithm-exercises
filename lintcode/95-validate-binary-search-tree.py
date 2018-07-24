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
        def valid(node, mn, mx):
            if not node: return True
            if not mn < node.val < mx: return False
            return all([valid(node.left, mn, node.val),
                        valid(node.right, node.val, mx)])

        return valid(root, -float('inf'), float('inf'))
