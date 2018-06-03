"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """

    def isSubtree(self, s, t):
        # Write your code here
        def is_subtree(s, t):
            if s is None: return False
            return is_same(s, t) or is_subtree(s.left, t) or is_subtree(s.right, t)

        def is_same(s, t):
            if s is None and t is None: return True
            if s is None or t is None: return False
            return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)

        return is_subtree(s, t)
