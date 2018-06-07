"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """

    def isSymmetric(self, root):
        # Write your code here
        def is_mirror(left, right):
            if left is None and right is None: return True
            if left is None or right is None: return False
            return left.val == right.val \
                   and is_mirror(left.left, right.right) \
                   and is_mirror(left.right, right.left)

        return is_mirror(root, root)
