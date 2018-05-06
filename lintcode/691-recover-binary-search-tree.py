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
    @return: the tree after swapping
    """

    def bstSwappedNode(self, root):
        # write your code here
        mis1, mis2, pre = None, None, None

        def trav(root):
            nonlocal mis1, mis2, pre
            if not root: return
            trav(root.left)
            if pre is not None and root.val < pre.val:
                if mis1 is None:
                    mis1, mis2 = pre, root
                else:
                    mis2 = root
            pre = root
            trav(root.right)

        trav(root)
        if mis1 and mis2:
            mis1.val, mis2.val = mis2.val, mis1.val
        return root
