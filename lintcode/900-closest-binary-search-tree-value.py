"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        kid = root.left if target < root.val else root.right
        if not kid: return root.val
        closest = self.closestValue(kid, target)
        return root.val if abs(root.val - target) < abs(closest - target) else closest
