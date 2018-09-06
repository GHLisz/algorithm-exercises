"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @return: the tilt of the whole tree
    """

    def findTilt(self, root):
        # Write your code here
        def trav(node):
            nonlocal res

            if not node: return 0
            left, right = trav(node.left), trav(node.right)
            tilt = abs(left - right)
            res += tilt
            return left + right + node.val

        res = 0
        trav(root)
        return res
