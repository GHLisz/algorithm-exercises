"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """

    def countUnivalSubtrees(self, root):
        # write your code here
        def is_unival(root, val):
            nonlocal res
            if not root: return True
            left = is_unival(root.left, root.val)
            right = is_unival(root.right, root.val)
            if not all([left, right]):
                return False
            res += 1
            return root.val == val

        res = 0
        is_unival(root, -1)
        return res
