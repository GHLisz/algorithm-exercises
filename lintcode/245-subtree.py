"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """

    def isSubtree(self, T1, T2):
        # write your code here
        def is_equal(t1, t2):
            if t1 is None or t2 is None: return t1 == t2
            if t1.val != t2.val: return False
            return is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right)

        if not T2: return True
        if not T1: return False
        if is_equal(T1, T2): return True
        if self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2): return True
        return False
