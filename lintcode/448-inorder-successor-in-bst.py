"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        if not all([root, p]): return None

        ans = None
        while root:
            if root.val > p.val:
                ans, root = root, root.left
            else:
                root = root.right
        return ans
