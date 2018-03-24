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
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        def inorder(root, target, k, res):
            if root is None:
                return
            inorder(root.left, target, k, res)
            if len(res) < k:
                res.append(root.val)
            elif abs(root.val - target) < abs(res[0] - target):
                res.pop(0)
                res.append(root.val)
            else:
                return
            inorder(root.right, target, k, res)

        res = []
        inorder(root, target, k, res)
        return res
