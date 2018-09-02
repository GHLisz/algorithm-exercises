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
        def recursive():
            def is_mirror(left, right):
                if left is None or right is None: return left == right
                return left.val == right.val \
                       and is_mirror(left.left, right.right) \
                       and is_mirror(left.right, right.left)

            return is_mirror(root, root)

        def iterative():
            if root is None: return True

            stack = [[root.left, root.right]]
            while stack:
                left, right = stack.pop(0)
                if left is None and right is None: continue
                if left is None or right is None: return False

                if left.val == right.val:
                    stack.insert(0, [left.left, right.right])
                    stack.insert(0, [left.right, right.left])
                else:
                    return False
            return True

        return recursive()
